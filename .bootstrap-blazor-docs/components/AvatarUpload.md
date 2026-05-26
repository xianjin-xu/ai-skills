# AvatarUpload (头像上传)

## 概述

`AvatarUpload` 组件用于**上传头像或类似头像的图片**，通常通过点击上传文件，用作上传预览一个或者一组类似头像的图片。组件支持圆形/方形预览、多文件上传、进度显示等功能。

**主要特性**：
- 支持点击上传文件
- 支持圆形头像预览（`IsCircle`）
- 支持自定义边框圆角（`BorderRadius`）
- 支持多文件上传（`IsMultiple`）
- 支持上传进度显示（`ShowProgress`）
- 支持文件格式过滤（`Accept`）
- 支持默认文件列表展示（`DefaultFileList`）
- 支持自定义上传回调（`OnChange`）

**在线演示**: https://www.blazor.zone/avatar-upload

---

## 使用场景

### 1. 基础用法（简单头像上传）

`AvatarUpload` 组件可以通过 `OnChange` 回调处理上传的文件。如果未提供此回调，将使用内置方法尝试读取上传文件生成 base64 格式预览数据。

```razor
<!-- 基础头像上传 -->
<AvatarUpload OnChange="OnAvatarChange" />

@code {
    private async Task OnAvatarChange(UploadFile file)
    {
        // 处理上传的文件
        // file.FileName - 文件名
        // file.Size - 文件大小
        // file.OriginFileName - 原始文件名
        
        // 示例：保存到服务器
        // await SaveFileAsync(file);
    }
}
```

---

### 2. 圆形头像（IsCircle）

通过 `IsCircle` 参数设置为 `true`，使头像显示为圆形。

```razor
<!-- 圆形头像上传 -->
<AvatarUpload IsCircle="true" OnChange="OnAvatarChange" />

@code {
    private async Task OnAvatarChange(UploadFile file)
    {
        // 处理上传的文件
    }
}
```

---

### 3. 自定义边框圆角（BorderRadius）

通过 `BorderRadius` 参数设置边框圆角曲率。

```razor
<!-- 自定义圆角 -->
<AvatarUpload BorderRadius="10" OnChange="OnAvatarChange" />

@code {
    private async Task OnAvatarChange(UploadFile file)
    {
        // 处理上传的文件
    }
}
```

---

### 4. 多文件上传（IsMultiple）

通过 `IsMultiple` 参数控制是否允许多文件上传。

```razor
<!-- 多文件上传 -->
<AvatarUpload IsMultiple="true" OnChange="OnAvatarChange" />

@code {
    private async Task OnAvatarChange(UploadFile file)
    {
        // 多文件上传时，此回调会触发多次
        // 每次触发对应一个文件
    }
}
```

---

### 5. 文件格式过滤（Accept）

通过 `Accept` 属性设置上传文件过滤功能。

```razor
<!-- 仅接受 GIF 和 JPEG 图像 -->
<AvatarUpload Accept="image/gif, image/jpeg" OnChange="OnAvatarChange" />

<!-- 接受所有图像格式 -->
<AvatarUpload Accept="image/*" OnChange="OnAvatarChange" />
```

**注意**：`Accept` 属性并不安全，应该使用服务器端验证进行文件格式验证。

---

### 6. 显示上传进度（ShowProgress）

通过 `ShowProgress` 参数控制是否显示上传进度。

```razor
<!-- 显示上传进度 -->
<AvatarUpload ShowProgress="true" OnChange="OnAvatarChange" />
```

---

### 7. 设置预览框尺寸（Width/Height）

通过 `Width` 和 `Height` 参数设置文件预览框的宽度和高度。

```razor
<!-- 设置预览框尺寸 -->
<AvatarUpload Width="200" Height="200" OnChange="OnAvatarChange" />
```

---

### 8. 禁用组件（IsDisabled）

通过 `IsDisabled` 参数禁用上传组件。

```razor
<!-- 禁用上传 -->
<AvatarUpload IsDisabled="true" />
```

---

### 9. 在 ValidateForm 中使用（表单验证）

