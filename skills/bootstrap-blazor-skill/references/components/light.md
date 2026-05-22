# Light

## 概述

指示灯组件

> Indicator Light Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/light](https://www.blazor.zone/light)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsFlash` | `bool` | `}` | 获得/设置 组件是否闪烁 默认为 false 不闪烁 |
| `IsFlat` | `bool` | `}` | 获得/设置 是否为平面图形 默认 false |
| `Color` | `Color` | `Color.Success` | 获得/设置 指示灯颜色 默认为 Success 绿色 |

## 代码示例

### 基本用法

```razor
<Light IsFlash="true" Color="@Color"></Light>
```

### 基本用法

```razor
<Light Color="Color.Danger" TooltipText="@Title"></Light>
```
