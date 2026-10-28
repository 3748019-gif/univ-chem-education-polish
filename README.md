# 大学化学教育论文润色

`univ-chem-education-polish` 帮助作者修改拟投《大学化学》的培养方案、国际比较与教学改革论文：保留作者结构和主要观点，检查逻辑、润色措辞、校准比较与结论口径，并集中指出需要补证的位置。

公开版 v1.0.0。它是按当前稿件工作的通用编辑技能，不预设学校名单、样本数量或章节数。技能文件提供方法，实际阅读与修改由调用它的 AI 模型完成。

## 可以处理什么

- 已有论文的逻辑、段落衔接、用词和证据范围。
- 调研报告改为论文时，研究问题、材料来源与建议的衔接。
- 学校与培养路线、不同学分制、必修与选修、拟行与已实施的区别。
- 课程和资源建设、学生反馈、学习结果与因果解释的区别。
- 确定事项直接修改，实质性论点变化交作者决定，补证事项集中列出。

方法参考153篇《大学化学》论文的编辑观察。[书目索引](references/corpus-index.json)保留题名、DOI和简短观察，不附论文全文。它不是期刊官方投稿指南，也不保证文章录用；需要引用或核实政策、学校事实时，应回到原始来源。

## 下载与安装

| 使用环境 | 下载文件 | 安装入口 |
| --- | --- | --- |
| Codex | [Codex ZIP](https://github.com/3748019-gif/univ-chem-education-polish/releases/download/v1.0.0/univ-chem-education-polish-codex-v1.0.0.zip) | 解压技能目录至用户技能目录 |
| WorkBuddy | [WorkBuddy ZIP](https://github.com/3748019-gif/univ-chem-education-polish/releases/download/v1.0.0/univ-chem-education-polish-workbuddy-v1.0.0.zip) | 技能上传入口；包含专用展示元数据 |
| Gemini CLI | [Gemini CLI .skill](https://github.com/3748019-gif/univ-chem-education-polish/releases/download/v1.0.0/univ-chem-education-polish-gemini-cli-v1.0.0.skill) | `gemini skills install` |
| Gemini 网页 | [Gemini 网页 ZIP](https://github.com/3748019-gif/univ-chem-education-polish/releases/download/v1.0.0/univ-chem-education-polish-gemini-web-v1.0.0.zip) | Customize → Skills → Upload |
| Claude Code | [Claude Code ZIP](https://github.com/3748019-gif/univ-chem-education-polish/releases/download/v1.0.0/univ-chem-education-polish-claude-code-v1.0.0.zip) | 解压至 `.claude/skills` |
| Claude 网页 | [Claude 网页 ZIP](https://github.com/3748019-gif/univ-chem-education-polish/releases/download/v1.0.0/univ-chem-education-polish-claude-web-v1.0.0.zip) | Customize → Skills → Upload a skill |

具体目录、命令、账号条件和安装后的检查见[安装说明](docs/INSTALL.md)。GitHub 的整个仓库源码 ZIP 用于查看和维护；上传技能时请选上表中对应的单技能包。

## 开始使用

安装后上传或指定稿件，再输入：

> 使用 univ-chem-education-polish 修改这篇化学教育论文。请保留原结构和主要观点，检查逻辑、措辞、数据与结论口径，交付修改稿及集中补证清单。不要新增未做过的研究或未提供的事实。

也可以限定任务，例如“只检查摘要与正文是否一致”“只处理课程比较的计数口径”“用真实修订模式修改Word，保留原格式”。正文、补证清单和修改说明的取舍以当次指令为准。

详细流程与示例见[使用说明](docs/USAGE.md)、[编辑方法](references/editorial-method.md)和[模拟修改示例](references/examples.md)。无需为每次润色准备153篇全文；若要核实其中某篇的具体引文，则须取得对应原文。

## 验证范围

发布前检查文件结构、元数据、相对引用、四个平台共用规则的一致性，以及模拟论文的编辑行为。结果和限制见[验证记录](docs/VALIDATION.md)。

平台安装格式与模型实际编辑效果是两件事。本包的网页导入和其他厂商模型调用状态会如实列出，不把同一模型读取不同封装的测试称为跨模型实测。

## 文件与维护

`SKILL.md` 是入口，`references/` 是按需参考，`agents/openai.yaml` 是Codex界面信息；`tests/` 保存纯模拟测试材料；`scripts/` 只用于维护者构建和检查发布包，不是润色时必须安装的依赖。

重新生成安装包：

```bash
python3 scripts/build_release.py
python3 scripts/validate_release.py
```

构建与检查脚本使用 Python 3.10 及以上的标准库。使用技能本身不要求额外Python包或模型API密钥；文件读取、联网和Word处理能力由宿主提供。

上传仓库与发布附件的步骤见[GitHub发布说明](docs/PUBLISH.md)。版本与包校验信息见[RELEASE.json](RELEASE.json)及[SHA256SUMS.txt](dist/SHA256SUMS.txt)。当前包未附独立开源许可证；维护者可在公开发布时选择并补充 `LICENSE`。
