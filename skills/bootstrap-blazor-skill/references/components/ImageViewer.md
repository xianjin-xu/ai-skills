# ImageViewer

## 概述

Image 组件

> Image Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/image-viewer](https://www.blazor.zone/image-viewer)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Url` | `string?` | `}` | 获得/设置 图片 Url 默认 null 必填 |
| `IsAsync` | `bool` | `}` | 获得/设置 图片是否异步加载 |
| `Alt` | `string?` | `}` | 获得/设置 原生 alt 属性 默认 null 未设置 |
| `ShowPlaceHolder` | `bool` | `}` | 获得/设置 是否显示占位符 适用于大图片加载 默认 false |
| `HandleError` | `bool` | `}` | 获得/设置 加载失败时是否显示错误占位符 默认 false |
| `PlaceHolderTemplate` | `RenderFragment?` | `}` | 获得/设置 占位模板 未设置 <see cref="Url"/> 或者 正在加载时显示 默认 null 未设置 |
| `ErrorTemplate` | `RenderFragment?` | `}` | 获得/设置 错误模板 默认 null 未设置 |
| `FitMode` | `ObjectFitMode` | `}` | 获得/设置 原生 object-fit 属性 默认 fill 未设置 |
| `ZIndex` | `int` | `2050` | 获得/设置 原生 z-index 属性 默认 2050 |
| `PreviewList` | `List<string>?` | `}` | 获得/设置 预览大图链接集合 默认 null |
| `PreviewIndex` | `int` | `0` | 获得/设置 预览大图当前链接集合点开的索引 默认为 0 |
| `Task` | `Func<string,` | `}` | 获得/设置 图片加载失败时回调方法 |
| `FileIcon` | `string?` | `}` | 获得/设置 图片文件图标 |
| `IsIntersectionObserver` | `bool` | `}` | - |
| `ZoomSpeed` | `double?` | `}` | 获得/设置 预览缩放速度 默认 null 未设置取 0.015 值 |

## 代码示例

### 基本用法

```razor
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/image-ph.jpeg")" ShowPlaceHolder="true" />
        </div>
        <div class="images-item">
            <div>@Localizer["ImageViewerPlaceHolderCustom"]</div>
            <ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/image-ph.jpeg")" ShowPlaceHolder="true">
                <PlaceHolderTemplate>
                    <div class="bb-img-holder">
                        <div class="bb-img-loading">@Localizer["ImageViewerPlaceHolderLoading"]</div>
                    </div>
                </PlaceHolderTemplate>
            </ImageViewer>
```

### 基本用法

```razor
<ImageViewer Url="">
                <PlaceHolderTemplate>
                    <div class="bb-img-holder">
                        <div class="bb-img-loading">@Localizer["ImageViewerPlaceHolderTemplatePlaceholder"]</div>
                    </div>
                </PlaceHolderTemplate>
            </ImageViewer>
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/image-ph.jpeg")" ShowPlaceHolder="true">
                <PlaceHolderTemplate>
                    <div class="bb-img-holder">
                        <div class="bb-img-loading">@Localizer["ImageViewerPlaceHolderTemplatePlaceholder"]</div>
                    </div>
                </PlaceHolderTemplate>
            </ImageViewer>
```

### 基本用法

```razor
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/error-image.jpeg")" HandleError="true" />
        </div>
        <div class="images-item">
            <div>@Localizer["ImageViewerErrorTemplateCustom"]</div>
            <ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/error-image.jpeg")">
                <ErrorTemplate>
                    <div class="bb-img-holder">
                        <div class="bb-img-loading">@Localizer["ImageViewerErrorTemplateLoadFailed"]</div>
                    </div>
                </ErrorTemplate>
            </ImageViewer>
```

### 基本用法

```razor
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/tutorials/waterfall.png")" IsIntersectionObserver="true" IsAsync="true" style="height: 400px;"></ImageViewer>
```
