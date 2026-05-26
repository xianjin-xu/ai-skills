# CardUpload (卡片上传)

## 概述

`CardUpload` 组件用于**通过点击按钮弹出选择文件框选择一个或者多个文件，呈现为卡片式带预览模式**。组件支持卡片式布局、文件图标展示、自定义操作按钮、删除确认、下载、放大等功能。

**主要特性**：
- 支持点击按钮选择文件
- 卡片式预览布局
- 支持不同文件格式图标显示（.xls, .doc, .ppt, .mp3, .mp4, .pdf 等）
- 支持自定义文件图标（`IconTemplate`）
- 支持自定义操作按钮（`ActionButtonTemplate`、`BeforeActionButtonTemplate`）
- 支持删除确认对话框（`IsConfirmDelete`）
- 支持下载按钮（`ShowDownloadButton`）
- 支持放大按钮（`ShowZoomButton`）
- 支持多文件上传（`IsMultiple`）
- 支持 Base64 格式文件预览

**在线演示**: https://www.blazor.zone/card-upload

---

## 使用场景

### 1. 基础用法（简单卡片上传）

`CardUpload` 组件可以通过 `DefaultFileList` 设置已上传的内容。

```razor
<!-- 基础卡片上传 -->
<CardUpload DefaultFileList="DefaultFiles" OnChange="OnFileChange" />

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private async Task OnFileChange(UploadFile file)
    {
        // 处理上传的文件
    }
}
```

---

### 2. 显示删除按钮（ShowDeleteButton）

通过 `ShowDeleteButton` 参数控制是否显示删除按钮。

```razor
<!-- 显示删除按钮 -->
<CardUpload ShowDeleteButton="true" DefaultFileList="DefaultFiles" OnDelete="OnFileDelete" />

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private async Task<bool> OnFileDelete(UploadFile file)
    {
        // 处理删除逻辑
        // 返回 true 表示允许删除，返回 false 表示取消删除
        return true;
    }
}
```

---

### 3. 删除确认对话框（IsConfirmDelete）

通过 `IsConfirmDelete` 参数控制删除按钮是否显示确认对话框（依赖 `ShowDeleteButton="true"`）。

```razor
<!-- 删除前显示确认对话框 -->
<CardUpload 
    ShowDeleteButton="true" 
    IsConfirmDelete="true" 
    DefaultFileList="DefaultFiles" 
    OnDelete="OnFileDelete" />

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private async Task<bool> OnFileDelete(UploadFile file)
    {
        return true;
    }
}
```

---

### 4. 显示下载按钮（ShowDownloadButton）

通过 `ShowDownloadButton` 参数控制是否显示下载按钮。

```razor
<!-- 显示下载按钮 -->
<CardUpload 
    ShowDownloadButton="true" 
    DefaultFileList="DefaultFiles" 
    OnDownload="OnFileDownload" />

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private async Task OnFileDownload(UploadFile file)
    {
        // 处理下载逻辑
        // 例如：导航到文件下载地址
        // NavigationManager.NavigateTo(file.Url);
    }
}
```

---

### 5. 显示放大按钮（ShowZoomButton）

通过 `ShowZoomButton` 参数控制是否显示放大按钮，默认为 `true`。

```razor
<!-- 显示放大按钮（默认） -->
<CardUpload 
    ShowZoomButton="true" 
    DefaultFileList="DefaultFiles" 
    OnZoomAsync="OnFileZoom" />

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private async Task OnFileZoom(UploadFile file)
    {
        // 处理放大逻辑
        // 例如：显示图片预览弹窗
    }
}
```

---

### 6. 自定义操作按钮（ActionButtonTemplate）

通过 `ActionButtonTemplate` 参数自定义卡片上的操作按钮（在默认按钮后面追加）。

```razor
<!-- 自定义操作按钮 -->
<CardUpload ShowDeleteButton="true" DefaultFileList="DefaultFiles">
    <ActionButtonTemplate>
        <UploadFile file="context">
            <Button Size="Size.ExtraSmall" OnClick="() => OnCustomAction(file)">
                <i class="fa fa-cog"></i> 自定义操作
            </Button>
        </UploadFile>
    </ActionButtonTemplate>
</CardUpload>

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private void OnCustomAction(UploadFile file)
    {
        // 处理自定义操作
    }
}
```

---

### 7. 自定义操作按钮（BeforeActionButtonTemplate）

通过 `BeforeActionButtonTemplate` 参数自定义卡片上的操作按钮（在默认按钮前面追加）。

