# Input (输入框)

## 概述

Input 组件是 Bootstrap Blazor 中最基础、最常用的表单输入组件。它支持文本、密码、数字等多种输入类型，并提供数据绑定、验证、格式化等功能。

**主要功能特性**：
- 支持多种输入类型（text、password、email、number、tel 等）
- 支持双向数据绑定（`@bind-Value`）
- 支持泛型绑定（TValue）
- 支持数据验证（客户端验证）
- 支持格式化显示（`FormatString`、`Formatter`）
- 支持清除按钮（`IsClearable`）
- 支持自动获取焦点（`IsAutoFocus`）
- 支持文本选择（`IsSelectAllTextOnFocus`、`IsSelectAllTextOnEnter`）
- 支持修剪空白（`IsTrim`）
- 支持键盘事件（`OnEnterAsync`、`OnEscAsync`）

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/input](https://www.blazor.zone/input)

## 使用场景

### 1. 基础用法

提供基本的文本录入组件。

```razor
<BootstrapInput @bind-Value="Model.Name" />
```

**功能说明**：
- 可通过设置 `IsAutoFocus` 是否自动获取焦点
- 多个文本框设置自动获取焦点时，最后执行的组件将会获得焦点
- 获得焦点时全选（`IsSelectAllTextOnFocus="true"`）
- 回车时全选（`IsSelectAllTextOnEnter="true"`）

---

### 2. 颜色

通过设置 `Color` 更改文本框边框颜色。

```razor
<BootstrapInput @bind-Value="Model.Name" Color="Color.Primary" />
<BootstrapInput @bind-Value="Model.Name" Color="Color.Success" />
<BootstrapInput @bind-Value="Model.Name" Color="Color.Danger" />
```

---

### 3. 键盘响应

使用 `OnEnterAsync`、`OnEscAsync` 回调委托对 Enter、ESC 按键进行回调响应。

```razor
<BootstrapInput @bind-Value="Model.Name" 
              OnEnterAsync="OnEnter" 
              OnEscAsync="OnEsc" />

@code {
    private async Task OnEnter(string value)
    {
        // 按 Enter 键时触发
        await ToastService.Information($"输入内容：{value}");
    }

    private async Task OnEsc()
    {
        // 按 ESC 键时触发
        await ToastService.Information("已取消");
    }
}
```

---

### 4. 单向绑定数据

显示组件内变量值。

```razor
<BootstrapInput Value="Model.Name" />
```

**注意**：单向绑定不会更新 Model 的值，仅显示。

---

### 5. 双向绑定数据

绑定组件内变量，数据自动同步。

```razor
<BootstrapInput @bind-Value="Model.Name" />
```

**说明**：
- BootstrapInput 组件开启双向绑定时，会根据绑定的 Model 属性值去自动获取 `Display/DisplayName` 标签值并且显示为前置 Label
- 通过 `DisplayText` 属性可以自定义显示前置标签
- 或者通过 `ShowLabel` 属性关闭前置标签是否显示

---

### 6. 自定义标签

设置 `DisplayText` 值为"自定义标签"。

```razor
<BootstrapInput @bind-Value="Model.Name" DisplayText="姓名" />
```

**标签显示规则**：
- 无论是否设置 `DisplayText` 值，当 `ShowLabel="true"` 时均显示
- 无论是否设置 `DisplayText` 值，当 `ShowLabel="false"` 时均不显示

---

### 7. 客户端验证

根据自定义验证规则进行数据有效性检查并自动提示。

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="Model.Name" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

**小提示**：
- 使用双向绑定时会自动寻找资源文件中 Key 值为 `{FieldName}.PlaceHolder` 对应值作为 placeholder 显示
- 本例中 placeholder 值为资源文件中 `Name.PlaceHolder` 键对应值

---

### 8. 密码框

通过设置属性 `type="password"` 使输入文字后以 `*` 进行屏蔽的密码输入框。

```razor
<BootstrapInput type="password" @bind-Value="Model.Password" />
```

**说明**：
- 为了支持更多的文本框属性，本组件可以直接写入 `type="email"`、`type="number"`、`type="tel"` 等 HTML5 新标准支持的全部属性值
- 组件未设置 `type` 值时使用默认的 `type="text"`

---

### 9. 泛型绑定

BootstrapInput 组件双向绑定值是泛型的，本例中双向绑定一个 `int` 类型数值。

```razor
<BootstrapInput @bind-Value="Model.Age" />
```

**说明**：绑定值为 `int` 类型时，组件会自动验证输入是否为有效数字。

---

### 10. 禁用

设置 `IsDisabled="true"` 属性值为 true 时，组件禁止输入。

```razor
<BootstrapInput @bind-Value="Model.Name" IsDisabled="true" />
```

---

### 11. 自定义格式

设置 `FormatString` 属性值为 `"yyyy-MM-dd"` 时，组件显示的时间格式为年月日。

```razor
<BootstrapInput @bind-Value="Model.Birthday" FormatString="yyyy-MM-dd" />
```

或者使用 `Formatter` 函数：

```razor
<BootstrapInput @bind-Value="Model.Name" Formatter="FormatName" />

@code {
    private string FormatName(string value)
    {
        return $"姓名：{value}";
    }
}
```

---

### 12. 修剪空白

使用 `IsTrim="true"` 可在输入内容的时候自动修剪空白。

```razor
<BootstrapInput @bind-Value="Model.Name" IsTrim="true" />
```

**说明**：设置参数 `IsTrim` 值为 true 后，组件内的前后空格将会被裁剪。

---

### 13. 文本框的值更改时触发

使用 `UseInputEvent="true"` 文本框的值更改时触发，用于逐键响应场合。

```razor
<BootstrapInput @bind-Value="Model.Name" UseInputEvent="true" OnValueChanged="OnValueChanged" />

@code {
    private void OnValueChanged(string value)
    {
        // 每次按下键盘都会触发 ValueChanged 事件
        Console.WriteLine($"输入值：{value}");
    }
}
```

---

### 14. 清除

通过设置 `IsClearable="true"` 参数，使组件获得焦点或者鼠标悬浮时显示一个"清除"小按钮。

```razor
<BootstrapInput @bind-Value="Model.Name" IsClearable="true" />
```

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TValue` | `default` | 获得/设置组件值 |
| `@bind-Value` | `TValue` | `default` | 获得/设置组件值（双向绑定） |
| `DisplayText` | `string?` | `null` | 获得/设置显示名称（前置标签） |
| `ShowLabel` | `bool?` | `null` | 获得/设置是否显示标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置是否显示标签 Tooltip |
| `Color` | `Color` | `Color.None` | 获得/设置按钮颜色 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用，默认为 false |
| `IsReadonly` | `bool` | `false` | 获得/设置是否只读，默认为 false |
| `IsClearable` | `bool` | `false` | 获得/设置是否显示清空小按钮，默认为 false |
| `ClearIcon` | `string?` | `null` | 获得/设置清空小按钮图标，默认为 null |
| `IsAutoFocus` | `bool` | `false` | 获得/设置是否自动获取焦点，默认值为 false |
| `IsSelectAllTextOnFocus` | `bool` | `false` | 获得/设置是否在获取焦点时自动选择所有文本，默认值为 false |
| `IsSelectAllTextOnEnter` | `bool` | `false` | 获得/设置是否在按下回车键时自动选择所有文本，默认值为 false |
| `IsTrim` | `bool` | `false` | 获得/设置是否自动去除空格，默认值为 false |
| `FormatString` | `string?` | `null` | 获得/设置格式字符串，例如 "yyyy-MM-dd" 用于日期类型 |
| `Formatter` | `Func<TValue, string>?` | `null` | 获得/设置格式化函数 |
| `type` | `string` | `"text"` | 获得/设置输入框类型（text、password、email、number、tel 等） |
| `placeholder` | `string?` | `null` | 获得/设置占位符文本 |
| `maxlength` | `int?` | `null` | 获得/设置最大输入长度 |
| `UseInputEvent` | `bool` | `false` | 获得/设置是否使用 input 事件（逐键响应），默认值为 false |
| `OnEnterAsync` | `Func<string, Task>?` | `null` | 获得/设置按下 Enter 键时的回调方法 |
| `OnEscAsync` | `Func<Task>?` | `null` | 获得/设置按下 ESC 键时的回调方法 |
| `OnBlurAsync` | `Func<TValue, Task>?` | `null` | 获得/设置失去焦点时的回调方法 |
| `OnClear` | `Func<TValue, Task>?` | `null` | 获得/设置清除时的回调方法 |
| `OnValueChanged` | `EventCallback<TValue>` | - | 获得/设置值变化时的回调方法 |
| `Id` | `string?` | `null` | 获得/设置组件 id 属性 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |

## 最佳实践

### 1. 双向绑定最佳实践

**推荐做法**：使用 `@bind-Value` 进行双向绑定，组件会自动处理标签显示和验证。

```razor
<BootstrapInput @bind-Value="Model.Name" />
```

**标签显示规则**：
- 组件会自动查找模型属性的 `Display` 或 `DisplayName` 特性作为标签文本
- 可以通过 `DisplayText` 参数自定义标签文本
- 可以通过 `ShowLabel="false"` 隐藏标签

---

### 2. 数据验证最佳实践

**推荐做法**：将 Input 组件放在 `ValidateForm` 组件内，并使用数据注解进行验证。

```csharp
public class Foo
{
    [Required(ErrorMessage = "姓名不能为空")]
    [StringLength(10, ErrorMessage = "姓名长度不能超过10个字符")]
    public string? Name { get; set; }
}
```

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="Model.Name" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

---

### 3. 格式化显示最佳实践

**场景**：需要自定义显示格式（如日期、货币等）。

**推荐做法**：使用 `FormatString` 或 `Formatter` 参数。

```razor
@* 使用 FormatString *@
<BootstrapInput @bind-Value="Model.Birthday" FormatString="yyyy-MM-dd" />

@* 使用 Formatter *@
<BootstrapInput @bind-Value="Model.Price" Formatter="FormatPrice" />

@code {
    private string FormatPrice(decimal value)
    {
        return $"￥{value:N2}";
    }
}
```

---

### 4. 键盘事件处理最佳实践

**场景**：需要处理 Enter 或 ESC 按键。

**推荐做法**：使用 `OnEnterAsync` 和 `OnEscAsync` 回调。

```razor
<BootstrapInput @bind-Value="Model.Name" 
              OnEnterAsync="OnEnter" 
              OnEscAsync="OnEsc" />

@code {
    private async Task OnEnter(string value)
    {
        // 按 Enter 键：执行搜索或提交
        await SearchAsync(value);
    }

    private async Task OnEsc()
    {
        // 按 ESC 键：清空输入或取消
        Model.Name = "";
        await InvokeAsync(StateHasChanged);
    }
}
```

---

### 5. 常见错误

**错误 1**：未设置 `@bind-Value`，只设置了 `Value`

**解决方法**：使用 `@bind-Value` 进行双向绑定，或者同时设置 `Value` 和 `ValueChanged`。

**错误 2**：泛型类型不匹配

**解决方法**：确保 `@bind-Value` 的类型与 Model 属性类型一致。

**错误 3**：在 `ValidateForm` 外使用 Input 组件

**解决方法**：Input 组件应在 `ValidateForm` 内使用以支持验证。

---

## 相关组件

- `BootstrapPassword` - 密码输入框组件（专门处理密码输入）
- `BootstrapInputNumber` - 数字输入框组件
- `ValidateForm` - 验证表单组件
- `BootstrapTextarea` - 多行文本框组件

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 Input 组件的核心功能和使用方法。
