# ImageCropper 图像裁剪

## 概述

`ImageCropper` 是一个图像裁剪组件，提供了直观的界面来裁剪和编辑图像。组件基于 Cropper.js 库实现，支持调整裁剪框大小、旋转图像、设置纵横比等功能。

**注意事项**：本组件依赖于 `BootstrapBlazor.ImageCropper`，使用本组件时需要引用其组件包。

## 安装

使用 Nuget.org 进行 `BootstrapBlazor.ImageCropper` 组件的安装：

**.NET CLI**
```bash
dotnet add package BootstrapBlazor.ImageCropper
```

**PackageReference**
```xml
<PackageReference Include="BootstrapBlazor.ImageCropper" Version="11.0.0" />
```

**Package Manager**
```
Install-Package BootstrapBlazor.ImageCropper
```

## 使用场景

### 1. 基础用法

通过设置 `Url` 参数设置图片地址，可通过设置 `ImageCropperOption.AspectRatio=16/9f` 设置裁剪框比例，`1` 时为正方形。

```razor
<ImageCropper Url="images/logo.jpg" 
           Options="@Options" 
           OnCropAsync="OnCropAsync" />

@code {
    private ImageCropperOption Options { get; set; } = new ImageCropperOption();
    private string? CroppedImage { get; set; }

    private Task OnCropAsync(ImageCropperResult result)
    {
        CroppedImage = result.Data;
        StateHasChanged();
        return Task.CompletedTask;
    }
}
```

**说明**:
- `Url` - 设置要裁剪的图像地址
- `Options` - 设置裁剪选项（如宽高比、视图模式等）
- `OnCropAsync` - 裁剪结果回调方法，返回 `ImageCropperResult` 对象

### 2. 圆形裁剪

通过设置 `IsRound` 参数设置裁剪方式为圆形。

```razor
<ImageCropper Url="images/logo.jpg" 
           Options="@(new ImageCropperOption { IsRound = true })" />
```

**说明**:
- 默认裁剪框为矩形
- `IsRound = true` - 裁剪框变为圆形
- 适用于头像裁剪等场景

## 参数

### ImageCropper 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `CropperShape` ⚠️弃用 | 获取/设置 裁剪形状（矩形/圆形）默认为 `Rectangle` | `ImageCropperShape` | `Rectangle` |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `IsDisabled` | 获取/设置 是否被禁用 默认 `false` | `bool` | `false` |
| `OnCropAsync` | 获得/设置 剪裁结果回调方法 | `Func<ImageCropperResult, Task>` | - |
| `OnCropChangedAsync` | 获得/设置 剪裁框调整大小位置回调方法 | `Func<ImageCropperData, Task>` | - |
| `Options` | 获取/设置 裁剪选项 | `ImageCropperOption` | - |
| `Url` | 获得/设置 图片地址 URL | `string` | - |

### ImageCropperOption 裁剪选项

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AspectRatio` | 获取/设置 裁剪框宽高比，默认 `0` 为自由比例 | `float` | `0` |
| `ViewMode` | 获取/设置 视图模式 `0-3`，默认 `0` | `int` | `0` |
| `IsRound` | 获取/设置 是否圆形裁剪，默认 `false` | `bool` | `false` |
| `DragMode` | 获取/设置 拖拽模式，默认 `Crop` | `DragMode` | `Crop` |
| `Scalable` | 获取/设置 是否可缩放，默认 `true` | `bool` | `true` |
| `Rotatable` | 获取/设置 是否可旋转，默认 `true` | `bool` | `true` |
| `Zoomable` | 获取/设置 是否可缩放，默认 `true` | `bool` | `true` |
| `AutoCrop` | 获取/设置 是否初始化时自动裁剪，默认 `true` | `bool` | `true` |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `OnCropAsync` | 获得/设置 剪裁结果回调方法 | `Func<ImageCropperResult, Task>` |
| `OnCropChangedAsync` | 获得/设置 剪裁框调整大小位置回调方法 | `Func<ImageCropperData, Task>` |

## ImageCropperResult 裁剪结果

| 属性 | 说明 | 类型 |
|------|------|------|
| `Data` | Base64 格式的裁剪后图像数据 | `string` |
| `Width` | 裁剪后图像宽度 | `int` |
| `Height` | 裁剪后图像高度 | `int` |
| `X` | 裁剪区域 X 坐标 | `int` |
| `Y` | 裁剪区域 Y 坐标 | `int` |

## 最佳实践

### 1. 设置合理的宽高比

根据使用场景设置合适的 `AspectRatio` 宽高比。

```razor
<!-- 正方形头像：1:1 -->
<ImageCropper Url="avatar.jpg" 
           Options="@(new ImageCropperOption { AspectRatio = 1f })" />

