# 上传 GitHub 与发布版本

## 上传仓库

在GitHub创建一个名为 `univ-chem-education-polish` 的仓库。将本目录中的文件和子目录上传，使 `README.md` 与 `SKILL.md` 直接出现在仓库根目录。不要将外层总包再多嵌套一层。

本目录是公开源码与说明；不需要上传生成本包时的其他工作区、私人稿件或原论文PDF。维护者可在建仓时决定可见性与许可证。本包未代替维护者选择 `LICENSE`。

## 发布安装包

仓库上传完成后，进入 `Releases → Draft a new release`，建立标签 `v1.0.0`。将 `dist/` 中六个ZIP/.skill文件及 `SHA256SUMS.txt` 作为附件上传，填写功能与验证范围，再发布。

README中已经使用相对路径指向仓库的安装文件，不需要先填GitHub用户名。发布Releases后，可将这些下载链接改为实际Release附件地址。发布操作见[GitHub官方说明](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)。

## 更新维护

修改技能源文件后先测试，再更新 `release-config.json` 中的版本，运行：

```bash
python3 scripts/build_release.py
python3 scripts/validate_release.py
```

同步更新README中的下载链接、安装示例中的版本号和验证记录，上传新文件并建立新版本标签。不要把旧模型或旧平台的测试结果自动标成新版本已验证。构建脚本不上传文件、不安装技能、不改用户配置。

如希望提供类似其他开源技能的安装命令，可在发布后实测该仓库是否能被通用技能安装器发现，再将实测命令写入README。平台专用导入仍使用对应安装包。