```razor
<!-- 在默认按钮前追加操作按钮 -->
<CardUpload ShowDeleteButton="true" DefaultFileList="DefaultFiles">
    <BeforeActionButtonTemplate>
        <UploadFile file="context">
            <Button Size="Size.ExtraSmall" OnClick="() => OnCustomAction(file)">
                <i class="fa fa-star"></i> 前置操作
            </Button>
        </UploadFile>
    </BeforeActionButtonTemplate>
</CardUpload>

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
    
    private void OnCustomAction(UploadFile file)
    {
        // 处理自定义操作
    }
}
```

---

### 8. 文件图标展示

不同文件格式显示的图标不同：

```razor
<!-- 不同文件格式的图标 -->
<CardUpload DefaultFileList="FilesWithDifferentIcons" />

@code {
    private List<UploadFile> FilesWithDifferentIcons { get; set; } = new List<UploadFile>
    {
        new UploadFile { FileName = "Test.xls", OriginFileName = "Test.xls", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.doc", OriginFileName = "Test.doc", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.ppt", OriginFileName = "Test.ppt", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.mp3", OriginFileName = "Test.mp3", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.mp4", OriginFileName = "Test.mp4", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.pdf", OriginFileName = "Test.pdf", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.cs", OriginFileName = "Test.cs", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.zip", OriginFileName = "Test.zip", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.txt", OriginFileName = "Test.txt", Size = 0, Uploaded = true },
        new UploadFile { FileName = "Test.dat", OriginFileName = "Test.dat", Size = 0, Uploaded = true }
    };
}
```

支持的图标格式包括：`.xls`, `.doc`, `.ppt`, `.mp3`, `.mp4`, `.pdf`, `.cs`, `.zip`, `.txt`, `.dat` 等。

---

### 9. 自定义文件图标（IconTemplate）

通过 `IconTemplate` 参数，使用 `FileIcon` 组件可以对文件图标进行进一步自定义。

```razor
<!-- 自定义文件图标 -->
<CardUpload DefaultFileList="DefaultFiles">
    <IconTemplate>
        <UploadFile file="context">
            <FileIcon FileName="file.FileName" />
        </UploadFile>
    </IconTemplate>
</CardUpload>

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test.xls", 
            OriginFileName = "Test.xls",
            Size = 0,
            Uploaded = true
        }
    };
}
```

---

### 10. Base64 格式文件预览

通过设置 `UploadFile` 实例的 `PrevUrl` 参数值使用 `data:image/xxx;base64,XXXXX` 格式图片内容字符串作为预览文件路径。

```razor
<!-- Base64 格式文件预览 -->
<CardUpload DefaultFileList="Base64Files" />

@code {
    private List<UploadFile> Base64Files { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "Test", 
            OriginFileName = "Test",
            Size = 0,
            Uploaded = true,
            PrevUrl = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
        }
    };
}
```

---

### 11. 多文件上传（IsMultiple）

通过 `IsMultiple` 参数控制是否允许多文件上传。

```razor
<!-- 多文件上传 -->
<CardUpload IsMultiple="true" OnChange="OnFileChange" />

@code {
    private async Task OnFileChange(UploadFile file)
    {
        // 多文件上传时，此回调会触发多次
    }
}
```

---

### 12. 显示上传进度（ShowProgress）

通过 `ShowProgress` 参数控制是否显示上传进度。

```razor
<!-- 显示上传进度 -->
<CardUpload ShowProgress="true" OnChange="OnFileChange" />
```

---

### 13. 禁用组件（IsDisabled）

通过 `IsDisabled` 参数禁用上传组件。

```razor
<!-- 禁用上传 -->
<CardUpload IsDisabled="true" />
```

---

### 14. 上传整个目录（IsDirectory）

通过 `IsDirectory` 参数控制是否上传整个目录。

```razor
<!-- 上传整个目录 -->
<CardUpload IsDirectory="true" OnChange="OnFileChange" />
```

---

### 15. 继续上传按钮位置（IsUploadButtonAtFirst）

通过 `IsUploadButtonAtFirst` 参数控制继续上传按钮是否在列表前。

```razor
<!-- 继续上传按钮在列表前 -->
<CardUpload IsUploadButtonAtFirst="true" IsMultiple="true" OnChange="OnFileChange" />
```

---

### 16. 显示文件大小（ShowFileSize）

通过 `ShowFileSize` 参数控制是否显示文件尺寸，默认为 `true`。

```razor
<!-- 不显示文件大小 -->
<CardUpload ShowFileSize="false" DefaultFileList="DefaultFiles" />
```

---

## 大文件上传配置（SignalR）

如果上传文件过大，可能会触发 SignalR 通讯中断问题。请自行调整 `HubOptions` 配置：

```csharp
// Program.cs 或 Startup.cs
builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);
```

---

## 参数 (Parameters)

