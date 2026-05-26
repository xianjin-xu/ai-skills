# OfficeViewer Office 文档预览组件

## 组件概述

OfficeViewer 组件通过使用微软在线文档预览功能预览 Office 文档内容。本组件依赖于 `BootstrapBlazor.OfficeViewer`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.OfficeViewer
```

或

```xml
<PackageReference Include="BootstrapBlazor.OfficeViewer" Version="10.0.0" />
```

## 使用场景

### 1. 基本用法

通过设置 `Url` 值设置预览文档地址。

```razor
<OfficeViewer Url="https://example.com/document.docx" />
```

**说明：**
- `Url` 参数指向 Office 文档的 URL 地址
- 组件会使用微软在线预览服务来显示文档内容
- 支持的文档类型：Word (.docx, .doc)、Excel (.xlsx, .xls)、PowerPoint (.pptx, .ppt)、PDF (.pdf)

### 2. 设置文档加载完成回调

通过 `OnLoaded` 参数设置文档加载完成的事件回调。

```razor
<OfficeViewer Url="@documentUrl" OnLoaded="OnDocumentLoaded" />

@code {
    private string documentUrl = "https://example.com/report.docx";
    
    private async Task OnDocumentLoaded()
    {
        // 文档加载完成后的处理逻辑
        Console.WriteLine("文档加载完成");
        await Task.CompletedTask;
    }
}
```

### 3. 设置查看器高度

通过 `Height` 参数设置 Office 文档查看器的高度。

```razor
<OfficeViewer Url="@documentUrl" Height="800px" />
```

```razor
<OfficeViewer Url="@documentUrl" Height="100vh" />
```

**说明：**
- `Height` 参数支持任何有效的 CSS 高度值
- 默认值为 `null`，此时使用组件默认高度
- 建议使用固定像素值或视口高度（vh）以确保显示效果

### 4. 动态切换文档

通过动态修改 `Url` 参数实现文档切换。

```razor
<OfficeViewer Url="@currentDocumentUrl" OnLoaded="OnDocumentLoaded" />

<Button OnClick="SwitchToDocument1">查看文档1</Button>
<Button OnClick="SwitchToDocument2">查看文档2</Button>

@code {
    private string currentDocumentUrl = "https://example.com/document1.docx";
    
    private Task SwitchToDocument1()
    {
        currentDocumentUrl = "https://example.com/document1.docx";
        return Task.CompletedTask;
    }
    
    private Task SwitchToDocument2()
    {
        currentDocumentUrl = "https://example.com/document2.docx";
        return Task.CompletedTask;
    }
    
    private async Task OnDocumentLoaded()
    {
        Console.WriteLine("文档加载完成");
        await Task.CompletedTask;
    }
}
```

### 5. 完整示例

包含文档预览、加载状态提示、错误处理等完整功能。

```razor
@if (isLoading)
{
    <div class="text-center">
        <Spinner />
        <p>正在加载文档...</p>
    </div>
}

<OfficeViewer Url="@documentUrl" 
             Height="600px" 
             OnLoaded="OnDocumentLoaded"
             @ref="officeViewerRef" />

@code {
    private string documentUrl = "https://example.com/report.docx";
    private OfficeViewer officeViewerRef;
    private bool isLoading = true;
    
    private async Task OnDocumentLoaded()
    {
        isLoading = false;
        Console.WriteLine("文档加载完成");
        await Task.CompletedTask;
    }
    
    private async Task ReloadDocument()
    {
        isLoading = true;
        // 重新加载文档
        await officeViewerRef.Reload();
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Url` | 获取/设置 要显示的 Office 文件的 url | `string` | - |
| `Height` | 获取/设置 查看器高度 | `string` | `null` |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `OnLoaded` | 获取/设置 文档加载完成的事件回调 | `Func<Task>` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 支持的文档类型

OfficeViewer 组件支持以下文档类型的在线预览：

**Word 文档：**
- `.docx` - Word 文档（推荐）
- `.doc` - Word 97-2003 文档

**Excel 文档：**
- `.xlsx` - Excel 工作簿（推荐）
- `.xls` - Excel 97-2003 工作簿

**PowerPoint 文档：**
- `.pptx` - PowerPoint 演示文稿（推荐）
- `.ppt` - PowerPoint 97-2003 演示文稿

**PDF 文档：**
- `.pdf` - PDF 文档

## 最佳实践

1. **文档地址**：确保 `Url` 指向的文档地址是可公开访问的，微软在线预览服务需要能够访问该地址
2. **文档大小**：建议预览的文档大小不要超过 10MB，过大的文档可能导致加载缓慢
3. **高度设置**：根据页面布局合理设置 `Height` 参数，确保用户能够完整查看文档内容
4. **加载回调**：使用 `OnLoaded` 回调处理文档加载完成后的逻辑，如隐藏加载提示
5. **错误处理**：考虑添加错误处理机制，处理文档加载失败的情况

## 常见问题

**Q: OfficeViewer 组件支持本地文件预览吗？**
A: 不支持。OfficeViewer 组件需要使用微软在线预览服务，因此文档必须可以通过公网访问。`Url` 参数必须是一个可公开访问的 HTTP/HTTPS 地址。

**Q: 为什么我的文档无法预览？**
A: 可能的原因包括：
1. 文档地址不可访问（需要公网可访问）
2. 文档格式不支持
3. 文档大小超过限制
4. 网络连接问题

**Q: 如何设置 OfficeViewer 的高度？**
A: 使用 `Height` 参数设置，支持任何有效的 CSS 高度值，如 `"600px"`、`"100vh"`、`"50%"` 等。

**Q: 文档加载完成后如何执行自定义逻辑？**
A: 使用 `OnLoaded` 参数设置回调方法，当文档加载完成时会自动调用该方法。

**Q: OfficeViewer 组件支持哪些浏览器？**
A: OfficeViewer 组件基于微软在线预览服务，支持所有现代浏览器，包括 Chrome、Firefox、Safari、Edge 等。

## 版本历史

- **10.0.0**: 初始版本，支持 Office 文档在线预览、加载回调、高度设置功能
