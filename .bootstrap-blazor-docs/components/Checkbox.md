# Checkbox (多选框)

## 概述

Checkbox 组件是 Bootstrap Blazor 中用于在一组备选项中进行多选的组件。支持两种状态（选中/未选）和三种状态（选中/未选/不确定）。

**主要功能特性**：
- 支持单向/双向数据绑定
- 支持泛型绑定（TValue）
- 支持布尔类型、枚举类型、字符串类型等
- 支持禁用状态（IsDisabled）
- 支持颜色设置（Color）
- 支持大小设置（Size）
- 支持项目模板（ItemTemplate）
- 支持选中前回调（OnBeforeStateChanged）
- 支持标签显示控制（DisplayText、ShowLabel）
- 支持客户端验证（ValidateForm）

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/checkbox](https://www.blazor.zone/checkbox)

## 使用场景

### 1. 基础用法

单独使用可以表示两种状态之间的切换，列头或者表头使用时可以表示三种状态之间的切换。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" />
```

**组件支持泛型数据绑定**，通过 `TValue` 设置绑定数据类型，通过 `State` 设置组件状态。

**状态说明**：
- 选中（Checked）
- 未选（UnChecked）
- 不确定（Indeterminate）

---

### 2. 禁用复选框

复选框不可用状态，通过 `IsDisabled="true"` 设置组件是否可用。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" IsDisabled="true" />
```

---

### 3. 颜色

通过设置 `Color` 属性改变组件背景色。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Color="Color.Primary" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Color="Color.Success" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Color="Color.Danger" />
```

---

### 4. 项目模板

通过设置 `ItemTemplate` 自定义显示 UI。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed">
    <ItemTemplate>
        <div class="custom-checkbox">
            <i class="@(context.State == CheckboxState.Checked ? "fa-solid fa-square-check" : "fa-regular fa-square")"></i>
            @context.DisplayText
        </div>
    </ItemTemplate>
</Checkbox>
```

---

### 5. 大小

通过设置 `Size` 属性改变组件大小。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Size="Size.Default" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Size="Size.Small" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Size="Size.Medium" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Size="Size.Large" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Size="Size.ExtraLarge" />
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" Size="Size.ExtraExtraLarge" />
```

---

### 6. Label 文字

复选框显示文字，通过 `DisplayText` 设置组件显示文本，点击显示文字时组件状态也会进行翻转。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" DisplayText="同意用户协议" />
```

**设置 `DisplayText` 属性**，或者通过双向绑定均可以显示文本信息。

---

### 7. 双向绑定 boolean 数据

绑定组件内变量，数据自动同步，绑定数据类型为 `bool` 类型时自动翻转值。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" />
```

---

### 8. 双向绑定 string 数据

绑定组件内变量，数据自动同步。

```razor
<Checkbox TValue="string" @bind-Value="Model.SelectedValue" />
```

---

### 9. 选中前回调方法

通过设置 `OnBeforeStateChanged` 回调方法，可取消选中逻辑。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" 
        OnBeforeStateChanged="OnBeforeChange" />

@code {
    private async Task<bool> OnBeforeChange(CheckboxState state)
    {
        // 弹窗确认是否更改状态
        return await SwalService.Confirm("确认", $"确定要{(state == CheckboxState.Checked ? "选中" : "取消选中")}吗？");
    }
}
```

---

### 10. 表单中使用

在表单中使用 Checkbox 时，显示标签文字会放置到组件前面。

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <Checkbox TValue="bool" @bind-Value="Model.IsAgreed" DisplayText="同意用户协议" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

**前置标签显示规则与 BootstrapInput 组件一致**。

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TValue` | `default` | 获得/设置组件值 |
| `@bind-Value` | `TValue` | `default` | 获得/设置组件值（双向绑定） |
| `State` | `CheckboxState` | `CheckboxState.UnChecked` | 获得/设置选择框状态 |
| `StateChanged` | `EventCallback<CheckboxState>` | - | 获得/设置 State 状态改变的回调方法 |
| `DisplayText` | `string?` | `null` | 获得/设置显示名称（标签文字） |
| `ShowLabel` | `bool?` | `null` | 获得/设置是否显示前置标签，默认值为 null，为空时不显示标签 |
| `ShowAfterLabel` | `bool` | `false` | 获得/设置是否显示 Checkbox 后置 label 文字，默认为 false |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null |
| `ShowRequired` | `bool?` | `null` | 获得/设置是否显示必填项标记，默认为 null 未设置 |
| `Color` | `Color` | `Color.None` | 获得/设置按钮颜色，默认为 None |
| `Size` | `Size` | `Size.None` | 获得/设置 Size 大小，默认为 None |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用，默认为 false |
| `IsReadonly` | `bool` | `false` | 获得/设置是否只读，默认为 false |
| `OnBeforeStateChanged` | `Func<CheckboxState, Task<bool>>?` | `null` | 获得/设置选中状态改变前的回调方法。返回 false 可以阻止状态改变 |
| `OnStateChanged` | `Func<CheckboxState, TValue, Task>?` | `null` | 获得/设置选择框状态改变时回调此方法 |
| `OnValueChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置子组件 RenderFragment 实例 |
| `ItemTemplate` | `RenderFragment?` | `null` | 获得/设置项目模板 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置类型转化失败格式化字符串，默认为 null |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置必填项错误文本，默认为 null 未设置 |
| `SkipValidate` | `bool` | `false` | 获得/设置是否不进行验证，默认为 false |
| `StopPropagation` | `bool` | `false` | 获得/设置是否事件冒泡，默认为 false |
| `ValidateRules` | `List<IValidator>?` | `null` | 获得/设置自定义验证集合 |
| `Id` | `string?` | `null` | 获得/设置组件 id 属性 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |

## 状态枚举 (CheckboxState)

| 值 | 说明 |
|-----|------|
| `UnChecked` | 未选中 |
| `Checked` | 已选中 |
| `Indeterminate` | 不确定（用于全选/半选场景） |

## 最佳实践

### 1. 数据绑定最佳实践

**推荐做法**：根据数据类型选择合适的绑定方式。

**场景 1**：绑定 `bool` 类型（最常用）

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsAgreed" />
```

**场景 2**：绑定 `string` 类型

```razor
<Checkbox TValue="string" @bind-Value="Model.SelectedValue" />
```

**场景 3**：绑定枚举类型

```razor
<Checkbox TValue="EnumPermission" @bind-Value="Model.Permission" />
```

---

### 2. 全选/半选场景最佳实践

**场景**：表格中全选复选框，需要显示不确定状态。

**推荐做法**：使用 `Indeterminate` 状态。

```razor
<Checkbox TValue="bool" State="GetSelectAllState()" 
        OnStateChanged="OnSelectAllChanged" />

@code {
    private CheckboxState GetSelectAllState()
    {
        if (SelectedItems.Count == 0)
            return CheckboxState.UnChecked;
        if (SelectedItems.Count == TotalCount)
            return CheckboxState.Checked;
        return CheckboxState.Indeterminate;
    }

    private void OnSelectAllChanged(CheckboxState state)
    {
        if (state == CheckboxState.Checked)
        {
            // 全选
            SelectedItems = AllItems.ToList();
        }
        else
        {
            // 取消全选
            SelectedItems.Clear();
        }
    }
}
```

---

### 3. 选中前确认最佳实践

**场景**：需要确认才能更改选中状态（如删除确认）。

**推荐做法**：使用 `OnBeforeStateChanged` 回调。

```razor
<Checkbox TValue="bool" @bind-Value="Model.IsDeleted" 
        OnBeforeStateChanged="OnBeforeDelete" />

@code {
    private async Task<bool> OnBeforeDelete(CheckboxState state)
    {
        if (state == CheckboxState.Checked)
        {
            // 确认是否删除
            return await SwalService.Confirm("确认", "确定要删除吗？");
        }
        return true;
    }
}
```

---

### 4. 表单验证最佳实践

**场景**：在表单中使用 Checkbox，需要进行验证（如必须同意协议）。

**推荐做法**：在模型中使用数据注解，并在 `ValidateForm` 中使用 Checkbox。

```csharp
public class Foo
{
    [Required(ErrorMessage = "必须同意用户协议")]
    public bool IsAgreed { get; set; }
}
```

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <Checkbox TValue="bool" @bind-Value="Model.IsAgreed" DisplayText="同意用户协议" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

---

### 5. 常见错误

**错误 1**：未设置 `TValue` 类型参数

**解决方法**：必须指定 `TValue` 类型参数，如 `TValue="bool"`。

**错误 2**：绑定 `bool?` 类型时，状态显示异常

**解决方法**：使用 `CheckboxState` 类型绑定，或确保 `bool?` 值正确初始化。

**错误 3**：在全选场景中使用 `Value` 而不是 `State`

**解决方法**：全选场景应使用 `State` 属性，它支持 `Indeterminate` 状态。

---

## 相关组件

- `CheckboxList` - 多选框组组件（用于多个复选框）
- `Toggle` - 开关组件（类似 Checkbox，但外观不同）
- `ValidateForm` - 验证表单组件
- `Table` - 表格组件（全选场景）

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 Checkbox 组件的核心功能和使用方法。
