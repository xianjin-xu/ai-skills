# Reconnector

## 概述

ReconnectorContent 组件

> ReconnectorContent Component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/reconnector](https://www.blazor.zone/reconnector)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ReconnectingTemplate` | `RenderFragment?` | `}` | 获得/设置 ReconnectingTemplate 模板 |
| `ReconnectFailedTemplate` | `RenderFragment?` | `}` | 获得/设置 ReconnectFailedTemplate 模板 |
| `ReconnectRejectedTemplate` | `RenderFragment?` | `}` | 获得/设置 ReconnectRejectedTemplate 模板 |
| `AutoReconnect` | `bool` | `true` | 获得/设置 是否自动尝试重连 默认 true |
| `ReconnectInterval` | `int` | `5000` | 获得/设置 自动重连间隔 默认 5000 毫秒 最小值为 1000 毫秒 |
