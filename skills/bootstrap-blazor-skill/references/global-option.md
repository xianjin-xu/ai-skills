# Bootstrap Blazor 全局配置指南

## 概述

`BootstrapBlazorOptions` 是 Bootstrap Blazor 的全局配置类，通过 `AddBootstrapBlazor` 注册时设置，影响所有组件的默认行为。

**官方文档**: https://www.blazor.zone/global-option

---

## 配置方式

### 代码配置

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    // 在此配置各项参数
    opts.DefaultCultureInfo = "zh-CN";
});
```

### JSON 配置（appsettings.json）

```json
{
    "BootstrapBlazorOptions": {
        "DefaultCultureInfo": "zh-CN",
        "IsPopover": true,
        "TableSettings": {
            "ShowSearch": true
        }
    }
}
```

---

## 核心选项

### 通用配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `DefaultCultureInfo` | `string?` | `null` | 默认文化信息。WASM 模式必须显式设置，否则默认为 `en` |
| `FallbackCulture` | `string` | `"en"` | 本地化回退默认语言文化 |
| `EnableFallbackCulture` | `bool` | `true` | 是否启用本地化回退机制 |
| `JSModuleVersion` | `string?` | `null` | JavaScript 模块脚本版本号，用于缓存控制 |
| `DisableAutoSubmitFormByEnter` | `bool?` | `null` | 是否禁用按 Enter 自动提交表单 |
| `IsPopover` | `bool` | `false` | 是否将 Select 等组件的 `IsPopover` 参数默认值改为 `true`（解决 Dialog 内下拉框被遮挡问题） |
| `IsMemorialMode` | `bool` | `false` | 是否启用网站纪念模式 |
| `ChangeDetectionTaskInterval` | `int` | `5000` | 组件变更检测后台服务执行间隔（毫秒） |

### 延时配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `ToastDelay` | `int` | `0` | Toast 组件默认自动关闭延时（毫秒），0 表示不自动关闭 |
| `MessageDelay` | `int` | `0` | Message 组件默认自动关闭延时（毫秒） |
| `SwalDelay` | `int` | `0` | SweetAlert 组件默认自动关闭延时（毫秒） |

### 错误日志配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `EnableErrorLogger` | `bool` | `true` | 是否启用全局异常捕获 |
| `ShowErrorLoggerToast` | `bool` | `true` | 全局异常捕获时是否显示 Toast 弹窗 |
| `EnableErrorLoggerILogger` | `bool` | `true` | 是否启用基于 `ILogger` 的错误日志记录 |

### 本地化配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `SupportedCultures` | `List<string>?` | `null` | 组件内置本地化语言列表，null 时默认为 `["en", "zh"]` |
| `IgnoreLocalizerMissing` | `bool?` | `null` | 是否忽略缺失文化的日志信息 |
| `DisableGetLocalizerFromService` | `bool?` | `false` | 是否禁用从服务获取本地化资源 |
| `DisableGetLocalizerFromResourceManager` | `bool?` | `false` | 是否禁用从 ResourceManager 获取本地化资源 |

---

## 子配置项

### TableSettings（表格全局设置）

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.TableSettings.CheckboxColumnWidth = 36;
    opts.TableSettings.ShowSearch = true;
});
```

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `CheckboxColumnWidth` | `int` | `36` | 复选框列宽度 |
| `CheckboxColumnCompactWidth` | `int` | `28` | 复选框列紧凑模式宽度 |
| `DetailColumnWidth` | `int` | `24` | 明细行 Row Header 宽度 |
| `ShowCheckboxTextColumnWidth` | `int` | `80` | 显示文字的复选框列宽度 |
| `LineNoColumnWidth` | `int` | `60` | 行号列宽度 |
| `ColumnMinWidth` | `int` | `64` | 列最小宽度 |
| `TableRenderMode` | `TableRenderMode?` | `null` | 表格渲染模式 |
| `TableExportOptions` | `TableExportOptions` | `new()` | 表格导出 Excel 配置 |

