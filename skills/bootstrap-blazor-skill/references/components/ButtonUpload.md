# ButtonUpload 按钮上传组件#

## 组件概述#

ButtonUpload 是一个按钮上传组件，通过点击按钮弹出选择文件框选择一个或者多个文件，通常用作上传文件附件。

**重要提示：**如果上传文件过大，可能会触发 SignalR 通讯中断问题，请自行调整 HubOptions 配置即可：

```csharp
builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);
```

## 使用场景#

### 1. 基础用法#

通过设置 `ShowUploadFileList="true"` 可以显示上传文件列表，设置 `ShowDeleteButton="true"` 显示删除按钮。

```razor
<ButtonUpload TValue="string" @bind-Value="FileValue" 
           ShowUploadFileList="true" 
           ShowDeleteButton="true" />
```

```csharp
@code {
    private string FileValue { get; set; }
}
```

**说明：**
- `TValue"` - 值类型参数
- `Value"` - 当前选中值
- `ShowUploadFileList"` - 是否显示上传文件列表
- `ShowDeleteButton"` - 是否显示删除按钮#

### 2. 禁用状态#

设置 `IsDisabled="true"` 禁用组件。

```razor
<ButtonUpload TValue="string" IsDisabled="true" />
```

**说明：**
- `IsDisabled="true"` 禁用组件#
### 3. 多文件上传#

设置 `IsMultiple="true"` 允许多文件上传。

```razor
<ButtonUpload TValue="string" IsMultiple="true" 
           ShowUploadFileList="true" />
```

**说明：**
- `IsMultiple="true"` 允许多文件上传（默认 `true`）
- 可上传多个文件#

### 4. 显示下载按钮#

设置 `ShowDownloadButton="true"` 显示下载按钮。

```razor
<ButtonUpload TValue="string" ShowDownloadButton="true" 
           ShowUploadFileList="true" />
```

**说明：**
- `ShowDownloadButton="true"` 显示下载按钮
- 点击下载按钮触发 `OnDownload` 回调#

### 5. 显示上传进度#

设置 `ShowProgress="true"` 显示上传进度。

```razor
<ButtonUpload TValue="string" ShowProgress="true" />
```

**说明：**
- `ShowProgress="true"` 显示上传进度条#
### 6. 自定义按钮样式#

通过设置 `BrowserButtonColor`、`BrowserButtonIcon`、`BrowserButtonText` 自定义浏览按钮。

```razor
<ButtonUpload TValue="string" 
           BrowserButtonColor="Color.Success" 
           BrowserButtonIcon="fa fa-upload" 
           BrowserButtonText="选择文件" />
```

**说明：**
- `BrowserButtonColor"` - 浏览按钮颜色
- `BrowserButtonIcon"` - 浏览按钮图标
- `BrowserButtonText"` - 浏览按钮文字#

### 7. 完整示例#

包含上传、下载、删除、进度显示等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>按钮上传组件示例</CardTitle>
    </CardHeader>
    <CardBody>
        <div class="row g-3">
            <div class="col-12">
                <ButtonUpload TValue="string" 
                           @bind-Value="FileValue" 
                           IsMultiple="true"
                           ShowUploadFileList="true"
                           ShowDeleteButton="true"
                           ShowDownloadButton="true"
                           ShowProgress="true"
                           BrowserButtonColor="Color.Primary"
                           BrowserButtonIcon="fa fa-upload"
                           BrowserButtonText="选择文件"
                           OnChange="OnFileChange"
                           OnDelete="OnFileDelete"
                           OnDownload="OnFileDownload"
                           OnAllFilesUploaded="OnAllUploaded" />
            </div>
        </div>
    </CardBody>
</Card>

