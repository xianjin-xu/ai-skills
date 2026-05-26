# JitViewer 文件预览器

## 组件概述

JitViewer 是一个通用文件预览组件，可用于在页面中直接浏览多种类型文件。本组件依赖于 `BootstrapBlazor.JitViewer`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.JitViewer
```

或

```xml
<PackageReference Include="BootstrapBlazor.JitViewer" Version="10.0.0" />
```

## 使用场景

### 1. 基础用法

支持在线预览 Office 文档、PDF、OFD、图片、文本、代码、视频等多种文件格式。

```razor
<JitViewer File="https://example.com/document.docx" />
```

**说明：**
- `File` 参数指向要预览的文件 URL 地址
- 组件会自动根据文件类型选择合适的预览方式
- 支持多种文件格式，包括 Office 文档、PDF、图片、文本等

### 2. 预览 Office 文档

预览 Word、Excel、PowerPoint 等 Office 文档。

```razor
<JitViewer File="https://example.com/report.docx" FileName="年度报告.docx" />
```

**支持的 Office 文档格式：**
- Word: `.docx`, `.doc`
- Excel: `.xlsx`, `.xls`
- PowerPoint: `.pptx`, `.ppt`
- Visio: `.vsdx`, `.vsd`

### 3. 预览 PDF 文档

预览 PDF 格式文档。

```razor
<JitViewer File="https://example.com/document.pdf" FileName="用户手册.pdf" />
```

**说明：**
- 支持 PDF 文件的在线预览
- 可以显示 PDF 的页面缩略图、大纲等
- 支持搜索、缩放、旋转等操作

### 4. 预览图片文件

预览 JPG、PNG、GIF 等图片格式。

```razor
<JitViewer File="https://example.com/photo.jpg" FileName="产品图片.jpg" />
```

**支持的图片格式：**
- JPG/JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- SVG (.svg)
- WebP (.webp)

### 5. 预览文本和代码文件

预览 TXT、CSV、JSON、XML、HTML 等文本和代码文件。

```razor
<JitViewer File="https://example.com/data.json" FileName="配置数据.json" />
```

**支持的文本/代码格式：**
- 纯文本: `.txt`, `.log`
- 数据格式: `.json`, `.xml`, `.yaml`, `.csv`
- 代码文件: `.cs`, `.js`, `.html`, `.css`, `.py`, `.java`
- Markdown: `.md`

### 6. 预览 OFD 文档

预览 OFD (Open Fixed Document) 格式文档，这是中国国家标准版式文档格式。

```razor
<JitViewer File="https://example.com/document.ofd" FileName="电子发票.ofd" />
```

**说明：**
- OFD 是中国自主制定的版式文档格式标准
- 常用于电子发票、电子合同等场景
- JitViewer 提供完整的 OFD 预览功能

### 7. 自定义组件高度

通过 `Height` 参数设置组件的高度。

```razor
<JitViewer File="https://example.com/document.pdf" Height="800" />
```

```razor
<JitViewer File="https://example.com/document.pdf" Height="1000" />
```

**说明：**
- `Height` 参数类型为 `Nullable<int>`，单位为像素
- 默认值为 `null`，此时使用组件默认高度
- 建议根据页面布局设置合适的高度

### 8. 显示/隐藏工具栏

通过 `ShowToolbar` 参数控制是否显示工具栏。

```razor
<JitViewer File="https://example.com/document.pdf" ShowToolbar="false" />
```

**说明：**
- `ShowToolbar` 参数类型为 `bool`，默认值为 `true`
- 设置为 `false` 时隐藏工具栏，节省显示空间
- 工具栏通常包含缩放、旋转、下载等功能按钮

### 9. 设置主题

通过 `Theme` 参数设置组件的主题模式。

```razor
<JitViewer File="https://example.com/document.pdf" Theme="dark" />
```

**可用的主题值：**
- `light` - 浅色主题
- `dark` - 深色主题
- `auto` - 自动主题（默认），根据系统主题自动切换

### 10. 完整示例

包含文件预览、工具栏控制、主题切换等完整功能。

```razor
< div class="row g-3">
    <div class="col-12">
        <div class="form-inline">
            <Label>选择文件:</Label>
            <Input SelectItems="@fileItems" @bind-Value="selectedFile" />
        </div>
    </div>
    <div class="col-12">
        <div class="form-inline">
            <Label>主题:</Label>
            <RadioList Items="@themeItems" @bind-Value="selectedTheme" />
        </div>
    </div>
    <div class="col-12">
        <Switch @bind-Value="showToolbar">显示工具栏</Switch>
    </div>
