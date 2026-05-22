# Slider

## 概述

滑块组件

> Slider Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/slider](https://www.blazor.zone/slider)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Min` | `TValue?` | `}` | 获得/设置 最小值 默认为 null 未设置 |
| `Max` | `TValue?` | `}` | 获得/设置 最大值 默认为 null 未设置 |
| `Step` | `TValue?` | `}` | 获得/设置 步长 默认为 null 未设置 |

## 代码示例

### 基本用法

```razor
<Slider @bind-Value="@CurrentValue" Max="MaxValue" Min="MinValue" Step="Step" UseInputEvent="UseInput"
                    DisplayText="@DisplayText" ShowLabel="ShowLabel" IsDisabled="IsDisabled" OnValueChanged="OnRangeSliderValueChanged"></Slider>
<Slider @bind-Value="@CurrentValue" Max="MaxValue" Min="MinValue" Step="Step" UseInputEvent="UseInput"
                DisplayText="@DisplayText" ShowLabel="ShowLabel" IsDisabled="IsDisabled" OnValueChanged="OnRangeSliderValueChanged"></Slider>
```

### 基本用法

```razor
<Slider @bind-Value="@RangeValue" Step="1" UseInputEvent="true"></Slider>
```

### 基本用法

```razor
<Slider TValue="double" Step="1" IsDisabled="true"></Slider>
```
