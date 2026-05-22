# Waterfall

## 概述

Waterfall 组件

> Waterfall Component

**分类**: 其他

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Task` | `Func<WaterfallItem,` | `}` | 获得/设置 点击列表项回调方法 |
| `Item` | `RenderFragment<(WaterfallItem` | `}` | 获得/设置 模板 默认为 null |
| `ItemTemplate` | `RenderFragment<WaterfallItem>?` | `}` | 获得/设置 图片模板 默认为 null |
| `LoadTemplate` | `RenderFragment?` | `}` | 获得/设置 加载模板 |
| `ItemWidth` | `int` | `216` | 获得/设置 每一项宽度 默认 216 |
| `ItemMinHeight` | `int` | `316` | 获得/设置 每一项最小宽度 默认 316 用于显示 loading 图标 |
