# UniverSheet (电子表格)

## 概述

`UniverSheet` 组件用于**封装开源办公套件 Univer 的核心电子表格组件，提供高性能、可扩展的在线表格解决方案**。组件支持数据推送、工具栏样式设置、暗黑模式、自定义插件等功能。

**主要特性**：
- 封装 Univer 核心电子表格功能
- 支持通过 `PushDataAsync` 方法推送数据到电子表格
- 支持工具栏样式设置（`RibbonType`）
- 支持暗黑模式（`IsDarkMode`）
- 支持自定义插件（`Plugins`）
- 支持数据回调（`OnPostDataAsync`）
- 支持页面加载完毕回调（`OnReadyAsync`）
- 支持主题颜色设置（`Theme`）
- 支持多语言（`Lang`）

**依赖说明**：本组件依赖于 `BootstrapBlazor.UniverSheet`，使用本组件时需要引用其组件包。

**在线演示**: https://www.blazor.zone/universe-sheet

---

## 安装 Nuget 包

使用 nuget.org 进行 `BootstrapBlazor.UniverSheet` 组件的安装：

### .NET CLI

```bash
dotnet add package BootstrapBlazor.UniverSheet
```

### PackageReference

```xml
<PackageReference Include="BootstrapBlazor.UniverSheet" Version="10.0.11" />
```

### Package Manager

```powershell
Install-Package BootstrapBlazor.UniverSheet
```

---

## 使用场景

### 1. 基础用法（简单电子表格）

通过调用实例方法 `PushDataAsync` 推送数据到电子表格。点击"推送数据"按钮主动将数据推送给表格，点击"保存数据"按钮获得表格数据序列化的数据。

```razor
<!-- 基础电子表格 -->
<UniverSheet @ref="UniverSheetRef" OnPostDataAsync="OnPostDataAsync" />

<Button OnClick="PushData">推送数据</Button>
<Button OnClick="SaveData">保存数据</Button>

@code {
    private UniverSheet UniverSheetRef { get; set; }
    
    private async Task PushData()
    {
        // 推送数据到电子表格
        var data = new UniverSheetData
        {
            // 设置数据
        };
        await UniverSheetRef.PushDataAsync(data);
    }
    
    private async Task<UniverSheetData> OnPostDataAsync(UniverSheetData data)
    {
        // 处理从表格回传的数据
        return data;
    }
    
    private async Task SaveData()
    {
        // 保存数据
        // 通过调用相关方法获取表格数据
    }
}
```

---

### 2. 设置工具栏样式（RibbonType）

通过参数 `RibbonType` 设置工具栏样式。

```razor
<!-- 设置工具栏样式 -->
<UniverSheet RibbonType="UniverSheetRibbonType.Default" />

@code {
    // UniverSheetRibbonType 枚举值：
    // - Default: 默认样式
    // - 其他样式请参考官方文档
}
```

---

### 3. 暗黑模式（IsDarkMode）

通过参数 `IsDarkMode` 控制组件是否使用暗黑模式。

```razor
<!-- 启用暗黑模式 -->
<UniverSheet IsDarkMode="true" />

<!-- 自动模式（默认） -->
<UniverSheet IsDarkMode="null" />
```

---

### 4. 自定义插件（Plugins）

通过设置 `Plugins` 参数设置自己的插件。

```razor
<!-- 自定义插件 -->
<UniverSheet Plugins="CustomPlugins" />

@code {
    private Dictionary<string, string> CustomPlugins { get; set; } = new Dictionary<string, string>
    {
        { "plugin1", "path/to/plugin1.js" },
        { "plugin2", "path/to/plugin2.js" }
    };
}
```

---

### 5. 页面加载完毕回调（OnReadyAsync）

通过 `OnReadyAsync` 参数设置页面加载完毕后回调方法。

```razor
<!-- 页面加载完毕回调 -->
<UniverSheet OnReadyAsync="OnSheetReady" />

@code {
    private async Task OnSheetReady()
    {
        // 页面加载完毕后的处理
        // 例如：自动推送数据
        await PushData();
    }
}
```

---

### 6. 数据回调（OnPostDataAsync）

通过 `OnPostDataAsync` 参数设置 UniverSheet 数据回调方法（一般由 Excel 按钮触发）。

```razor
<!-- 数据回调 -->
<UniverSheet OnPostDataAsync="OnPostDataAsync" />

@code {
    private async Task<UniverSheetData> OnPostDataAsync(UniverSheetData data)
    {
        // 处理从表格回传的数据
        // 可以对数据进行验证、转换等操作
        return data;
    }
}
```

---

### 7. 设置主题颜色（Theme）

通过 `Theme` 参数设置主题颜色。

```razor
<!-- 设置绿色主题 -->
<UniverSheet Theme="greenTheme" />
```

---

### 8. 设置语言（Lang）

通过 `Lang` 参数设置语言。

```razor
<!-- 设置中文 -->
<UniverSheet Lang="zh-CN" />

<!-- 设置英文 -->
<UniverSheet Lang="en-US" />
```

