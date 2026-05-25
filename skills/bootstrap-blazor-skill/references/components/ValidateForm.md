# ValidateForm (验证表单)

## 概述

ValidateForm 组件是 Bootstrap Blazor 中用于表单验证的核心组件。它扩展了 Blazor 原生的 `EditForm` 组件，提供了更强大的验证功能和更灵活的表单控制。

**主要功能特性**：
- 支持数据注解验证（DataAnnotations）
- 支持客户端验证
- 支持自定义验证规则
- 支持表单提交验证（OnValidSubmit、OnInvalidSubmit）
- 支持字段值变化回调（OnFieldValueChanged）
- 支持无表单模式（IsFormless，用于 Table InCell 编辑）
- 支持必填项标记（ShowRequiredMark）
- 支持标签显示控制（ShowLabel、ShowLabelTooltip）

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/validate-form](https://www.blazor.zone/validate-form)

## 使用场景

### 1. 基本用法

使用 ValidateForm 包裹表单字段，实现数据验证。

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="Model.Name" />
    <BootstrapInput @bind-Value="Model.Email" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>

@code {
    [NotNull]
    private Foo? Model { get; set; }

    protected override void OnInitialized()
    {
        Model = new Foo();
    }

    private async Task OnValidSubmit(EditContext editContext)
    {
        // 表单验证通过，执行提交逻辑
        await SaveAsync(Model);
    }
}
```

**功能说明**：
- `Model` 参数绑定验证模型
- `OnValidSubmit` 回调在表单验证通过时触发
- 表单字段使用 `@bind-Value` 绑定模型属性

---

### 2. 验证失败处理

通过 `OnInvalidSubmit` 回调处理验证失败情况。

```razor
<ValidateForm Model="Model" 
              OnValidSubmit="OnValidSubmit" 
              OnInvalidSubmit="OnInvalidSubmit">
    <BootstrapInput @bind-Value="Model.Name" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>

@code {
    private async Task OnInvalidSubmit(EditContext editContext)
    {
        // 表单验证失败，显示错误信息
        await ToastService.Error("表单验证失败，请检查输入");
    }
}
```

---

### 3. 显示所有验证错误

默认情况下，只显示第一个验证失败字段的错误信息。设置 `ShowAllInvalidResult="true"` 可显示所有验证错误。

```razor
<ValidateForm Model="Model" 
              OnValidSubmit="OnValidSubmit"
              ShowAllInvalidResult="true">
    <BootstrapInput @bind-Value="Model.Name" />
    <BootstrapInput @bind-Value="Model.Email" />
</ValidateForm>
```

---

### 4. 验证所有属性

默认情况下，只验证表单中绑定的字段。设置 `ValidateAllProperties="true"` 可验证模型的所有属性。

```razor
<ValidateForm Model="Model" 
              OnValidSubmit="OnValidSubmit"
              ValidateAllProperties="true">
    <BootstrapInput @bind-Value="Model.Name" />
</ValidateForm>
```

**注意**：`ValidateAllProperties="true"` 会验证模型的所有属性，即使某些属性没有在表单中绑定。

---

### 5. 无表单模式（IsFormless）

在 Table 组件的 InCell 编辑模式中，需要使用无表单模式（不渲染 form 元素）。

```razor
<ValidateForm Model="Model" IsFormless="true">
    <BootstrapInput @bind-Value="Model.Name" />
</ValidateForm>
```

**使用场景**：
- Table 组件的 InCell 编辑模式
- 在 dialog 中编辑数据（避免嵌套 form 元素）

---

### 6. 字段值变化回调

通过 `OnFieldValueChanged` 回调监听字段值变化。

```razor
<ValidateForm Model="Model" 
              OnValidSubmit="OnValidSubmit"
              OnFieldValueChanged="OnFieldValueChanged">
    <BootstrapInput @bind-Value="Model.Name" />
</ValidateForm>

@code {
    private void OnFieldValueChanged(string fieldName, object? value)
    {
        // 字段值变化时触发
        Console.WriteLine($"字段 {fieldName} 值变为 {value}");
    }
}
```

---

### 7. 禁用回车自动提交

默认情况下，表单内按回车键会自动提交表单。设置 `DisableAutoSubmitFormByEnter="true"` 可禁用此行为。

```razor
<ValidateForm Model="Model" 
              OnValidSubmit="OnValidSubmit"
              DisableAutoSubmitFormByEnter="true">
    <BootstrapInput @bind-Value="Model.Name" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

---

### 8. 自定义错误信息

通过 `SetError` 方法动态设置字段错误信息。

```razor
<ValidateForm @ref="ValidateFormRef" Model="Model" OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="Model.Name" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>

@code {
    [NotNull]
    private ValidateForm? ValidateFormRef { get; set; }

    private async Task OnValidSubmit(EditContext editContext)
    {
        // 手动验证并设置错误信息
        if (Model.Name == "admin")
        {
            await ValidateFormRef.SetError("Name", "用户名已存在");
            return;
        }

        await SaveAsync(Model);
    }
}
```

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Model` | `object?` | `null` | 获得/设置表单绑定模型对象 |
| `OnValidSubmit` | `Func<EditContext, Task>?` | `null` | 获得/设置表单提交后验证合规时回调方法 |
| `OnInvalidSubmit` | `Func<EditContext, Task>?` | `null` | 获得/设置表单提交后验证不合规时回调方法 |
| `OnFieldValueChanged` | `Action<string, object?>?` | `null` | 获得/设置表单内绑定字段值变化时回调方法 |
| `ShowAllInvalidResult` | `bool` | `false` | 获得/设置是否显示所有验证失败字段的提示信息，默认 false 仅显示第一个验证失败字段的提示信息 |
| `ValidateAllProperties` | `bool` | `false` | 获得/设置是否验证所有字段，默认 false |
| `ShowRequiredMark` | `bool` | `true` | 获得/设置是否获取必填项标记，默认为 true 显示 |
| `ShowLabel` | `bool?` | `null` | 获得/设置是否显示验证表单内的 Label，默认为 null |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置是否显示标签 Tooltip，多用于标签文字过长导致裁减时使用，默认 null |
| `IsFormless` | `bool` | `false` | 获得/设置是否为无表单模式，默认 false。设置为 true 时不渲染 form 元素，仅级联 EditContext 用于 Table InCell 编辑模式 |
| `DisableAutoSubmitFormByEnter` | `bool?` | `null` | 获得/设置是否禁用表单内回车自动提交功能，默认 null 未设置 |
| `LabelWidth` | `int?` | `null` | 获得/设置标签宽度，默认 null 未设置使用全局设置 `--bb-row-label-width` 值 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置组件子内容 |

## 方法 (Methods)

| 方法名 | 参数 | 返回类型 | 说明 |
|--------|------|----------|------|
| `SetError<TModel>` | `Expression<Func<TModel, object?>> expression, string errorMessage` | `Task` | 设置指定字段错误信息（使用表达式） |
| `SetError` | `string propertyName, string errorMessage` | `Task` | 设置指定字段错误信息（使用属性名，支持多层如 "a.b.c"） |

## 最佳实践

### 1. 模型定义最佳实践

**推荐做法**：在模型类中使用数据注解（DataAnnotations）定义验证规则。

```csharp
public class Foo
{
    [Required(ErrorMessage = "姓名不能为空")]
    [StringLength(10, ErrorMessage = "姓名长度不能超过10个字符")]
    public string? Name { get; set; }

    [Required(ErrorMessage = "邮箱不能为空")]
    [EmailAddress(ErrorMessage = "邮箱格式不正确")]
    public string? Email { get; set; }

    [Range(1, 100, ErrorMessage = "年龄必须在1-100之间")]
    public int Age { get; set; }
}
```

---

### 2. 表单提交最佳实践

**推荐做法**：使用 `OnValidSubmit` 处理提交逻辑，避免在 `OnInvalidSubmit` 中执行提交相关操作。

```csharp
private async Task OnValidSubmit(EditContext editContext)
{
    // 1. 显示加载状态
    IsLoading = true;

    // 2. 执行提交
    await SaveAsync(Model);

    // 3. 显示成功提示
    await ToastService.Success("保存成功");

    // 4. 关闭弹窗（如果在弹窗中）
    await DialogService.CloseDialogAsync();
}
```

---

### 3. 自定义验证最佳实践

**场景**：需要执行服务器端验证（如检查用户名是否已存在）。

**推荐做法**：在 `OnValidSubmit` 中执行自定义验证，使用 `SetError` 方法设置错误信息。

```csharp
private async Task OnValidSubmit(EditContext editContext)
{
    // 检查用户名是否已存在
    var exists = await UserService.CheckUserNameExistsAsync(Model.Name);
    if (exists)
    {
        await ValidateFormRef.SetError("Name", "用户名已存在");
        return;
    }

    // 验证通过，执行提交
    await SaveAsync(Model);
}
```

---

### 4. 无表单模式使用场景

**场景 1**：Table 组件的 InCell 编辑模式

```razor
<Table TItem="Foo" Items="Items" EditMode="EditMode.InCell">
    <TableColumns>
        <TableColumn @bind-Field="@context.Name">
            <EditTemplate>
                <ValidateForm Model="context" IsFormless="true">
                    <BootstrapInput @bind-Value="@context.Name" />
                </ValidateForm>
            </EditTemplate>
        </TableColumn>
    </TableColumns>
</Table>
```

**场景 2**：在 Dialog 中编辑数据（避免嵌套 form 元素）

```razor
<Dialog>
    <BodyTemplate>
        <ValidateForm Model="Model" IsFormless="true">
            <BootstrapInput @bind-Value="Model.Name" />
        </ValidateForm>
    </BodyTemplate>
</Dialog>
```

---

### 5. 常见错误

**错误 1**：未设置 `Model` 参数

**解决方法**：确保设置了 `Model` 参数，且 Model 不为 null。

**错误 2**：模型属性为 null 但未标记 `[Required]`

**解决方法**：如果属性允许为 null，不要标记 `[Required]`；如果不允许为 null，标记 `[Required]` 或使用不可为 null 的类型（`string?` vs `string`）。

**错误 3**：在 `OnValidSubmit` 中未处理自定义验证失败情况

**解决方法**：在 `OnValidSubmit` 中执行自定义验证，如果验证失败，使用 `SetError` 设置错误信息并 return。

**错误 4**：嵌套表单（form 内还有 form）

**解决方法**：使用 `IsFormless="true"` 避免渲染 form 元素。

---

## 相关组件

- `EditForm` - Blazor 原生编辑表单组件（ValidateForm 扩展自 EditForm）
- `BootstrapInput` - Bootstrap Blazor 输入框组件
- `BootstrapSelect` - Bootstrap Blazor 下拉选择组件
- `Table` - 表格组件（InCell 编辑模式需要使用 ValidateForm）

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 ValidateForm 组件的核心功能和使用方法。
