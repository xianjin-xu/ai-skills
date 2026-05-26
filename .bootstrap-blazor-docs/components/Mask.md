# Mask (加载遮罩)

## 概述

`Mask` 组件用于在页面或元素上**显示加载遮罩**，常用于数据加载、提交中等需要阻止用户操作的场景。

**主要特性**：
- 支持全页遮罩或局部遮罩
- 支持自定义遮罩颜色
- 支持显示加载提示文本
- 支持自定义提示内容
- 支持通过 `@ref` 控制显隐

**在线演示**: https://www.blazor.zone/mask

---

## 使用场景

### 1. 基础用法（全页遮罩）

通过 `@ref` 获取组件引用，然后调用 `Show()` 和 `Hide()` 方法控制显隐。

```razor
<!-- 全页遮罩 -->
<Mask @ref="MaskRef" />

<Button OnClick="ShowMask">显示遮罩</Button>
<Button OnClick="HideMask">隐藏遮罩</Button>

@code {
    private Mask? MaskRef { get; set; }

    private void ShowMask() => MaskRef?.Show();
    private void HideMask() => MaskRef?.Hide();
}
```

---

### 2. 局部遮罩（Target）

通过 `Target` 参数指定遮罩目标元素（局部遮罩）。

```razor
<!-- 局部遮罩 -->
<div @ref="TargetElement" style="height: 200px; position: relative;">
    <p>这是目标区域内容...</p>
</div>

<Mask @ref="MaskRef" Target="@TargetElement" />

<Button OnClick="ShowMask">显示局部遮罩</Button>
<Button OnClick="HideMask">隐藏遮罩</Button>

@code {
    private ElementReference TargetElement { get; set; }
    private Mask? MaskRef { get; set; }

    private void ShowMask() => MaskRef?.Show();
    private void HideMask() => MaskRef?.Hide();
}
```

---

### 3. 显示提示文本（Text）

通过 `Text` 参数显示提示文本。

```razor
<!-- 带提示文本的遮罩 -->
<Mask @ref="MaskRef" Text="加载中，请稍候..." />

<Button OnClick="ShowMask">显示遮罩</Button>

@code {
    private Mask? MaskRef { get; set; }

    private void ShowMask() => MaskRef?.Show();
}
```

---

### 4. 自定义提示内容（ChildContent）

通过 `ChildContent` 自定义提示内容（支持任意 HTML）。

```razor
<!-- 自定义提示内容 -->
<Mask @ref="MaskRef">
    <ChildContent>
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2">正在加载数据，请稍候...</p>
        </div>
    </ChildContent>
</Mask>

<Button OnClick="ShowMask">显示自定义遮罩</Button>

@code {
    private Mask? MaskRef { get; set; }

    private void ShowMask() => MaskRef?.Show();
}
```

---

### 5. 自定义遮罩颜色（Color）

通过 `Color` 参数设置遮罩背景颜色。

```razor
<!-- 白色遮罩 -->
<Mask @ref="MaskRef" Color="Color.Light" Text="加载中..." />

<!-- 深色遮罩 -->
<Mask @ref="MaskRef" Color="Color.Dark" Text="加载中..." />

<Button OnClick="ShowMask">显示遮罩</Button>

@code {
    private Mask? MaskRef { get; set; }

    private void ShowMask() => MaskRef?.Show();
}
```

---

## 参数 (Parameters)

### Mask 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置提示文本 |
| `Target` | `ElementReference?` | `null` | 获得/设置遮罩目标元素（局部遮罩） |
| `Color` | `Color` | `Color.Light` | 获得/设置遮罩背景颜色 |
| `Opacity` | `double` | `0.5` | 获得/设置遮罩透明度 |
| `ZIndex` | `int` | `1050` | 获得/设置遮罩 z-index |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置自定义提示内容 |

---

## 方法 (Methods)

### Mask 组件方法

| 方法名 | 返回类型 | 说明 |
|--------|----------|------|
| `Show()` | `void` | 显示遮罩 |
| `Show(string? text)` | `void` | 显示遮罩（可指定提示文本） |
| `Hide()` | `void` | 隐藏遮罩 |

---

## 最佳实践

1. **合理使用 Target**：全页遮罩不需要 `Target`，局部遮罩需要指定 `Target`（通过 `@ref` 获取 `ElementReference`）
2. **自定义提示内容**：通过 `ChildContent` 自定义加载提示（如添加进度条、百分比等）
3. **设置合适的 Opacity**：通过 `Opacity` 参数控制遮罩透明度（0-1），默认 0.5
4. **与 Loading 的区别**：`Mask` 是遮罩层（阻止交互），`Loading` 是加载指示器（不阻止交互）
5. **避免过度使用**：频繁显示/隐藏遮罩会影响用户体验，考虑使用骨架屏（Skeleton）
6. **异步场景**：在异步操作开始时 `Show()`，操作完成后 `Hide()`
