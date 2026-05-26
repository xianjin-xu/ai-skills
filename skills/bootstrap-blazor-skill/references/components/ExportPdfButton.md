# ExportPdfButton (导出 Pdf 按钮)

## 概述

`ExportPdfButton` 组件用于**将指定网页内容转成 Pdf，将 Html 片段或者网页元素导出为 Pdf**。组件支持通过元素 Id 或选择器导出 PDF，并提供了丰富的回调事件。

**主要特性**：
- 支持通过 `ElementId` 导出指定元素 Id
- 支持通过 `Selector` 指定元素选择器导出 Pdf
- 支持自动下载 Pdf（`AutoDownload`）
- 支持自定义 Pdf 文件名（`FileName`）
- 支持导出前回调（`OnBeforeExport`）
- 支持下载前回调（`OnBeforeDownload`）
- 支持下载后回调（`OnAfterDownload`）
- 支持自定义按钮样式（颜色、大小、图标等）
- 支持异步按钮模式（`IsAsync`）

**依赖说明**：本组件依赖于 `BootstrapBlazor.Html2Pdf`，使用本组件时需要引用其组件包。

**在线演示**: https://www.blazor.zone/export-pdf-button

---

## 安装 Nuget 包

使用 nuget.org 进行 `BootstrapBlazor.Html2Pdf` 组件的安装：

### .NET CLI

```bash
dotnet add package BootstrapBlazor.Html2Pdf
```

### PackageReference

```xml
<PackageReference Include="BootstrapBlazor.Html2Pdf" Version="10.0.6" />
```

### Package Manager

```powershell
Install-Package BootstrapBlazor.Html2Pdf
```

**IHtml2Pdf 服务接口请参阅**: [传送门]

---

## 使用场景

### 1. 基础用法（导出指定元素 Id）

通过 `ElementId` 参数导出指定元素 Id 的内容为 Pdf。

```razor
<!-- 导出指定元素 Id -->
<div id="export-content">
    <table class="table">
        <thead>
            <tr>
                <th>日期</th>
                <th>姓名</th>
                <th>地址</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>2026/5/26 03:37:53</td>
                <td>张三 0001</td>
                <td>上海市普陀区金沙江路 1898 弄</td>
            </tr>
            <tr>
                <td>2026/5/27 03:37:53</td>
                <td>张三 0002</td>
                <td>上海市普陀区金沙江路 1901 弄</td>
            </tr>
            <tr>
                <td>2026/5/28 03:37:53</td>
                <td>张三 0003</td>
                <td>上海市普陀区金沙江路 1159 弄</td>
            </tr>
        </tbody>
    </table>
</div>

<ExportPdfButton ElementId="export-content" Text="导出 Pdf" />

@code {
    // 组件会自动将 id 为 "export-content" 的元素内容导出为 Pdf
}
```

---

### 2. 通过选择器导出（Selector）

通过 `Selector` 参数指定元素选择器导出 Pdf。

```razor
<!-- 通过选择器导出 -->
<EditForm Model="Model">
    <div class="form-group">
        <label>Name</label>
        <InputText @bind-Value="Model.Name" class="form-control" />
    </div>
    <div class="form-group">
        <label>Address</label>
        <InputText @bind-Value="Model.Address" class="form-control" />
    </div>
    <div class="form-group">
        <label>DateTime</label>
        <InputDate @bind-Value="Model.DateTime" class="form-control" />
    </div>
    <div class="form-group">
        <label>Education</label>
        <InputSelect @bind-Value="Model.Education" class="form-control">
            <option value="小学">小学</option>
            <option value="中学">中学</option>
            <option value="大学">大学</option>
        </InputSelect>
    </div>
</EditForm>

<ExportPdfButton Selector=".form-group" Text="导出表单" />

@code {
    private FormModel Model { get; set; } = new FormModel();
    
    public class FormModel
    {
        public string Name { get; set; } = "张三 1000";
        public string Address { get; set; } = "上海市普陀区金沙江路 1391 弄";
        public DateTime DateTime { get; set; } = new DateTime(2026, 5, 26, 3, 37, 53);
        public string Education { get; set; } = "中学";
    }
}
```

