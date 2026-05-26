# PdfReader PDF 文档阅读器

## 组件概述

PdfReader 组件用于在网页中直接嵌入和显示 PDF 文档，无需依赖用户本地安装的 PDF 阅读器。本组件依赖于 `BootstrapBlazor.PdfReader`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.PdfReader
```

或

```xml
<PackageReference Include="BootstrapBlazor.PdfReader" Version="10.0.26" />
```

**重要提示：**

PdfReader 组件图标依赖 `BootstrapBlazor.FontAwesome` 包，需要引用如下样式，否则工具栏图标无法显示：

```html
<link rel="stylesheet" href="@Assets["_content/BootstrapBlazor.FontAwesome/css/font-awesome.min.css"]" />
```

## 使用场景

### 1. 基础用法

通过 `Url` 参数设置 PDF 文件地址，或者使用 `OnGetStreamAsync` 参数指定用于渲染的文件流。

```razor
<PdfReader Url="https://example.com/document.pdf" />
```

**说明：**
- `Url` 参数设置 PDF 文档路径
- `OnGetStreamAsync` 参数通过流加载 PDF 文档
- 可以通过调用实例方法 `SetPdfStreamAsync` 或者 `SetPdfBase64DataAsync` 推流进行渲染
- 可以通过设置参数 `DownloadFileName` 值，用于设置下载文件名

### 2. 通过 URL 加载 PDF

直接通过 URL 地址加载 PDF 文档。

```razor
<PdfReader Url="https://example.com/report.pdf" 
           ShowToolbar="true" 
           ShowFileName="true" />
```

**说明：**
- `Url` 参数指向 PDF 文件的 HTTP/HTTPS 地址
- `ShowToolbar` 控制是否显示工具栏
- `ShowFileName` 控制是否显示文件名

### 3. 通过流加载 PDF

通过 `OnGetStreamAsync` 回调方法使用流加载 PDF 文档。

```razor
<PdfReader OnGetStreamAsync="OnGetPdfStream" 
           FileName="document.pdf" />
```

```csharp
@code {
    private async Task<Stream> OnGetPdfStream()
    {
        // 从数据库或文件系统读取 PDF 流
        var stream = await File.ReadAllBytesAsync("document.pdf");
        return new MemoryStream(stream);
    }
}
```

**说明：**
- `OnGetStreamAsync` 是 `Func<Task<Stream>>` 类型，返回 PDF 文件流
- 适用于从数据库、API 或其他非 URL 来源加载 PDF
- 可以配合 `FileName` 参数设置显示的文件名

### 4. 推流渲染 PDF

通过实例方法 `SetPdfStreamAsync` 或 `SetPdfBase64DataAsync` 动态推送 PDF 数据流。

```razor
<PdfReader @ref="pdfReaderRef" />
<Button OnClick="LoadPdf">加载 PDF</Button>

@code {
    private PdfReader pdfReaderRef;
    
    private async Task LoadPdf()
    {
        // 从数据库读取 PDF 字节数组
        var pdfBytes = await GetPdfFromDatabase();
        
        // 方式1: 使用流推送
        await pdfReaderRef.SetPdfStreamAsync(new MemoryStream(pdfBytes));
        
        // 方式2: 使用 Base64 字符串推送
        // await pdfReaderRef.SetPdfBase64DataAsync(Convert.ToBase64String(pdfBytes));
    }
    
    private async Task<byte[]> GetPdfFromDatabase()
    {
        // 模拟从数据库读取 PDF
        return await File.ReadAllBytesAsync("document.pdf");
    }
}
```

**说明：**
- `SetPdfStreamAsync` 方法接受 `Stream` 参数
- `SetPdfBase64DataAsync` 方法接受 Base64 编码的字符串参数
- 适用于动态加载、切换 PDF 文档的场景

### 5. 显示/隐藏工具栏

通过 `ShowToolbar` 参数控制是否显示工具栏。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           ShowToolbar="false" />
```

**说明：**
- `ShowToolbar` 参数类型为 `bool`，默认值为 `true`
- 设置为 `false` 时隐藏工具栏，节省显示空间
- 工具栏通常包含缩放、旋转、下载、打印等功能按钮

### 6. 显示/隐藏文件名

通过 `ShowFileName` 参数控制是否显示文件名。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           ShowFileName="false" />
```

**说明：**
- `ShowFileName` 参数类型为 `bool`，默认值为 `true`
- 设置为 `false` 时隐藏文件名显示区域

### 7. 显示/隐藏下载按钮

通过 `ShowDownload` 参数控制是否显示下载按钮。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           ShowDownload="true" 
           DownloadFileName="report.pdf" />
```

**说明：**
- `ShowDownload` 参数类型为 `bool`，默认值为 `true`
- `DownloadFileName` 参数设置下载文件名，默认值为 `null`
- 设置 `DownloadFileName` 可以自定义下载时的文件名

### 8. 显示/隐藏打印按钮

