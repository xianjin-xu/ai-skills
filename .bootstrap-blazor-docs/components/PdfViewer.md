# PdfViewer PDF 阅读器

## 组件概述

PdfViewer 组件用于在组件中打开 Pdf 文件阅读其内容。本组件依赖于 `BootstrapBlazor.PdfViewer`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.PdfViewer
```

或

```xml
<PackageReference Include="BootstrapBlazor.PdfViewer" Version="10.0.1" />
```

## 使用场景

### 1. 基础用法

通过设置 `Url` 参数加载 Pdf 文件，设置 `UseGoogleDocs` 使用 `docs.google.com` 预览。

```razor
<PdfViewer Url="https://example.com/document.pdf" />
```

**说明：**
- `Url` 参数设置文档 Url 地址
- `UseGoogleDocs` 参数设置是否使用 Google Docs 渲染 PDF
- 默认情况下，组件会使用微软在线预览服务
- 设置 `UseGoogleDocs="true"` 时，使用 Google Docs 预览服务

### 2. 使用 Google Docs 预览

通过设置 `UseGoogleDocs="true"` 使用 Google Docs 服务预览 PDF。

```razor
<PdfViewer Url="https://example.com/document.pdf" UseGoogleDocs="true" />
```

**说明：**
- `UseGoogleDocs` 参数类型为 `bool`，默认值为 `false`
- 设置为 `true` 时，使用 Google Docs 在线预览服务
- 需要网络连接访问 Google Docs 服务器
- 适用于需要 Google Docs 功能的场景

### 3. 设置页码索引

通过 `PageIndex` 参数设置初始页码。

```razor
<PdfViewer Url="https://example.com/document.pdf" PageIndex="3" />
```

**说明：**
- `PageIndex` 参数类型为 `int`，默认值为 `0`
- 设置初始打开时显示的页码（从 0 开始）
- 适用于需要直接跳转到特定页面的场景

### 4. 显示/隐藏工具栏

通过 `ShowToolbar` 参数控制是否显示工具栏与缩略图侧边栏。

```razor
<PdfViewer Url="https://example.com/document.pdf" ShowToolbar="false" />
```

**说明：**
- `ShowToolbar` 参数类型为 `bool`，默认值为 `true`
- 设置为 `false` 时隐藏工具栏和缩略图侧边栏
- 适用于需要简洁显示或嵌入到其他界面的场景

### 5. 设置查看器高度

通过 `Height` 参数设置查看器的高度。

```razor
<PdfViewer Url="https://example.com/document.pdf" Height="800px" />
```

**说明：**
- `Height` 参数类型为 `string`，默认值为 `null`
- 可以设置为像素值（如 `800px`）或百分比（如 `100%`）
- 根据页面布局合理设置高度，确保用户能够完整查看 PDF 内容

### 6. 文档加载完成回调

通过 `OnLoaded` 参数设置文档加载完成的回调事件。

```razor
<PdfViewer Url="https://example.com/document.pdf" OnLoaded="OnDocumentLoaded" />
```

```csharp
@code {
    private Task OnDocumentLoaded()
    {
        Console.WriteLine("PDF 文档加载完成");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `OnLoaded` 参数类型为 `Func<Task>`
- 文档加载完成后自动调用此回调方法
- 可以在此回调中执行后续操作，如隐藏加载提示等

### 7. 文档不支持回调

通过 `NotSupportCallback` 参数设置文档不支持的回调事件。

```razor
<PdfViewer Url="https://example.com/document.pdf" NotSupportCallback="OnNotSupport" />
```

```csharp
@code {
    private Task OnNotSupport()
    {
        Console.WriteLine("PDF 文档不支持预览");
        // 可以在这里处理不支持的情况，如显示提示信息
        return Task.CompletedTask;
    }
}
```

**说明：**
- `NotSupportCallback` 参数类型为 `Func<Task>`
- 当文档格式不支持或预览服务不可用时触发
- 可以在此回调中处理错误情况，如显示错误信息、提供替代方案等

### 8. 完整示例

包含 PDF 预览、工具栏控制、加载回调等完整功能。

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
                    <Switch @bind-Value="useGoogleDocs">使用 Google Docs</Switch>
                    <Switch @bind-Value="showToolbar">显示工具栏</Switch>
                </div>
            </div>
            <div class="col-12">
                @if (isLoading)
                {
                    <Spinner />
                    <span>正在加载 PDF 文档...</span>
                }
                @if (notSupported)
                {
                    <Alert Color="Color.Warning">
                        <Icon Name="fa fa-exclamation-triangle" />
                        当前文档不支持预览，请下载后查看。
                        <Button Size="Size.Small" OnClick="DownloadPdf">下载 PDF</Button>
                    </Alert>
                }
            </div>
        </div>
    </CardBody>
</Card>

<PdfViewer Url="@selectedPdf" 
           UseGoogleDocs="@useGoogleDocs" 
           ShowToolbar="@showToolbar" 
           Height="800px" 
           PageIndex="@pageIndex" 
           OnLoaded="OnLoaded" 
           NotSupportCallback="OnNotSupport" />

@code {
    private string selectedPdf = "https://example.com/document1.pdf";
    private bool useGoogleDocs = false;
    private bool showToolbar = true;
    private int pageIndex = 0;
    private bool isLoading = true;
    private bool notSupported = false;
    
    private List<SelectedItem> pdfItems = new List<SelectedItem>
    {
        new SelectedItem("https://example.com/document1.pdf", "文档1"),
        new SelectedItem("https://example.com/document2.pdf", "文档2"),
        new SelectedItem("https://example.com/document3.pdf", "文档3")
    };
    
    private Task OnLoaded()
    {
        isLoading = false;
        notSupported = false;
        Console.WriteLine("PDF 文档加载完成");
        return Task.CompletedTask;
    }
    
    private Task OnNotSupport()
    {
        isLoading = false;
        notSupported = true;
        Console.WriteLine("PDF 文档不支持预览");
        return Task.CompletedTask;
    }
    
    private Task DownloadPdf()
    {
        // 实现 PDF 下载逻辑
        Console.WriteLine("下载 PDF 文档");
        return Task.CompletedTask;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Url` | 获得/设置 文档 Url 属性 | `string` | - |
| `UseGoogleDocs` | 获得/设置 是否使用 Google Docs 渲染 PDF | `bool` | `false` |
| `PageIndex` | 获得/设置 页码索引 | `int` | `0` |
| `ShowToolbar` | 获得/设置 是否显示工具栏与缩略图侧边栏 | `bool` | `true` |
| `Height` | 获得/设置 查看器高度 | `string` | `null` |
| `OnLoaded` | 获得/设置 文档加载完成回调事件 | `Func<Task>` | - |
| `NotSupportCallback` | 获得/设置 文档不支持回调事件 | `Func<Task>` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 最佳实践

1. **预览服务选择**：根据网络环境和用户群体选择预览服务，国内用户建议使用默认（微软服务），国外用户可使用 Google Docs
2. **高度设置**：根据页面布局合理设置 `Height` 参数，建议使用固定像素值
3. **错误处理**：使用 `NotSupportCallback` 处理不支持的情况，提供友好的错误提示
4. **加载状态**：使用 `OnLoaded` 回调管理加载状态，提供更好的用户体验
5. **工具栏控制**：根据需求显示/隐藏工具栏，提供简洁的用户体验

## 常见问题

**Q: PdfViewer 和 PdfReader 有什么区别？**
A: PdfViewer 是使用 Google Docs 或微软在线服务预览 PDF 的组件，依赖于外部服务；PdfReader 是在网页中直接嵌入和显示 PDF 文档的组件，功能更丰富且不依赖外部服务。

**Q: 为什么 PDF 文档无法预览？**
A: 可能的原因包括：
1. 文档地址不可访问（需要公网可访问）
2. 文档格式不支持
3. 预览服务不可用（Google Docs 或微软服务无法访问）
4. 网络连接问题

**Q: 如何选择合适的预览服务？**
A: 国内用户建议使用默认设置（微软服务），国外用户可使用 `UseGoogleDocs="true"` 切换到 Google Docs 服务。

**Q: 如何自定义查看器高度？**
A: 使用 `Height` 参数设置，如 `Height="800px"` 或 `Height="100%"`。

**Q: 如何处理文档不支持的情况？**
A: 使用 `NotSupportCallback` 回调方法处理，可以在此方法中显示错误提示或提供替代方案（如下载链接）。

**Q: PdfViewer 支持本地文件预览吗？**
A: 不支持。PdfViewer 组件需要访问文档 URL，因此文档必须可以通过公网访问。`Url` 参数必须是一个可公开访问的 HTTP/HTTPS 地址。

## 版本历史

- **10.0.1**: 初始版本，支持 Google Docs 和微软服务预览、页码设置、工具栏控制、加载回调、不支持回调等功能
