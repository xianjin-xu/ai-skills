# Camera 摄像头拍照组件

## 概述

`Camera` 是一个摄像头拍照组件，通过调用摄像头进行拍照操作。适用于需要在网页中调用摄像头拍照、上传照片等场景。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/camera](https://www.blazor.zone/camera)

> **特别注意**：站点要启用 HTTPS，这是浏览器厂商要求的。

## 使用场景

### 1. 基础用法

通过摄像头进行拍照。操作步骤：点击"开启"打开摄像头，点击"拍照"按钮拍照，点击"关闭"按钮关闭摄像头。

```razor
<Camera @ref="Camera" OnClose="OnClose" OnOpen="OnOpen" />

<Button Text="开启" OnClick="() => Camera.Start()" />
<Button Text="关闭" OnClick="() => Camera.Stop()" />
<Button Text="拍照" OnClick="() => Camera.Capture()" />
<Button Text="保存" OnClick="() => Camera.Save()" />

@code {
    private Camera? Camera { get; set; }

    private Task OnOpen()
    {
        Console.WriteLine("摄像头已开启");
        return Task.CompletedTask;
    }

    private Task OnClose()
    {
        Console.WriteLine("摄像头已关闭");
        return Task.CompletedTask;
    }
}
```

**说明**:
- 点击"开启"按钮打开摄像头（调用 `Start()` 方法）
- 点击"拍照"按钮拍照（调用 `Capture()` 方法）
- 点击"关闭"按钮关闭摄像头（调用 `Stop()` 方法）
- 点击"保存"按钮保存照片（调用 `Save()` 方法）

### 2. 自动开启摄像头

通过设置 `AutoStart="true"` 参数，页面加载后自动开启摄像头。

```razor
<Camera AutoStart="true" OnOpen="OnOpen" />

@code {
    private Task OnOpen()
    {
        Console.WriteLine("摄像头已自动开启");
        return Task.CompletedTask;
    }
}
```

**说明**:
- `AutoStart="true"` - 页面加载后自动开启摄像头
- `AutoStart="false"`（默认值）- 需要手动点击"开启"按钮

### 3. 设置摄像头分辨率

通过 `VideoWidth` 和 `VideoHeight` 参数设置摄像头视频的宽度和高度。

```razor
<Camera VideoWidth="640" VideoHeight="480" />

<!-- 常见分辨率 -->
<Camera VideoWidth="320" VideoHeight="240" />   <!-- QVGA -->
<Camera VideoWidth="640" VideoHeight="480" />   <!-- VGA -->
<Camera VideoWidth="800" VideoHeight="600" />   <!-- HD -->
<Camera VideoWidth="1280" VideoHeight="720" />  <!-- Full HD -->
<Camera VideoWidth="1920" VideoHeight="1080" /> <!-- Television -->
<Camera VideoWidth="3840" VideoHeight="2160" /> <!-- 4K -->
```

**说明**:
- `VideoWidth` 默认值：320
- `VideoHeight` 默认值：240
- 分辨率越高，图像越清晰，但性能消耗也越大

### 4. 设置拍照格式和质量

通过 `CaptureJpeg` 参数设置拍照格式为 JPEG（默认为 PNG 格式），通过 `Quality` 参数设置图像质量。

```razor
<Camera CaptureJpeg="true" Quality="0.8f" />
```

**说明**:
- `CaptureJpeg="false"`（默认值）- 使用 PNG 格式
- `CaptureJpeg="true"` - 使用 JPEG 格式
- `Quality="0.9f"`（默认值）- 图像质量 90%
- `Quality` 范围：0.1f - 1.0f（10% - 100%）

### 5. 选择摄像头设备

通过 `DeviceId` 参数设置当前使用的摄像头设备 ID。

```razor
<Camera @ref="Camera" OnInit="OnInit" />

@code {
    private Camera? Camera { get; set; }
    private List<DeviceItem> Devices { get; set; } = new();

    private async Task OnInit(List<DeviceItem> devices)
    {
        Devices = devices;
        
        // 选择第一个摄像头
        if (Devices.Any())
        {
            Camera.DeviceId = Devices.First().DeviceId;
            await Camera.RestartAsync();
        }
    }
}
```

**说明**:
- `OnInit` 回调返回可用的摄像头设备列表
- 可以通过 `DeviceId` 切换不同的摄像头（如前置/后置摄像头）
- 切换后需要调用 `RestartAsync()` 重启摄像头

## 参数

### Camera 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `AutoStart` | 获得/设置 是否自动开启摄像头，默认为 `false` | `bool` | `false` |
| `CaptureJpeg` | 获得/设置 拍照格式为 JPEG，默认为 `false` 使用 PNG 格式 | `bool` | `false` |
| `DeviceId` | 获得/设置 当前设备 ID，默认 `null` | `string` | `null` |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `Quality` | 获得/设置 图像质量，默认为 `0.9f` | `float` | `0.9f` |
| `VideoWidth` | 获得/设置 摄像头视频宽度，默认 `320` | `int?` | `320` |
| `VideoHeight` | 获得/设置 摄像头视频高度，默认 `240` | `int?` | `240` |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `OnInit` | 获得/设置 初始化摄像头回调方法，返回设备列表 | `Func<List<DeviceItem>, Task>` |
| `OnOpen` | 获得/设置 打开摄像头回调方法 | `Func<Task>` |
| `OnClose` | 获得/设置 关闭摄像头回调方法 | `Func<Task>` |
| `OnError` | 获得/设置 拍照出错回调方法 | `Func<string, Task>` |

## 方法

| 方法 | 说明 |
|------|------|
| `Start()` | 开启摄像头 |
| `Stop()` | 关闭摄像头 |
| `Capture()` | 拍照 |
| `Save()` | 保存照片 |
| `RestartAsync()` | 重启摄像头（切换设备后调用） |

## 最佳实践

### 1. 使用 @ref 获取组件引用

Camera 组件通常通过 `@ref` 获取引用，然后调用 `Start()`、`Stop()`、`Capture()`、`Save()` 等方法。

```razor
<Camera @ref="MyCamera" />

<Button Text="开启" OnClick="() => MyCamera.Start()" />
<Button Text="关闭" OnClick="() => MyCamera.Stop()" />
<Button Text="拍照" OnClick="() => MyCamera.Capture()" />
<Button Text="保存" OnClick="() => MyCamera.Save()" />

@code {
    private Camera? MyCamera { get; set; }
}
```

### 2. 处理摄像头权限

浏览器会请求摄像头权限，需要在代码中处理用户拒绝权限的情况。

```razor
<Camera @ref="Camera" OnError="OnError" />

@code {
    private async Task OnError(string errorMsg)
    {
        // 处理错误：用户拒绝权限、摄像头被占用等
        await ToastService.Error(errorMsg);
    }
}
```

### 3. 选择合适的分辨率

根据使用场景选择合适的分辨率，平衡清晰度和性能。

```razor
<!-- 场景 1：头像上传 - 使用较低分辨率 -->
<Camera VideoWidth="320" VideoHeight="240" CaptureJpeg="true" Quality="0.7f" />

<!-- 场景 2：证件照上传 - 使用较高分辨率 -->
<Camera VideoWidth="1280" VideoHeight="720" CaptureJpeg="true" Quality="0.9f" />

<!-- 场景 3：文档拍照 - 使用高分辨率 -->
<Camera VideoWidth="1920" VideoHeight="1080" CaptureJpeg="true" Quality="0.95f" />
```

### 4. 保存照片到服务器

拍照后通常需要将照片保存到服务器。

```razor
<Camera @ref="Camera" OnClose="OnClose" />

<Button Text="拍照并上传" OnClick="CaptureAndUpload" />

@code {
    private Camera? Camera { get; set; }

    private async Task CaptureAndUpload()
    {
        // 1. 拍照
        Camera?.Capture();
        
        // 2. 获取照片数据（假设通过 JS 互操作获取）
        var imageData = await JSRuntime.InvokeAsync<string>("getCameraImage");
        
        // 3. 上传到服务器
        await ImageService.UploadAsync(imageData);
        
        // 4. 提示用户
        await ToastService.Success("照片已上传");
    }
}
```

## 常见问题

### 1. 摄像头无法开启

**问题**: 点击"开启"按钮后，摄像头无法开启，或浏览器提示权限错误。

**原因**: 
- 网站未启用 HTTPS（浏览器要求 HTTPS）
- 用户拒绝了摄像头权限
- 摄像头被其他程序占用

**解决方案**:
- 确保网站使用 HTTPS 协议（检查地址栏是否显示🔒图标）
- 检查浏览器权限设置，允许该网站使用摄像头
- 关闭其他可能占用摄像头的程序（如微信、QQ 等）

```razor
<Camera OnError="OnError" />

@code {
    private async Task OnError(string error)
    {
        // 输出详细错误信息
        Console.WriteLine($"摄像头错误: {error}");
        await ToastService.Error($"摄像头错误: {error}");
    }
}
```

### 2. 拍照后无法保存

**问题**: 点击"拍照"按钮后，照片无法保存或上传。

**原因**: 可能是未正确获取照片数据，或者保存逻辑有误。

**解决方案**:
- 确保先调用 `Capture()` 拍照，再调用 `Save()` 保存
- 检查 JS 互操作代码是否正确获取照片数据
- 检查服务器端接收逻辑

```razor
<!-- 正确的拍照和保存顺序 -->
<Button Text="拍照" OnClick="() => Camera.Capture()" />
<Button Text="保存" OnClick="() => Camera.Save()" />  <!-- 先拍照，再保存 -->
```

### 3. 切换摄像头无效

**问题**: 设置 `DeviceId` 后，摄像头没有切换。

**原因**: 可能是未调用 `RestartAsync()` 重启摄像头。

**解决方案**: 切换 `DeviceId` 后，必须调用 `RestartAsync()` 重启摄像头。

```razor
<Camera @ref="Camera" OnInit="OnInit" />

@code {
    private Camera? Camera { get; set; }

    private async Task SwitchCamera(string deviceId)
    {
        Camera.DeviceId = deviceId;  // 1. 设置设备 ID
        await Camera.RestartAsync();    // 2. 重启摄像头（重要！）
    }
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | Camera 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 `OnError` 回调；优化设备选择逻辑 |
| 8.0.0 | 2024-11-10 | 新增 `Quality` 参数；支持 4K/8K 分辨率 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Camera](https://www.blazor.zone/camera)
- [Bootstrap Blazor API - Camera](https://www.blazor.zone/api/Camera)
- [MDN Web Docs - MediaDevices.getUserMedia()](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) (浏览器摄像头 API)
