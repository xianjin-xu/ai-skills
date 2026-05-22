# ColorPicker

## 概述

ColorPicker 颜色拾取器组件

> ColorPicker component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/color-picker](https://www.blazor.zone/color-picker)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Template` | `RenderFragment<string>?` | `}` | 获得/设置 显示模板 |
| `Task` | `Func<string,` | `}` | 获得/设置 显示颜色值格式化回调方法 |
| `IsSupportOpacity` | `bool` | `}` | 获得/设置 是否支持透明度 默认 false 不支持 |
| `Swatches` | `List<string>?` | `}` | - |

## 代码示例

### 基本用法

```razor
<ColorPicker Value="@Value"></ColorPicker>
```

### 基本用法

```razor
<ColorPicker @bind-Value="@Value"></ColorPicker>
```

### 基本用法

```razor
<ColorPicker Value="@Value" IsDisabled="true"></ColorPicker>
```

### 基本用法

```razor
<ColorPicker Value="@Value">
        <Template>
            <input type="text" class="form-control" readonly value="@FormatValue(context)" />
        </Template>
    </ColorPicker>
```

### 基本用法

```razor
<ColorPicker Value="@Value" Formatter="FormatValueAsync"></ColorPicker>
```
