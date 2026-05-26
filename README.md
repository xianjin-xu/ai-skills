# ai-skills

Personal collection of AI agent skills. Installable via `npx skills add`.

## Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [bootstrap-blazor-skill](./skills/bootstrap-blazor-skill/SKILL.md) | Bootstrap Blazor 组件文档（140+ 组件 API + 最佳实践 + 示例代码），消除 AI 幻觉 | `npx skills add https://github.com/xianjin-xu/ai-skills --skill bootstrap-blazor-skill` |
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

## Bootstrap Blazor Skill 使用说明

### 1. 下载组件文档

Bootstrap Blazor Skill 需要额外的组件说明文档才能正常工作。请按照以下步骤下载：

#### 方式 1：从 GitHub Releases 下载（推荐）

1. 访问：[GitHub Releases](https://github.com/xianjin-xu/ai-skills/releases)
2. 下载最新版本的 `bootstrap-blazor-docs.zip`
3. 解压到用户目录：
   - **Windows**: `C:\Users\{YourUsername}\.bootstrap-blazor-docs\`
   - **Mac/Linux**: `/Users/{your-username}/.bootstrap-blazor-docs/`

#### 方式 2：从源码构建（开发者）

如果您是开发者，想要从源码生成组件文档：

```bash
# 确保 BootstrapBlazor 源码最新
cd D:\WorkSpace\DotnetProject\BootstrapBlazor
git pull

# 重新生成组件文档（需要 conda py310 环境）
conda activate py310
python skills/bootstrap-blazor-skill/scripts/update_docs.py

# 组件文档将生成到 .bootstrap-blazor-docs/ 目录
```

然后将 `.bootstrap-blazor-docs/` 目录复制到用户目录：
- **Windows**: `C:\Users\{YourUsername}\.bootstrap-blazor-docs\`
- **Mac/Linux**: `/Users/{your-username}/.bootstrap-blazor-docs/`

### 2. 验证安装

下载完成后，目录结构应该如下：

```
用户目录 (~)
└── .bootstrap-blazor-docs/
    └── components/
        ├── Table.md
        ├── Button.md
        ├── Input.md
        └── ... (140+ 组件文档)
```

### 3. 开始使用

现在您可以在 AI IDE 中使用 Bootstrap Blazor Skill 了。当您提到 Bootstrap Blazor 组件时，Skill 会自动触发并帮助您生成代码。

**示例对话**：

```
用户：帮我做一个 Table 显示用户列表

AI：好的，让我先查看 Table 组件的文档...
[AI 会自动读取 C:\Users\{Username}\.bootstrap-blazor-docs\components\Table.md]
[然后根据文档生成代码]
```

## Bootstrap Blazor Skill 更新

```bash
# 确保 BootstrapBlazor 源码最新
cd D:\WorkSpace\DotnetProject\BootstrapBlazor
git pull

# 重新冲官方地址中抓取组件的详细说明文档（需要 conda py310 环境）
conda activate py310
python skills/bootstrap-blazor-skill/scripts/scrape_bootstrap_blazor.py
```

## 项目结构

```
ai-skills/
├── README.md                           # 本文件
├── skills/
│   ├── bootstrap-blazor-skill/        # Bootstrap Blazor Skill
│   │   ├── SKILL.md                   # Skill 定义（很小，~2KB）
│   │   └── references/
│   │       └── index.md     # 组件索引（轻量，~3KB）
└── .bootstrap-blazor-docs/            # 组件文档（需要下载到用户目录）
    └── components/                    # 140+ 组件文档（.md 文件）
        ├── Table.md
        ├── Button.md
        ├── Input.md
        └── ...
```

## 常见问题

### Q: 为什么组件文档不在 Git 仓库中？

A: 组件文档体积较大（~5MB），不适合放在 Git 仓库, 否则Token消耗非常大。通过下载方式可以保证：
- Git 仓库体积小，克隆速度快
- 组件文档可以独立更新
- 减少 Skill 的加载时间，降低 Token 消耗

### Q: 我可以修改组件文档吗？

A: 可以。组件文档在您的用户目录中，您可以自由修改。但建议先通过 `scrape_bootstrap_blazor.py`抓取官方详细说明文档，以保证与官方文档同步；然后通过 `generate_components.py` 脚本结合AI生成。

### Q: Skill 触发后，AI 会读取所有组件文档吗？

A: 不会。Skill 设计为按需加载：
1. AI 首先读取轻量索引（~5KB）
2. 然后根据用户需求，只读取需要的个相关组件的详细文档（3~10KB each）
3. 总 Token 消耗约 50KB

## 许可证

[MIT License](LICENSE)
