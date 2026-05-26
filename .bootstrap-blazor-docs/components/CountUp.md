# CountUp (计数器)

## 概述

`CountUp` 组件用于**报表数据动态展示，数字以跳动的形式展现**。组件支持多种配置选项，包括动画时长、小数位数、前缀后缀、分组分隔符等。

**主要特性**：
- 支持动态数字跳动展示
- 支持动画时长设置（`Duration`）
- 支持小数位数设置（`DecimalPlaces`）
- 支持前缀和后缀文本（`Prefix`、`Suffix`）
- 支持数字分组和分隔符（`UseGrouping`、`Separator`）
- 支持滚动监听（`EnableScrollSpy`）
- 支持计数结束回调（`OnCompleted`）
- 支持自定义配置项（`Option`）

**在线演示**: https://www.blazor.zone/count-up

---

## 使用场景

### 1. 基础用法（简单计数器）

通过设置 `Value` 参数赋值，更改配置后，改变 `Value` 值后生效。

```razor
<!-- 基础计数器 -->
<CountUp TValue="double" Value="@Value" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
}
```

---

### 2. 设置动画时长（Duration）

通过 `Option` 参数设置 `Duration` 属性，控制动画时长（单位：秒）。

```razor
<!-- 设置动画时长 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        Duration = 3.0f // 3秒动画
    };
}
```

---

### 3. 设置小数位数（DecimalPlaces）

通过 `Option` 参数设置 `DecimalPlaces` 属性，控制小数位数。

```razor
<!-- 设置小数位数 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.5678;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        DecimalPlaces = 2 // 显示2位小数
    };
}
```

---

### 4. 设置前缀和后缀（Prefix/Suffix）

通过 `Option` 参数设置 `Prefix` 和 `Suffix` 属性，添加前缀和后缀文本。

```razor
<!-- 设置前缀和后缀 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        Prefix = "$", // 前缀：美元符号
        Suffix = " USD" // 后缀：货币单位
    };
}
```

---

### 5. 设置分隔符（Separator）

通过 `Option` 参数设置 `Separator` 属性，控制千分位分隔符。

```razor
<!-- 设置分隔符 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234567.89;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        Separator = ",", // 使用逗号作为分隔符
        UseGrouping = true // 启用分组
    };
}
```

---

### 6. 设置小数点符号（Decimal）

通过 `Option` 参数设置 `Decimal` 属性，控制小数点符号。

```razor
<!-- 设置小数点符号 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        Decimal = ".", // 使用点作为小数点
        DecimalPlaces = 2
    };
}
```

---

### 7. 启用滚动监听（EnableScrollSpy）

通过 `Option` 参数设置 `EnableScrollSpy` 属性，启用滚动监听，当组件进入视口时触发动画。

```razor
<!-- 启用滚动监听 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        EnableScrollSpy = true, // 启用滚动监听
        ScrollSpyDelay = 200, // 滚动延时 200ms
        ScrollSpyOnce = false // 是否只监听一次
    };
}
```

---

### 8. 计数结束回调（OnCompleted）

通过 `OnCompleted` 参数设置计数结束回调方法。

```razor
<!-- 计数结束回调 -->
<CountUp TValue="double" Value="@Value" OnCompleted="OnCountCompleted" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private async Task OnCountCompleted()
    {
        // 计数结束后的处理
        Console.WriteLine("计数动画结束");
        await Task.CompletedTask;
    }
}
```

---

### 9. 设置起始值（StartValue）

通过 `Option` 参数设置 `StartValue` 属性，控制计数起始值。

```razor
<!-- 设置起始值 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1000.0;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        StartValue = 0 // 从0开始计数
    };
}
```

---

### 10. 使用缓动动画（UseEasing）

通过 `Option` 参数设置 `UseEasing` 属性，控制是否使用过渡动画。

```razor
<!-- 使用缓动动画 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        UseEasing = true, // 启用缓动动画
        EasingAmount = 333, // 动画总量
        EasingThreshold = 999 // 动画阈值
    };
}
```

---

### 11. 禁用分组（UseGrouping）

通过 `Option` 参数设置 `UseGrouping` 属性，控制是否启用数字分组。

```razor
<!-- 禁用分组 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234567.89;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        UseGrouping = false // 禁用分组，不显示千分位分隔符
    };
}
```

---

### 12. 使用印度式分隔符（UseIndianSeparators）

通过 `Option` 参数设置 `UseIndianSeparators` 属性，控制是否使用印度式数字分隔符。

```razor
<!-- 使用印度式分隔符 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234567.89;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        UseIndianSeparators = true // 使用印度式分隔符
    };
}
```

---

### 13. 自定义数字字形（Numerals）

通过 `Option` 参数设置 `Numerals` 属性，自定义数字字形替换数组。

```razor
<!-- 自定义数字字形 -->
<CountUp TValue="double" Value="@Value" Option="_option" class="fw-bold fs-1 mb-2 d-block" />

@code {
    private double Value { get; set; } = 1234.56;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        Numerals = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }
        // 可以替换为其他字符集，例如罗马数字、中文数字等
    };
}
```

---

### 14. 完整示例（包含所有配置）

