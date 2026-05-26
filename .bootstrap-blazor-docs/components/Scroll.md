# Scroll 滚动条

## 概述

Scroll 滚动条组件用于给高度或者宽度超标的组件增加滚动条。其元素必须拥有固定高度时才可呈现滚动条，可以通过外套元素设置其 `Height` 属性。

> Scroll component is used to add scrollbar to components that exceed height or width. The element must have a fixed height to display scrollbar, which can be set by wrapping element with `Height` property.

**分类**: 布局组件
**在线演示**: [https://www.blazor.zone/scroll](https://www.blazor.zone/scroll)

---

## 使用场景

### 1. 基础用法

给组件增加滚动条，通过设置 `Height` 高度值为 `200px` 使内部子元素高度为 `500px` 时出现滚动条。

```razor
<Scroll Height="200px">
    <div class="m-1">请滚动右侧滚动条</div>
    <div class="bg-primary" style="height: 100px;"></div>
    <div class="bg-secondary" style="height: 100px;"></div>
    <div class="bg-warning" style="height: 100px;"></div>
    <div class="bg-success" style="height: 100px;"></div>
    <div class="bg-info" style="height: 100px;"></div>
    <div class="m-1">我是最底端</div>
</Scroll>
```

### 2. 滚动到底部

通过组件实例方法 `ScrollToEnd()` 滚动到底部。

```razor
<Scroll @ref="_scroll" Height="200px">
    <div class="m-1">请滚动右侧滚动条</div>
    <div class="bg-primary" style="height: 100px;"></div>
    <div class="bg-secondary" style="height: 100px;"></div>
    <div class="bg-warning" style="height: 100px;"></div>
    <div class="bg-success" style="height: 100px;"></div>
    <div class="bg-info" style="height: 100px;"></div>
    <div class="m-1">我是最底端</div>
</Scroll>
<Button Text="滚动到底部" OnClick="ScrollToEnd"></Button>

@code {
    private Scroll? _scroll { get; set; }

    private async Task ScrollToEnd()
    {
        if (_scroll != null)
        {
            await _scroll.ScrollToEnd();
        }
    }
}
```

### 3. 自定义滚动条宽度

通过设置 `ScrollWidth` 和 `ScrollHoverWidth` 自定义滚动条宽度。

```razor
<Scroll Height="200px" ScrollWidth="10" ScrollHoverWidth="15">
    <div class="m-1">自定义滚动条宽度</div>
    <div class="bg-primary" style="height: 500px;"></div>
</Scroll>
```

### 4. 设置宽度

通过设置 `Width` 参数设置组件宽度。

```razor
<Scroll Height="200px" Width="300px">
    <div class="m-1">设置组件宽度</div>
    <div class="bg-primary" style="height: 500px;"></div>
</Scroll>
```

---

## 参数 (Parameters)

### Scroll 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件 |
| `Height` | `string?` | `null` | 获得/设置 组件高度 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `ScrollHoverWidth` | `int?` | `null` | 获得/设置 滚动条 hover 状态下宽度 |
| `ScrollWidth` | `int?` | `null` | 获得/设置 滚动条宽度 |

---

## 方法 (Methods)

### Scroll 方法

| 方法名 | 说明 |
|--------|------|
| `ScrollToEnd()` | 滚动到底部 |
| `ScrollToStart()` | 滚动到顶部 |

---

## 最佳实践

### 1. 固定高度要求

Scroll 组件的内部元素必须拥有固定高度时才可呈现滚动条。通常通过以下方式设置：
- 直接设置 `Height` 参数
- 在外层容器设置固定高度样式

### 2. 滚动条宽度配置

可以通过 `ScrollWidth` 和 `ScrollHoverWidth` 自定义滚动条宽度，提升用户体验。

### 3. 滚动控制

通过 `@ref` 获取组件实例，可以调用 `ScrollToEnd()` 和 `ScrollToStart()` 方法控制滚动位置。

---

## 常见问题 (FAQ)

### Q1: 为什么滚动条不显示？

**A**: 确保 Scroll 组件的内部元素总高度超过设置的 `Height` 值，并且 `Height` 参数已正确设置。

### Q2: 如何动态更新内容并滚动到底部？

**A**: 更新内容后，调用 `ScrollToEnd()` 方法滚动到底部。

```razor
<Scroll @ref="_scroll" Height="200px">
    @foreach (var item in _items)
    {
        <div>@item</div>
    }
</Scroll>

@code {
    private Scroll? _scroll { get; set; }
    private List<string> _items { get; set; } = new();

    private async Task AddItem()
    {
        _items.Add($"Item {_items.Count + 1}");
        await InvokeAsync(StateHasChanged);
        if (_scroll != null)
        {
            await _scroll.ScrollToEnd();
        }
    }
}
```

### Q3: 如何自定义滚动条样式？

**A**: 通过 `ScrollWidth` 和 `ScrollHoverWidth` 参数控制滚动条宽度，或通过 CSS 自定义滚动条样式。

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 Scroll 组件 |
