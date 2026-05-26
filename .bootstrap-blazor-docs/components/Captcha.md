# Captcha 滑块验证码

## 概述

`Captcha` 是一个滑块验证码组件，通过拖动滑块进行人机识别。适用于需要在网页中进行人机验证、防止机器人自动提交等场景。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/captcha](https://www.blazor.zone/captcha)

## 使用场景

### 1. 基础功能

进行简单的人机识别。用户需要拖动滑块完成拼图验证。

```razor
<Captcha OnValidAsync="OnValidAsync" />

@code {
    private async Task OnValidAsync(bool success)
    {
        if (success)
        {
            // 验证成功
            await ToastService.Success("验证成功！");
        }
        else
        {
            // 验证失败
            await ToastService.Error("验证失败，请重试！");
        }
    }
}
```

**说明**:
- 用户拖动滑块完成拼图验证
- 验证结果通过 `OnValidAsync` 回调返回
- 成功时 `success = true`，失败时 `success = false`

### 2. 指定图床路径与名称

通过 `ImagesPath` 和 `ImagesName` 参数指定验证码背景图片的路径和名称。

```razor
<Captcha ImagesPath="images/captcha" 
           ImagesName="CaptchaBg.jpg" 
           OnValidAsync="OnValidAsync" />
```

**说明**:
- `ImagesPath` 默认值：`"images"` - 图片所在文件夹路径
- `ImagesName` 默认值：`"Pic.jpg"` - 图片文件名
- 组件会随机从指定路径加载图片作为验证码背景

### 3. 指定图床委托方法

通过 `GetImageName` 参数设置自定义方法拼接随机图片全路径名称。

```razor
<Captcha GetImageName="GetRandomImageName" OnValidAsync="OnValidAsync" />

@code {
    private string GetRandomImageName()
    {
        // 自定义逻辑：从数据库或API获取随机图片名称
        var imageNames = new[] { "img1.jpg", "img2.jpg", "img3.jpg" };
        var randomIndex = new Random().Next(imageNames.Length);
        return $"/images/captcha/{imageNames[randomIndex]}";
    }
}
```

**说明**:
- `GetImageName` 是 `Func<string>` 类型
- 可以自定义图片选择逻辑（如从数据库、API、云存储获取）
- 返回图片的完整路径或URL

### 4. 自定义显示文本

通过 `HeaderText`、`BarText`、`FailedText`、`LoadText` 参数自定义显示文本。

```razor
<Captcha HeaderText="安全验证" 
           BarText="拖动滑块完成拼图" 
           FailedText="验证失败，请重试" 
           LoadText="加载中..." 
           OnValidAsync="OnValidAsync" />
```

**说明**:
- `HeaderText` - 头部显示文本（默认"请完成安全验证"）
- `BarText` - 滑块条显示文本（默认"向右滑动填充拼图"）
- `FailedText` - 验证失败文本（默认"验证失败，请重试"）
- `LoadText` - 加载中文本（默认"正在加载..."）

## 参数

### Captcha 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `BarIcon` | 获得/设置 滑块图标，默认值 `fa-solid fa-arrow-right` | `string` | `fa-solid fa-arrow-right` |
| `BarText` | 获得/设置 滑块条显示文本 | `string` | - |
| `Diameter` | 获得/设置 拼图直径 | `int` | `9` |
| `FailedText` | 获得/设置 验证失败显示文本 | `string` | - |
| `GetImageName` | 获得/设置 获取背景图方法委托 | `Func<string>` | `null` |
| `HeaderText` | 获得/设置 头部显示文本 | `string` | - |
| `Height` | 获得/设置 图片高度 | `int` | `155` |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `ImagesName` | 获得/设置 图片名称，默认值为 `Pic.jpg` | `string` | `Pic.jpg` |
| `ImagesPath` | 获得/设置 图片路径，默认值为 `images` | `string` | `images` |
| `LoadText` | 获得/设置 加载中显示文本 | `string` | - |
| `Max` | 获得/设置 随机图片最大张数，默认 `1024` | `int` | `1024` |
| `Offset` | 获得/设置 容错偏差 | `int` | `5` |
| `RefreshIcon` | 获得/设置 刷新按钮图标，默认值 `fa-solid fa-arrows-rotate` | `string` | `fa-solid fa-arrows-rotate` |
| `SideLength` | 获得/设置 拼图边长 | `int` | `42` |
| `Width` | 获得/设置 图片宽度 | `int` | `280` |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `OnValidAsync` | 获得/设置 验证码结果回调委托 | `Func<bool, Task>` |

## 最佳实践

### 1. 验证成功后执行操作

在 `OnValidAsync` 回调中，根据验证结果执行相应操作。

```razor
<Captcha OnValidAsync="OnCaptchaValid" />

@code {
    private async Task OnCaptchaValid(bool success)
    {
        if (success)
        {
            // 验证成功：允许提交表单
            IsCaptchaVerified = true;
            await ToastService.Success("验证成功！");
        }
        else
        {
            // 验证失败：禁止提交，刷新验证码
            IsCaptchaVerified = false;
            await ToastService.Error("验证失败，请重试！");
        }
    }

    private bool IsCaptchaVerified { get; set; }
}
```

### 2. 配合表单使用

将 Captcha 组件与表单配合使用，确保用户完成验证后才能提交。

```razor
<EditForm Model="Model" OnValidSubmit="OnValidSubmit">
    <DataAnnotationsValidator />
    
    <div class="mb-3">
        <label>用户名</label>
        <InputText @bind-Value="Model.UserName" class="form-control" />
        <ValidationMessage For="() => Model.UserName" />
    </div>
    
    <div class="mb-3">
        <label>验证码</label>
        <Captcha OnValidAsync="OnCaptchaValid" />
        @if (!IsCaptchaVerified)
        {
            <div class="text-danger">请完成验证码验证</div>
        }
    </div>
    
    <button type="submit" class="btn btn-primary" disabled="@(!IsCaptchaVerified)">
        提交
    </button>
</EditForm>

@code {
    private MyModel Model { get; set; } = new();
    private bool IsCaptchaVerified { get; set; }

    private async Task OnCaptchaValid(bool success)
    {
        IsCaptchaVerified = success;
    }

    private async Task OnValidSubmit()
    {
        // 表单提交逻辑
        await ToastService.Success("表单提交成功！");
    }
}
```

### 3. 自定义图片源

通过 `GetImageName` 从数据库或API动态获取验证码背景图片。

```razor
<Captcha GetImageName="GetCaptchaImage" OnValidAsync="OnValidAsync" />

@code {
    private async Task<string> GetCaptchaImage()
    {
        // 从API获取随机验证码图片URL
        var imageUrl = await Http.GetStringAsync("api/captcha/get-image");
        return imageUrl;
    }

    private async Task OnValidAsync(bool success)
    {
        // 验证结果回调
        if (success)
        {
            await ToastService.Success("验证成功！");
        }
    }
}
```

### 4. 调整拼图难度

通过 `Offset`、`SideLength`、`Diameter` 参数调整拼图难度。

```razor
<!-- 简单难度：容错偏差大 -->
<Captcha Offset="10" SideLength="50" Diameter="12" />

<!-- 中等难度：默认设置 -->
<Captcha Offset="5" SideLength="42" Diameter="9" />

<!-- 困难难度：容错偏差小 -->
<Captcha Offset="2" SideLength="35" Diameter="6" />
```

**说明**:
- `Offset` - 容错偏差（默认5像素），值越大越容易通过
- `SideLength` - 拼图边长（默认42像素），值越小拼图越小越难
- `Diameter` - 拼图直径（默认9像素），值越小拼图边缘越平滑

## 常见问题

### 1. 验证码图片不显示

**问题**: 验证码区域显示，但背景图片不显示。

**原因**: 可能是 `ImagesPath` 或 `ImagesName` 设置不正确，或者图片文件不存在。

**解决方案**:
- 检查 `ImagesPath` 路径是否正确（相对于 wwwroot）
- 检查图片文件是否存在于指定路径
- 使用浏览器开发者工具查看网络请求，确认图片URL是否正确

```razor
<!-- 错误：路径不正确 -->
<Captcha ImagesPath="image" />  <!-- 应为 "images" -->

<!-- 正确：路径正确 -->
<Captcha ImagesPath="images" ImagesName="captcha-bg.jpg" />
```

### 2. 验证始终失败

**问题**: 用户拼图位置正确，但验证始终返回失败。

**原因**: 可能是 `Offset` 容错偏差设置过小，或者服务器端验证逻辑有误。

**解决方案**:
- 增大 `Offset` 容错偏差值
- 检查服务器端验证日志
- 使用浏览器开发者工具查看验证请求和响应

```razor
<!-- 增大容错偏差 -->
<Captcha Offset="10" OnValidAsync="OnValidAsync" />
```

### 3. 自定义图片不生效

**问题**: 设置了 `GetImageName` 但验证码仍使用默认图片。

**原因**: 可能是 `GetImageName` 委托未正确绑定，或者返回的路径不正确。

**解决方案**:
- 确保 `GetImageName` 返回有效的图片路径或URL
- 在委托方法中添加日志输出，确认方法被调用

```razor
<Captcha GetImageName="GetImageName" />

@code {
    private string GetImageName()
    {
        Console.WriteLine("GetImageName called");
        return "/images/custom-captcha.jpg";  // 确保路径正确
    }
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | Captcha 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 `GetImageName` 委托；优化验证逻辑 |
| 8.0.0 | 2024-11-10 | 新增 `BarIcon`、`RefreshIcon` 参数；支持自定义图标 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Captcha](https://www.blazor.zone/captcha)
- [Bootstrap Blazor API - Captcha](https://www.blazor.zone/api/Captcha)
- [CSDN - 滑块验证码原理](https://blog.csdn.net/slider_captcha) (滑块验证码实现原理)
