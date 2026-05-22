# Badge

## 概述

Badge 徽章组件

> Badge component

**分类**: 基础组件
**在线演示**: [https://www.blazor.zone/badge](https://www.blazor.zone/badge)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.Primary` | 获得/设置 徽章颜色 默认为 <see cref="Color.Primary"/> |
| `IsPill` | `bool` | `}` | - |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件内容 默认为 false |

## 代码示例

### 基本用法

```razor
<Badge Color="Color.Danger">1</Badge>
<Badge Color="Color.Success"><span style="padding: 0 2px;">8</span></Badge>
```