```razor
<!-- 完整计数器示例 -->
<CountUp 
    TValue="double" 
    Value="@Value" 
    Option="_option" 
    OnCompleted="OnCountCompleted" 
    class="fw-bold fs-1 mb-2 d-block" />

<div class="mb-3">
    <Button OnClick="UpdateValue">更新数值</Button>
</div>

@code {
    private double Value { get; set; } = 0;
    
    private CountUpOption _option { get; set; } = new CountUpOption
    {
        StartValue = 0,
        Duration = 2.0f,
        DecimalPlaces = 2,
        Decimal = ".",
        UseEasing = true,
        UseGrouping = true,
        Separator = ",",
        Prefix = "$",
        Suffix = " USD",
        Numerals = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' },
        EnableScrollSpy = false,
        ScrollSpyDelay = 200,
        ScrollSpyOnce = false
    };
    
    private async Task OnCountCompleted()
    {
        Console.WriteLine("计数动画结束");
        await Task.CompletedTask;
    }
    
    private void UpdateValue()
    {
        Value = 1234.56;
    }
}
```

---

## 参数 (Parameters)

### CountUp 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `OnCompleted` | `Func<Task>?` | `null` | 获得/设置 计数结束回调方法 默认 null |
| `Option` | `CountUpOption?` | `null` | 获得/设置 计数配置项 默认 null |
| `Value` | `TValue` | `default` | 获得/设置 Value 值 |

---

### CountUpOption 配置项参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Decimal` | `string?` | `.` | 小数点符号 默认 点 |
| `DecimalPlaces` | `int` | `0` | 小数位数 默认 0 |
| `Duration` | `float` | `2.0` | 动画时长 默认 2.0 单位秒 |
| `EnableScrollSpy` | `bool` | `false` | 是否启用滚动监听 默认 false |
| `Numerals` | `char[]?` | `null` | 数字字形替换数组 默认值为空 |
| `Prefix` | `string?` | `string.Empty` | 前缀文本 默认 string.Empty 未设置 |
| `ScrollSpyDelay` | `int` | `200` | 滚动延时 默认 200 毫秒 |
| `ScrollSpyOnce` | `bool` | `false` | 滚动监听一次 默认 false |
| `Separator` | `string?` | `,` | 分隔符 默认 逗号 , |
| `EasingAmount` | `int` | `333` | 动画总量 默认 333 |
| `EasingThreshold` | `int` | `999` | 动画阈值 默认 999 |
| `StartValue` | `decimal` | `0` | 开始计数值 默认 0 |
| `Suffix` | `string?` | `string.Empty` | 后缀文本 默认 string.Empty 未设置 |
| `UseEasing` | `bool` | `true` | 是否使用过渡动画 默认 true |
| `UseGrouping` | `bool` | `true` | 是否分组 默认 true |
| `UseIndianSeparators` | `bool` | `false` | 是否使用分隔符 默认 false |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnCompleted` | `Func<Task>?` | 计数结束回调方法 |

---

## 最佳实践

1. **设置合适的动画时长**：通过 `Duration` 参数控制动画时长，避免过长或过短影响用户体验
2. **使用前缀后缀**：通过 `Prefix` 和 `Suffix` 添加单位或符号，使数字更具可读性
3. **启用分组显示**：设置 `UseGrouping="true"` 并配置 `Separator`，使大数字更易读
4. **滚动监听优化**：对于长页面，使用 `EnableScrollSpy="true"` 在组件进入视口时触发动画
5. **计数结束处理**：使用 `OnCompleted` 回调在计数结束后执行额外逻辑，例如显示提示、加载数据等
6. **自定义起始值**：通过 `StartValue` 设置计数起始值，适合从非零点开始计数的场景
7. **缓动动画配置**：通过 `UseEasing`、`EasingAmount`、`EasingThreshold` 配置缓动动画效果
8. **更新数值触发动画**：更改 `Value` 值后，计数动画会重新触发，适合动态数据展示

---

## 常见问题

### 1. 如何触发计数动画？

**回答**：更改 `Value` 参数的值后，计数动画会自动触发。

### 2. 如何设置动画时长？

**回答**：通过 `Option` 参数的 `Duration` 属性设置动画时长，单位为秒，默认值为 2.0 秒。

### 3. 如何添加前缀或后缀？

**回答**：通过 `Option` 参数的 `Prefix` 和 `Suffix` 属性添加前缀和后缀文本。

### 4. 如何启用滚动监听？

**回答**：设置 `Option` 参数的 `EnableScrollSpy="true"`，当组件进入视口时会自动触发计数动画。

### 5. 计数结束后如何执行回调？

**回答**：使用 `OnCompleted` 参数设置计数结束回调方法，该方法在计数动画结束后被调用。

### 6. 如何设置小数位数？

**回答**：通过 `Option` 参数的 `DecimalPlaces` 属性设置小数位数，默认值为 0。

### 7. 如何自定义分隔符？

**回答**：通过 `Option` 参数的 `Separator` 属性设置分隔符，默认值为逗号 `,`。

### 8. 如何禁用分组显示？

**回答**：设置 `Option` 参数的 `UseGrouping="false"` 禁用分组显示，不显示千分位分隔符。

### 9. 如何使用印度式分隔符？

**回答**：设置 `Option` 参数的 `UseIndianSeparators="true"` 使用印度式数字分隔符。

### 10. 如何自定义数字字形？

**回答**：通过 `Option` 参数的 `Numerals` 属性设置数字字形替换数组，可以替换为其他字符集。
