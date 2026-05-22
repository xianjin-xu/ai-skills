# Button

## 概述

Button 按钮组件

> Button component

**分类**: 基础组件
**在线演示**: [https://www.blazor.zone/button](https://www.blazor.zone/button)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsAutoFocus` | `bool` | `}` | 获得/设置 是否自动获取焦点，默认为 false |

## 代码示例

### 基本用法

```razor
<Button Color="Color.Primary">@Localizer["ButtonOne"]</Button>
<Button Color="Color.Success">@Localizer["ButtonTwo"]</Button>
```

### 基本用法

```razor
<Button Color="Color.Primary" Icon="fa-solid fa-font-awesome" Text="@Localizer["ButtonStatus"]"></Button>
<Button Color="Color.Info" Icon="fa-solid fa-spinner fa-spin fa-fw" Text="@Localizer["ButtonProgress"]"></Button>
```