---

### 3. 自定义 Pdf 文件名（FileName）

通过 `FileName` 参数设置导出 Pdf 文件名。

```razor
<!-- 自定义文件名 -->
<div id="content">
    <h1>测试内容</h1>
    <p>这是要导出的内容</p>
</div>

<ExportPdfButton ElementId="content" FileName="我的文档.pdf" Text="导出 Pdf" />
```

**说明**：如果不设置 `FileName`，默认使用 `pdf-时间戳.pdf` 作为文件名。

---

### 4. 自动下载控制（AutoDownload）

通过 `AutoDownload` 参数控制是否自动下载 Pdf，默认为 `true`。

```razor
<!-- 不自动下载，手动处理 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    AutoDownload="false" 
    OnBeforeDownload="OnBeforeDownload" 
    Text="导出 Pdf" />

@code {
    private async Task OnBeforeDownload(Stream stream)
    {
        // 手动处理 Pdf 流
        // 例如：保存到服务器或显示预览
        using var fileStream = File.Create("output.pdf");
        await stream.CopyToAsync(fileStream);
    }
}
```

---

### 5. 导出前回调（OnBeforeExport）

通过 `OnBeforeExport` 参数设置导出 Pdf 之前回调委托。

```razor
<!-- 导出前回调 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    OnBeforeExport="OnBeforeExport" 
    Text="导出 Pdf" />

@code {
    private async Task OnBeforeExport()
    {
        // 导出前的处理
        // 例如：显示加载提示、准备数据等
        await Task.Delay(500); // 模拟异步操作
    }
}
```

---

### 6. 下载前回调（OnBeforeDownload）

通过 `OnBeforeDownload` 参数设置下载 Pdf 之前回调委托。

```razor
<!-- 下载前回调 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    OnBeforeDownload="OnBeforeDownload" 
    Text="导出 Pdf" />

@code {
    private async Task OnBeforeDownload(Stream stream)
    {
        // 下载前的处理
        // stream 是生成的 Pdf 流
        // 可以在这里对 Pdf 进行二次处理
        using var memoryStream = new MemoryStream();
        await stream.CopyToAsync(memoryStream);
        
        // 例如：添加水印、加密等
        var pdfBytes = memoryStream.ToArray();
        // 处理 pdfBytes...
    }
}
```

---

### 7. 下载后回调（OnAfterDownload）

通过 `OnAfterDownload` 参数设置下载 Pdf 之后回调委托。

```razor
<!-- 下载后回调 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    OnAfterDownload="OnAfterDownload" 
    Text="导出 Pdf" />

@code {
    private async Task OnAfterDownload(string fileName)
    {
        // 下载后的处理
        // fileName 是下载的文件名
        Console.WriteLine($"文件 {fileName} 下载完成");
        await Task.CompletedTask;
    }
}
```

---

### 8. 自定义按钮样式

通过 `Color`、`Size`、`Icon` 等参数自定义按钮样式。

```razor
<!-- 自定义按钮样式 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    Color="Color.Primary" 
    Size="Size.Medium" 
    Icon="fa fa-file-pdf" 
    Text="导出 PDF" />
```

---

### 9. 异步按钮模式（IsAsync）

通过 `IsAsync` 参数设置是否为异步按钮，点击按钮后禁用自身并且等待异步完成，过程中显示 loading 动画。

```razor
<!-- 异步按钮 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    IsAsync="true" 
    Text="导出中..." 
    LoadingIcon="fa fa-spinner fa-spin" />
```

---

### 10. 添加脚本和样式文件（ScriptTags/StyleTags）

通过 `ScriptTags` 和 `StyleTags` 参数设置导出 Pdf 所需脚本文件集合和样式表文件集合。

