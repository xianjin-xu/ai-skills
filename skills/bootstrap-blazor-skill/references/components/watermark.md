# Watermark (水印)

## 概述

`Watermark` 组件用于**在页面或元素上添加水印**，常用于防盗用、标识版权等场景。

**主要特性**：
- 支持文本水印
- 支持图片水印
- 可设置水印密度
- 可设置水印颜色/透明度
- 支持全页水印或局部水印

**在线演示**: https://www.blazor.zone/watermark

---

## 使用场景

### 1. 基础用法（文本水印）

`Watermark` 组件可以通过 `Text` 参数设置水印文本。

```razor
<!-- 基础文本水印 -->
<Watermark Text="机密文件">
    <div style="height: 500px; padding: 20px;">
        <h1>文档标题</h1>
        <p>这是一份重要文档的内容...</p>
    </div>
</Watermark>
```

---

### 2. 图片水印（ImageUrl）

通过 `ImageUrl` 参数设置图片水印。

```razor
<!-- 图片水印 -->
<Watermark ImageUrl="https://via.placeholder.com/100x100?text=LOGO">
    <div style="height: 500px; padding: 20px;">
        <h1>品牌文档</h1>
        <p>这是一份带品牌水印的文档...</p>
    </div>
</Watermark>
```

---

### 3. 设置水印密度（Gap）

通过 `Gap` 参数设置水印间距（像素）。

```razor
<!-- 密集水印 -->
<Watermark Text="机密" Gap="50" />

<!-- 稀疏水印 -->
<Watermark Text="机密" Gap="200" />
```

---

### 4. 设置水印颜色/透明度（Color、Opacity）

通过 `Color` 和 `Opacity` 参数设置水印颜色和透明度。

```razor
<!-- 红色半透明水印 -->
<Watermark Text="机密" Color="rgba(255, 0, 0, 0.3)" Opacity="0.3" />

<!-- 灰色水印 -->
<Watermark Text="机密" Color="rgba(0, 0, 0, 0.2)" Opacity="0.2" />
```

---

### 5. 全页水印（IsFullPage）

通过设置 `IsFullPage="true"` 启用全页水印（覆盖整个页面）。

```razor
<!-- 全页水印 -->
<Watermark Text="机密文件" IsFullPage="true" />

<!-- 页面内容 -->
<h1>页面标题</h1>
<p>页面内容...</p>
```

---

### 6. 自定义水印样式（FontSize、Rotate）

通过 `FontSize` 和 `Rotate` 参数自定义水印字体大小和旋转角度。

```razor
<!-- 大字体，旋转 45 度 -->
<Watermark Text="机密" FontSize="24" Rotate="45" />

<!-- 小字体，旋转 -30 度 -->
<Watermark Text="机密" FontSize="12" Rotate="-30" />
```

**说明**：`Rotate` 参数控制水印旋转角度，常用值：
- `0` - 不旋转（默认）
- `45` - 旋转 45 度
- `-30` - 旋转 -30 度

---

## 参数 (Parameters)

### Watermark 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置水印文本 |
| `ImageUrl` | `string?` | `null` | 获得/设置水印图片地址 |
| `Gap` | `int` | `100` | 获得/设置水印间距（像素） |
| `Color` | `string?` | `null` | 获得/设置水印颜色 |
| `Opacity` | `double` | `0.5` | 获得/设置水印透明度（0-1） |
| `FontSize` | `int` | `16` | 获得/设置水印字体大小（像素） |
| `Rotate` | `int` | `0` | 获得/设置水印旋转角度（度） |
| `IsFullPage` | `bool` | `false` | 获得/设置是否全页水印 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 最佳实践

1. **合理使用 Text 或 ImageUrl**：文本水印适合简单标识，图片水印适合品牌 logo
2. **控制水印密度**：通过 `Gap` 参数控制水印密度，过密影响阅读，过疏防盗用效果差
3. **设置合适的透明度**：通过 `Opacity` 参数设置透明度，既要可见又要不影响内容阅读（建议 0.2-0.5）
4. **全页水印需谨慎**：`IsFullPage="true"` 会覆盖整个页面，确保不会影响页面交互（如点击、选择文本）
5. **自定义旋转角度**：通过 `Rotate` 参数设置旋转角度，常用 45 度或 -30 度，增加防盗用难度
6. **与 CSS 背景图的区别**：`Watermark` 是组件级水印（可控制透明度、密度等），CSS 背景图是静态背景，根据需求选择
7. **性能考虑**：全页水印会创建大量 DOM 元素，对于超长页面可能影响性能，考虑分块加载
