# TimePicker

## 概述

TimePicker 组件

> TimePicker Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/time-picker](https://www.blazor.zone/time-picker)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `CancelButtonText` | `string?` | `}` | 获得/设置 取消按钮显示文字 |
| `ConfirmButtonText` | `string?` | `}` | 获得/设置 确定按钮显示文字 |
| `HasSeconds` | `bool` | `true` | 获得/设置 是否显示秒，默认为 true |
| `OnClose` | `Func<Task>?` | `}` | 获得/设置 取消按钮回调委托 |
| `Task` | `Func<TimeSpan,` | `}` | 获得/设置 确认按钮回调委托 |