---

### 9. 显示加载遮罩（ShowLoading）

通过 `ShowLoading` 参数控制是否显示加载遮罩，默认为 `true`。

```razor
<!-- 不显示加载遮罩 -->
<UniverSheet ShowLoading="false" />
```

---

### 10. 自定义加载文本（LoadingText）

通过 `LoadingText` 参数设置正在加载显示文本。

```razor
<!-- 自定义加载文本 -->
<UniverSheet LoadingText="正在加载电子表格，请稍候..." />
```

---

## 参数 (Parameters)

### UniverSheet 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `Data` | `UniverSheetData?` | `null` | 获得/设置 需要传递的数据 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsDarkMode` | `bool?` | `null` | 获得/设置 是否为暗黑模式 默认 null 未设置 自动 |
| `Lang` | `string?` | `null` | 获得/设置 语言 默认 null 未设置 |
| `LoadingText` | `string?` | `null` | 获得/设置 正在加载显示文本 默认 null 未设置读取资源文件 |
| `OnPostDataAsync` | `Func<UniverSheetData, Task<UniverSheetData>>?` | `null` | 获得/设置 UniverSheet 数据回调方法（一般由 Excel 按钮触发） |
| `OnReadyAsync` | `Func<Task>?` | `null` | 获得/设置 页面加载完毕后回调方法 |
| `Plugins` | `Dictionary<string, string>?` | `null` | 获得/设置 插件集合 默认 null 未设置 |
| `RibbonType` | `UniverSheetRibbonType` | `UniverSheetRibbonType.Default` | 获得/设置 工具栏样式 默认 default 未设置 |
| `ShowLoading` | `bool` | `true` | 获得/设置 是否显示加载遮罩 默认 true 显示遮罩 |
| `Theme` | `string?` | `null` | 获得/设置 主题颜色 默认 null 未设置 可设置为 greenTheme |

---

## 方法 (Methods)

### UniverSheet 组件方法

| 方法名 | 返回类型 | 说明 |
|--------|----------|------|
| `PushDataAsync(UniverSheetData data)` | `Task` | 推送数据到电子表格 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnPostDataAsync` | `Func<UniverSheetData, Task<UniverSheetData>>?` | UniverSheet 数据回调方法（一般由 Excel 按钮触发） |
| `OnReadyAsync` | `Func<Task>?` | 页面加载完毕后回调方法 |

---

## 最佳实践

1. **安装依赖包**：使用 `UniverSheet` 组件前，必须先安装 `BootstrapBlazor.UniverSheet` Nuget 包
2. **推送数据**：通过 `PushDataAsync` 方法推送数据到电子表格，适合动态更新表格数据的场景
3. **数据回调处理**：使用 `OnPostDataAsync` 处理从表格回传的数据，例如数据验证、转换等
4. **页面加载完毕处理**：使用 `OnReadyAsync` 在页面加载完毕后执行初始化操作，例如自动推送数据
5. **自定义插件**：通过 `Plugins` 参数可以扩展 UniverSheet 的功能，添加自定义插件
6. **暗黑模式适配**：根据应用程序的主题设置 `IsDarkMode` 参数，提供更好的用户体验
7. **加载遮罩控制**：对于快速加载的场景，可以设置 `ShowLoading="false"` 禁用加载遮罩
8. **多语言支持**：通过 `Lang` 参数设置组件语言，支持国际化需求

---

## 常见问题

### 1. 使用 UniverSheet 组件需要安装什么包？

**回答**：使用 `UniverSheet` 组件需要安装 `BootstrapBlazor.UniverSheet` Nuget 包。可以通过 .NET CLI、PackageReference 或 Package Manager 安装。

### 2. 如何推送数据到电子表格？

**回答**：通过调用 `UniverSheet` 组件的实例方法 `PushDataAsync(UniverSheetData data)` 推送数据到电子表格。

### 3. 如何处理从表格回传的数据？

**回答**：通过 `OnPostDataAsync` 参数设置数据回调方法，该方法会在 Excel 按钮触发时被调用，可以在其中处理回传的数据。

### 4. 如何设置暗黑模式？

**回答**：设置 `IsDarkMode="true"` 启用暗黑模式，设置 `IsDarkMode="false"` 禁用暗黑模式，设置 `IsDarkMode="null"`（默认）自动跟随系统。

### 5. 如何自定义工具栏样式？

**回答**：通过 `RibbonType` 参数设置工具栏样式，例如 `RibbonType="UniverSheetRibbonType.Default"`。

### 6. 如何添加自定义插件？

**回答**：通过 `Plugins` 参数设置插件集合，类型为 `Dictionary<string, string>`，键为插件名称，值为插件路径。

### 7. 如何设置主题颜色？

**回答**：通过 `Theme` 参数设置主题颜色，例如 `Theme="greenTheme"`。

### 8. 如何设置组件语言？

**回答**：通过 `Lang` 参数设置语言，例如 `Lang="zh-CN"` 表示中文，`Lang="en-US"` 表示英文。
