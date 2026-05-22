# Transition

## 概述

Transition 动画组件

> Transition Animation Component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/transition](https://www.blazor.zone/transition)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Show` | `bool` | `true` | 获得/设置 是否显示动画，默认 true |
| `TransitionType` | `TransitionType` | `TransitionType.FadeIn` | 获得/设置 动画名称，默认 FadeIn |
| `Duration` | `int` | `}` | 获得/设置 动画执行时长，单位毫秒，默认为 0 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子内容 |
| `OnTransitionEnd` | `Func<Task>?` | `}` | 获得/设置 动画执行完成回调委托 |

## 代码示例

### 基本用法

```razor
<Transition TransitionType="TransitionType.FadeOut" Show="Show" OnTransitionEnd="OnShowEnd">
        <div class="my-3">FadeOut</div>
    </Transition>
```

### 基本用法

```razor
<Transition TransitionType="TransitionType.FadeOut" Show="TransitionEndShow" OnTransitionEnd="OnTransitionEndShow">
        <div class="my-3">FadeOut</div>
    </Transition>
```

### 基本用法

```razor
<Transition TransitionType="TransitionType.FadeIn" Show="FadeInShow" Duration="3000" OnTransitionEnd="OnFadeInEndShow">
        <div class="my-3">FadeIn</div>
    </Transition>
```
