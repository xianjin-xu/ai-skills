# Scroll

## 概述

Scroll 组件

> Scroll Component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/scroll](https://www.blazor.zone/scroll)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |
| `Height` | `string?` | `}` | 获得/设置 组件高度 |
| `Width` | `string?` | `}` | 获得/设置 组件宽度 |
| `ScrollWidth` | `int?` | `}` | 获得/设置 滚动条宽度 默认 null 未设置使用 <see cref="ScrollOptions"/> 配置类中的 <see cref="ScrollOptions.ScrollWidth"/> |
| `ScrollHoverWidth` | `int?` | `}` | 获得/设置 滚动条 hover 状态下宽度 默认 null 未设置使用 <see cref="ScrollOptions"/> 配置类中的 <see cref="ScrollOptions.ScrollHoverWidth"/> |

## 代码示例

### 基本用法

```razor
<Scroll @ref="_scroll" Height="200px">
            <div class="m-1">@Localizer["ScrollNormalDescription"]</div>
            <div class="bg-primary" style="height: 100px;"></div>
            <div class="bg-secondary" style="height: 100px;"></div>
            <div class="bg-warning" style="height: 100px;"></div>
            <div class="bg-success" style="height: 100px;"></div>
            <div class="bg-info" style="height: 100px;"></div>
            <div class="m-1">@Localizer["ScrollNormalBottom"]</div>
        </Scroll>
```
