#!/usr/bin/env python3
"""Create native skill bundles; no network access or user configuration writes."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = {
    "codex": ".zip", "workbuddy": ".zip", "gemini-cli": ".skill",
    "gemini-web": ".zip", "claude-code": ".zip", "claude-web": ".zip",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def quoted(value):
    return json.dumps(value, ensure_ascii=False)


def main():
    config = json.loads((ROOT / "release-config.json").read_text(encoding="utf-8"))
    name, version = config["name"], config["version"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Invalid skill name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid version")
    source = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    _, front, body = source.split("---", 2)
    base_files = {"SKILL.md": source.encode("utf-8")}
    for path in sorted((ROOT / "references").iterdir()):
        if path.is_file() and path.suffix in {".md", ".json"}:
            base_files[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    packages = []
    for platform, ext in PLATFORMS.items():
        files = dict(base_files)
        if platform == "codex":
            files["agents/openai.yaml"] = (ROOT / "agents/openai.yaml").read_bytes()
        if platform == "workbuddy":
            fields = {
                "name": name, "display_name": config["display_name"],
                "display_name_en": config["display_name_en"],
                "description": config["description_en"],
                "description_zh": config["description_zh"],
                "description_en": config["description_en"],
                "version": version, "author": config["author"],
            }
            wb_body = re.sub(r"\[([^\]]+)\]\((references/[^)]+)\)",
                             lambda m: m[1] + "（@" + m[2] + "）", body)
            header = "\n".join(k + ": " + quoted(v) for k, v in fields.items())
            files["SKILL.md"] = ("---\n" + header + "\n---" + wb_body).encode("utf-8")
        filename = f"{name}-{platform}-v{version}{ext}"
        with zipfile.ZipFile(output / filename, "w", zipfile.ZIP_DEFLATED) as archive:
            for relative, data in sorted(files.items()):
                info = zipfile.ZipInfo(name + "/" + relative, (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        raw = (output / filename).read_bytes()
        packages.append({"platform": platform, "file": filename,
                         "sha256": sha(raw), "bytes": len(raw),
                         "files": {key: sha(value) for key, value in sorted(files.items())}})
    manifest = {"name": name, "version": version, "packages": packages,
                "archive_layout": "single named root directory",
                "scope": "Local release artifacts; no automatic upload or installation"}
    (ROOT / "RELEASE.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sums = "".join(item["sha256"] + "  " + item["file"] + "\n" for item in packages)
    (output / "SHA256SUMS.txt").write_text(sums, encoding="utf-8")
    print(json.dumps({"name": name, "version": version, "packages": len(packages)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
