#!/usr/bin/env python3
"""Validate package contents and native layout using only Python's stdlib."""
from pathlib import Path
import hashlib
import json
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def fields(text):
    lines = text.split("---", 2)[1].strip().splitlines()
    result = {}
    for line in lines:
        key, value = line.split(":", 1)
        value = value.strip()
        result[key.strip()] = json.loads(value) if value.startswith('"') else value
    return result


def check_links(path, root):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if "://" not in target and not target.startswith("#"):
            assert (path.parent / target.split("#")[0]).exists(), (path, target)
    for target in re.findall(r"@references/([\w.-]+)", text):
        assert (root / "references" / target).exists(), target


def main():
    manifest = json.loads((ROOT / "RELEASE.json").read_text(encoding="utf-8"))
    name = manifest["name"]
    corpus = json.loads((ROOT / "references/corpus-index.json").read_text(encoding="utf-8"))
    assert len(corpus["papers"]) == 153
    assert len({p["id"] for p in corpus["papers"]}) == 153
    for p in corpus["papers"]:
        assert not ({"sha256", "source_file_names", "reference_role"} & p.keys())
    base_body = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2]
    result = []
    for item in manifest["packages"]:
        path = ROOT / "dist" / item["file"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
        with zipfile.ZipFile(path) as archive:
            assert archive.testzip() is None
            assert {n.split("/")[0] for n in archive.namelist()} == {name}
            assert all(not Path(n).is_absolute() and ".." not in Path(n).parts for n in archive.namelist())
            with tempfile.TemporaryDirectory(prefix="chem-skill-check-") as directory:
                archive.extractall(directory)
                skill = Path(directory) / name
                meta = fields((skill / "SKILL.md").read_text(encoding="utf-8"))
                assert meta["name"] == name
                assert 0 < len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                assert meta["description"] and len(meta["description"]) <= 200
                required = {"name", "description"}
                if item["platform"] == "workbuddy":
                    required |= {"display_name", "display_name_en", "description_zh", "description_en", "version", "author"}
                assert required <= meta.keys()
                body = (skill / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2]
                expected = base_body
                if item["platform"] == "workbuddy":
                    expected = re.sub(r"\[([^\]]+)\]\((references/[^)]+)\)",
                                      lambda m: m[1] + "（@" + m[2] + "）", base_body)
                assert body == expected
                for relative, digest in item["files"].items():
                    f = skill / relative
                    data = f.read_bytes()
                    assert hashlib.sha256(data).hexdigest() == digest
                    assert not data.startswith(b"\xef\xbb\xbf") and b"\r\n" not in data
                    text = data.decode("utf-8")
                    assert "/Users/" not in text and "C:\\Users\\" not in text
                    if f.suffix == ".md":
                        check_links(f, skill)
                    if relative.startswith("references/"):
                        assert data == (ROOT / relative).read_bytes()
                if item["platform"] != "codex":
                    assert not (skill / "agents").exists()
        result.append({"platform": item["platform"], "status": "passed", "file_count": len(item["files"])})
    for path in ROOT.rglob("*.md"):
        if "build" not in path.relative_to(ROOT).parts:
            check_links(path, ROOT)
    print(json.dumps({"checks": result, "same_editorial_rules": True,
                      "validation_scope": "Structure and extracted contents; no account upload or model invocation"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
