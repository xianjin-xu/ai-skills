---
name: bootstrap-blazor-skill
description: >
  Bootstrap Blazor component documentation skill.
  Use when working with Bootstrap Blazor components in Blazor projects.
  Trigger on: component names (Table, Button, etc.), namespace "BootstrapBlazor.Components",
  or .razor files with Bootstrap Blazor tags.
---

# Bootstrap Blazor Skill

## ⚠️ 重要：组件文档位置

组件详细文档**不在本 Skill 目录中**，而是位于用户本地目录：

- **Windows**: `C:\Users\{Username}\.bootstrap-blazor-docs\components\`
- **Mac/Linux**: `/Users/{username}/.bootstrap-blazor-docs/components/`

如果用户本地目录不存在组件详细文档，请提示用户参考项目 README.md 下载组件文档。

## 使用流程

- 1.加载组件索引, 读取 `references/index.md` 了解有哪些组件可用。
- 2.识别需要的组件, 从索引中找到相关的组件。**不要**读取所有相关组件！仅读取用户明确需要的组件。
- 3.按需读取组件详细文档, 使用 `read_file` 工具读取用户本地目录`.bootstrap-blazor-docs\components\{ComponentName}.md`中的文档.例如：需要使用 Table 组件：read_file: C:\Users\{Username}\.bootstrap-blazor-docs\components\Table.md
- 4.让AI根据文档生成代码用户需要的代码
**规则**：
1. 仅使用文档中存在的属性
2. 不要编造参数名
3. 可参考示例代码

## 示例

**用户**：使用Table组件显示用户列表
**你的行动**：
1. 读取 `references/index.md`（确认 Table 组件存在）
2. 读取 `C:\Users\{Username}\.bootstrap-blazor-docs\components\Table.md`（获取 Table 的详细文档）
3. 生成代码

**不要做**：
- ❌ 读取用户没有提到的其他组件
- ❌ 读取所有 140+ 组件文档（会导致Token 爆炸！）

## 故障排查

### 问题：无法读取组件文档

**原因**：用户还没有下载组件文档到本地目录

**解决**：提示用户参考项目 README.md 下载组件文档
