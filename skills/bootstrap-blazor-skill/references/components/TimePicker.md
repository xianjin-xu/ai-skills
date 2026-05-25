# TimePicker (时间选择器)

## 概述

`TimePicker` 组件用于**选择时间**，支持小时、分钟、秒的选择。

**主要特性**：
- 支持 12 小时制或 24 小时制
- 支持选择小时、分钟、秒
- 可设置时间格式（Format）
- 可设置最小/最大时间（Min、Max）
- 支持只读（Readonly）
- 支持禁用（Disabled）

**在线演示**: https://www.blazor.zone/time-picker

---

## 使用场景

### 1. 基础用法（选择时间）

`TimePicker` 组件可以通过 `@bind-Value` 绑定选择的时间值。

```razor
<!-- 基础时间选择器 -->
<TimePicker @bind-Value="SelectedTime" />

<p>选择的时间: @SelectedTime</p>

@code {
    private TimeSpan? SelectedTime { get; set; }
}
```

---

### 2. 设置时间格式（Format）

通过 `Format` 参数设置时间显示格式。

```razor
<!-- 12 小时制 -->
<TimePicker @bind-Value="SelectedTime" Format="hh:mm tt" />

<!-- 24 小时制 -->
<TimePicker @bind-Value="SelectedTime" Format="HH:mm" />

<!-- 带秒 -->
<TimePicker @bind-Value="SelectedTime" Format="HH:mm:ss" />

@code {
    private TimeSpan? SelectedTime { get; set; }
}
```

**常用格式**：
- `hh:mm tt` - 12 小时制（如 02:30 PM）
- `HH:mm` - 24 小时制（如 14:30）
- `HH:mm:ss` - 24 小时制带秒（如 14:30:45）

---

### 3. 设置最小/最大时间（Min、Max）

通过 `Min` 和 `Max` 参数限制可选择的时间范围。

```razor
<!-- 限制时间范围：9:00 - 18:00 -->
<TimePicker @bind-Value="SelectedTime" Min="09:00" Max="18:00" />

@code {
    private TimeSpan? SelectedTime { get; set; }
}
```

---

### 4. 只读模式（Readonly）

通过设置 `Readonly="true"` 使时间选择器只读。

```razor
<!-- 只读时间选择器 -->
<TimePicker @bind-Value="SelectedTime" Readonly="true" />

@code {
    private TimeSpan? SelectedTime { get; set; } = TimeSpan.FromHours(14);
}
```

---

### 5. 禁用状态（Disabled）

通过设置 `Disabled="true"` 禁用时间选择器。

```razor
<!-- 禁用时间选择器 -->
<TimePicker @bind-Value="SelectedTime" Disabled="true" />

@code {
    private TimeSpan? SelectedTime { get; set; }
}
```

---

### 6. 显示秒选择（ShowSeconds）

通过设置 `ShowSeconds="true"` 显示秒选择。

```razor
<!-- 显示秒的时间选择器 -->
<TimePicker @bind-Value="SelectedTime" ShowSeconds="true" />

@code {
    private TimeSpan? SelectedTime { get; set; }
}
```

---

## 参数 (Parameters)

### TimePicker 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TimeSpan?` | `null` | 获得/设置选择的时间值 |
| `Format` | `string?` | `null` | 获得/设置时间格式 |
| `Min` | `TimeSpan?` | `null` | 获得/设置最小时间 |
| `Max` | `TimeSpan?` | `null` | 获得/设置最大时间 |
| `ShowSeconds` | `bool` | `false` | 获得/设置是否显示秒选择 |
| `Readonly` | `bool` | `false` | 获得/设置是否只读 |
| `Disabled` | `bool` | `false` | 获得/设置是否禁用 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<TimeSpan?>` | 时间值变化回调 |

---

## 最佳实践

1. **使用 @bind-Value 双向绑定**：推荐使用 `@bind-Value` 实现双向绑定，简化代码
2. **合理设置 Format**：根据用户习惯选择 12 小时制或 24 小时制，避免混淆
3. **限制时间范围**：通过 `Min` 和 `Max` 参数限制可选择的时间范围，避免无效输入
4. **显示秒选择**：对于需要精确时间的场景，设置 `ShowSeconds="true"` 显示秒选择
5. **处理 ValueChanged 事件**：对于需要在时间变化时执行逻辑的场景，处理 `ValueChanged` 事件
6. **与 DateTimePicker 的区别**：`TimePicker` 仅选择时间，`DateTimePicker` 选择日期和时间
