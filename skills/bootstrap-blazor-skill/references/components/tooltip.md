# Tooltip

## 概述

Tooltip 组件

> Tooltip Component

**分类**: 反馈
**在线演示**: [https://www.blazor.zone/tooltip](https://www.blazor.zone/tooltip)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Delay` | `string?` | `}` | - |
| `Selector` | `string?` | `}` | - |
| `Title` | `string?` | `}` | - |
| `GetTitleCallback` | `Func<Task<string>>?` | `}` | 获得/设置 获取显示内容的异步回调方法，默认 null |
| `IsHtml` | `bool` | `}` | - |
| `Sanitize` | `bool` | `true` | - |
| `Placement` | `Placement` | `Placement.Top` | - |
| `FallbackPlacements` | `string[]?` | `}` | 获得/设置 位置，默认为 null |
| `Offset` | `string?` | `}` | 获得/设置 偏移量，默认为 null |
| `CustomClass` | `string?` | `}` | - |
| `Trigger` | `string?` | `}` | - |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |

## 代码示例

### 基本用法

```razor
<Tooltip Title="Test tooltip">
        <i class="fa-solid fa-flag" />
    </Tooltip>
```

### 基本用法

```razor
<Tooltip Title="@HtmlString" IsHtml="true" Sanitize="false" Selector=".tooltip-selector">
        <div>
            <i class="fa-solid fa-flag" />
            <span class="tooltip-selector ms-2">This is Tooltip</span>
        </div>
    </Tooltip>
```

### 基本用法

```razor
<Tooltip Title="Test tooltip" CustomClass="is-invalid">
        <i class="fa-solid fa-flag" />
    </Tooltip>
```

### 基本用法

```razor
<Tooltip Title="Manual trigger tooltip" Trigger="manual" @ref="_tooltip">
        <TooltipContent></TooltipContent>
    </Tooltip>
```
