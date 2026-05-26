# Anchor (锚点组件)

## 概述

`Anchor` 组件用于**页面内锚点导航**，点击后平滑滚动到指定元素位置。

**主要特性**：
- 支持平滑滚动动画（IsAnimation）
- 支持设置目标元素 ID（Target）
- 支持设置滚动容器（Container）
- 支持设置偏移量（Offset）

**在线演示**: https://www.blazor.zone/anchor

---

## 使用场景

### 1. 基础用法（锚点导航）

`Anchor` 组件通过 `Target` 参数指定目标元素 ID，点击后滚动到该元素。

```razor
<!-- 锚点按钮 -->
<Anchor Target="section1">跳转到章节 1</Anchor>
<Anchor Target="section2">跳转到章节 2</Anchor>

<!-- 目标元素 -->
<div id="section1">
    <h2>章节 1</h2>
    <p>这是章节 1 的内容...</p>
</div>

<div id="section2">
    <h2>章节 2</h2>
    <p>这是章节 2 的内容...</p>
</div>
```

---

### 2. 平滑滚动动画（IsAnimation）

通过设置 `IsAnimation="true"`（默认）启用平滑滚动动画。

```razor
<!-- 启用平滑动画（默认） -->
<Anchor Target="section1" IsAnimation="true">平滑滚动</Anchor>

<!-- 禁用平滑动画 -->
<Anchor Target="section1" IsAnimation="false">立即跳转</Anchor>
```

---

### 3. 设置滚动容器（Container）

通过 `Container` 参数指定滚动容器 ID（默认为 `null`，使用最近滚动条容器元素）。

```razor
<!-- 指定滚动容器 -->
<div id="scrollContainer" style="height: 300px; overflow-y: auto;">
    <div style="height: 800px;">
        <Anchor Target="target1" Container="scrollContainer">跳转到目标 1</Anchor>
        <div style="height: 400px;"></div>
        <div id="target1">目标位置 1</div>
    </div>
</div>
```

---

### 4. 设置偏移量（Offset）

通过 `Offset` 参数设置距离顶端偏移量（像素）。

```razor
<!-- 偏移 50px（避开固定头部） -->
<Anchor Target="section1" Offset="50">跳转（偏移 50px）</Anchor>
```

---

### 5. 与 AnchorLink 配合（导航菜单）

通常使用 `AnchorLink` 组件配合 `Anchor` 实现导航菜单高亮。

```razor
<!-- 导航菜单 -->
<AnchorLink GroupName="导航">
    <Anchor Target="section1" Text="章节 1" />
    <Anchor Target="section2" Text="章节 2" />
    <Anchor Target="section3" Text="章节 3" />
</AnchorLink>

<!-- 内容区域 -->
<div id="section1"><h2>章节 1</h2></div>
<div id="section2"><h2>章节 2</h2></div>
<div id="section3"><h2>章节 3</h2></div>
```

**说明**：`AnchorLink` 是导航菜单容器，`Anchor` 是具体的锚点链接。

---

## 参数 (Parameters)

### Anchor 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Target` | `string?` | `null` | 获得/设置 目标组件 Id |
| `Container` | `string?` | `null` | 获得/设置 滚动组件 Id 默认为 null 使用最近滚动条容器元素 |
| `IsAnimation` | `bool` | `true` | 获得/设置 滚动时是否开启动画 默认 true |
| `Offset` | `int` | `0` | 获得/设置 距离顶端偏移量 默认为 0 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子内容 |

---

## 最佳实践

1. **确保目标 ID 存在**：`Target` 指定的 ID 必须在页面中存在，否则滚动无效
2. **设置合适的 Offset**：如果页面有固定头部，设置 `Offset` 为头部高度，避免遮挡目标内容
3. **使用 AnchorLink 构建导航**：对于多锚点页面，使用 `AnchorLink` 组件构建导航菜单，自动高亮当前章节
4. **与 Nav 组件的区别**：`Anchor` 是页面内锚点导航，`Nav` 是全局导航菜单
5. **性能考虑**：避免在页面中放置过多 `Anchor`，会影响滚动性能
6. **测试平滑滚动**：在不同浏览器测试平滑滚动效果，确保兼容性

---

## 常见问题

### Q: 点击 Anchor 后没有滚动？
A: 检查 `Target` 的 ID 是否正确，以及目标元素是否在可滚动容器内。

### Q: 滚动后内容被固定头部遮挡？
A: 设置 `Offset` 参数为固定头部的高度（像素）。

### Q: 如何高亮当前章节？
A: 使用 `AnchorLink` 组件包装 `Anchor`，会自动高亮当前可见章节。
