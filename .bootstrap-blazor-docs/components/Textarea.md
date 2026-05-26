# Textarea (多行文本框)

## 概述

Textarea 组件是 Bootstrap Blazor 中用于录入大量文字的组件。支持多行文本输入、高度设置、内容滚动等功能。

**主要功能特性**：
- 支持单向/双向数据绑定
- 支持禁用状态（IsDisabled）
- 支持只读状态（IsReadonly）
- 支持高度设置（rows 属性）
- 支持内容滚动（ScrollToTop、ScrollToBottom）
- 支持 Shift + Enter 换行（UseShiftEnter）
- 支持 Enter/Esc 按键事件（OnEnterAsync、OnEscAsync）
- 支持自动获取焦点（IsAutoFocus）
- 支持文本选择（IsSelectAllTextOnFocus、IsSelectAllTextOnEnter）
- 支持修剪空白（IsTrim）
- 支持客户端验证（ValidateForm）

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/textarea](https://www.blazor.zone/textarea)

## 使用场景

### 1. 基础用法

可接受大量文字。

```razor
<BootstrapTextarea @bind-Value="Model.Description" />
```

---

### 2. 禁用

设置 `IsDisabled="true"` 属性时，组件禁止输入。

```razor
<BootstrapTextarea @bind-Value="Model.Description" IsDisabled="true" />
```

---

### 3. 只读

设置 `IsReadonly="true"` 属性时，组件禁止输入。

```razor
<BootstrapTextarea @bind-Value="Model.Description" IsReadonly="true" />
```

**说明**：只读状态下，用户无法修改内容，但可以复制、滚动。

---

### 4. 高度

设置 `rows` 属性时，组件初始化显示固定行数高度。

```razor
<BootstrapTextarea @bind-Value="Model.Description" rows="5" />
```

**说明**：`rows` 属性控制文本区域的高度（行数）。

---

### 5. 双向绑定

绑定组件内变量，数据自动同步。

```razor
<BootstrapTextarea @bind-Value="Model.Description" />
```

**绑定值**：显示当前绑定的值。

---

### 6. 内容滚动

滚动到底部/顶部/指定位置。

```razor
<BootstrapTextarea @bind-Value="Model.Description" @ref="TextareaRef" />

<Button Text="滚动到顶部" OnClick="ScrollToTop" />
<Button Text="滚动到底部" OnClick="ScrollToBottom" />
<Button Text="滚动+20" OnClick="ScrollPlus20" />

@code {
    [NotNull]
    private BootstrapTextarea? TextareaRef { get; set; }

    private async Task ScrollToTop()
    {
        await TextareaRef.ScrollToTop();
    }

    private async Task ScrollToBottom()
    {
        await TextareaRef.ScrollToBottom();
    }

    private async Task ScrollPlus20()
    {
        await TextareaRef.ScrollTo(20);
    }
}
```

**功能说明**：
- 滚动到顶部
- 滚动到底部
- 滚动+20

---

### 7. Shift Enter

通过设置 `UseShiftEnter="true"` 开始使用 Shift + Enter 进行换行操作，适用于对话框类应用。

```razor
<BootstrapTextarea @bind-Value="Model.Description" UseShiftEnter="true" />
```

**功能说明**：
- 默认情况下，按 Enter 键会触发 `OnEnterAsync` 回调
- 设置 `UseShiftEnter="true"` 后，按 Shift + Enter 才换行，按 Enter 触发回调

---

### 8. Enter/Esc 按键事件

通过设置 `OnEnterAsync`、`OnEscAsync` 开始 Enter、Esc 按键回调事件。

```razor
<BootstrapTextarea @bind-Value="Model.Description" 
              OnEnterAsync="OnEnter" 
              OnEscAsync="OnEsc" />

@code {
    private async Task OnEnter(string value)
    {
        // 按 Enter 键时触发
        await ToastService.Information($"输入内容：{value}");
    }

    private async Task OnEsc(string value)
    {
        // 按 ESC 键时触发
        await ToastService.Information("已取消");
    }
}
```

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置组件值 |
| `@bind-Value` | `string?` | `null` | 获得/设置组件值（双向绑定） |
| `DisplayText` | `string?` | `null` | 获得/设置显示名称（前置标签） |
| `ShowLabel` | `bool?` | `null` | 获得/设置是否显示前置标签，默认值为 null，为空时不显示标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null |
| `Color` | `Color` | `Color.None` | 获得/设置按钮颜色 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用，默认为 false |
| `IsReadonly` | `bool` | `false` | 获得/设置是否只读，默认为 false |
| `rows` | `int` | `3` | 获得/设置文本区域高度（行数），默认 3 行 |
| `IsAutoFocus` | `bool` | `false` | 获得/设置是否自动获取焦点，默认值为 false |
| `IsAutoScroll` | `bool` | `false` | 获得/设置是否自动滚动，默认为 false |
| `IsSelectAllTextOnFocus` | `bool` | `false` | 获得/设置是否在获取焦点时自动选择所有文本，默认值为 false |
| `IsSelectAllTextOnEnter` | `bool` | `false` | 获得/设置是否在按下回车键时自动选择所有文本，默认值为 false |
| `IsTrim` | `bool` | `false` | 获得/设置是否自动去除空格，默认值为 false |
| `UseShiftEnter` | `bool` | `false` | 获得/设置是否 Shift + Enter 替代默认 Enter 键行为，默认为 false |
| `UseInputEvent` | `bool` | `false` | 获得/设置是否在文本框输入值时触发 bind-value:event="oninput"，默认 false |
| `FormatString` | `string?` | `null` | 获得/设置格式字符串 |
| `Formatter` | `Func<string, string>?` | `null` | 获得/设置格式化函数 |
| `PlaceHolder` | `string?` | `null` | 获得/设置占位符属性值 |
| `OnEnterAsync` | `Func<string, Task>?` | `null` | 获得/设置回车键按下时的回调方法 |
| `OnEscAsync` | `Func<string, Task>?` | `null` | 获得/设置 Esc 键按下时的回调方法 |
| `OnBlurAsync` | `Func<string, Task>?` | `null` | 获得/设置失去焦点时的回调方法 |
| `OnValueChanged` | `Func<string, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置类型转化失败格式化字符串，默认为 null |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置必填项错误文本，默认为 null 未设置 |
| `ShowRequired` | `bool?` | `null` | 获得/设置是否显示必填项标记，默认为 null 未设置 |
| `SkipValidate` | `bool` | `false` | 获得/设置是否不进行验证，默认为 false |
| `ValidateRules` | `List<IValidator>?` | `null` | 获得/设置自定义验证集合 |
| `Id` | `string?` | `null` | 获得/设置组件 id 属性 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |

## 方法 (Methods)

| 方法名 | 参数 | 返回类型 | 说明 |
|--------|------|----------|------|
| `ScrollToTop` | 无 | `Task` | 滚动到顶部 |
| `ScrollToBottom` | 无 | `Task` | 滚动到底部 |
| `ScrollTo` | `int position` | `Task` | 滚动到指定位置 |

## 最佳实践

### 1. 数据绑定最佳实践

**推荐做法**：使用 `@bind-Value` 进行双向绑定。

```razor
<BootstrapTextarea @bind-Value="Model.Description" />
```

**标签显示规则**：
- 组件会自动查找模型属性的 `Display` 或 `DisplayName` 特性作为标签文本
- 可以通过 `DisplayText` 参数自定义标签文本
- 可以通过 `ShowLabel="false"` 隐藏标签

---

### 2. 高度设置最佳实践

**场景**：需要显示多行文本。

**推荐做法**：使用 `rows` 属性设置高度。

```razor
@* 显示 5 行 *@
<BootstrapTextarea @bind-Value="Model.Description" rows="5" />

@* 显示 10 行 *@
<BootstrapTextarea @bind-Value="Model.Description" rows="10" />
```

---

### 3. Shift + Enter 换行最佳实践

**场景**：在对话框类应用中，需要按 Enter 发送，按 Shift + Enter 换行。

**推荐做法**：使用 `UseShiftEnter="true"`。

```razor
<BootstrapTextarea @bind-Value="Model.Message" 
              UseShiftEnter="true" 
              OnEnterAsync="OnSend" />

@code {
    private async Task OnSend(string message)
    {
        // 按 Enter 键：发送消息
        await SendMessageAsync(message);
        Model.Message = "";
    }
}
```

---

### 4. 内容滚动最佳实践

**场景**：聊天应用中，需要自动滚动到底部显示最新消息。

**推荐做法**：使用 `ScrollToBottom()` 方法。

```razor
<BootstrapTextarea @bind-Value="Model.Messages" @ref="TextareaRef" readonly />

@code {
    [NotNull]
    private BootstrapTextarea? TextareaRef { get; set; }

    private async Task AddMessage(string message)
    {
        Model.Messages += $"\n{message}";
        await InvokeAsync(StateHasChanged);
        await TextareaRef.ScrollToBottom();
    }
}
```

---

### 5. 数据验证最佳实践

**推荐做法**：将 Textarea 组件放在 `ValidateForm` 组件内，并使用数据注解进行验证。

```csharp
public class Foo
{
    [Required(ErrorMessage = "描述不能为空")]
    [StringLength(500, ErrorMessage = "描述长度不能超过500个字符")]
    public string? Description { get; set; }
}
```

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <BootstrapTextarea @bind-Value="Model.Description" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

---

### 6. 常见错误

**错误 1**：未设置 `@bind-Value`，只设置了 `Value`

**解决方法**：使用 `@bind-Value` 进行双向绑定，或者同时设置 `Value` 和 `ValueChanged`。

**错误 2**：在对话框应用中，按 Enter 键导致关闭对话框

**解决方法**：设置 `UseShiftEnter="true"`，使 Enter 键触发回调而不是关闭对话框。

**错误 3**：文本区域高度不够，内容被截断

**解决方法**：增加 `rows` 属性值，或使用 CSS 自定义高度。

---

## 相关组件

- `BootstrapInput` - 输入框组件（单行文本）
- `ValidateForm` - 验证表单组件
- `BootstrapMarkdown` - Markdown 编辑器组件（富文本）