### CardUpload 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Accept` | `string?` | `null` | 获得/设置 上传接收的文件格式，默认为 null 接收任意格式 |
| `ActionButtonTemplate` | `RenderFragment<UploadFile>?` | `null` | 获得/设置 操作按钮模板（在默认按钮后面追加） |
| `AddIcon` | `string?` | `null` | 获得/设置 新建图标 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `AllowExtensions` | `List<string>?` | `null` | 获得/设置 允许的文件扩展名集合 ".png" |
| `BeforeActionButtonTemplate` | `RenderFragment<UploadFile>?` | `null` | 获得/设置 操作按钮前模板（在默认按钮前面追加） |
| `CancelIcon` | `string?` | `null` | 获得/设置 取消按钮图标 |
| `CanPreviewCallback` | `Func<UploadFile, bool>?` | `null` | 获得/设置 是否允许预览的回调方法，默认 null |
| `Capture` | `string?` | `null` | 获得/设置 媒体捕获机制的首选面向模式，默认为 null |
| `DefaultFileList` | `List<UploadFile>?` | `null` | 获得/设置 已上传文件集合，可用于组件初始化 |
| `DeleteCloseButtonText` | `string?` | `null` | 获得/设置 删除确认弹窗中取消按钮显示文字，默认 null |
| `DeleteConfirmButtonColor` | `Color` | `Color.Danger` | 获得/设置 删除确认弹窗中确认按钮颜色，默认 Color.Danger |
| `DeleteConfirmButtonIcon` | `string?` | `null` | 获得/设置 删除确认弹窗中确认按钮图标，默认 null |
| `DeleteConfirmButtonText` | `string?` | `null` | 获得/设置 删除确认弹窗中确认按钮显示文字，默认 null |
| `DeleteConfirmContent` | `string?` | `null` | 获得/设置 删除确认弹窗中确认文本内容，默认 null 使用资源文件中内置文字 |
| `DeleteIcon` | `string?` | `null` | 获得/设置 删除按钮图标 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `DownloadIcon` | `string?` | `null` | 获得/设置 下载按钮图标 |
| `IconTemplate` | `RenderFragment<UploadFile>?` | `null` | 获得/设置 图标模板 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsConfirmDelete` | `bool` | `false` | 获得/设置 删除按钮是否显示确认对话框，依赖 ShowDeleteButton 属性为 true 时有效 |
| `IsDirectory` | `bool` | `false` | 获得/设置 是否上传整个目录，默认为 false |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 默认为 false |
| `IsMultiple` | `bool` | `true` | 获得/设置 是否允许多文件上传，默认 true |
| `IsSingle` | `bool` | `false` | **已弃用** 获得/设置 是否仅上传一次，默认 false（已弃用 请使用 IsMultiple 参数） |
| `IsUploadButtonAtFirst` | `bool` | `false` | 获得/设置 继续上传按钮是否在列表前，默认 false |
| `Max` | `int` | `int.MaxValue` | **已弃用** 获得/设置 最大上传个数，默认为最大值 int.MaxValue（已弃用。请使用 MaxFileCount 参数。） |
| `MaxFileCount` | `int?` | `null` | 获得/设置 最大上传个数，默认为 null |
| `OnAllFileUploaded` | `Func<IReadOnlyCollection<UploadFile>, Task>?` | `null` | 获得/设置 所有文件上传完毕回调方法，默认 null |
| `OnCancel` | `Func<UploadFile, Task>?` | `null` | 获得/设置 点击取消按钮回调方法，默认 null |
| `OnChange` | `Func<UploadFile, Task>?` | `null` | 获得/设置 点击浏览按钮时回调此方法，如果多文件上传此回调会触发多次，默认 null |
| `OnDelete` | `Func<UploadFile, Task<bool>>?` | `null` | 获得/设置 点击删除按钮时回调此方法，默认 null |
| `OnDownload` | `Func<UploadFile, Task>?` | `null` | 获得/设置 点击下载按钮回调方法，默认 null |
| `OnValueChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `OnZoomAsync` | `Func<UploadFile, Task>?` | `null` | 获得/设置 点击放大图标回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 默认为 null |
| `RemoveIcon` | `string?` | `null` | 获得/设置 移除图标 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 默认为 null 未设置 |
| `ShowDeleteButton` | `bool` | `false` | 获得/设置 是否显示删除按钮，默认 false |
| `ShowDeleteConfirmButton` | `bool` | `false` | **已弃用** 获得/设置 删除前是否显示确认对话框，依赖 ShowDeleteButton 属性为 true 时有效 |
| `ShowDeletedButton` | `bool` | `true` | **已弃用** 获得/设置 是否显示删除按钮，默认 true |
| `ShowDownloadButton` | `bool` | `false` | 获得/设置 是否显示下载按钮，默认 false |
| `ShowFileSize` | `bool` | `true` | 获得/设置 是否显示文件尺寸，默认为 true |
| `ShowLabel` | `bool?` | `null` | 获得/设置 是否显示前置标签，默认值为 null，为空时不显示标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null |
| `ShowProgress` | `bool` | `false` | 获得/设置 是否显示上传进度，默认为 false |
| `ShowRequired` | `bool?` | `null` | 获得/设置 是否显示必填项标记 默认为 null 未设置 |
| `ShowZoomButton` | `bool` | `true` | 获得/设置 是否显示放大按钮，默认 true |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 默认为 false |
| `StatusIcon` | `string?` | `null` | 获得/设置 状态图标 |
| `ValidateRules` | `List<IValidator>?` | `null` | 获得/设置 自定义验证集合 |
| `Value` | `TValue` | `default` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<TValue>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<TValue>>?` | `null` | 获得/设置 标识绑定值的表达式 |
| `ZoomIcon` | `string?` | `null` | 获得/设置 放大图标 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnChange` | `Func<UploadFile, Task>?` | 点击浏览按钮时回调此方法，如果多文件上传此回调会触发多次 |
| `OnDelete` | `Func<UploadFile, Task<bool>>?` | 点击删除按钮时回调此方法 |
| `OnDownload` | `Func<UploadFile, Task>?` | 点击下载按钮回调方法 |
| `OnCancel` | `Func<UploadFile, Task>?` | 点击取消按钮回调方法 |
| `OnZoomAsync` | `Func<UploadFile, Task>?` | 点击放大图标回调方法 |
| `OnAllFileUploaded` | `Func<IReadOnlyCollection<UploadFile>, Task>?` | 所有文件上传完毕回调方法 |
| `OnValueChanged` | `Func<TValue, Task>?` | Value 改变时回调方法 |