将 `AvatarUpload` 放置到 `ValidateForm` 内，集成自动数据验证功能。

```razor
<!-- 在 ValidateForm 中使用 -->
<ValidateForm OnValidSubmit="OnValidSubmit">
    <AvatarUpload 
        Accept="image/png, image/jpg, image/jpeg" 
        OnChange="OnAvatarChange" 
        ShowRequired="true" />
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>

@code {
    private async Task OnAvatarChange(UploadFile file)
    {
        // 处理上传的文件
    }
    
    private async Task OnValidSubmit()
    {
        // 表单验证通过后的处理
    }
}
```

**说明**：本例中上传文件扩展名仅限制为 `.png`, `.jpg`, `.jpeg`，上传其他格式时会有错误提示，文件大小限制为 5M，超过时也会有错误提示显示。

---

### 10. 设置默认文件列表（DefaultFileList）

通过 `DefaultFileList` 参数设置已上传文件集合，用于组件初始化。

```razor
<!-- 设置默认文件列表 -->
<AvatarUpload DefaultFileList="DefaultFiles" OnChange="OnAvatarChange" />

@code {
    private List<UploadFile> DefaultFiles { get; set; } = new List<UploadFile>
    {
        new UploadFile 
        { 
            FileName = "avatar.jpg", 
            OriginFileName = "avatar.jpg",
            Size = 1024,
            Uploaded = true
        }
    };
    
    private async Task OnAvatarChange(UploadFile file)
    {
        // 处理上传的文件
    }
}
```

---

### 11. 继续上传按钮位置（IsUploadButtonAtFirst）

通过 `IsUploadButtonAtFirst` 参数控制继续上传按钮是否在列表前。

