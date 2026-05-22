# Timer

## 概述

Timer 组件

> Timer Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/timer](https://www.blazor.zone/timer)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TimeSpan` | `}` | 获得/设置 当前值 |
| `int` | `override` | `300` | 获得/设置 组件宽度 |
| `OnTimeout` | `Func<Task>?` | `}` | 获得/设置 倒计时结束时的回调委托 |
| `OnCancel` | `Func<Task>?` | `}` | 获得/设置 取消时的回调委托 |
| `IsVibrate` | `bool` | `true` | 获得/设置 倒计时结束时是否设备震动 |
| `PauseText` | `string?` | `}` | 获得/设置 暂停按钮显示文字 |
| `ResumeText` | `string?` | `}` | 获得/设置 继续按钮显示文字 |
| `CancelText` | `string?` | `}` | 获得/设置 取消按钮显示文字 |
| `StarText` | `string?` | `}` | 获得/设置 开始按钮显示文字 |
| `Icon` | `string?` | `}` | 获得/设置 Alert 图标 |