@code {
    private string FileValue { get; set; }
    
    private Task OnFileChange(UploadFile file)
    {
        Console.WriteLine($"文件变化: {file.FileName}");
        return Task.CompletedTask;
    }
    
    private async Task<bool> OnFileDelete(UploadFile file)
    {
        Console.WriteLine($"删除文件: {file.FileName}");
        return await Task.FromResult(true);
    }
    
    private Task OnFileDownload(UploadFile file)
    {
        Console.WriteLine($"下载文件: {file.FileName}");
        return Task.CompletedTask;
    }
    
    private Task OnAllUploaded(IReadOnlyCollection<UploadFile> files)
    {
        Console.WriteLine($"所有文件上传完成: {files.Count} 个");
        return Task.CompletedTask;
    }
}
```

## 组件参数#

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Value` | 获得/设置 输入组件的值，支持双向绑定 | `TValue` | - |
| `Accept` | 获得/设置 上传接收的文件格式，默认为 null 接收任意格式 | `string` | `null` |
| `BrowserButtonClass` | 获得/设置 上传按钮样式 | `string` | `null` |
| `BrowserButtonColor` | 获得/设置 浏览按钮颜色 | `Color` | - |
| `BrowserButtonIcon` | 获得/设置 浏览按钮图标 | `string` | - |
| `BrowserButtonText` | 获得/设置 浏览按钮显示文字 | `string` | - |
| `CancelIcon` | 获得/设置 取消按钮图标 | `string` | - |
| `Capture` | 获得/设置 媒体捕获机制的首选面向模式 | `string` | `null` |
| `DefaultFileList` | 获得/设置 已上传文件集合，可用于组件初始化 | `List<UploadFile>` | - |
| `DeleteIcon` | 获得/设置 删除按钮图标 | `string` | - |
| `DisplayText` | 获得/设置 显示名称 | `string` | - |
| `DownloadIcon` | 获得/设置 下载按钮图标 | `string` | - |
| `IsDirectory` | 获得/设置 是否上传整个目录，默认为 false | `bool` | `false` |
| `IsDisabled` | 获得/设置 是否禁用 | `bool` | `false` |
| `IsMultiple` | 获得/设置 是否允许多文件上传，默认 true | `bool` | `true` |
| `LoadingIcon` | 获得/设置 浏览按钮加载中图标 | `string` | - |
| `MaxFileCount` | 获得/设置 最大上传个数 | `Nullable<int>` | `null` |
| `ShowDeleteButton` | 获得/设置 是否显示删除按钮 | `bool` | `true` |
| `ShowDownloadButton` | 获得/设置 是否显示下载按钮 | `bool` | `false` |
| `ShowLabel` | 获得/设置 是否显示前置标签 | `Nullable<bool>` | `null` |
| `ShowProgress` | 获得/设置 是否显示上传进度 | `bool` | `false` |
| `ShowRequired` | 获得/设置 是否显示必填项标记 | `Nullable<bool>` | `null` |
| `ShowUploadFileList` | 获得/设置 是否显示上传列表 | `bool` | `true` |
| `Size` | 获得/设置 按钮大小 | `Size` | - |
| `ValidStatusIcon` | 获得/设置 上传成功状态图标 | `string` | - |
| `InvalidStatusIcon` | 获得/设置 上传失败状态图标 | `string` | - |
| `OnAllFilesUploaded` | 获得/设置 所有文件上传完毕回调方法 | `Func<IReadOnlyCollection<UploadFile>, Task>` | - |
| `OnCancel` | 获得/设置 点击取消按钮回调方法 | `Func<UploadFile, Task>` | - |
| `OnChange` | 获得/设置 点击浏览按钮时回调此方法 | `Func<UploadFile, Task>` | - |
| `OnDelete` | 获得/设置 点击删除按钮时回调此方法 | `Func<UploadFile, Task<bool>>` | - |
| `OnDownload` | 获得/设置 点击下载按钮回调方法 | `Func<UploadFile, Task>` | - |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<TValue, Task>` | - |

## 最佳实践#

1. **SignalR 配置**：上传大文件时需调整 `MaximumReceiveMessageSize` 避免通讯中断
2. **多文件上传**：设置 `IsMultiple="true"` 支持多文件选择
3. **文件列表**：设置 `ShowUploadFileList="true"` 显示已上传文件
4. **下载功能**：设置 `ShowDownloadButton="true"` 提供下载入口
5. **进度显示**：设置 `ShowProgress="true"` 显示上传进度#

## 常见问题#

**Q: 上传大文件失败怎么办？**
A: 调整 SignalR 配置：`builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);`

**Q: 如何允许多文件上传？**
A: 设置 `IsMultiple="true"`（默认值）。

**Q: 如何显示已上传文件列表？**
A: 设置 `ShowUploadFileList="true"`。

**Q: 如何实现文件下载？**
A: 设置 `ShowDownloadButton="true"`，并实现 `OnDownload` 回调方法。

**Q: 如何限制上传文件类型？**
A: 使用 `Accept` 参数，如 `Accept=".jpg,.png"` 限制图片格式。

## 版本历史#

- **初始版本**: 支持按钮上传、多文件、下载、删除、进度显示等功能
