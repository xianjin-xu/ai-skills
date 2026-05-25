# Slider (滑块)

## 概述

`Slider` 是一个滑块组件，允许用户在最小值和最大值之间选择一个值，支持步长、范围等配置。

> Slider Component

**分类**: 表单输入  
**在线演示**: [https://www.blazor.zone/slider](https://www.blazor.zone/slider)

## 使用场景

### 1. 基本用法

```razor
<Slider @bind-Value="SliderValue" />
```

```csharp
@code {
    double SliderValue { get; set; } = 50;
}
```

### 2. 设置最小值和最大值

```razor
<Slider @bind-Value="SliderValue" Min="0" Max="100" />
```

### 3. 设置步长

```razor
<Slider @bind-Value="SliderValue" Min="0" Max="100" Step="5" />
```

### 4. 禁用状态

```razor
<Slider @bind-Value="SliderValue" IsDisabled="true" />
```

### 5. 显示标签

```razor
<Slider @bind-Value="SliderValue" ShowLabel="true" />
```

### 6. 使用输入事件

```razor
<Slider @bind-Value="SliderValue" UseInputEvent="true" />
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TValue?` | `null` | 获得/设置组件值 |
| `Min` | `TValue?` | `null` | 获得/设置最小值 |
| `Max` | `TValue?` | `null` | 获得/设置最大值 |
| `Step` | `TValue?` | `null` | 获得/设置步长 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用组件 |
| `ShowLabel` | `bool` | `false` | 获得/设置是否显示标签 |
| `UseInputEvent` | `bool` | `false` | 获得/设置是否使用输入事件 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `ValueChanged` | 值改变时触发 |

## 最佳实践

1. **值绑定**: 使用 `Value` 参数绑定到数值类型变量（`int`, `double`, `float` 等）
2. **范围设置**: 使用 `Min` 和 `Max` 参数设置滑块范围
3. **步长设置**: 使用 `Step` 参数设置每次滑动的步长
4. **禁用状态**: 使用 `IsDisabled` 参数禁用滑块
5. **标签显示**: 使用 `ShowLabel` 参数显示当前值标签
6. **输入事件**: 使用 `UseInputEvent` 参数启用实时输入事件

## 常见问题

### Q: 如何绑定滑块值？
A: 使用 `Value` 参数绑定到数值类型变量，支持 `int`, `double`, `float` 等类型。

### Q: 如何设置滑块范围？
A: 使用 `Min` 和 `Max` 参数设置最小值和最大值，例如 `Min="0" Max="100"`。

### Q: 如何设置步长？
A: 使用 `Step` 参数设置步长，例如 `Step="5"` 表示每次滑动增加/减少 5。

### Q: 如何禁用滑块？
A: 设置 `IsDisabled="true"` 禁用滑块，用户无法拖动。

### Q: 如何显示当前值？
A: 设置 `ShowLabel="true"` 显示当前值标签。