#### TableExportOptions（表格导出配置）

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `EnableFormat` | `bool` | `true` | 是否使用 FormatString/Formatter 格式化值 |
| `EnableLookup` | `bool` | `true` | 是否使用 Lookup 映射值 |
| `AutoMergeArray` | `bool` | `true` | 是否合并数组类型值 |
| `UseEnumDescription` | `bool` | `true` | 枚举类型是否使用 Description 特性 |
| `ArrayDelimiter` | `string` | `","` | 数组合并分隔符 |
| `EnableAutoFilter` | `bool` | `true` | 是否启用 Excel 自动筛选 |
| `EnableAutoWidth` | `bool` | `false` | 是否启用 Excel 自动列宽 |

### EditDialogSettings（编辑弹窗设置）

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.EditDialogSettings.ShowCloseConfirm = true; // 关闭未保存弹窗时显示确认
});
```

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `ShowCloseConfirm` | `bool?` | `null` | 关闭编辑弹窗时是否显示未保存确认提示 |

### ModalSettings（模态框设置）

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.ModalSettings.IsFade = true; // 启用淡入淡出动画
});
```

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `IsFade` | `bool?` | `null` | 是否启用淡入淡出动画 |

### StepSettings（步骤条/数字输入步长设置）

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.StepSettings.Int = "1";      // int 类型步长
    opts.StepSettings.Decimal = "0.1"; // decimal 类型步长
    opts.StepSettings.Double = "0.01"; // double 类型步长
});
```

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `SByte` | `string?` | `null` | sbyte 步长 |
| `Byte` | `string?` | `null` | byte 步长 |
| `Short` | `string?` | `null` | short 步长 |
| `UShort` | `string?` | `null` | ushort 步长 |
| `Int` | `string?` | `null` | int 步长 |
| `UInt` | `string?` | `null` | uint 步长 |
| `Long` | `string?` | `null` | long 步长 |
| `ULong` | `string?` | `null` | ulong 步长 |
| `Float` | `string?` | `null` | float 步长 |
| `Double` | `string?` | `null` | double 步长 |
| `Decimal` | `string?` | `null` | decimal 步长 |

---

## 完整配置示例

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    // 本地化
    opts.DefaultCultureInfo = "zh-CN";
    opts.FallbackCulture = "en";

    // 延时
    opts.ToastDelay = 5000;
    opts.MessageDelay = 3000;

    // 全局行为
    opts.IsPopover = true;                              // 解决 Dialog 内下拉框遮挡
    opts.DisableAutoSubmitFormByEnter = true;            // 禁用 Enter 提交表单
    opts.ShowErrorLoggerToast = false;                   // 关闭异常 Toast

    // Table 全局设置
    opts.TableSettings.CheckboxColumnWidth = 40;
    opts.TableSettings.ColumnMinWidth = 80;
    opts.TableSettings.TableExportOptions.EnableAutoWidth = true;

    // EditDialog 设置
    opts.EditDialogSettings.ShowCloseConfirm = true;

    // Modal 设置
    opts.ModalSettings.IsFade = true;

    // Step 数字输入步长
    opts.StepSettings.Decimal = "0.01";
    opts.StepSettings.Double = "0.01";
});
```

---

## 常见场景

### 场景 1：Dialog 内 Select 下拉框被遮挡

```csharp
opts.IsPopover = true; // 全局启用 Popover 模式
```

或在组件上单独设置：`<Select IsPopover="true" ... />`

### 场景 2：Table 导出 Excel 格式优化

```csharp
opts.TableSettings.TableExportOptions = new TableExportOptions
{
    EnableFormat = true,       // 使用格式化值
    EnableLookup = true,       // 使用 Lookup 映射
    UseEnumDescription = true, // 枚举用 Description
    EnableAutoFilter = true,   // 自动筛选
    EnableAutoWidth = false    // 关闭自动列宽（大数据量时可提升性能）
};
```

### 场景 3：多语言项目配置

```csharp
opts.DefaultCultureInfo = "zh-CN";
opts.SupportedCultures = ["zh-CN", "en-US"];
opts.FallbackCulture = "en";
opts.EnableFallbackCulture = true;
```

---

## 参考链接

- 官方文档：https://www.blazor.zone/global-option
- 源码：`src/BootstrapBlazor/Options/BootstrapBlazorOptions.cs`
