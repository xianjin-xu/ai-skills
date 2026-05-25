# Stack (堆叠布局)

## 概述

`Stack` 组件用于**在水平或垂直堆栈中排列其子组件**，是弹性布局容器。

`Stack` 的子组件必须是 `StackItem`。

**主要特性**：
- 支持垂直/水平方向（IsRow）
- 支持子项间距控制
- 支持对齐方式设置（AlignItems、Justify）
- 支持是否折行（IsWrap）
- 支持反转方向（IsReverse）
- 子项可通过 `StackItem` 控制 Grow/Shrink

**在线演示**: https://www.blazor.zone/stack

---

## 使用场景

### 1. 基础用法（垂直堆叠）

`Stack` 组件默认垂直堆叠子组件，子组件必须是 `StackItem`。

```razor
<!-- 垂直堆叠 -->
<Stack>
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 3</div>
    </StackItem>
</Stack>
```

---

### 2. 水平布局（IsRow）

通过 `IsRow="true"` 设置为水平布局。

```razor
<!-- 水平布局 -->
<Stack IsRow="true">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 3</div>
    </StackItem>
</Stack>
```

---

### 3. 水平对齐方式（Justify）

通过 `Justify` 参数设置水平对齐方式。

```razor
<!-- 左对齐（默认） -->
<Stack IsRow="true" Justify="StackJustifyContent.Start">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
</Stack>

<!-- 居中对齐 -->
<Stack IsRow="true" Justify="StackJustifyContent.Center">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
</Stack>

<!-- 右对齐 -->
<Stack IsRow="true" Justify="StackJustifyContent.End">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
</Stack>

<!-- 两端对齐 -->
<Stack IsRow="true" Justify="StackJustifyContent.Between">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 3</div>
    </StackItem>
</Stack>
```

**Justify 选项**：
- `StackJustifyContent.Start` - 左对齐（默认）
- `StackJustifyContent.Center` - 居中对齐
- `StackJustifyContent.End` - 右对齐
- `StackJustifyContent.Between` - 两端对齐
- `StackJustifyContent.Around` - 周围间距相等
- `StackJustifyContent.Evenly` - 间距相等

---

### 4. 垂直对齐方式（AlignItems）

通过 `AlignItems` 参数设置垂直对齐方式（水平布局时）或水平对齐方式（垂直布局时）。

```razor
<!-- 顶部对齐 -->
<Stack IsRow="true" AlignItems="StackAlignItems.Start" Style="height: 100px;">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
</Stack>

<!-- 居中对齐 -->
<Stack IsRow="true" AlignItems="StackAlignItems.Center" Style="height: 100px;">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
</Stack>

<!-- 底部对齐 -->
<Stack IsRow="true" AlignItems="StackAlignItems.End" Style="height: 100px;">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
</Stack>
```

**AlignItems 选项**：
- `StackAlignItems.Stretch` - 拉伸（默认）
- `StackAlignItems.Start` - 顶部/左侧对齐
- `StackAlignItems.Center` - 居中对齐
- `StackAlignItems.End` - 底部/右侧对齐
- `StackAlignItems.Baseline` - 基线对齐

---

### 5. 是否折行（IsWrap）

通过 `IsWrap="true"` 允许子项折行。

```razor
<!-- 允许折行 -->
<Stack IsRow="true" IsWrap="true">
    <StackItem>
        <div class="p-3 border">项目 1</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 3</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 4</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 5</div>
    </StackItem>
</Stack>
```

---

### 6. 反转方向（IsReverse）

通过 `IsReverse="true"` 反转布局方向。

```razor
<!-- 反转垂直方向 -->
<Stack IsReverse="true">
    <StackItem>
        <div class="p-3 border">项目 1（底部）</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2（顶部）</div>
    </StackItem>
</Stack>

<!-- 反转水平方向 -->
<Stack IsRow="true" IsReverse="true">
    <StackItem>
        <div class="p-3 border">项目 1（右侧）</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 2（左侧）</div>
    </StackItem>
</Stack>
```

---

### 7. StackItem 控制 Grow/Shrink

`StackItem` 子项可以通过 `class` 属性控制 Grow（是否尽可能多占用剩余空间）和 Shrink（是否尽可能把空间让给前面兄弟元素）。

```razor
<Stack IsRow="true">
    <StackItem>
        <div class="p-3 border">项目 1（不增长）</div>
    </StackItem>
    <StackItem class="flex-grow-1">
        <div class="p-3 border">项目 2（增长占用剩余空间）</div>
    </StackItem>
    <StackItem>
        <div class="p-3 border">项目 3（不增长）</div>
    </StackItem>
</Stack>
```

**Grow/Shrink 类**：
- `flex-grow-0` - 不增长（默认）
- `flex-grow-1` - 增长占用剩余空间
- `flex-shrink-0` - 不收缩
- `flex-shrink-1` - 收缩让出空间

---

## 参数 (Parameters)

### Stack 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsRow` | `bool` | `false` | 获得/设置 是否为行布局（水平），默认 false（垂直） |
| `AlignItems` | `StackAlignItems` | `StackAlignItems.Stretch` | 获得/设置 垂直布局模式 |
| `Justify` | `StackJustifyContent` | `StackJustifyContent.Start` | 获得/设置 水平布局调整 |
| `IsWrap` | `bool` | `false` | 获得/设置 是否允许折行 |
| `IsReverse` | `bool` | `false` | 获得/设置 是否反向布局 |
| `AdditionalAttributes` | `IDictionary<string, object>` | `null` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 内容 |

---

### StackItem 组件参数

`StackItem` 是 `Stack` 的子组件，用于包裹内容。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子内容 |
| `class` | `string?` | `null` | 可通过 `flex-grow-*` 和 `flex-shrink-*` 控制行为 |

---

## 最佳实践

1. **使用 StackItem 包裹子项**：`Stack` 的直接子组件必须是 `StackItem`，不能用 `div` 或其他组件直接放在 `Stack` 内
2. **合理选择方向**：垂直堆叠用默认（`IsRow="false"`），水平排列用 `IsRow="true"`
3. **使用 Justify 控制间距**：水平布局时用 `Justify` 控制子项水平间距（Start、Center、End、Between 等）
4. **使用 AlignItems 控制对齐**：控制子项交叉轴对齐方式
5. **需要折行时用 IsWrap**：子项可能超出容器宽度时，设置 `IsWrap="true"`
6. **与 Row 组件的区别**：`Stack` 是简单的一维堆叠布局，`Row` 是通过 `ItemsPerRow` 控制每行组件数量的布局组件
