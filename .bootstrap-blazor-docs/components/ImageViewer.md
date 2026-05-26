# ImageViewer 图片#

## 概述#

`ImageViewer` 是一个图片组件，图片容器，在保留原生 img 的特性下，支持懒加载、自定义占位、加载失败等。适用于需要展示图片并优化加载体验的场景。#

**命名空间**: `BootstrapBlazor.Components`#

**在线演示**: [https://www.blazor.zone/image-viewer](https://www.blazor.zone/image-viewer)#

## 使用场景#

### 1. 基本用法#

加载并显示图片文件。#

```razor#
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/image-ph.jpeg")" ShowPlaceHolder="true" />#
```#

**说明**:#
- `Url` 设置图片 URL（必填）#
- `ShowPlaceHolder="true"` 显示加载占位符#
- 图片加载完成后自动显示#

### 2. 占位内容#

可通过设置 `ShowPlaceHolder` 开启占位符功能，通过设置 `PlaceHolderTemplate` 自定义占位内容。#

```razor#
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/image-ph.jpeg")" ShowPlaceHolder="true">#
    <PlaceHolderTemplate>#
        <div class="bb-img-holder">#
            <div class="bb-img-loading">加载中...</div>#
        </div>#
    </PlaceHolderTemplate>#
</ImageViewer>#
```#

**说明**:#
- `PlaceHolderTemplate` 自定义占位内容#
- 未设置 `Url` 或者正在加载时显示此模板内容#
- 图片加载后浏览器默认会缓存，建议 F12 关闭缓存体验此功能#

### 3. 加载失败#

可通过设置 `ErrorTemplate` 开启错误模板功能，参数 `Url` 无法加载图片时显示此模板内容。#

```razor#
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/error-image.jpeg")" HandleError="true">#
    <ErrorTemplate>#
        <div class="bb-img-holder">#
            <div class="bb-img-loading">加载失败</div>#
        </div>#
    </ErrorTemplate>#
</ImageViewer>#
```#

**说明**:#
- `HandleError="true"` 加载失败时显示错误占位符#
- `ErrorTemplate` 自定义错误提示内容#
- 适用于图片 URL 可能无效的场景#

### 4. 大图预览#

可通过设置 `PreviewList` 开启预览大图的功能，设置 `ZoomSpeed` 控制滚动缩放时的速度。#

```razor#
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/tutorials/waterfall.png")" #
           PreviewList="@PreviewList" #
           ZoomSpeed="0.015" />#

@code {#
    private List<string>? PreviewList { get; set; }

    protected override void OnInitialized()#
    {#
        base.OnInitialized();#
        PreviewList = new List<string>#
        {#
            WebsiteOption.Value.GetAssetUrl("images/tutorials/waterfall.png"),#
            WebsiteOption.Value.GetAssetUrl("images/Pic0.jpg"),#
            WebsiteOption.Value.GetAssetUrl("images/Pic1.jpg")#
        };#
    }#
}#
```#

**说明**:#
- `PreviewList` 设置预览大图的图片链接集合#
- 点击图片后弹出大图预览，可缩放、旋转#
- `ZoomSpeed` 控制缩放速度（默认 0.015）#

### 5. 懒加载#

通过设置 `IsIntersectionObserver="true"` 开启懒加载特性，当图片在不可见区域时不加载图片，当图片即将可见时才开始加载图片。#

```razor#
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/tutorials/waterfall.png")" #
           IsIntersectionObserver="true" #
           IsAsync="true" #
           style="height: 400px;">#
```#

**说明**:#
- `IsIntersectionObserver="true"` 开启懒加载#
- `IsAsync="true"` 图片异步加载#
- 适用于图片列表、瀑布流等场景，提升页面加载性能#

### 6. Object-Fit 模式#

`FitMode` 设置原生 object-fit 属性，控制图片填充模式。#

```razor#
<!-- Fill：填充（默认） -->#
<ImageViewer Url="image.jpg" FitMode="ObjectFitMode.Fill" />#

<!-- Contain：包含 -->#
<ImageViewer Url="image.jpg" FitMode="ObjectFitMode.Contain" />#

<!-- Cover：覆盖 -->#
<ImageViewer Url="image.jpg" FitMode="ObjectFitMode.Cover" />#

<!-- None：无 -->#
<ImageViewer Url="image.jpg" FitMode="ObjectFitMode.None" />#

<!-- ScaleDown：降低 -->#
<ImageViewer Url="image.jpg" FitMode="ObjectFitMode.ScaleDown" />#
```#

**说明**:#
- `Fill` - 使图片拉伸填满整个容器，不保证保持原有的比例#
- `Contain` - 保持原有尺寸比例缩放，保证整个图片都可以出现在容器中#
- `Cover` - 保持原有尺寸比例缩放，宽度和高度至少有一个和容器一致#
- `None` - 保持原有尺寸比例，同时保持图片原始尺寸大小#
- `ScaleDown` - 就好像依次设置了 None 或 Contain，最终呈现的是尺寸比较小的那个#

## 参数#

### ImageViewer 组件参数#

| 参数 | 说明 | 类型 | 默认值 |#
|------|------|------|--------|#
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |#
| `Alt` | 获得/设置 原生 alt 属性，默认 `null` 未设置 | `string?` | `null` |#
| `ErrorTemplate` | 获得/设置 错误模板，默认 `null` 未设置 | `RenderFragment?` | `null` |#
| `FileIcon` | 获得/设置 图片文件图标 | `string?` | - |#
| `FitMode` | 获得/设置 原生 object-fit 属性，默认 `fill` 未设置 | `ObjectFitMode` | `Fill` |#
| `HandleError` | 获得/设置 加载失败时是否显示错误占位符，默认 `false` | `bool` | `false` |#
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |#
| `IsAsync` | 获得/设置 图片是否异步加载 | `bool` | - |#
| `IsIntersectionObserver` | 获得/设置 是否交叉监听，默认 `false` | `bool` | `false` |#
| `OnErrorAsync` | 获得/设置 图片加载失败时回调方法 | `Func<string, Task>` | - |#
| `OnLoadAsync` | 获得/设置 图片加载成功时回调方法 | `Func<string, Task>` | - |#
| `PlaceHolderTemplate` | 获得/设置 占位模板，未设置 `Url` 或者正在加载时显示，默认 `null` 未设置 | `RenderFragment?` | `null` |#
| `PreviewIndex` | 获得/设置 预览大图当前链接集合点开的索引，默认为 `0` | `int` | `0` |#
| `PreviewList` | 获得/设置 预览大图链接集合，默认 `null` | `List<string>?` | `null` |#
| `ShowPlaceHolder` | 获得/设置 是否显示占位符，适用于大图片加载，默认 `false` | `bool` | `false` |#
| `Url` | 获得/设置 图片 Url，默认 `null` 必填 | `string?` | `null` |#
| `ZIndex` | 获得/设置 原生 z-index 属性，默认 `2050` | `int` | `2050` |#
| `ZoomSpeed` | 获得/设置 预览缩放速度，默认 `null` 未设置取 `0.015` 值 | `double?` | `null` |#

## 事件回调#

| 事件 | 说明 | 类型 |#
|------|------|------|#
| `OnErrorAsync` | 获得/设置 图片加载失败时回调方法 | `Func<string, Task>` |#
| `OnLoadAsync` | 获得/设置 图片加载成功时回调方法 | `Func<string, Task>` |#

## 最佳实践#

### 1. 使用懒加载优化性能#

在图片列表场景使用 `IsIntersectionObserver="true"` 开启懒加载，提升页面性能。#

```razor#
@foreach (var imageUrl in ImageList)#
{#
    <ImageViewer Url="@imageUrl" #
               IsIntersectionObserver="true" #
               ShowPlaceHolder="true" #
               style="height: 200px;" />#
}#
```#

### 2. 自定义占位和错误模板#

使用 `PlaceHolderTemplate` 和 `ErrorTemplate` 自定义加载状态和错误状态的显示。#

```razor#
<ImageViewer Url="@ImageUrl" #
           ShowPlaceHolder="true" #
           HandleError="true">#
    <PlaceHolderTemplate>#
        <div class="custom-placeholder">#
            <SpinLoader />#
            <p>图片加载中...</p>#
        </div>#
    </PlaceHolderTemplate>#
    <ErrorTemplate>#
        <div class="custom-error">#
            <Icon Name="fa-solid fa-triangle-exclamation" />#
            <p>图片加载失败</p>#
            <button @onclick="ReloadImage">重试</button>#
        </div>#
    </ErrorTemplate>#
</ImageViewer>#
```#

### 3. 开启大图预览功能#

设置 `PreviewList` 开启大图预览，让用户可以查看高清大图。#

```razor#
<ImageViewer Url="@ThumbnailUrl" #
           PreviewList="@ImageUrls" #
           PreviewIndex="0" />#

@code {#
    private string ThumbnailUrl = "image-small.jpg";#
    private List<string> ImageUrls = new()#
    {#
        "image-large1.jpg",#
        "image-large2.jpg",#
        "image-large3.jpg"#
    };#
}#
```

**说明**:#
- 点击缩略图后弹出大图预览#
- 可以缩放、旋转、切换图片#
- `PreviewIndex` 设置初始预览的图片索引#

## 常见问题#

### 1. 图片不显示#

**问题**: ImageViewer 区域显示，但图片不显示。#

**原因**: 可能是 `Url` 路径不正确，或者图片文件不存在。#

**解决方案**:#
- 检查 `Url` 路径是否正确（相对于 wwwroot）#
- 检查图片文件是否存在于指定路径#
- 使用浏览器开发者工具查看网络请求，确认图片 URL 是否正确#

```razor#
<!-- 错误：路径不正确 -->#
<ImageViewer Url="image.jpg" />  /* 应为 "images/image.jpg" */#

<!-- 正确：路径正确 -->#
<ImageViewer Url="@WebsiteOption.Value.GetAssetUrl("images/image.jpg")" />#
```

### 2. 懒加载不工作#

**问题**: 设置了 `IsIntersectionObserver="true"`，但图片仍然立即加载。#

**原因**: 可能是浏览器不支持 IntersectionObserver API，或者组件未正确渲染。#

**解决方案**:#
- 检查浏览器是否支持 IntersectionObserver（现代浏览器都支持）#
- 确保图片在可视区域外时才设置懒加载#
- 使用浏览器开发者工具检查元素属性#

```razor#
<ImageViewer Url="@ImageUrl" #
           IsIntersectionObserver="true" #
           IsAsync="true" />#
```

### 3. 大图预览无法弹出#

**问题**: 点击图片后，大图预览没有弹出。#

**原因**: 可能是未设置 `PreviewList`，或者 `PreviewList` 为 `null`。#

**解决方案**: 确保设置了 `PreviewList` 并且包含有效的图片 URL。#

```razor#
<ImageViewer Url="@ImageUrl" PreviewList="@PreviewList" />#

@code {#
    private List<string> PreviewList { get; set; } = new();#

    protected override void OnInitialized()#
    {#
        PreviewList = new List<string> { "large-image1.jpg", "large-image2.jpg" };#
    }#
}#
```

## 版本历史#

| 版本 | 发布日期 | 变更内容 |#
|------|----------|----------|#
| 6.0.0 | 2023-01-15 | ImageViewer 组件首次发布 |#
| 7.0.0 | 2024-01-15 | 新增 `IsIntersectionObserver` 参数；优化懒加载逻辑 |#
| 8.0.0 | 2024-11-10 | 新增 `ZoomSpeed` 参数；支持预览缩放速度控制 |#

## 参考链接#

- [Bootstrap Blazor 官方文档 - ImageViewer](https://www.blazor.zone/image-viewer)#
- [Bootstrap Blazor API - ImageViewer](https://www.blazor.zone/api/ImageViewer)#
- [MDN Web Docs - img](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) (HTML img 元素)#
- [MDN Web Docs - IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver) (懒加载 API)#
