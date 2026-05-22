# Console

## 概述

控制台消息组件

> Console message component

**分类**: 反馈
**在线演示**: [https://www.blazor.zone/console](https://www.blazor.zone/console)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<ConsoleMessageItem>?` | `}` | - |
| `HeaderText` | `string?` | `}` | 获得/设置 Header 显示文字 默认值为 系统监控 |
| `LightTitle` | `string?` | `}` | 获得/设置 指示灯 Title 显示文字 |
| `IsFlashLight` | `bool` | `true` | 获得/设置 指示灯 是否闪烁 默认 true 闪烁 |
| `LightColor` | `Color` | `Color.Success` | 获得/设置 指示灯颜色 |
| `ShowLight` | `bool` | `true` | 获得/设置 是否显示指示灯 默认 true 显示 |
| `AutoScrollText` | `string?` | `}` | 获得/设置 自动滚屏显示文字 |
| `ShowAutoScroll` | `bool` | `}` | 获得/设置 是否显示自动滚屏选项 默认 false |
| `IsAutoScroll` | `bool` | `true` | 获得/设置 是否自动滚屏 默认 true |
| `ClearButtonText` | `string?` | `}` | 获得/设置 按钮 显示文字 默认值为 清屏 |
| `ClearButtonIcon` | `string?` | `}` | 获得/设置 按钮 显示图标 默认值为 fa-solid fa-xmark |
| `ClearButtonColor` | `Color` | `Color.Secondary` | 获得/设置 清除按钮颜色 默认值为 Color.Secondary |
| `OnClear` | `Func<Task>?` | `}` | 获得/设置 清空委托方法 |
| `Height` | `int` | `}` | 获得/设置 组件高度 默认为 126px; |
| `FooterTemplate` | `RenderFragment?` | `}` | 获得/设置 Footer 模板 |
| `HeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 Header 模板 |
| `ItemTemplate` | `RenderFragment<ConsoleMessageItem>?` | `}` | 获得/设置 Item 模板 |
