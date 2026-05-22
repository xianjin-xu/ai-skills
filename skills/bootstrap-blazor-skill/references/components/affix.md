# Affix

## 概述

Affix 固钉组件

> Affix component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/affix](https://www.blazor.zone/affix)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Offset` | `float` | `}` | 获得/设置 指定偏移量后触发 |
| `Position` | `AffixPosition` | `}` | 获得/设置 固定位置枚举 默认 <see cref="AffixPosition.Top"/> |
| `ZIndex` | `int?` | `}` | 获得/设置 z-index 值 默认 100 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 组件内容 |

## 代码示例

### 基本用法

```razor
<Affix>
            <div style="line-height: 50px;">固定行 Affix</div>
        </Affix>
```

### 基本用法

```razor
<Affix Position="AffixPosition.Bottom" Offset="10">
            <div>底部固定行 Affix</div>
        </Affix>
```
