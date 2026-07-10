# Bootstrap Blazor 本地化实践指南

## 概述

Bootstrap Blazor 组件内置本地化支持，可将按钮文本、过滤器操作符、表格工具栏等 UI 元素自动转换为所需语言。组件内部使用 `IStringLocalizer` 机制，默认跟随当前请求的 UI 文化语言。

**官方文档**: https://www.blazor.zone/localization

---

## 项目配置

### 1. 注册本地化服务

```csharp
// Program.cs
builder.Services.AddLocalization();

builder.Services.AddBootstrapBlazor(opts =>
{
    opts.DefaultCultureInfo = "zh-CN"; // 设置默认文化
});
```

### 2. 配置请求本地化中间件

```csharp
// Program.cs
var supportedCultures = new[] { "zh-CN", "en-US" };
var localizationOptions = new RequestLocalizationOptions()
    .SetDefaultCulture(supportedCultures[0])
    .AddSupportedCultures(supportedCultures)
    .AddSupportedUICultures(supportedCultures);

app.UseRequestLocalization(localizationOptions);
```

> **注意**：`UseRequestLocalization` 必须在任何可能检查请求区域性的中间件之前调用，通常在 `MapRazorComponents` 之前。

### 3. 完整配置示例（使用 BootstrapBlazor 推荐方式）

```csharp
// Program.cs - 推荐使用 BootstrapBlazor 的集成扩展
builder.Services.AddRequestLocalization<IOptionsMonitor<BootstrapBlazorOptions>>((localizerOption, blazorOption) =>
{
    blazorOption.OnChange(() =>
    {
        var cultures = blazorOption.CurrentValue.GetSupportedCultures();
        localizerOption.SupportedCultures = cultures;
        localizerOption.SupportedUICultures = cultures;
    });
});
```

---

## 资源文件组织

### 文件结构

```
项目根目录/
├── Locales/
│   ├── zh-CN.json    # 中文资源
│   └── en-US.json    # 英文资源
```

Bootstrap Blazor 包自带以下内置资源：
- **中文** (`zh`)
- **英语** (`en`)

额外社区贡献的资源文件（需手动下载）：
- 德语 (`de`)
- 西班牙语 (`es`)
- 葡萄牙语 (`pt`)
- 中国台湾 (`zh-TW`)

### JSON 资源文件格式

```json
// Locales/zh-CN.json
{
    "YourApp.Pages.Index": {
        "Welcome": "欢迎",
        "Submit": "提交"
    },
    "BootstrapBlazor.Components.Table": {
        "AddButtonText": "新增",
        "DeleteButtonText": "删除"
    }
}
```

```json
// Locales/en-US.json
{
    "YourApp.Pages.Index": {
        "Welcome": "Welcome",
        "Submit": "Submit"
    },
    "BootstrapBlazor.Components.Table": {
        "AddButtonText": "Add",
        "DeleteButtonText": "Delete"
    }
}
```

> **键名格式**：`{Namespace}.{ClassName}.{Key}`，组件库内部资源使用 `BootstrapBlazor.Components.{ComponentName}` 格式。

### 在 Razor 组件中注入和使用

```razor
@page "/"
@using Microsoft.Extensions.Localization
@inject IStringLocalizer<Index> Localizer

<h1>@Localizer["Welcome"]</h1>
<Button Text="@Localizer["Submit"]" />
```

### 使用 Display 特性自动获取标签文本

```csharp
public class Foo
{
    [Display(Name = "Name")]
    [Required(ErrorMessage = "名称不能为空")]
    public string Name { get; set; }

    [Display(Name = "Address")]
    public string Address { get; set; }
}
```

```razor
<!-- DisplayText="@null" 时自动从资源文件获取 Display 特性的 Name -->
<BootstrapInput @bind-Value="Foo.Name" ShowLabel="true" DisplayText="@null" />
```

---

## 组件内置文本本地化

Bootstrap Blazor 组件的内置文本（如 Table 的工具栏按钮、筛选器操作符等）使用 `BootstrapBlazor.Components.{ComponentName}` 命名空间的资源键。

### 常用组件资源键示例

| 组件 | 资源键 | 默认值(中文) |
|------|--------|-------------|
| Table | `AddButtonText` | 新增 |
| Table | `DeleteButtonText` | 删除 |
| Table | `EditButtonText` | 编辑 |
| Table | `SearchButtonText` | 搜索 |
| Table | `ResetButtonText` | 重置 |
| ValidateForm | `SubmitButtonText` | 提交 |
| Dialog | `CloseButtonText` | 关闭 |

### 自定义组件内置文本

在资源文件中覆盖组件的默认文本：

```json
// Locales/zh-CN.json
{
    "BootstrapBlazor.Components.Table": {
        "AddButtonText": "新建记录",
        "DeleteButtonText": "移除选中"
    }
}
```

---

## 运行时切换语言

### 方式一：使用 CultureChooser 组件（推荐）

Bootstrap Blazor 内置 `CultureChooser` 组件：

```razor
<CultureChooser />
```

### 方式二：手动切换

```csharp
// 通过 Cookie 设置文化
var culture = new CookieRequestCultureProvider();
HttpContext.Response.Cookies.Append(
    CookieRequestCultureProvider.DefaultCookieName,
    CookieRequestCultureProvider.MakeCookieValue(new RequestCulture(culture)));
```

### 方式三：URL 查询字符串

```razor
<a href="?culture=en-US">English</a>
<a href="?culture=zh-CN">中文</a>
```

---

## 常见陷阱

### 1. WASM 模式下无法获取系统语言

Blazor WebAssembly 模式无法获取系统语言文化信息，默认文化为 `en`。**必须显式配置**默认文化：

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.DefaultCultureInfo = "zh-CN";
});
```

### 2. 资源键找不到时的回退机制

Bootstrap Blazor 的 JSON 本地化支持回落机制：
- 查找 `zh-CN` → 找不到 → 查找 `zh` → 找不到 → 使用 `en`（默认）
- 确保至少提供 `en` 作为兜底语言

### 3. AdditionalJsonFiles 使用相对路径

```csharp
// ❌ 错误：不要使用绝对路径
options.AdditionalJsonFiles = new string[] {
    @"D:\Project\Resources\zh-CN.json"
};

// ✅ 正确：使用相对路径
options.AdditionalJsonFiles = new string[] {
    "Locales/zh-CN.json"
};
```

### 4. 编程式弹窗中的本地化

`DialogService.Show()` 创建的弹窗需要手动传递本地化文本，因为不在 Razor 上下文中：

```csharp
await DialogService.Show(new DialogOption()
{
    Title = Localizer["EditTitle"], // 必须在调用前注入 Localizer
    BodyTemplate = builder => { /* ... */ }
});
```

---

## 参考链接

- 官方文档：https://www.blazor.zone/localization
- ASP.NET Core 本地化：https://learn.microsoft.com/zh-cn/aspnet/core/blazor/globalization-localization
