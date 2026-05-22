# Handwritten

## 概述

Handwritten 手写签名

> Handwritten Signature

**分类**: 其他
**在线演示**: [https://www.blazor.zone/handwritten](https://www.blazor.zone/handwritten)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ClearButtonText` | `string?` | `}` | 清除按钮文本 |
| `SaveButtonText` | `string?` | `}` | 保存按钮文本 |
| `Result` | `string?` | `}` | 手写签名imgBase64字符串 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `HandwrittenBase64` | `EventCallback<string>` | 手写结果回调方法 |