---

## 最佳实践

1. **使用 DefaultFileList 初始化**：推荐通过 `DefaultFileList` 参数设置已上传文件集合，用于组件初始化展示
2. **删除确认保护数据**：设置 `IsConfirmDelete="true"` 可以在删除文件前显示确认对话框，防止误删
3. **自定义操作按钮**：通过 `ActionButtonTemplate` 和 `BeforeActionButtonTemplate` 参数可以自定义卡片上的操作按钮，扩展组件功能
4. **文件格式图标**：组件会自动根据文件扩展名显示对应的图标，支持常见格式（.xls, .doc, .ppt, .mp3, .mp4, .pdf 等）
5. **Base64 预览**：对于图片文件，可以通过设置 `UploadFile.PrevUrl` 为 `data:image/xxx;base64,XXXXX` 格式实现预览
6. **大文件上传配置**：上传大文件时，需要配置 `HubOptions` 的 `MaximumReceiveMessageSize`，否则可能导致 SignalR 通讯中断
7. **多文件上传处理**：当 `IsMultiple="true"` 时，`OnChange` 回调会对每个文件触发一次，需要注意性能
8. **使用 OnDownload 处理下载**：通过 `OnDownload` 回调处理文件下载逻辑，例如导航到文件下载地址

---

## 常见问题

### 1. 上传大文件时出现 SignalR 通讯中断？

**问题**：上传文件过大，可能会触发 SignalR 通讯中断问题。

**解决方案**：调整 `HubOptions` 配置，设置 `MaximumReceiveMessageSize` 为 `null` 或更大的值。

```csharp
// Program.cs 或 Startup.cs
builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);
```

### 2. 如何自定义操作按钮？

**回答**：使用 `ActionButtonTemplate` 参数在默认按钮后面追加自定义按钮，或使用 `BeforeActionButtonTemplate` 参数在默认按钮前面追加自定义按钮。通过 `context` 可以访问当前的 `UploadFile` 对象。

### 3. 如何显示删除确认对话框？

**回答**：设置 `ShowDeleteButton="true"` 和 `IsConfirmDelete="true"` 即可在删除文件前显示确认对话框。

### 4. ShowDeleteConfirmButton 参数已弃用，应该用什么？

**回答**：`ShowDeleteConfirmButton` 参数已弃用，请使用 `IsConfirmDelete` 参数来控制删除确认对话框的显示。

### 5. 如何自定义文件图标？

**回答**：使用 `IconTemplate` 参数，结合 `FileIcon` 组件可以对文件图标进行自定义。

### 6. 如何显示文件大小？

**回答**：设置 `ShowFileSize="true"`（默认值）即可显示文件大小。设置为 `false` 可隐藏文件大小显示。

### 7. Max 参数已弃用，应该用什么？

**回答**：`Max` 参数已弃用，请使用 `MaxFileCount` 参数来限制最大上传个数。