```razor
<!-- 继续上传按钮在列表前 -->
<AvatarUpload IsUploadButtonAtFirst="true" IsMultiple="true" OnChange="OnAvatarChange" />
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

### AvatarUpload 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Accept` | `string?` | `null` | 获得/设置 上传接收的文件格式，默认为 null 接收任意格式 |
| `AddIcon` | `string?` | `null` | 获得/设置 新增图标 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `AllowExtensions` | `List<string>?` | `null` | 获得/设置 允许的文件扩展名集合，".png" |
| `BorderRadius` | `string?` | `null` | 获得/设置 边框圆角，默认为 null |
| `CanPreviewCallback` | `Func<UploadFile, bool>?` | `null` | 获得/设置 是否允许预览的回调方法，默认 null |
| `Capture` | `string?` | `null` | 获得/设置 媒体捕获机制的首选面向模式，默认为 null |
| `DefaultFileList` | `List<UploadFile>?` | `null` | 获得/设置 已上传文件集合，可用于组件初始化 |
| `DeleteIcon` | `string?` | `null` | 获得/设置 删除图标 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `Height` | `int` | `0` | 获得/设置 文件预览框高度 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `InvalidStatusIcon` | `string?` | `null` | 获得/设置 上传失败状态图标 |
| `IsCircle` | `bool` | `false` | 获得/设置 是否圆形图片框，Avatar 模式时生效，默认为 false |
| `IsDirectory` | `bool` | `false` | 获得/设置 是否上传整个目录，默认为 false |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 默认为 false |
| `IsMultiple` | `bool` | `true` | 获得/设置 是否允许多文件上传，默认 true |
| `IsSingle` | `bool` | `false` | **已弃用** 获得/设置 是否仅上传一次，默认 false（已弃用 请使用 IsMultiple 参数） |
| `IsUploadButtonAtFirst` | `bool` | `false` | 获得/设置 继续上传按钮是否在列表前，默认 false |
| `LoadingIcon` | `string?` | `null` | 获得/设置 加载中图标 |
| `Max` | `int` | `int.MaxValue` | **已弃用** 获得/设置 最大上传个数，默认为最大值 int.MaxValue（已弃用。请使用 MaxFileCount 参数。） |
| `MaxFileCount` | `int?` | `null` | 获得/设置 最大上传个数，默认为 null |
| `OnAllFileUploaded` | `Func<IReadOnlyCollection<UploadFile>, Task>?` | `null` | 获得/设置 所有文件上传完毕回调方法，默认 null |
| `OnChange` | `Func<UploadFile, Task>?` | `null` | 获得/设置 点击浏览按钮时回调此方法，如果多文件上传此回调会触发多次，默认 null |
| `OnDelete` | `Func<UploadFile, Task<bool>>?` | `null` | 获得/设置 点击删除按钮时回调此方法，默认 null |
| `OnValueChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 默认为 null |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 默认为 null 未设置 |
| `ShowLabel` | `bool?` | `null` | 获得/设置 是否显示前置标签，默认值为 null，为空时不显示标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null |
| `ShowProgress` | `bool` | `false` | 获得/设置 是否显示上传进度，默认为 false |
| `ShowRequired` | `bool?` | `null` | 获得/设置 是否显示必填项标记 默认为 null 未设置 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 默认为 false |
| `ValidateRules` | `List<IValidator>?` | `null` | 获得/设置 自定义验证集合 |
| `ValidStatusIcon` | `string?` | `null` | 获得/设置 上传成功状态图标 |
| `Value` | `TValue` | `default` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<TValue>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<TValue>>?` | `null` | 获得/设置 标识绑定值的表达式 |
| `Width` | `int` | `0` | 获得/设置 文件预览框宽度 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnChange` | `Func<UploadFile, Task>?` | 点击浏览按钮时回调此方法，如果多文件上传此回调会触发多次 |
| `OnDelete` | `Func<UploadFile, Task<bool>>?` | 点击删除按钮时回调此方法 |
| `OnAllFileUploaded` | `Func<IReadOnlyCollection<UploadFile>, Task>?` | 所有文件上传完毕回调方法 |
| `OnValueChanged` | `Func<TValue, Task>?` | Value 改变时回调方法 |

---

## 最佳实践

1. **使用 OnChange 处理上传**：推荐通过 `OnChange` 回调处理用户上传的文件，在回调中进行文件保存或处理
2. **未提供 OnChange 时的行为**：如果未提供 `OnChange` 回调，组件将使用内置方法尝试读取上传文件生成 base64 格式预览数据
3. **多文件上传处理**：当 `IsMultiple="true"` 时，`OnChange` 回调会对每个文件触发一次，需要注意性能
4. **文件格式验证**：`Accept` 属性仅用于客户端过滤，不安全，必须在服务器端进行文件格式验证
5. **大文件上传配置**：上传大文件时，需要配置 `HubOptions` 的 `MaximumReceiveMessageSize`，否则可能导致 SignalR 通讯中断
6. **使用 ValidateForm 集成验证**：将组件放置到 `ValidateForm` 内可以集成自动数据验证功能
7. **设置 MaxFileCount 限制上传数量**：使用 `MaxFileCount` 参数限制最大上传个数（注意：`Max` 参数已弃用）
8. **圆形头像使用 IsCircle**：设置 `IsCircle="true"` 可使头像显示为圆形，适合头像上传场景

---

## 常见问题

### 1. 上传大文件时出现 SignalR 通讯中断？

**问题**：上传文件过大，可能会触发 SignalR 通讯中断问题。

**解决方案**：调整 `HubOptions` 配置，设置 `MaximumReceiveMessageSize` 为 `null` 或更大的值。

```csharp
// Program.cs 或 Startup.cs
builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);
```

### 2. Accept 属性是否安全？

**回答**：`Accept` 属性并不安全，只是客户端过滤。必须在服务器端进行文件格式验证，以防止恶意文件上传。

### 3. IsSingle 参数已弃用，应该用什么？

**回答**：`IsSingle` 参数已弃用，请使用 `IsMultiple` 参数。`IsMultiple="false"` 等价于原来的 `IsSingle="true"`。

### 4. Max 参数已弃用，应该用什么？

**回答**：`Max` 参数已弃用，请使用 `MaxFileCount` 参数来限制最大上传个数。

### 5. 如何显示上传进度？

**回答**：设置 `ShowProgress="true"` 即可显示上传进度条。