<!-- 16:9 横幅 -->
<ImageCropper Url="banner.jpg" 
           Options="@(new ImageCropperOption { AspectRatio = 16f/9f })" />

<!-- 4:3 标准 -->
<ImageCropper Url="photo.jpg" 
           Options="@(new ImageCropperOption { AspectRatio = 4f/3f })" />

<!-- 自由比例 -->
<ImageCropper Url="photo.jpg" 
           Options="@(new ImageCropperOption { AspectRatio = 0 })" />
```

### 2. 处理裁剪结果

通过 `OnCropAsync` 回调处理裁剪后的图像数据。

```razor
<ImageCropper Url="@ImageUrl" 
           OnCropAsync="HandleCrop" />

<img src="@CroppedImage" />

@code {
    private string? ImageUrl { get; set; }
    private string? CroppedImage { get; set; }

    private async Task HandleCrop(ImageCropperResult result)
    {
        CroppedImage = result.Data;  // Base64 格式
        await UploadImageToServer(result.Data);
    }

    private async Task UploadImageToServer(string base64Data)
    {
        // 上传到服务器
        await Http.PostAsJsonAsync("api/upload", new { Image = base64Data });
    }
}
```

### 3. 禁用状态

通过 `IsDisabled` 参数禁用裁剪功能。

```razor
<ImageCropper Url="image.jpg" 
           IsDisabled="@(!CanEdit)" />

@code {
    private bool CanEdit { get; set; } = true;
}
```

### 4. 圆形头像裁剪

使用 `IsRound` 参数裁剪圆形头像。

```razor
<ImageCropper Url="avatar.jpg" 
           Options="@(new ImageCropperOption 
           { 
               AspectRatio = 1f, 
               IsRound = true,
               ViewMode = 1 
           })" 
           OnCropAsync="OnCropAsync" />

@code {
    private async Task OnCropAsync(ImageCropperResult result)
    {
        // 保存圆形头像
        await UserService.UpdateAvatar(result.Data);
    }
}
```

## 常见问题

### 1. 组件不显示

**问题**: 添加了 `ImageCropper` 组件但页面不显示。

**原因**: 可能是未正确安装 `BootstrapBlazor.ImageCropper` Nuget 包，或者 JS 资源未加载。

**解决方案**:
- 确认已安装 `BootstrapBlazor.ImageCropper` 包
- 检查 `_Host.cshtml` 或 `index.html` 中是否引入了相关 JS 文件
- 检查浏览器控制台是否有错误信息

### 2. 裁剪无反应

**问题**: 拖动裁剪框或调整大小无反应。

**原因**: 可能是 `ViewMode` 设置不当，或者组件被禁用。

**解决方案**:
- 检查 `IsDisabled` 是否为 `false`
- 尝试设置 `ViewMode = 0`（默认）
- 检查浏览器控制台是否有 JS 错误

```razor
<ImageCropper Url="image.jpg" 
           Options="@(new ImageCropperOption { ViewMode = 0 })" />
```

### 3. 裁剪结果数据格式

**问题**: `OnCropAsync` 回调中 `result.Data` 是什么格式？

**原因**: `Data` 属性是 Base64 格式的字符串。

**解决方案**: 使用 `result.Data` 获取 Base64 图像数据，或以 `result.Width`、`result.Height` 获取尺寸。

```razor
@code {
    private async Task OnCropAsync(ImageCropperResult result)
    {
        // Data: "data:image/png;base64,iVBORw0KGgo..."
        var base64Data = result.Data;
        var width = result.Width;
        var height = result.Height;
    }
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | ImageCropper 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 `IsRound` 参数；优化裁剪逻辑 |
| 8.0.0 | 2024-11-10 | 新增 `ViewMode` 参数；支持多种视图模式 |

## 参考链接

- [Bootstrap Blazor 官方文档 - ImageCropper](https://www.blazor.zone/image-cropper)
- [Bootstrap Blazor API - ImageCropper](https://www.blazor.zone/api/ImageCropper)
- [Cropper.js 官方文档](https://fengyuanchen.github.io/cropperjs/) (Cropper.js 库)