```razor
<!-- 添加脚本和样式 -->
<div id="content">
    <h1>测试内容</h1>
</div>

<ExportPdfButton 
    ElementId="content" 
    ScriptTags="CustomScripts" 
    StyleTags="CustomStyles" 
    Text="导出 Pdf" />

@code {
    private List<string> CustomScripts { get; set; } = new List<string>
    {
        "https://cdn.example.com/script1.js",
        "https://cdn.example.com/script2.js"
    };
    
    private List<string> CustomStyles { get; set; } = new List<string>
    {
        "https://cdn.example.com/style1.css",
        "https://cdn.example.com/style2.css"
    };
}
```

---

## 参数 (Parameters)

### ExportPdfButton 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `AutoDownload` | `bool` | `true` | 获得/设置 是否自动下载 Pdf 默认为 true |
| `ButtonStyle` | `ButtonStyle` | `ButtonStyle.None` | 获得/设置 按钮风格枚举 |
| `ButtonType` | `ButtonType` | `ButtonType.Button` | 获得/设置 按钮类型 Submit 为表单提交按钮 Reset 为表单重置按钮 默认为 Button |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 RenderFragment 实例 |
| `Color` | `Color` | `Color.None` | 获得/设置 按钮颜色 默认 |
| `ElementId` | `string?` | `null` | 获得/设置 导出 Pdf 元素 Id 默认为 null |
| `FileName` | `string?` | `null` | 获得/设置 导出 Pdf 文件名 默认为 null 未设置时使用 pdf-时间戳.pdf |
| `Icon` | `string?` | `null` | 获得/设置 显示图标 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsAsync` | `bool` | `false` | 获得/设置 是否为异步按钮，默认为 false 如果为 true 表示是异步按钮，点击按钮后禁用自身并且等待异步完成，过程中显示 loading 动画 |
| `IsAutoFocus` | `bool` | `false` | 获得/设置 是否自动获取焦点，默认为 false |
| `IsBlock` | `bool` | `false` | 获得/设置 Block 模式 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 默认为 false |
| `IsKeepDisabled` | `bool` | `false` | 获得/设置 是否异步结束后是否保持禁用状态，默认为 false |
| `IsOutline` | `bool` | `false` | 获得/设置 Outline 样式 默认 false |
| `LoadingIcon` | `string?` | `fa-solid fa-spin fa-spinner` | 获得/设置 正在加载动画图标 默认为 fa-solid fa-spin fa-spinner |
| `OnAfterDownload` | `Func<string, Task>?` | `null` | 获得/设置 下载 Pdf 之后回调委托 默认为 null |
| `OnBeforeDownload` | `Func<Stream, Task>?` | `null` | 获得/设置 下载 Pdf 之前回调委托 默认为 null |
| `OnBeforeExport` | `Func<Task>?` | `null` | 获得/设置 导出 Pdf 之前回调委托 默认为 null |
| `OnClick` | `EventCallback<MouseEventArgs>` | - | 获得/设置 OnClick 事件 |
| `OnClickWithoutRender` | `Func<Task>?` | `null` | 获得/设置 OnClick 事件不刷新父组件 |
| `ScriptTags` | `List<string>?` | `null` | 获得/设置 导出 Pdf 所需脚本文件集合 默认为 null |
| `Selector` | `string?` | `null` | 获得/设置 导出 Pdf 选择器 默认为 null |
| `Size` | `Size` | `Size.None` | 获得/设置 Size 大小 |
| `StopPropagation` | `bool` | `false` | 获得/设置 点击事件是否向上传播 默认 false |
| `StyleTags` | `List<string>?` | `null` | 获得/设置 导出 Pdf 所需样式表文件集合 默认为 null |
| `Text` | `string?` | `null` | 获得/设置 显示文字 |
| `TooltipPlacement` | `Placement` | `Placement.Top` | 获得/设置 Tooltip 显示位置，默认为 Top |
| `TooltipText` | `string?` | `null` | 获得/设置 Tooltip 显示文字，默认为 null |
| `TooltipTrigger` | `string?` | `hover focus` | 获得/设置 Tooltip 触发方式，默认为 hover focus |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnBeforeExport` | `Func<Task>?` | 导出 Pdf 之前回调委托 |
| `OnBeforeDownload` | `Func<Stream, Task>?` | 下载 Pdf 之前回调委托 |
| `OnAfterDownload` | `Func<string, Task>?` | 下载 Pdf 之后回调委托 |
| `OnClick` | `EventCallback<MouseEventArgs>` | OnClick 事件 |
| `OnClickWithoutRender` | `Func<Task>?` | OnClick 事件不刷新父组件 |

