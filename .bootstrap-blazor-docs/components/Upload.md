# Upload (上传组件)

## 概述

`Upload` 组件用于**文件上传功能**，支持单文件/多文件上传、拖拽上传、进度显示等。

**主要特性**：
- 支持单文件/多文件上传
- 支持拖拽上传
- 显示上传进度
- 支持文件类型限制
- 支持文件大小限制
- 可自定义上传逻辑

**在线演示**: https://www.blazor.zone/upload

---

## 使用场景

### 1. 基础用法（单文件上传）

`Upload` 组件可以通过 `OnUpload` 事件处理上传逻辑。

```razor
<!-- 单文件上传 -->
<Upload @ref="UploadRef" OnUpload="OnUpload" />

@code {
    private Upload? UploadRef { get; set; }

    private async Task OnUpload(UploadFile file)
    {
        // 处理上传逻辑
        // file.File 是 IBrowserFile 对象
        // file.FileName 是文件名
        // file.Size 是文件大小
        
        // 保存到服务器或数据库
        // ...
        
        // 标记上传完成
        file.Uploaded = true;
    }
}
```

---

### 2. 多文件上传（Multiple）

通过设置 `Multiple="true"` 启用多文件上传。

```razor
<!-- 多文件上传 -->
<Upload @ref="UploadRef" OnUpload="OnUpload" Multiple="true" />

@code {
    private Upload? UploadRef { get; set; }

    private async Task OnUpload(UploadFile file)
    {
        // 处理每个文件的上传
        // ...
        file.Uploaded = true;
    }
}
```

---

### 3. 拖拽上传（IsDrag）

通过设置 `IsDrag="true"` 启用拖拽上传区域。

```razor
<!-- 拖拽上传 -->
<Upload @ref="UploadRef" OnUpload="OnUpload" IsDrag="true" />

@code {
    private Upload? UploadRef { get; set; }

    private async Task OnUpload(UploadFile file)
    {
        // 处理上传
        // ...
        file.Uploaded = true;
    }
}
```

---

### 4. 文件类型限制（Accept）

通过 `Accept` 参数限制可上传的文件类型。

```razor
<!-- 仅允许图片 -->
<Upload @ref="UploadRef" OnUpload="OnUpload" Accept="image/*" />

<!-- 仅允许 PDF -->
<Upload @ref="UploadRef" OnUpload="OnUpload" Accept=".pdf" />

<!-- 允许多种类型 -->
<Upload @ref="UploadRef" OnUpload="OnUpload" Accept=".jpg,.jpeg,.png,.pdf" />

@code {
    private Upload? UploadRef { get; set; }

    private async Task OnUpload(UploadFile file)
    {
        // 处理上传
        // ...
        file.Uploaded = true;
    }
}
```

**常用 Accept 值**：
- `image/*` - 所有图片
- `.pdf` - PDF 文件
- `.jpg,.jpeg,.png` - 特定图片格式
- `.doc,.docx` - Word 文档

---

### 5. 文件大小限制（MaxSize）

通过 `MaxSize` 参数限制上传文件大小（字节）。

```razor
<!-- 最大 10MB -->
<Upload @ref="UploadRef" OnUpload="OnUpload" MaxSize="10485760" />

@code {
    private Upload? UploadRef { get; set; }

    private async Task OnUpload(UploadFile file)
    {
        // 检查文件大小
        if (file.Size > 10485760) // 10MB
        {
            // 文件过大，提示用户
            return;
        }
        
        // 处理上传
        // ...
        file.Uploaded = true;
    }
}
```

**常用大小**：
- `1048576` - 1MB
- `5242880` - 5MB
- `10485760` - 10MB
- `52428800` - 50MB

---

### 6. 显示上传进度（ShowProgress）

通过设置 `ShowProgress="true"` 显示上传进度条。

```razor
<!-- 显示进度 -->
<Upload @ref="UploadRef" OnUpload="OnUpload" ShowProgress="true" />

@code {
    private Upload? UploadRef { get; set; }

    private async Task OnUpload(UploadFile file)
    {
        // 处理上传，进度会自动显示
        // ...
        file.Uploaded = true;
    }
}
```

---

## 参数 (Parameters)

### Upload 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Multiple` | `bool` | `false` | 获得/设置是否多文件上传 |
| `IsDrag` | `bool` | `false` | 获得/设置是否拖拽上传 |
| `Accept` | `string?` | `null` | 获得/设置允许的文件类型 |
| `MaxSize` | `long` | `0` | 获得/设置最大文件大小（字节），0 表示不限制 |
| `ShowProgress` | `bool` | `true` | 获得/设置是否显示进度 |
| `Disabled` | `bool` | `false` | 获得/设置是否禁用 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnUpload` | `Func<UploadFile, Task>` | 上传文件回调 |
| `OnDelete` | `Func<UploadFile, Task>` | 删除文件回调 |
| `OnChange` | `Func<List<UploadFile>, Task>` | 文件列表变化回调 |

---

## 数据类 (UploadFile)

`UploadFile` 类表示上传的文件。

| 参数名 | 类型 | 说明 |
|--------|------|------|
| `File` | `IBrowserFile?` | 获得浏览器文件对象 |
| `FileName` | `string?` | 获得/设置文件名 |
| `Size` | `long` | 获得文件大小（字节） |
| `Uploaded` | `bool` | 获得/设置是否上传完成 |
| `Progress` | `int` | 获得上传进度（0-100） |
| `Error` | `string?` | 获得错误信息 |

---

## 最佳实践

1. **处理 OnUpload 事件**：在 `OnUpload` 事件中实现实际上传逻辑（如调用 API 上传到服务器）
2. **验证文件类型和大小**：在 `OnUpload` 事件中验证 `Accept` 和 `MaxSize`，避免无效文件上传
3. **显示上传进度**：设置 `ShowProgress="true"` 让用户了解上传进度，提升体验
4. **处理 OnDelete 事件**：在 `OnDelete` 事件中清理服务器上的文件，避免孤立文件
5. **多文件上传注意性能**：多文件上传时，考虑并发控制，避免同时上传过多文件
6. **错误处理**：在 `OnUpload` 事件中捕获异常，设置 `file.Error` 显示错误信息
7. **与 InputFile 的区别**：`Upload` 是封装好的上传组件（带 UI），`InputFile` 是原生文件输入（需自行处理 UI）
