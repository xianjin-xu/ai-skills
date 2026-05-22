# Textarea

## 概述

Textarea 文本域组件

> Textarea Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/textarea](https://www.blazor.zone/textarea)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsAutoScroll` | `bool` | `}` | 获得/设置 是否自动滚动，默认为 false |
| `UseShiftEnter` | `bool` | `}` | 获得/设置 是否 Shift + Enter 替代默认 Enter 键行为，默认为 false |

## 代码示例

### 基本用法

```razor
<Textarea PlaceHolder="@Localizer["TextAreaPlaceHolder"]" rows="4" @bind-Value="@Text"></Textarea>
```

### 基本用法

```razor
<Textarea rows="4" autocomplete="off" autocorrect="off" spellcheck="false"
              UseInputEvent="true" UseShiftEnter="true" PlaceHolder="@Localizer["TextAreaUseShiftEnterPlaceHolder"]"
              @bind-Value="@KeyText"></Textarea>
```

### 基本用法

```razor
<Textarea rows="4" OnEnterAsync="OnEnterAsync" OnEscAsync="OnEscAsync"
              PlaceHolder="@Localizer["TextAreaKeyEventPlaceHolder"]"></Textarea>
```
