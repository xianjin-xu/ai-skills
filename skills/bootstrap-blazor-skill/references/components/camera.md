# Camera

## 概述

Camera 组件

> Camera component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/camera](https://www.blazor.zone/camera)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `DeviceId` | `string?` | `}` | 获得/设置 当前设备 Id 默认 null |
| `AutoStart` | `bool` | `}` | 获得/设置 是否自动开启摄像头 默认为 false |
| `VideoWidth` | `int?` | `320` | 获得/设置 摄像头视频宽度 默认 320 |
| `VideoHeight` | `int?` | `240` | 获得/设置 摄像头视频高度 默认 240 |
| `CaptureJpeg` | `bool` | `}` | 获得/设置 拍照格式为 Jpeg 默认为 false 使用 png 格式 |
| `Quality` | `float` | `0.9f` | 获得/设置 图像质量 默认为 0.9 |
| `Task` | `Func<List<DeviceItem>,` | `}` | 获得/设置 初始化摄像头回调方法 |
| `OnOpen` | `Func<Task>?` | `}` | 获得/设置 打开摄像头回调方法 |
| `OnClose` | `Func<Task>?` | `}` | 获得/设置 关闭摄像头回调方法 |