通过 `ShowPrint` 参数控制是否显示打印按钮。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           ShowPrint="true" />
```

**说明：**
- `ShowPrint` 参数类型为 `bool`，默认值为 `true`
- 设置为 `true` 时显示打印按钮，用户可以打印 PDF 文档

### 9. 启用缩略图

通过 `EnableThumbnails` 参数控制是否显示缩略图。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           EnableThumbnails="true" />
```

**说明：**
- `EnableThumbnails` 参数类型为 `bool`，默认值为 `true`
- 设置为 `true` 时显示页面缩略图，方便快速跳转
- 缩略图会占用一定的内存和加载时间

### 10. 双页单视图模式

通过 `ShowTwoPagesOneView` 参数控制是否显示双页单视图按钮。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           ShowTwoPagesOneView="true" />
```

**说明：**
- `ShowTwoPagesOneView` 参数类型为 `bool`，默认值为 `true`
- 设置为 `true` 时显示双页单视图按钮，用户可以切换到双页显示模式

### 11. 设置组件高度

通过 `ViewHeight` 参数设置 PDF 组件的高度。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           ViewHeight="800px" />
```

**说明：**
- `ViewHeight` 参数类型为 `string`，默认值为 `600px`
- 可以设置为像素值（如 `800px`）或百分比（如 `100%`）
- 根据页面布局合理设置高度，确保用户能够完整查看 PDF 内容

### 12. 页面回调方法

PdfReader 提供多个页面相关的回调方法。

```razor
<PdfReader Url="https://example.com/document.pdf" 
           OnPageChangedAsync="OnPageChanged" 
           OnPagesInitAsync="OnPagesInit" 
           OnPagesLoadedAsync="OnPagesLoaded" 
           OnRotationChanged="OnRotationChanged" 
           OnScaleChangedAsync="OnScaleChanged" 
           OnTwoPagesOneViewAsync="OnTwoPagesOneView" />
```

```csharp
@code {
    private Task OnPageChanged(uint pageNumber)
    {
        Console.WriteLine($"页码变化: {pageNumber}");
        return Task.CompletedTask;
    }
    
    private Task OnPagesInit(int totalPages)
    {
        Console.WriteLine($"页面初始化: 共 {totalPages} 页");
        return Task.CompletedTask;
    }
    
    private Task OnPagesLoaded(int loadedPages)
    {
        Console.WriteLine($"页面加载完毕: {loadedPages} 页");
        return Task.CompletedTask;
    }
    
    private Task OnRotationChanged(int rotation)
    {
        Console.WriteLine($"页面旋转: {rotation} 度");
        return Task.CompletedTask;
    }
    
    private Task OnScaleChanged(float scale)
    {
        Console.WriteLine($"缩放变化: {scale}");
        return Task.CompletedTask;
    }
    
    private Task OnTwoPagesOneView(bool isTwoPages)
    {
        Console.WriteLine($"双页模式: {isTwoPages}");
        return Task.CompletedTask;
    }
}
```

**回调方法说明：**
- `OnPageChangedAsync` - 页码变化时回调方法
- `OnPagesInitAsync` - 页面初始化回调方法
- `OnPagesLoadedAsync` - 页面加载完毕回调方法
- `OnRotationChanged` - 页面旋转回调方法
- `OnScaleChangedAsync` - 设置缩放倍率回调方法
- `OnTwoPagesOneViewAsync` - 设置双页单视图模式回调方法

### 13. 完整示例

包含 PDF 加载、工具栏控制、页面回调等完整功能。

```razor
<Card>
    <CardBody>
        <div class="row g-3">
            <div class="col-12">
                <div class="form-inline">
                    <Label>选择 PDF:</Label>
                    <Input SelectItems="@pdfItems" @bind-Value="selectedPdf" />
                </div>
            </div>
            <div class="col-12">
                <div class="form-inline">
                    <Switch @bind-Value="showToolbar">显示工具栏</Switch>
                    <Switch @bind-Value="showFileName">显示文件名</Switch>
                    <Switch @bind-Value="showDownload">显示下载</Switch>
                    <Switch @bind-Value="showPrint">显示打印</Switch>
                </div>
            </div>
        </div>
    </CardBody>
</Card>

<PdfReader Url="@selectedPdf" 
           ShowToolbar="@showToolbar" 
           ShowFileName="@showFileName" 
           ShowDownload="@showDownload" 
           ShowPrint="@showPrint" 
           EnableThumbnails="true" 
           ViewHeight="800px" 
           OnPageChangedAsync="OnPageChanged" 
           OnPagesLoadedAsync="OnPagesLoaded" />

@code {
    private string selectedPdf = "https://example.com/document1.pdf";
    private bool showToolbar = true;
    private bool showFileName = true;
    private bool showDownload = true;
    private bool showPrint = true;
    
    private List<SelectedItem> pdfItems = new List<SelectedItem>
    {
        new SelectedItem("https://example.com/document1.pdf", "文档1"),
        new SelectedItem("https://example.com/document2.pdf", "文档2"),
        new SelectedItem("https://example.com/document3.pdf", "文档3")
    };
    
    private Task OnPageChanged(uint pageNumber)
    {
        Console.WriteLine($"当前页码: {pageNumber}");
        return Task.CompletedTask;
    }
    
    private Task OnPagesLoaded(int loadedPages)
    {
        Console.WriteLine($"已加载页数: {loadedPages}");
        return Task.CompletedTask;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Url` | 获得/设置 PDF 文档路径 | `string` | - |
