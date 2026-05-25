# Divider (分割线)

## 概述

`Divider` 组件用于**在内容之间创建视觉分隔**，支持水平/垂直方向，可自定义样式。

**主要特性**：
- 支持水平/垂直方向
- 支持自定义文本
- 支持不同样式（实线、虚线、点线）
- 可设置颜色

**在线演示**: https://www.blazor.zone/divider

---

## 使用场景

### 1. 基础用法（水平分割线）

`Divider` 组件默认水平显示。

```razor
<!-- 基础分割线 -->
<p>上方内容</p>
<Divider />
<p>下方内容</p>
```

---

### 2. 带文本的分割线（Text）

通过 `Text` 参数在分割线上显示文本。

```razor
<!-- 带文本的分割线 -->
<p>上方内容</p>
<Divider Text="分割线标题" />
<p>下方内容</p>
```

---

### 3. 垂直分割线（IsVertical）

通过设置 `IsVertical="true"` 显示为垂直分割线。

```razor
<!-- 垂直分割线 -->
<div class="d-flex align-items-center" style="height: 100px;">
    <div>左侧内容</div>
    <Divider IsVertical="true" />
    <div>右侧内容</div>
</div>
```

---

### 4. 自定义样式（LineStyle）

通过 `LineStyle` 参数设置线条样式。

```razor
<!-- 实线（默认） -->
<Divider Text="实线" LineStyle="DividerLineStyle.Solid" />

<!-- 虚线 -->
<Divider Text="虚线" LineStyle="DividerLineStyle.Dashed" />

<!-- 点线 -->
<Divider Text="点线" LineStyle="DividerLineStyle.Dotted" />
```

**LineStyle 选项**：
- `DividerLineStyle.Solid` - 实线（默认）
- `DividerLineStyle.Dashed` - 虚线
- `DividerLineStyle.Dotted` - 点线

---

### 5. 设置颜色（Color）

通过 `Color` 参数设置分割线颜色。

```razor
<!-- 主要颜色 -->
<Divider Text="主要" Color="Color.Primary" />

<!-- 成功颜色 -->
<Divider Text="成功" Color="Color.Success" />

<!-- 危险颜色 -->
<Divider Text="危险" Color="Color.Danger" />
```

---

### 6. 自定义文本位置（TextPosition）

通过 `TextPosition` 参数设置文本位置。

```razor
<!-- 文本居中（默认） -->
<Divider Text="居中" TextPosition="DividerTextPosition.Center" />

<!-- 文本左侧 -->
<Divider Text="左侧" TextPosition="DividerTextPosition.Left" />

<!-- 文本右侧 -->
<Divider Text="右侧" TextPosition="DividerTextPosition.Right" />
```

**TextPosition 选项**：
- `DividerTextPosition.Left` - 左侧
- `DividerTextPosition.Center` - 居中（默认）
- `DividerTextPosition.Right` - 右侧

---

## 参数 (Parameters)

### Divider 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置分割线文本 |
| `IsVertical` | `bool` | `false` | 获得/设置是否垂直分割线 |
| `LineStyle` | `DividerLineStyle` | `DividerLineStyle.Solid` | 获得/设置线条样式 |
| `Color` | `Color` | `Color.None` | 获得/设置分割线颜色 |
| `TextPosition` | `DividerTextPosition` | `DividerTextPosition.Center` | 获得/设置文本位置 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 最佳实践

1. **合理使用文本**：只在需要说明分组的场景使用 `Text`，简单分隔不需要文本
2. **选择合适样式**：`Solid` 适合正式文档，`Dashed` 适合非正式场景
3. **避免过度使用**：页面中过多分割线会显得杂乱，适度使用
4. **与 HR 标签的区别**：`Divider` 是组件（支持样式、文本），`<hr>` 是原生 HTML（样式有限）
5. **垂直分割线场景**：垂直分割线适合在水平布局中分隔内容（如按钮组、链接组）
6. **与 Margin/Padding 的区别**：`Divider` 是视觉分隔，`Margin`/`Padding` 是空间控制，根据需求选择