</div>

<JitViewer File="@selectedFile" 
           FileName="@GetFileName(selectedFile)" 
           Height="800" 
           ShowToolbar="@showToolbar" 
           Theme="@selectedTheme" />

@code {
    private string selectedFile = "https://example.com/document.docx";
    private string selectedTheme = "auto";
    private bool showToolbar = true;
    
    private List<SelectedItem> fileItems = new List<SelectedItem>
    {
        new SelectedItem("https://example.com/document.docx", "Word 文档"),
        new SelectedItem("https://example.com/report.xlsx", "Excel 表格"),
        new SelectedItem("https://example.com/presentation.pptx", "PowerPoint 演示"),
        new SelectedItem("https://example.com/document.pdf", "PDF 文档"),
        new SelectedItem("https://example.com/photo.jpg", "图片文件")
    };
    
    private List<SelectedItem> themeItems = new List<SelectedItem>
    {
        new SelectedItem("light", "浅色"),
        new SelectedItem("dark", "深色"),
        new SelectedItem("auto", "自动")
    };
    
    private string GetFileName(string fileUrl)
    {
        return Path.GetFileName(fileUrl);
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `File` | 预览文件路径 | `string` | - |
| `FileName` | 预览文件显示名称 | `string` | - |
| `Height` | 组件高度（像素） | `Nullable<int>` | `null` |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `ShowToolbar` | 组件是否显示工具栏 | `bool` | `true` |
| `Theme` | 组件主题 | `string` | `auto` |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 支持的文件类型

### Office 文档
- Word: `.docx`, `.doc`
- Excel: `.xlsx`, `.xls`
- PowerPoint: `.pptx`, `.ppt`
- Visio: `.vsdx`, `.vsd`

### PDF 和 OFD
- PDF: `.pdf`
- OFD: `.ofd`

### 图片文件
- JPG/JPEG: `.jpg`, `.jpeg`
- PNG: `.png`
- GIF: `.gif`
- BMP: `.bmp`
- SVG: `.svg`
- WebP: `.webp`

### 文本和代码
- 纯文本: `.txt`, `.log`
- 数据格式: `.json`, `.xml`, `.yaml`, `.csv`
- 代码文件: `.cs`, `.js`, `.html`, `.css`, `.py`, `.java`
- Markdown: `.md`

### 视频文件
- MP4: `.mp4`
- WebM: `.webm`
- OGG: `.ogv`

## 最佳实践

1. **文件地址**：确保 `File` 参数指向的文件地址是可公开访问的，JitViewer 需要能够访问该地址
2. **文件大小**：建议预览的文件大小不要超过 50MB，过大的文件可能导致加载缓慢
3. **文件名称**：使用 `FileName` 参数提供友好的文件名称，改善用户体验
4. **高度设置**：根据页面布局合理设置 `Height` 参数，确保用户能够完整查看文件内容
5. **主题选择**：根据网站主题选择合适的 `Theme` 值，保持视觉一致性

## 常见问题

**Q: JitViewer 支持本地文件预览吗？**
A: 不支持。JitViewer 组件需要访问文件 URL，因此文件必须可以通过公网访问。`File` 参数必须是一个可公开访问的 HTTP/HTTPS 地址。

**Q: 为什么我的文件无法预览？**
A: 可能的原因包括：
1. 文件地址不可访问（需要公网可访问）
2. 文件格式不支持
3. 文件大小超过限制
4. 网络连接问题

**Q: 如何设置 JitViewer 的高度？**
A: 使用 `Height` 参数设置，单位为像素，如 `Height="800"` 表示 800 像素高度。

**Q: 如何隐藏工具栏？**
A: 设置 `ShowToolbar="false"` 可以隐藏工具栏。

**Q: JitViewer 支持哪些主题？**
A: 支持 `light`（浅色）、`dark`（深色）、`auto`（自动）三种主题模式。

**Q: JitViewer 和 OfficeViewer 有什么区别？**
A: OfficeViewer 只支持 Office 文档预览，而 JitViewer 是通用文件预览器，支持更多文件类型包括 PDF、OFD、图片、文本、代码等。

## 版本历史

- **10.0.0**: 初始版本，支持 Office 文档、PDF、OFD、图片、文本、代码等多种文件格式预览，支持工具栏控制、主题切换功能
