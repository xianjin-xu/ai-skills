# Affix (固钉组件)

## 概述

`Affix` 组件用于**将内容固定在页面的某个位置**，当页面滚动到指定位置时，内容会固定在顶部或底部。

**主要特性**：
- 支持顶部固定（Top）和底部固定（Bottom）
- 支持设置触发偏移量（Offset）
- 支持自定义 z-index（ZIndex）
- 可固定任何内容

**在线演示**: https://www.blazor.zone/affix

---

## 使用场景

### 1. 基础用法（顶部固定）

`Affix` 组件默认在页面滚动时固定在顶部。

```razor
<Affix>
    <div style="line-height: 50px;">固定行 Affix</div>
</Affix>
```

---

### 2. 底部固定（Position）

通过设置 `Position` 参数将组件固定在底部。

```razor
<Affix Position="AffixPosition.Bottom" Offset="10">
    <div>底部固定行 Affix</div>
</Affix>
```

**Position 选项**：
- `AffixPosition.Top` - 顶部固定（默认）
- `AffixPosition.Bottom` - 底部固定

---

### 3. 设置偏移量（Offset）

通过 `Offset` 参数设置滚动多少距离后触发固定。

```razor
<!-- 滚动 100px 后固定 -->
<Affix Offset="100">
    <div>滚动 100px 后固定</div>
</Affix>
```

---

### 4. 设置 z-index（ZIndex）

通过 `ZIndex` 参数设置固定元素的 z-index 值。

```razor
<Affix ZIndex="1000">
    <div>z-index: 1000</div>
</Affix>
```

---

### 5. 固定导航菜单（实际场景）

常见用法是固定页面导航菜单，滚动时始终可见。

```razor
<Affix Position="AffixPosition.Top" Offset="0">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">固定导航</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="#">首页</a></li>
                <li class="nav-item"><a class="nav-link" href="#">产品</a></li>
                <li class="nav-item"><a class="nav-link" href="#">关于</a></li>
            </ul>
        </div>
    </nav>
</Affix>
```

---

## 参数 (Parameters)

### Affix 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Offset` | `float` | `0` | 获得/设置 指定偏移量后触发 |
| `Position` | `AffixPosition` | `AffixPosition.Top` | 获得/设置 固定位置枚举 |
| `ZIndex` | `int?` | `100` | 获得/设置 z-index 值 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 组件内容 |

---

## 最佳实践

1. **合理使用 Offset**：根据页面头部高度设置 `Offset`，避免固定过早或过晚
2. **设置合适的 ZIndex**：确保固定元素在其他元素之上（默认 100 通常足够）
3. **避免过度使用**：页面中避免多个 `Affix`，会造成视觉混乱
4. **与 Sticky 的区别**：`Affix` 是 JS 计算的固定定位，`position: sticky` 是 CSS 原生粘性定位
5. **性能考虑**：滚动频繁触发计算，避免在 `Affix` 内放置复杂组件
6. **测试响应式**：在不同屏幕尺寸测试固定效果，确保移动端体验良好

---

## 常见问题

### Q: Affix 不工作？
A: 检查父容器是否有 `overflow: hidden/auto`，这会破坏固定定位。

### Q: 如何只在桌面端固定？
A: 使用 CSS 媒体查询或 Blazor 的 `MediaQuery` 组件控制 `Affix` 显示。

### Q: 固定后内容跳动？
A: 原位置内容消失导致页面跳动，可考虑用占位元素或 `Javascript` 计算高度补偿。
