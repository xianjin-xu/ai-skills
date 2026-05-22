# FlipClock

## 概述

FlipClock 组件

> FlipClock Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/flip-clock](https://www.blazor.zone/flip-clock)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ShowYear` | `bool` | `}` | 获得/设置 是否显示 Year 默认 false |
| `ShowMonth` | `bool` | `}` | 获得/设置 是否显示 Month 默认 false |
| `ShowDay` | `bool` | `}` | 获得/设置 是否显示 Day 默认 false |
| `ShowHour` | `bool` | `true` | 获得/设置 是否显示 Hour 默认 true |
| `ShowMinute` | `bool` | `true` | 获得/设置 是否显示 Minute 默认 true |
| `ShowSecond` | `bool` | `true` | 获得/设置 是否显示 Second 默认 true |
| `OnCompletedAsync` | `Func<Task>?` | `}` | 获得/设置 计时结束回调方法 默认 null |
| `ViewMode` | `FlipClockViewMode` | `}` | 获得/设置 显示模式 默认 <see cref="FlipClockViewMode.DateTime"/> |
| `Height` | `string?` | `}` | - |
| `BackgroundColor` | `string?` | `}` | 获得/设置 组件背景色 默认 null 未设置使用样式默认值 radial-gradient(ellipse at center, rgba(150, 150, 150, 1) 0%, rgba(89, 89, 89, 1) 100%); |
| `FontSize` | `string?` | `}` | 获得/设置 组件字体大小 默认 null 未设置使用样式默认值 80px; |
| `CardWidth` | `string?` | `}` | 获得/设置 组件卡片宽度 默认 null 未设置使用样式默认值 60px; |
| `CardHeight` | `string?` | `}` | 获得/设置 组件卡片高度 默认 null 未设置使用样式默认值 90px; |
| `CardColor` | `string?` | `}` | 获得/设置 组件卡片字体颜色 默认 null 未设置使用样式默认值 #ccc; |
| `CardBackgroundColor` | `string?` | `}` | 获得/设置 组件卡片背景颜色 默认 null 未设置使用样式默认值 #333; |
| `CardDividerHeight` | `string?` | `}` | 获得/设置 组件卡片分割线高度 默认 null 未设置使用样式默认值 1px; |
| `CardDividerColor` | `string?` | `}` | 获得/设置 组件卡片分割线颜色 默认 null 未设置使用样式默认值 rgba(0, 0, 0, .4); |
| `CardMargin` | `string?` | `}` | 获得/设置 组件卡片间隔 默认 null 未设置使用样式默认值 5; |
| `CardGroupMargin` | `string?` | `}` | 获得/设置 组件卡片组间隔 默认 null 未设置使用样式默认值 20; |
| `StartValue` | `TimeSpan` | `}` | 获得/设置 倒计时或者计时的开始时间 <see cref="FlipClockViewMode.Count"/> 默认 <see cref="FlipClockViewMode.CountDown" /> 模式下生效 |

## 代码示例

### 基本用法

```razor
<FlipClock ViewMode="FlipClockViewMode.Count"></FlipClock>
```

### 基本用法

```razor
<FlipClock ViewMode="FlipClockViewMode.CountDown" StartValue="@TimeSpan.FromSeconds(10)" OnCompletedAsync="OnCompletedAsync"></FlipClock>
```

### 基本用法

```razor
<FlipClock BackgroundColor="radial-gradient(ellipse at center, #ac85f1 0%, #833bf8 100%)" Height="@HeightValueString"
               FontSize="@FontSizeValueString" CardHeight="@CardHeightValueString" CardWidth="@CardWidthValueString"
               CardMargin="@CardMarginValueString" CardGroupMargin="@CardGroupMarginValueString"
               ShowYear="_showYear" ShowMonth="_showMonth" ShowDay="_showDay"
               ShowHour="_showHour" ShowMinute="_showMinute" ShowSecond="_showSecond"></FlipClock>
```
