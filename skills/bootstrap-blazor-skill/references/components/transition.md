# Transition (过渡动画)

## 概述

`Transition` 组件用于**在元素显示/隐藏时添加过渡动画效果**，支持多种动画类型和自定义持续时间。

**主要特性**：
- 支持多种动画类型（Fade、Slide、Scale、Rotate 等）
- 可设置动画持续时间（Duration）
- 可设置动画延迟（Delay）
- 支持显示/隐藏切换
- 支持自定义动画曲线（Easing）

**在线演示**: https://www.blazor.zone/transition

---

## 使用场景

### 1. 基础用法（淡入淡出动画）

`Transition` 组件可以通过 `Show` 参数控制显示/隐藏。

```razor
<!-- 淡入淡出动画 -->
<Transition Show="IsVisible">
    <div class="alert alert-info">
        这是一个带过渡动画的内容
    </div>
</Transition>

<Button OnClick="ToggleVisibility">切换显示</Button>

@code {
    private bool IsVisible { get; set; } = true;

    private void ToggleVisibility()
    {
        IsVisible = !IsVisible;
    }
}
```

---

### 2. 不同动画类型（Type）

通过 `Type` 参数设置动画类型。

```razor
<!-- 滑动动画 -->
<Transition Show="IsVisible" Type="TransitionType.Slide">
    <div class="alert alert-info">滑动动画内容</div>
</Transition>

<!-- 缩放动画 -->
<Transition Show="IsVisible" Type="TransitionType.Scale">
    <div class="alert alert-info">缩放动画内容</div>
</Transition>

<!-- 旋转动画 -->
<Transition Show="IsVisible" Type="TransitionType.Rotate">
    <div class="alert alert-info">旋转动画内容</div>
</Transition>

@code {
    private bool IsVisible { get; set; } = true;
}
```

**常用动画类型**：
- `TransitionType.Fade` - 淡入淡出（默认）
- `TransitionType.Slide` - 滑动
- `TransitionType.Scale` - 缩放
- `TransitionType.Rotate` - 旋转
- `TransitionType.Bounce` - 弹跳

---

### 3. 设置动画持续时间（Duration）

通过 `Duration` 参数设置动画持续时间（毫秒）。

```razor
<!-- 快速动画（200ms） -->
<Transition Show="IsVisible" Duration="200">
    <div class="alert alert-info">快速动画</div>
</Transition>

<!-- 慢速动画（1000ms） -->
<Transition Show="IsVisible" Duration="1000">
    <div class="alert alert-info">慢速动画</div>
</Transition>

@code {
    private bool IsVisible { get; set; } = true;
}
```

---

### 4. 设置动画延迟（Delay）

通过 `Delay` 参数设置动画延迟（毫秒）。

```razor
<!-- 延迟 500ms 后执行动画 -->
<Transition Show="IsVisible" Delay="500">
    <div class="alert alert-info">延迟动画</div>
</Transition>

@code {
    private bool IsVisible { get; set; } = true;
}
```

---

### 5. 自定义动画曲线（Easing）

通过 `Easing` 参数设置动画曲线。

```razor
<!-- 匀速动画 -->
<Transition Show="IsVisible" Easing="EasingType.Linear">
    <div class="alert alert-info">匀速动画</div>
</Transition>

<!-- 缓入动画 -->
<Transition Show="IsVisible" Easing="EasingType.EaseIn">
    <div class="alert alert-info">缓入动画</div>
</Transition>

<!-- 缓出动画 -->
<Transition Show="IsVisible" Easing="EasingType.EaseOut">
    <div class="alert alert-info">缓出动画</div>
</Transition>

@code {
    private bool IsVisible { get; set; } = true;
}
```

**常用动画曲线**：
- `EasingType.Linear` - 匀速
- `EasingType.EaseIn` - 缓入
- `EasingType.EaseOut` - 缓出
- `EasingType.EaseInOut` - 缓入缓出

---

## 参数 (Parameters)

### Transition 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Show` | `bool` | `false` | 获得/设置是否显示 |
| `Type` | `TransitionType` | `TransitionType.Fade` | 获得/设置动画类型 |
| `Duration` | `int` | `300` | 获得/设置动画持续时间（毫秒） |
| `Delay` | `int` | `0` | 获得/设置动画延迟（毫秒） |
| `Easing` | `EasingType` | `EasingType.EaseInOut` | 获得/设置动画曲线 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnShown` | `Func<Task>?` | 显示动画完成回调 |
| `OnHidden` | `Func<Task>?` | 隐藏动画完成回调 |

---

## 最佳实践

1. **合理使用动画类型**：`Fade` 适合简单过渡，`Slide` 适合面板展开/收起，`Scale` 适合弹出框
2. **控制动画时长**：快速交互（如按钮点击）使用 200-300ms，复杂动画可使用 500-1000ms
3. **避免过多动画**：过多动画会影响性能，尤其是在移动设备上
4. **处理动画完成事件**：对于需要在动画完成后执行逻辑的场景，处理 `OnShown` 或 `OnHidden` 事件
5. **与 CSS 动画的区别**：`Transition` 是 Blazor 组件级动画，CSS 动画是元素级动画，根据需求选择
6. **性能优化**：对于频繁显示/隐藏的元素，考虑使用 `Display` 组件（通过 CSS `display` 控制）而不是 `Transition`（有动画开销）
