# IntersectionObserver

## 概述

可见检测组件

> 可见检测component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/intersection-observer](https://www.blazor.zone/intersection-observer)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `UseElementViewport` | `bool` | `true` | 获得/设置 是否使用元素视口作为根元素 默认为 true 使用当前元素作为根元素 <para>The element that is used as the viewport for checking visibility of the target. Must be the ancestor of the target. Defaults to the browser viewport if value is false. Default value is true |
| `RootMargin` | `string?` | `}` | Margin around the root. Can have values similar to the CSS margin 属性, e.g. "10px 20px 30px 40px" (top, right, bottom, left). values can be percentages. This set of values serves to grow or shrink each side of the root element's bounding box before computing intersections. 默认s to all zeros |
| `Threshold` | `string?` | `}` | Either a single number or an array of numbers which indicate at what percentage of the target's visibility the observer's 回调 should be executed. If you only want to detect when visibility passes the 50% mark, you can use a value of 0.5. If you want the 回调 to run every time visibility passes another 25%, you would specify the array [0, 0.25, 0.5, 0.75, 1]. default is 0 (meaning as soon as even one pixel is visible, the 回调 will be run). A value of 1.0 means that the threshold isn't considered passed until every pixel is visible |
| `AutoUnobserveWhenIntersection` | `bool` | `true` | 获得/设置 可见后是否自动取消观察 默认 true 可见后自动取消观察提高性能 |
| `AutoUnobserveWhenNotIntersection` | `bool` | `}` | 获得/设置 不可见后是否自动取消观察 默认 false 不可见后自动取消观察提高性能 |
| `Task` | `Func<IntersectionObserverEntry,` | `}` | 获得/设置 已经交叉回调方法 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |

## 代码示例

### 基本用法

```razor
<IntersectionObserver OnIntersecting="OnIntersectingAsync">
        <div class="bb-list-main scroll">
            @foreach (var image in _images)
            {
                <IntersectionObserverItem>
                    <div class="bb-list-item">
                        <img src="@image" />
                    </div>
                </IntersectionObserverItem>
            }
        </div>
    </IntersectionObserver>
```

### 基本用法

```razor
<IntersectionObserver OnIntersecting="OnLoadMoreAsync" Threshold="1" AutoUnobserveWhenIntersection="false">
        <div class="bb-list-load scroll">
            <div class="bb-list-demo">
                @foreach (var image in _items)
                {
                    <div class="bb-list-item">
                        <img src="@image" />
                    </div>
                }
            </div>
            <IntersectionObserverItem>
                <div class="bb-list-item-loading">
                    <Spinner></Spinner>
                </div>
            </IntersectionObserverItem>
        </div>
    </IntersectionObserver>
```

### 基本用法

```razor
<IntersectionObserver OnIntersecting="OnVisibleChanged" Threshold="1" AutoUnobserveWhenIntersection="false">
        <div class="bb-video-demo scroll">
            <div class="bb-video">
                <IntersectionObserverItem>
                    <VideoDemo @ref="_video"></VideoDemo>
                </IntersectionObserverItem>
            </div>
        </div>
    </IntersectionObserver>
```

### 基本用法

```razor
<IntersectionObserver OnIntersecting="OnThresholdChanged" Threshold="0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1"
                          AutoUnobserveWhenIntersection="false">
        <div class="bb-list-load scroll" style="height: 200px;">
            <div class="d-flex" style="height: 600px; justify-content: center; align-items: center;">
                <IntersectionObserverItem>
                    <div class="bb-list-item bg-info"></div>
                </IntersectionObserverItem>
            </div>
        </div>
    </IntersectionObserver>
```
