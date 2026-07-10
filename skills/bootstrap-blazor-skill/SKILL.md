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
  - 💡 **进阶提示**：若任务涉及**表单验证、Table 高级功能（分页/编辑/导出）、Dialog/Modal、全局配置、本地化**，建议额外阅读 `references/best-practices.md` 避免常见陷阱。
- 3.按需读取组件详细文档, 使用 `read_file` 工具读取用户本地目录`.bootstrap-blazor-docs\components\{ComponentName}.md`中的文档.例如：需要使用 Table 组件：read_file: C:\Users\{Username}\.bootstrap-blazor-docs\components\Table.md
- 4.让AI根据文档生成代码用户需要的代码

## 强制规则

- 必须使用 BootstrapBlazor 组件，禁止直接使用 <div> 实现布局/UI，除非该 UI 模式确实没有对应组件。
- 仅有在确认 BootstrapBlazor 没有提供对应组件时，才可以使用原生 HTML 标签替代。
- 不确定是否有对应组件时，优先查 references/index.md 确认，而不是直接回退到 <div>。
- 仅使用文档中存在的属性，不要编造不存在的属性，参数名或枚举值。
- 可参考文档中的示例代码，但需适配当前项目的实际模型和数据。

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