---

## 最佳实践

1. **安装依赖包**：使用 `ExportPdfButton` 组件前，必须先安装 `BootstrapBlazor.Html2Pdf` Nuget 包
2. **选择导出方式**：可以通过 `ElementId` 或 `Selector` 两种方式指定导出内容，选择适合的方式
3. **自定义文件名**：通过 `FileName` 参数设置有意义的文件名，提升用户体验
4. **处理导出流程**：使用 `OnBeforeExport`、`OnBeforeDownload`、`OnAfterDownload` 回调处理导出流程中的各个阶段
5. **异步按钮模式**：对于耗时的导出操作，使用 `IsAsync="true"` 启用异步按钮模式，避免用户重复点击
6. **添加必要资源**：如果导出内容依赖外部脚本或样式，使用 `ScriptTags` 和 `StyleTags` 参数添加所需资源
7. **自定义按钮样式**：通过 `Color`、`Size`、`Icon` 等参数自定义按钮外观，使其与应用程序风格一致
8. **手动处理 Pdf 流**：设置 `AutoDownload="false"` 并配合 `OnBeforeDownload` 回调，可以手动处理生成的 Pdf 流

---

## 常见问题

### 1. 使用 ExportPdfButton 组件需要安装什么包？

**回答**：使用 `ExportPdfButton` 组件需要安装 `BootstrapBlazor.Html2Pdf` Nuget 包。可以通过 .NET CLI、PackageReference 或 Package Manager 安装。

### 2. 如何指定导出内容？

**回答**：可以通过两种方式指定导出内容：
- 使用 `ElementId` 参数指定元素 Id
- 使用 `Selector` 参数指定 CSS 选择器

### 3. 如何自定义导出文件名？

**回答**：使用 `FileName` 参数设置导出 Pdf 文件名。如果不设置，默认使用 `pdf-时间戳.pdf`。

### 4. 如何手动处理生成的 Pdf 流？

**回答**：设置 `AutoDownload="false"` 并使用 `OnBeforeDownload` 回调，该回调的参数为 `Stream` 类型，表示生成的 Pdf 流。

### 5. 如何在导出前执行自定义逻辑？

**回答**：使用 `OnBeforeExport` 回调，在导出 Pdf 之前执行自定义逻辑，例如显示加载提示、准备数据等。

### 6. 如何在下载后执行自定义逻辑？

**回答**：使用 `OnAfterDownload` 回调，该回调的参数为文件名（`string` 类型），在下载完成后执行。

### 7. 如何启用异步按钮模式？

**回答**：设置 `IsAsync="true"` 启用异步按钮模式，点击按钮后按钮将被禁用并显示 loading 动画，直到异步操作完成。

### 8. 如何添加导出所需的脚本和样式？

**回答**：使用 `ScriptTags` 参数添加脚本文件集合，使用 `StyleTags` 参数添加样式表文件集合。

### 9. 如何自定义按钮图标？

**回答**：使用 `Icon` 参数设置按钮图标，例如 `Icon="fa fa-file-pdf"`。

### 10. 如何设置按钮提示信息？

**回答**：使用 `TooltipText` 参数设置提示文字，使用 `TooltipPlacement` 参数设置提示位置，使用 `TooltipTrigger` 参数设置触发方式。
