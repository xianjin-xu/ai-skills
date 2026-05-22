---
name: bootstrap-blazor-skill
description: >
  This skill provides accurate Bootstrap Blazor component documentation and examples.
  It should be used when the user is working with Bootstrap Blazor UI components in a Blazor project,
  including but not limited to: Table, ValidateForm, Dialog, Select, Input, Layout, Button, Row, Stack,
  DateTimePicker, Checkbox, Radio, and all other Bootstrap Blazor components.
  Trigger when the user mentions any Bootstrap Blazor component name, the namespace
  "BootstrapBlazor.Components", or when generating Blazor .razor pages with Bootstrap Blazor tags.
  This skill prevents AI hallucination by providing verified component API documentation
  and official code examples.
---

# Bootstrap Blazor 组件文档 Skill

## 目的

本 Skill 为 **Bootstrap Blazor** UI 组件库提供经过验证的 API 文档、代码示例和最佳实践。
通过确保所有生成的代码仅引用真实的组件属性、方法和参数，消除 AI 的幻觉问题。

Bootstrap Blazor 是一个基于 Bootstrap 的企业级 Blazor 组件库，提供 130+ 组件，用于构建响应式、交互式 Web 应用程序。

官网: https://www.blazor.zone

## 触发条件

当用户提到以下内容时，加载此 Skill：
- 任何 Bootstrap Blazor 组件名称（如 `Table`、`ValidateForm`、`Dialog`、`Select`、`Input`、`Layout`）
- 命名空间 `BootstrapBlazor.Components`
- 正在编写带 Bootstrap Blazor 标签的 `.razor` 文件
- 项目引用了 `BootstrapBlazor` NuGet 包

## 使用流程

### 步骤 1: 识别所需组件

根据用户需求，确定需要哪些 Bootstrap Blazor 组件。
参考 `references/index.md` 获取完整的组件分类索引，快速定位相关组件。

### 步骤 2: 加载组件文档

对每个需要的组件，读取 `references/components/` 中对应的 Markdown 文件：

```
references/components/{component-name}.md
```

组件文件命名规则为 **kebab-case**（连字符小写），例如：
- `Alert` → `alert.md`
- `ValidateForm` → `validate-form.md`
- `DateTimePicker` → `date-time-picker.md`
- `AutoComplete` → `auto-complete.md`

每个组件文档包含:
- **概述**: 组件的中英文描述
- **参数 (Parameters)**: 所有 `[Parameter]` 属性及其类型、默认值、说明
- **事件回调 (EventCallbacks)**: 所有 `EventCallback<T>` 类型的事件
- **代码示例**: 从官方示例页面提取的实际可用代码

### 步骤 3: 参考最佳实践

对于常见模式和架构指导，查阅 `references/best-practices.md`，包括：
- 表单验证模式
- 表格配置模式（分页、搜索、排序）
- 布局模式
- 对话框使用模式
- 全局配置与本地化

### 步骤 4: 生成代码

生成代码时必须：
1. **只使用组件文档中存在的属性和参数**
2. **参考示例代码结构**，替换业务逻辑
3. **不要编造**参数名、枚举值或方法签名
4. 不确定时，优先使用更简单的使用方式
5. 需要时包含 `@using BootstrapBlazor.Components` 命名空间

## 参考文档

| 文档 | 说明 |
|------|------|
| `references/index.md` | 完整组件分类索引，包含各组件的说明和在线演示链接 |
| `references/components/*.md` | 各组件的详细 API 文档和代码示例 |
| `references/best-practices.md` | 常见模式和架构最佳实践 |
| `references/component-url-mapping.md` | 组件名称与官方文档 URL 的映射表 |
