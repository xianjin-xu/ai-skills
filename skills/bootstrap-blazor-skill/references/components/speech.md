# Speech

## 概述

语音识别波形图组件

> Speech Recognition Waveform Component

**分类**: 其他

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Show` | `bool` | `}` | 获得/设置 是否显示波形图 默认 false |
| `ShowUsedTime` | `bool` | `true` | 获得/设置 是否显示已用时长 默认 true |
| `OnTimeout` | `Func<Task>?` | `}` | 获得/设置 倒计时结束时回调委托 |
| `TotalTime` | `int` | `60 * 1000` | 获得/设置 总时长 默认 60 000 毫秒 |
