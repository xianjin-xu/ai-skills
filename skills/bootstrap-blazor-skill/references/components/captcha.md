# Captcha

## 概述

Captcha 组件

> Captcha component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/captcha](https://www.blazor.zone/captcha)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `HeaderText` | `string?` | `}` | 获得/设置 Header 显示文本 |
| `BarText` | `string?` | `}` | 获得/设置 Bar 显示文本 |
| `FailedText` | `string?` | `}` | 获得/设置 Bar 显示文本 |
| `LoadText` | `string?` | `}` | 获得/设置 Bar 显示文本 |
| `Task` | `Func<bool,` | `}` | 获得/设置 验证码结果回调委托 |
| `ImagesPath` | `string` | `"images"` | 获得/设置 图床路径 默认值为 images |
| `ImagesName` | `string` | `"Pic.jpg"` | 获得/设置 图床路径 默认值为 Pic.jpg |
| `GetImageName` | `Func<string>?` | `}` | 获得/设置 获取背景图方法委托 |
| `Offset` | `int` | `5` | 获得/设置 容错偏差 |
| `Width` | `int` | `280` | 获得/设置 图片宽度 |
| `SideLength` | `int` | `42` | 获得/设置 拼图边长 |
| `Diameter` | `int` | `9` | 获得/设置 拼图直径 |
| `Height` | `int` | `155` | 获得/设置 图片高度 |
| `RefreshIcon` | `string?` | `}` | 获得/设置 刷新按钮图标 默认值 fa-solid fa-arrows-rotate |
| `Max` | `int` | `1024` | 获得/设置 随机图片最大张数 默认 1024 |
| `BarIcon` | `string?` | `}` | 获得/设置 刷新按钮图标 默认值 fa-solid fa-arrow-right |
