# ai-skills

Personal collection of AI agent skills. Installable via `npx skills add`.

## Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [bootstrap-blazor-skill](./skills/bootstrap-blazor-skill/SKILL.md) | Bootstrap Blazor 组件文档（111 组件 API + 最佳实践 + 示例代码），消除 AI 幻觉 | `npx skills add https://github.com/xianjin-xu/ai-skills --skill bootstrap-blazor-skill` |
| [commit-review-skill](./skills/commit-review-skill/SKILL.md) | 本地 Commit 代码审查 | `npx skills add https://github.com/xianjin-xu/ai-skills --skill commit-review-skill` |
| [pr-auto-review-skill](./skills/pr-auto-review-skill/SKILL.md) | 自动拉取 PR/MR 进行代码审查 | `npx skills add https://github.com/xianjin-xu/ai-skills --skill pr-auto-review-skill` |

## 安装

```bash
# 安装所有 skills
npx skills add https://github.com/xianjin-xu/ai-skills

# 安装指定 skill
npx skills add https://github.com/xianjin-xu/ai-skills --skill bootstrap-blazor-skill

# 列出可用 skills
npx skills add https://github.com/xianjin-xu/ai-skills --list
```

## Bootstrap Blazor Skill 更新

```bash
# 确保 BootstrapBlazor 源码最新
cd D:\WorkSpace\DotnetProject\BootstrapBlazor
git pull

# 重新生成组件文档（需要 conda py310 环境）
conda activate py310
python scripts/update_docs.py
```
