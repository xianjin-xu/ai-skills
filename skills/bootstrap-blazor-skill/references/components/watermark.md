# Watermark

## 概述

Watermark 组件

> Watermark Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/watermark](https://www.blazor.zone/watermark)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 组件内容 |
| `Text` | `string?` | `}` | 获得/设置 水印文本 默认 BootstrapBlazor |
| `FontSize` | `int?` | `}` | 获得/设置 字体大小 默认 null 未设置 默认使用 16px 字体大小 单位 px |
| `Color` | `string?` | `}` | 获得/设置 颜色 默认 null 未设置 |
| `Rotate` | `int?` | `}` | 获得/设置 水印的旋转角度 默认 null 45° |
| `ZIndex` | `int?` | `}` | 获得/设置 水印元素的 z-index 值 默认 null |
| `Gap` | `int?` | `}` | 获得/设置 水印之间的间距 值 默认 null |
| `IsPage` | `bool` | `}` | 获得/设置 是否为整页面水印 默认 false |

## 代码示例

### 基本用法

```razor
<Watermark Text="@_text" FontSize="@_fontSize" Color="@_color" Rotate="@_rotate"
               Gap="@_gap">
        <div style="height: 500px; padding-top: 40px; text-align: center;">
            <p>this is a watermark demo</p>
            <div>这是 watermark 演示</div>
        </div>
    </Watermark>
```