| `CurrentPage` | 获得/设置 当前页码 | `uint` | - |
| `CurrentRotation` | 获得/设置 当前旋转角度（0/90/180/270） | `int` | `0` |
| `DownloadFileName` | 获得/设置 下载文件名 | `string` | `null` |
| `EnableThumbnails` | 获得/设置 是否显示缩略图 | `bool` | `true` |
| `FitMode` | 获得/设置 是否适配当前页面宽度 | `PdfReaderFitMode` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `IsShow` | 获得/设置 是否显示组件 | `bool` | `true` |
| `MoreButtonIcon` | 获得/设置 更多按钮图标 | `string` | `null` |
| `OnGetStreamAsync` | 通过流加载 PDF 文档回调方法 | `Func<Task<Stream>>` | `null` |
| `OnPageChangedAsync` | 页码变化时回调方法 | `Func<uint, Task>` | - |
| `OnPagesInitAsync` | 页面初始化回调方法 | `Func<int, Task>` | - |
| `OnPagesLoadedAsync` | 页面加载完毕回调方法 | `Func<int, Task>` | - |
| `OnPrintingAsync` | 正在打印回调方法 | `Func<Task>` | `null` |
| `OnRotationChanged` | 页面旋转回调方法 | `Func<int, Task>` | - |
| `OnScaleChangedAsync` | 设置缩放倍率回调方法 | `Func<float, Task>` | - |
| `OnTwoPagesOneViewAsync` | 设置双页单视图模式回调方法 | `Func<bool, Task>` | - |
| `ShowDownload` | 获得/设置 是否显示下载按钮 | `bool` | `true` |
| `ShowFileName` | 获得/设置 是否显示文件名 | `bool` | `true` |
| `ShowPresentationMode` | 获得/设置 是否显示演示模式按钮 | `bool` | `true` |
| `ShowPrint` | 获得/设置 是否显示打印按钮 | `bool` | `true` |
| `ShowToolbar` | 获得/设置 是否显示工具栏 | `bool` | `true` |
| `ShowTwoPagesOneView` | 获得/设置 是否显示双页单视图按钮 | `bool` | `true` |
| `ViewHeight` | 获得/设置 PDF 组件高度 | `string` | `600px` |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## PdfReaderFitMode 枚举

| 值 | 说明 |
|-----|------|
| `None` | 不适配（默认） |
| `Width` | 适配页面宽度 |
| `Height` | 适配页面高度 |

## 实例方法

| 方法 | 说明 |
|------|------|
| `SetPdfStreamAsync(Stream stream)` | 通过流设置 PDF 文档 |
| `SetPdfBase64DataAsync(string base64Data)` | 通过 Base64 字符串设置 PDF 文档 |

## 最佳实践

1. **文件来源**：优先使用 `Url` 参数加载 PDF，对于需要权限验证的 PDF 使用 `OnGetStreamAsync` 流加载
2. **高度设置**：根据页面布局合理设置 `ViewHeight` 参数，建议使用固定像素值
3. **工具栏控制**：根据需求显示/隐藏工具栏按钮，提供简洁的用户体验
4. **缩略图**：对于大型 PDF 文档，考虑禁用缩略图以提高加载性能
5. **页面回调**：使用页面回调方法实现自定义逻辑，如统计、日志记录等

## 常见问题

**Q: PdfReader 和 PdfViewer 有什么区别？**
A: PdfReader 是在网页中直接嵌入和显示 PDF 文档的组件，功能更丰富；PdfViewer 是使用 Google Docs 或微软在线服务预览 PDF 的组件。

**Q: 为什么工具栏图标无法显示？**
A: 需要引用 `BootstrapBlazor.FontAwesome` 包的样式文件，在 `_Host.cshtml` 或 `Index.html` 中添加：`<link rel="stylesheet" href="@Assets["_content/BootstrapBlazor.FontAwesome/css/font-awesome.min.css"]" />`

**Q: 如何动态切换 PDF 文档？**
A: 使用实例方法 `SetPdfStreamAsync` 或 `SetPdfBase64DataAsync` 动态推送 PDF 数据流。

**Q: 如何自定义下载文件名？**
A: 使用 `DownloadFileName` 参数设置下载时的文件名。

**Q: 如何获取当前页码？**
A: 使用 `CurrentPage` 参数获取或设置当前页码，或通过 `OnPageChangedAsync` 回调监听页码变化。

## 版本历史

- **10.0.26**: 初始版本，支持 URL 加载、流加载、工具栏控制、页面回调、缩略图、打印、下载等功能
