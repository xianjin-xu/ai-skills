# Icon (图标)

## 概述

`Icon` 组件用于**显示图标**，支持 Font Awesome、Bootstrap Icons、Material Design Icons 等多种图标库。

**主要特性**：
- 支持多种图标库
- 支持图标大小设置
- 支持图标颜色设置
- 支持动画图标

**在线演示**: https://www.blazor.zone/icon

---

## 使用场景

### 1. 基础用法（Font Awesome 图标）

`Icon` 组件可以通过 `Name` 参数设置图标名称。

```razor
<!-- Font Awesome 图标 -->
<Icon Name="fa fa-home" />
<Icon Name="fa fa-user" />
<Icon Name="fa fa-cog" />
<Icon Name="fa fa-envelope" />
```

---

### 2. Bootstrap Icons（Bootstrap Icons）

通过 `Name` 参数使用 Bootstrap Icons。

```razor
<!-- Bootstrap Icons -->
<Icon Name="bi bi-house" />
<Icon Name="bi bi-person" />
<Icon Name="bi bi-gear" />
<Icon Name="bi bi-envelope" />
```

---

### 3. 设置图标大小（Size）

通过 `Size` 参数设置图标大小。

```razor
<!-- 小图标 -->
<Icon Name="fa fa-home" Size="16" />

<!-- 中图标（默认） -->
<Icon Name="fa fa-home" Size="24" />

<!-- 大图标 -->
<Icon Name="fa fa-home" Size="32" />

<!-- 超大图标 -->
<Icon Name="fa fa-home" Size="48" />
```

---

### 4. 设置图标颜色（Color）

通过 `Color` 参数或 CSS 类设置图标颜色。

```razor
<!-- 使用 Color 参数 -->
<Icon Name="fa fa-home" Color="Color.Primary" />

<!-- 使用 CSS 类 -->
<Icon Name="fa fa-home" class="text-danger" />
<Icon Name="fa fa-home" class="text-success" />
```

---

### 5. 动画图标（Animation）

通过 `Animation` 参数设置图标动画。

```razor
<!-- 旋转动画 -->
<Icon Name="fa fa-cog" Animation="IconAnimation.Spin" />

<!-- 脉冲动画 -->
<Icon Name="fa fa-spinner" Animation="IconAnimation.Pulse" />

<!-- 闪烁动画 -->
<Icon Name="fa fa-bell" Animation="IconAnimation.Tada" />
```

**Animation 选项**：
- `IconAnimation.None` - 无动画（默认）
- `IconAnimation.Spin` - 旋转
- `IconAnimation.Pulse` - 脉冲
- `IconAnimation.Tada` - 闪烁

---

### 6. 禁用状态（IsDisabled）

通过设置 `IsDisabled="true"` 禁用图标。

```razor
<!-- 禁用图标 -->
<Icon Name="fa fa-home" IsDisabled="true" />
```

---

## 参数 (Parameters)

### Icon 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Name` | `string?` | `null` | 获得/设置图标名称 |
| `Size` | `int` | `24` | 获得/设置图标大小（像素） |
| `Color` | `Color` | `Color.None` | 获得/设置图标颜色 |
| `Animation` | `IconAnimation` | `IconAnimation.None` | 获得/设置图标动画 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 最佳实践

1. **使用一致的图标库**：项目中选择一种图标库（Font Awesome 或 Bootstrap Icons）并保持一致性
2. **合理设置 Size**：按钮内图标用 16-20px，标题图标用 24-32px
3. **使用 Animation 吸引注意**：对于加载中、处理中的图标，使用 `Spin` 或 `Pulse` 动画
4. **与 Button 配合**：图标常放在 `Button` 内，提供视觉提示
5. **避免过度使用**：页面中图标过多会分散注意力，只在关键操作使用
6. **与 Image 的区别**：`Icon` 是图标字体（矢量，可缩放），`Image` 是图片（位图，可能失真）
