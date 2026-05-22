# Carousel

## 概述

Carousel 组件

> Carousel component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/carousel](https://www.blazor.zone/carousel)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Images` | `IEnumerable<string>` | `[]` | 获得 Images 集合 |
| `Width` | `string?` | `}` | 获得/设置 内部图片的宽度 |
| `IsFade` | `bool` | `}` | 获得/设置 是否采用淡入淡出效果 默认为 false |
| `Task` | `Func<string,` | `}` | 获得/设置 点击 Image 回调委托 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 要求使用 <see cref="CarouselItem"/> |
| `ShowControls` | `bool` | `true` | 获得/设置 是否显示控制按钮 默认 true |
| `ShowIndicators` | `bool` | `true` | 获得/设置 是否显示指示标志 默认 true |
| `DisableTouchSwiping` | `bool` | `}` | 获得/设置 是否禁用移动端手势滑动 默认 false |
| `PreviousIcon` | `string?` | `}` | 获得/设置 上一页图标 |
| `NextIcon` | `string?` | `}` | 获得/设置 下一页图标 |
| `HoverPause` | `bool` | `true` | 获得/设置 鼠标悬停时是否暂停播放 默认 true |
| `PlayMode` | `CarouselPlayMode` | `}` | 获得/设置 自动播放方式 默认 <see cref="CarouselPlayMode.AutoPlayOnload"/> |

## 代码示例

### 基本用法

```razor
<Carousel Width="280" IsFade="true">
        <CarouselItem Caption="First slide label">
            <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic0.jpg")" alt="demo-image" />
        </CarouselItem>
        <CarouselItem Caption="Second slide label">
            <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic1.jpg")" alt="demo-image" />
        </CarouselItem>
        <CarouselItem Caption="Third slide label">
            <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic2.jpg")" alt="demo-image" />
        </CarouselItem>
    </Carousel>
```

### 基本用法

```razor
<Carousel Width="280" IsFade="true">
        <CarouselItem Caption="First slide label" Interval="5000">
            <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic0.jpg")" alt="demo-image" />
        </CarouselItem>
        <CarouselItem Caption="Second slide label" Interval="2000">
            <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic1.jpg")" alt="demo-image" />
        </CarouselItem>
        <CarouselItem Caption="Third slide label">
            <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic2.jpg")" alt="demo-image" />
        </CarouselItem>
    </Carousel>
```

### 基本用法

```razor
<Carousel Width="280" IsFade="true">
        <CarouselItem>
            <CaptionTemplate>
                <h5>First slide label</h5>
                <p>Pic0.jpg</p>
            </CaptionTemplate>
            <ChildContent>
                <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic0.jpg")" alt="demo-image" />
            </ChildContent>
        </CarouselItem>
        <CarouselItem>
            <CaptionTemplate>
                <h5>Second slide label</h5>
                <p>Pic1.jpg</p>
            </CaptionTemplate>
            <ChildContent>
                <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic1.jpg")" alt="demo-image" />
            </ChildContent>
        </CarouselItem>
        <CarouselItem>
            <CaptionTemplate>
                <h5>Third slide label</h5>
                <p>Pic2.jpg</p>
            </CaptionTemplate>
            <ChildContent>
                <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic2.jpg")" alt="demo-image" />
            </ChildContent>
        </CarouselItem>
    </Carousel>
```

### 基本用法

```razor
<Carousel Width="280" IsFade="true">
        <CarouselItem CaptionClass="d-none d-md-block">
            <CaptionTemplate>
                <h5>First slide label</h5>
                <p>Pic0.jpg</p>
            </CaptionTemplate>
            <ChildContent>
                <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic0.jpg")" alt="demo-image" />
            </ChildContent>
        </CarouselItem>
        <CarouselItem CaptionClass="d-none d-md-block">
            <CaptionTemplate>
                <h5>Second slide label</h5>
                <p>Pic1.jpg</p>
            </CaptionTemplate>
            <ChildContent>
                <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic1.jpg")" alt="demo-image" />
            </ChildContent>
        </CarouselItem>
        <CarouselItem CaptionClass="d-none d-md-block">
            <CaptionTemplate>
                <h5>Third slide label</h5>
                <p>Pic2.jpg</p>
            </CaptionTemplate>
            <ChildContent>
                <img src="@WebsiteOption.Value.GetAssetUrl("images/Pic2.jpg")" alt="demo-image" />
            </ChildContent>
        </CarouselItem>
    </Carousel>
```

### 基本用法

```razor
<Carousel Images="@_images" Width="280" IsFade="true" OnClick="@OnClick"></Carousel>
```
