# InputUpload (输入框上传组件)

## 概述

`InputUpload` 是一个文件上传组件，提供文件浏览、上传、删除功能，支持单文件和多文件上传，提供丰富的配置选项和事件回调。

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/upload](https://www.blazor.zone/upload)

## 使用场景

### 1. 基本用法

```razor
<InputUpload @bind-Value="FileValue" />
```

```csharp
@code {
    IBrowserFile? FileValue { get; set; }
}
```

### 2. 多文件上传

```razor
<InputUpload @bind-Value="FileList" IsMultiple="true" />
```

```csharp
@code {
    List<IBrowserFile>? FileList { get; set; }
}
```

### 3. 显示删除按钮

```razor
<InputUpload @bind-Value="FileValue" ShowDeleteButton="true" />
```

### 4. 删除确认

```razor
<InputUpload @bind-Value="FileValue" ShowDeleteButton="true" IsConfirmDelete="true" />
```

### 5. 自定义按钮文本

```razor
<InputUpload @bind-Value="FileValue" 
           BrowserButtonText="选择文件" 
           DeleteButtonText="删除文件" />
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `BrowserButtonIcon` | `string?` | `null` | 获得/设置浏览按钮图标 |
| `BrowserButtonClass` | `string` | `"btn-primary"` | 获得/设置上传按钮样式 |
| `BrowserButtonText` | `string?` | `null` | 获得/设置浏览按钮显示文字 |
| `DeleteButtonClass` | `string` | `"btn-danger"` | 获得/设置删除按钮样式 |
| `DeleteButtonIcon` | `string?` | `null` | 获得/设置删除按钮图标 |
| `DeleteButtonText` | `string?` | `null` | 获得/设置删除按钮显示文字 |
| `ShowDeleteButton` | `bool` | `false` | 获得/设置是否显示删除按钮 |
| `IsConfirmDelete` | `bool` | `false` | 获得/设置删除按钮是否显示确认对话框 |
| `DeleteConfirmButtonIcon` | `string?` | `null` | 获得/设置删除确认弹窗中确认按钮图标 |
| `DeleteConfirmButtonColor` | `Color` | `Color.Danger` | 获得/设置删除确认弹窗中确认按钮颜色 |
| `DeleteConfirmButtonText` | `string?` | `null` | 获得/设置删除确认弹窗中确认按钮显示文字 |
| `DeleteCloseButtonText` | `string?` | `null` | 获得/设置删除确认弹窗中取消按钮显示文字 |
| `DeleteConfirmContent` | `string?` | `null` | 获得/设置删除确认弹窗中确认文本内容 |
| `PlaceHolder` | `string?` | `null` | 获得/设置 PlaceHolder 占位符文本 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `ValueChanged` | 值改变时触发 |
| `OnUpload` | 上传时触发 |

## 最佳实践

1. **文件绑定**: 使用 `Value` 参数绑定文件值，支持单文件 (`IBrowserFile`) 和多文件 (`List<IBrowserFile>`)
2. **多文件上传**: 设置 `IsMultiple="true"` 启用多文件上传
3. **删除功能**: 设置 `ShowDeleteButton="true"` 显示删除按钮
4. **删除确认**: 设置 `IsConfirmDelete="true"` 在删除前显示确认对话框
5. **按钮自定义**: 使用 `BrowserButtonText` 和 `DeleteButtonText` 自定义按钮文本
6. **上传限制**: 使用 `MaxFileSize` 和 `AllowedExtensions` 限制上传文件大小和类型

## 常见问题

### Q: 如何绑定上传的文件？
A: 使用 `Value` 参数绑定到 `IBrowserFile` 或 `List<IBrowserFile>` 类型的变量。

### Q: 如何限制上传文件类型？
A: 使用 `AllowedExtensions` 参数设置允许的文件扩展名。

### Q: 如何限制上传文件大小？
A: 使用 `MaxFileSize` 参数设置最大文件大小（字节）。

### Q: 如何自定义上传逻辑？
A: 使用 `OnUpload` 事件回调自定义上传逻辑。

### Q: 如何显示上传进度？
A: 使用 `OnProgress` 事件回调显示上传进度。