# ColorPicker (颜色选择器)

## 概述

`ColorPicker` 是一个颜色选择器组件，提供颜色选择功能，支持透明度、预设颜色等配置。

> ColorPicker component

**分类**: 表单输入  
**在线演示**: [https://www.blazor.zone/color-picker](https://www.blazor.zone/color-picker)

## 使用场景

### 1. 基本用法

```razor
<ColorPicker @bind-Value="ColorValue" />
```

```csharp
@code {
    string ColorValue { get; set; } = "#ff0000";
}
```

### 2. 支持透明度

```razor
<ColorPicker @bind-Value="ColorValue" IsSupportOpacity="true" />
```

### 3. 预设颜色

```razor
<ColorPicker @bind-Value="ColorValue" IsSupportOpacity="true" Swatches="PresetColors" />
```

```csharp
@code {
    List<string> PresetColors = new List<string>
    {
        "rgba(244, 67, 54, 1)",
        "rgba(233, 30, 99, 0.95)",
        "rgba(156, 39, 176, 0.9)"
    };
}
```

### 4. 自定义模板

```razor
<ColorPicker @bind-Value="ColorValue">
    <Template>
        <input type="text" class="form-control" readonly value="@context" />
    </Template>
</ColorPicker>
```

### 5. 禁用状态

```razor
<ColorPicker Value="ColorValue" IsDisabled="true" />
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置组件值（颜色值） |
| `Template` | `RenderFragment<string>?` | `null` | 获得/设置显示模板 |
| `Formatter` | `Func<string, Task<string>>?` | `null` | 获得/设置显示颜色值格式化回调方法 |
| `IsSupportOpacity` | `bool` | `false` | 获得/设置是否支持透明度 |
| `Swatches` | `List<string>?` | `null` | 获得/设置预设候选颜色（开启 `IsSupportOpacity` 时生效） |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用组件 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `ValueChanged` | 值改变时触发 |

## 最佳实践

1. **值绑定**: 使用 `Value` 参数绑定到字符串类型变量（颜色值格式如 `#ff0000` 或 `rgba(255,0,0,1)`）
2. **透明度支持**: 设置 `IsSupportOpacity="true"` 启用透明度选择
3. **预设颜色**: 使用 `Swatches` 参数提供预设颜色列表
4. **自定义显示**: 使用 `Template` 参数自定义颜色显示方式
5. **格式化显示**: 使用 `Formatter` 回调自定义颜色值显示格式
6. **禁用状态**: 使用 `IsDisabled` 参数禁用颜色选择器

## 常见问题

### Q: 如何绑定颜色值？
A: 使用 `Value` 参数绑定到 `string` 类型变量，支持 `#ff0000` 或 `rgba(255,0,0,1)` 格式。

### Q: 如何支持透明度选择？
A: 设置 `IsSupportOpacity="true"` 启用透明度选择功能。

### Q: 如何设置预设颜色？
A: 使用 `Swatches` 参数提供颜色字符串列表，格式为 `["rgba(244, 67, 54, 1)", ...]`。

### Q: 如何自定义颜色显示？
A: 使用 `Template` 参数自定义颜色显示方式，例如显示颜色方块和文本。

### Q: 如何禁用颜色选择器？
A: 设置 `IsDisabled="true"` 禁用颜色选择器，用户无法选择颜色。
