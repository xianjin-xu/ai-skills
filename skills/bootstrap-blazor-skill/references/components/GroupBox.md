# GroupBox

## 概述

GroupBox 组件

> GroupBox component

**分类**: 基础组件
**在线演示**: [https://www.blazor.zone/group-box](https://www.blazor.zone/group-box)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |
| `Title` | `string?` | `}` | 获得/设置 Title 属性 默认为 null |

## 代码示例

### 基本用法

```razor
<GroupBox Title="@Localizer["GroupTitle"]">
        <p>@((MarkupString)Localizer["GroupP1"].Value)</p>
        <p>@((MarkupString)Localizer["GroupP2"].Value)</p>
    </GroupBox>
```
