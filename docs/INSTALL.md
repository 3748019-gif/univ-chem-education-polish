# 安装说明

技能名统一为 `univ-chem-education-polish`。每个安装包只有一个同名顶层目录，目录中有 `SKILL.md` 和参考资料。复制时保留整个目录；若已有同名个人修改，先备份，不同时保留多个同名副本。

## Codex

下载Codex ZIP，解压后将 `univ-chem-education-polish` 文件夹放到用户目录：

```text
~/.agents/skills/univ-chem-education-polish/
```

项目内安装可放在 `.agents/skills/`。Windows的 `~` 表示当前用户主目录；可在资源管理器中进入用户目录后创建 `.agents/skills`。

安装后在技能列表中查找，或输入 `$univ-chem-education-polish` 加稿件任务。未出现时重启或新建会话。也可以让Codex自带的skill-installer从发布后的GitHub仓库安装。

这是独立技能目录的本地安装方式，不是插件市场上架包。[官方说明](https://learn.chatgpt.com/docs/build-skills)

## WorkBuddy

使用专门的WorkBuddy ZIP。此包增加中英文名称、介绍、版本和作者字段，入口引用采用 `@references/`。

在WorkBuddy的技能界面，使用添加或上传本地技能的入口选择该ZIP；界面名称以当前版本为准。若通过开放平台提交，也上传此包。导入后启用技能，使用统一名称发一个短段落润色任务，确认返回修改稿和补证项。

不要把Codex包当成WorkBuddy市场元数据包。上传功能或权限由当前客户端和账号决定。[官方结构与上传说明](https://open.workbuddy.cn/docs/skill)

## Gemini CLI

使用后缀为 `.skill` 的文件，不先改成 `.zip`。在文件所在目录执行：

```bash
gemini skills install ./univ-chem-education-polish-gemini-cli-v1.0.0.skill --scope user
gemini skills list
```

也可解压同结构包后执行 `gemini skills install ./univ-chem-education-polish --scope user`。如需项目范围，按CLI的scope选项安装。交互会话用 `/skills reload` 重载，再用 `/skills list` 检查；明确要求使用本技能并接受宿主的激活提示。

`.skill` 是ZIP容器，但CLI对其后缀有专门处理，不能假定普通ZIP可以直接安装。[管理说明](https://geminicli.com/docs/cli/using-agent-skills/) · [创建说明](https://geminicli.com/docs/cli/creating-skills/)

## Gemini 网页

下载Gemini网页ZIP。在网页版进入 `Customize → Skills → Create → Upload`，上传ZIP并检查名称与说明后创建。聊天中通过 `/` 或 `@` 的技能选择入口调用，具体入口以当前界面为准。

官方要求登录、年满18岁并开启相应活动设置；账号功能开放情况以实际菜单为准。本包只有纯文本指令和参考资料，不包含Word/Excel二进制或联网脚本。看不到Skills菜单时先确认账号与功能开放情况，不把ZIP上传到普通聊天窗口当作已安装。[官方说明](https://support.google.com/gemini/answer/17094296)

## Claude Code

下载Claude Code ZIP，解压完整技能目录到：

```text
~/.claude/skills/univ-chem-education-polish/
```

项目内可放在 `.claude/skills/`。启动Claude Code后使用：

```text
/univ-chem-education-polish 请润色这篇化学教育论文，保留结构与观点，集中列出补证事项。
```

在 `/skills` 或斜杠菜单核对发现情况；新增目录未出现时重载技能或重启会话。该包是独立技能，不需要插件清单。[官方说明](https://code.claude.com/docs/en/skills)

## Claude 网页

下载Claude网页ZIP，先确认代码执行与文件创建功能开启，再进入 `Customize → Skills → + → Create skill → Upload a skill` 上传并启用。发一个明确点名技能的短段落任务，确认它按该技能处理。组织账号还可能受管理员策略影响。[官方说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 安装后检查

先用不含私密内容的短段落，例如：“A方案80学分，B方案120 ECTS，因此B训练更强。”要求用本技能修改。结果应保留原数值、指出单位不可直接比较，并给出相应补证事项。

能看到技能条目只证明安装或发现成功。是否读全稿件、正确修订并保留文档格式，还需看实际任务结果。宿主缺少Word或PDF能力时，可提供文本稿或使用该宿主支持的文档工具。
