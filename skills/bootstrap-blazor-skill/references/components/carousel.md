# Carousel 走马灯

## 概述

`Carousel` 是一个走马灯组件，在有限空间内循环播放同一类型的图片、文字等内容。适用于需要在网页中展示图片轮播、新闻轮播等场景。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/carousel](https://www.blazor.zone/carousel)

## 使用场景

### 1. 基础用法

适用广泛的基础用法，通过设置 `Images` 属性值对组件进行图片的绑定，值为图片路径数组。

```razor
<Carousel Images="@Images" Width="280" />

@code {
    private List<string> Images { get; set; } = new()
    {
        "images/Pic0.jpg",
        "images/Pic1.jpg",
        "images/Pic2.jpg"
    };
}
```

**说明**:
- `Images` 是 `IEnumerable<string>` 类型，值为图片路径数组
- `Width` 设置走马灯宽度
- 默认显示控制按钮和指示器

### 2. 控制按钮

通过设置 `ShowControls` 属性，设置是否显示控制按钮，默认是 `true`。

```razor
<Carousel Images="@Images" Width="280" ShowControls="true" />

@code {
    private List<string> Images { get; set; } = new()
    {
        "images/Pic0.jpg",
        "images/Pic1.jpg",
        "images/Pic2.jpg"
    };
}
```

**说明**:
- `ShowControls="true"`（默认值）- 显示"上一张"/"下一张"控制按钮
- `ShowControls="false"` - 隐藏控制按钮
- 控制按钮图标可通过 `PreviousIcon`/`NextIcon` 自定义

### 3. 指示器

通过设置 `ShowIndicators` 属性，设置是否显示指示标识，默认是 `true`。

```razor
<Carousel Images="@Images" Width="280" ShowIndicators="true" />
```

**说明**:
- `ShowIndicators="true"`（默认值）- 显示底部的指示点
- `ShowIndicators="false"` - 隐藏指示点
- 点击指示点可直接跳转到对应幻灯片

### 4. 淡入淡出

通过设置 `IsFade` 属性，图片切换时采用淡入淡出效果。

```razor
<Carousel Images="@Images" Width="280" IsFade="true" />
```

**说明**:
- `IsFade="false"`（默认值）- 使用滑动切换效果
- `IsFade="true"` - 使用淡入淡出切换效果

### 5. 标题

通过设置 `CarouselItem` 的 `Caption` 属性，开启标题功能。

```razor
<Carousel Width="280" IsFade="true">
    <CarouselItem Caption="First slide label">
        <img src="images/Pic0.jpg" alt="demo-image" />
    </CarouselItem>
    <CarouselItem Caption="Second slide label">
        <img src="images/Pic1.jpg" alt="demo-image" />
    </CarouselItem>
    <CarouselItem Caption="Third slide label">
        <img src="images/Pic2.jpg" alt="demo-image" />
    </CarouselItem>
</Carousel>
```

**说明**:
- `Caption` 属性设置标题文本
- 标题显示在走马灯底部
- 支持 HTML 内容（通过 `CaptionTemplate`）

### 6. 切换间隔

通过设置 `CarouselItem` 的 `Interval` 属性，可以单独设置幻灯片单独切换时间间隔，间隔默认值 5000 毫秒。

```razor
<Carousel Width="280" IsFade="true">
    <CarouselItem Caption="First slide label" Interval="5000">
        <img src="images/Pic0.jpg" alt="demo-image" />
    </CarouselItem>
    <CarouselItem Caption="Second slide label" Interval="2000">
        <img src="images/Pic1.jpg" alt="demo-image" />
    </CarouselItem>
    <CarouselItem Caption="Third slide label">
        <img src="images/Pic2.jpg" alt="demo-image" />
    </CarouselItem>
</Carousel>
```

**说明**:
- `Interval` 单位：毫秒（ms）
- `Interval="5000"` - 5秒切换一次
- 未设置 `Interval` 的幻灯片使用默认间隔

### 7. 标题模板

通过设置 `CarouselItem` 的 `CaptionTemplate` 属性，自定义标题内容。

```razor
<Carousel Width="280" IsFade="true">
    <CarouselItem>
        <CaptionTemplate>
            <h5>First slide label</h5>
            <p>Pic0.jpg</p>
        </CaptionTemplate>
        <ChildContent>
            <img src="images/Pic0.jpg" alt="demo-image" />
        </ChildContent>
    </CarouselItem>
    <CarouselItem>
        <CaptionTemplate>
            <h5>Second slide label</h5>
            <p>Pic1.jpg</p>
        </CaptionTemplate>
        <ChildContent>
            <img src="images/Pic1.jpg" alt="demo-image" />
        </ChildContent>
    </CarouselItem>
</Carousel>
```

**说明**:
- `CaptionTemplate` 自定义标题区域的内容
- `ChildContent` 自定义幻灯片内容（通常是图片）
- 可以实现复杂的标题布局

### 8. 标题样式

通过设置 `CarouselItem` 的 `CaptionClass` 属性，自定义标题部分样式。

```razor
<Carousel Width="280" IsFade="true">
    <CarouselItem CaptionClass="d-none d-md-block">
        <CaptionTemplate>
            <h5>First slide label</h5>
            <p>Pic0.jpg</p>
        </CaptionTemplate>
        <ChildContent>
            <img src="images/Pic0.jpg" alt="demo-image" />
        </ChildContent>
    </CarouselItem>
</Carousel>
```

**说明**:
- `CaptionClass="d-none d-md-block"` - 在小屏幕下隐藏标题，中等屏幕以上显示
- 可以自定义任何 Bootstrap CSS 类

### 9. 点击图片回调事件

通过设置 `OnClick` 属性后，点击 Image 后触发 `OnClick` 回调委托。

```razor
<Carousel Images="@Images" Width="280" OnClick="OnImageClick" />

@code {
    private List<string> Images { get; set; } = new()
    {
        "images/Pic0.jpg",
        "images/Pic1.jpg",
        "images/Pic2.jpg"
    };

    private Task OnImageClick(string imageUrl)
    {
        Console.WriteLine($"点击了图片: {imageUrl}");
        return Task.CompletedTask;
    }
}
```

**说明**:
- `OnClick` 是 `Func<string, Task>` 类型
- 回调参数 `string` 是点击的图片路径
- 可用于图片预览、跳转链接等场景

### 10. 禁用手势滑动

通过设置 `DisableTouchSwiping` 属性，禁用移动端手势滑动功能。

```razor
<Carousel Images="@Images" Width="280" DisableTouchSwiping="true" />
```

**说明**:
- `DisableTouchSwiping="false"`（默认值）- 允许触摸滑动
- `DisableTouchSwiping="true"` - 禁用触摸滑动
- 适用于不需要移动端滑动的场景

### 11. 子组件

使用 `ChildContent` 渲染自定义组件。

```razor
<Carousel Width="280">
    <CarouselItem>
        <ChildContent>
            <div class="text-center p-5">
                <h3>Sales champion</h3>
                <p>www.blazor.zone</p>
            </div>
        </ChildContent>
    </CarouselItem>
    <CarouselItem>
        <ChildContent>
            <div class="text-center p-5">
                <h3>Sales champion</h3>
                <p>www.blazor.zone</p>
            </div>
        </ChildContent>
    </CarouselItem>
</Carousel>
```

**说明**:
- 不限于图片，可以放置任何自定义内容
- 适用于展示卡片、公告、广告等

## 参数

### Carousel 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `ChildContent` | 获得/设置 子组件，要求使用 `CarouselItem` | `RenderFragment` | `null` |
| `DisableTouchSwiping` | 获得/设置 是否禁用移动端手势滑动，默认 `false` | `bool` | `false` |
| `HoverPause` | 获得/设置 鼠标悬停时是否暂停播放，默认 `true` | `bool` | `true` |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `Images` | 获得 Images 集合 | `IEnumerable<string>` | `[]` |
| `IsFade` | 获得/设置 是否采用淡入淡出效果，默认为 `false` | `bool` | `false` |
| `NextIcon` | 获得/设置 下一页图标 | `string` | - |
| `OnClick` | 获得/设置 点击 Image 回调委托 | `Func<string, Task>` | - |
| `OnSlideChanged` | 获得/设置 幻灯片切换后回调方法 | `Func<int, Task>` | - |
| `PlayMode` | 获得/设置 自动播放方式，默认 `CarouselPlayMode.AutoPlayOnload` | `CarouselPlayMode` | `AutoPlayOnload` |
| `PreviousIcon` | 获得/设置 上一页图标 | `string` | - |
| `ShowControls` | 获得/设置 是否显示控制按钮，默认 `true` | `bool` | `true` |
| `ShowIndicators` | 获得/设置 是否显示指示标志，默认 `true` | `bool` | `true` |
| `Width` | 获得/设置 内部图片的宽度 | `string` | - |

### CarouselItem 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Caption` | 获得/设置 标题文本 | `string` | `null` |
| `CaptionClass` | 获得/设置 标题样式类 | `string` | `null` |
| `CaptionTemplate` | 获得/设置 标题模板 | `RenderFragment` | `null` |
| `ChildContent` | 获得/设置 子内容 | `RenderFragment` | `null` |
| `Interval` | 获得/设置 切换间隔（毫秒） | `int` | `5000` |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `OnClick` | 获得/设置 点击 Image 回调委托 | `Func<string, Task>` |
| `OnSlideChanged` | 获得/设置 幻灯片切换后回调方法 | `Func<int, Task>` |

## 最佳实践

### 1. 使用 Images 绑定简单图片列表

当只需要展示图片轮播时，使用 `Images` 参数最简单。

```razor
<!-- 推荐：使用 Images 绑定 -->
<Carousel Images="@Images" Width="280" />

@code {
    private List<string> Images { get; set; } = new()
    {
        "images/Pic0.jpg",
        "images/Pic1.jpg",
        "images/Pic2.jpg"
    };
}

<!-- 不推荐：手动写 CarouselItem -->
<Carousel Width="280">
    <CarouselItem><img src="images/Pic0.jpg" /></CarouselItem>
    <CarouselItem><img src="images/Pic1.jpg" /></CarouselItem>
    <CarouselItem><img src="images/Pic2.jpg" /></CarouselItem>
</Carousel>
```

### 2. 自定义内容使用 CarouselItem

当需要自定义标题、内容时，使用 `CarouselItem` 子组件。

```razor
<Carousel Width="280">
    <CarouselItem Caption="标题 1">
        <ChildContent>
            <div class="custom-content">
                <h3>自定义内容</h3>
                <p>可以是任何 HTML 内容</p>
            </div>
        </ChildContent>
    </CarouselItem>
</Carousel>
```

### 3. 设置合适的切换间隔

根据内容类型设置合适的切换间隔。

```razor
<!-- 场景 1：图片轮播 - 5秒 -->
<Carousel Images="@Images" Width="280" />

<!-- 场景 2：新闻公告 - 3秒 -->
<Carousel Width="280">
    <CarouselItem Interval="3000">
        <ChildContent><p>最新公告...</p></ChildContent>
    </CarouselItem>
</Carousel>

<!-- 场景 3：广告轮播 - 8秒 -->
<Carousel Width="280">
    <CarouselItem Interval="8000">
        <ChildContent><img src="ad.jpg" /></ChildContent>
    </CarouselItem>
</Carousel>
```

### 4. 响应式设计

使用 `CaptionClass` 实现响应式标题显示。

```razor
<Carousel Width="280">
    <CarouselItem CaptionClass="d-none d-md-block">
        <CaptionTemplate>
            <h5>标题</h5>
            <p>小屏幕隐藏标题，中等屏幕以上显示</p>
        </CaptionTemplate>
        <ChildContent>
            <img src="images/Pic0.jpg" />
        </ChildContent>
    </CarouselItem>
</Carousel>
```

## 常见问题

### 1. 图片不显示

**问题**: 走马灯区域显示，但图片不显示。

**原因**: 可能是 `Images` 路径不正确，或者图片文件不存在。

**解决方案**:
- 检查 `Images` 路径是否正确（相对于 wwwroot）
- 检查图片文件是否存在于指定路径
- 使用浏览器开发者工具查看网络请求，确认图片 URL 是否正确

```razor
<!-- 错误：路径不正确 -->
<Carousel Images="@Images" />
@code {
    private List<string> Images = new() { "Pic0.jpg" };  /* 应为 "images/Pic0.jpg" */
}

<!-- 正确：路径正确 -->
@code {
    private List<string> Images = new() { "images/Pic0.jpg" };
}
```

### 2. 自动播放不工作

**问题**: 走马灯加载后不自动播放。

**原因**: 可能是 `PlayMode` 设置不正确，或者 `HoverPause` 导致鼠标悬停时暂停。

**解决方案**:
- 检查 `PlayMode` 是否为 `AutoPlayOnload` 或 `AutoPlayOnLoad`
- 检查是否有鼠标悬停在走马灯上（会暂停播放）
- 设置 `HoverPause="false"` 禁用悬停暂停

```razor
<Carousel Images="@Images" Width="280" PlayMode="CarouselPlayMode.AutoPlayOnload" HoverPause="false" />
```

### 3. 手势滑动不工作

**问题**: 在移动设备上，滑动手势不工作。

**原因**: 可能是 `DisableTouchSwiping="true"` 禁用了触摸滑动。

**解决方案**: 设置 `DisableTouchSwiping="false"`（默认值）启用触摸滑动。

```razor
<Carousel Images="@Images" Width="280" DisableTouchSwiping="false" />
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | Carousel 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 `OnSlideChanged` 回调；优化触摸滑动逻辑 |
| 8.0.0 | 2024-11-10 | 新增 `PlayMode` 参数；支持自动播放控制 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Carousel](https://www.blazor.zone/carousel)
- [Bootstrap Blazor API - Carousel](https://www.blazor.zone/api/Carousel)
- [Bootstrap 官方文档 - Carousel](https://getbootstrap.com/docs/5.3/components/carousel/) (Bootstrap Carousel 组件)
