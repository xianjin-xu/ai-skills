# ValidateForm

## 概述

ValidateForm 组件类

> ValidateForm component

**分类**: 表单验证
**在线演示**: [https://www.blazor.zone/validate-form](https://www.blazor.zone/validate-form)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Task` | `Func<EditContext,` | `}` | 获得/设置 表单提交后验证合规时回调方法 |
| `object` | `Action<string,` | `}` | 获得/设置 表单内绑定字段值变化时回调方法 |
| `ShowAllInvalidResult` | `bool` | `}` | 获得/设置 是否显示所有验证失败字段的提示信息 默认 false 仅显示第一个验证失败字段的提示信息 |
| `ValidateAllProperties` | `bool` | `}` | 获得/设置 是否验证所有字段 默认 false |
| `Model` | `object?` | `}` | 获得/设置 表单绑定模型对象 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 组件子内容 |
| `ShowRequiredMark` | `bool` | `true` | 获得/设置 是否获取必填项标记 默认为 true 显示 |
| `ShowLabel` | `bool?` | `}` | 获得/设置 是否显示验证表单内的 Label 默认为 null |
| `ShowLabelTooltip` | `bool?` | `}` | 获得/设置 是否显示标签 Tooltip 多用于标签文字过长导致裁减时使用 默认 null |
| `IsFormless` | `bool` | `}` | - |
| `DisableAutoSubmitFormByEnter` | `bool?` | `}` | 获得/设置 是否禁用表单内回车自动提交功能 默认 null 未设置 |
| `LabelWidth` | `int?` | `}` | 获得/设置 标签宽度 默认 null 未设置 使用全局设置 <code>--bb-row-label-width</code> 值 |

## 代码示例

### 基本用法

```razor
<ValidateForm Model="@Model1" OnFieldValueChanged="@OnFiledChanged"
                  OnValidSubmit="@OnValidSubmit1" OnInvalidSubmit="@OnInvalidSubmit1">
        <div class="row g-3">
            <div class="col-12">
                <BootstrapInputGroup>
                    <BootstrapInputGroupLabel ShowRequiredMark DisplayText="Test"></BootstrapInputGroupLabel>
                    <BootstrapInput @bind-Value="@Model1.Name" DisplayText="@Localizer["LongDisplayText"]" />
                </BootstrapInputGroup>
            </div>
        </div>
        <div class="row g-3 form-inline mt-0">
            <div class="col-12">
                <BootstrapInput @bind-Value="@Model1.Address" DisplayText="@Localizer["LongDisplayText"]" ShowLabelTooltip="true" />
            </div>
            <div class="col-12">
                <Button ButtonType="ButtonType.Submit" Icon="fa-fw fa-solid fa-floppy-disk" Text="@Localizer["ValidateFormsSubmitButtonText"]" IsAsync="true"></Button>
            </div>
        </div>
    </ValidateForm>
```

### 基本用法

```razor
<ValidateForm Model="@Model2" OnValidSubmit="@OnValidSubmit2" OnInvalidSubmit="@OnInvalidSubmit2">
        <div class="row g-3">
            <div class="col-12 col-sm-6">
                <BootstrapInputGroupLabel @bind-Value="@Model2.Name" />
                <BootstrapInputGroup>
                    <BootstrapInputGroupLabel DisplayText="Test" />
                    <Display @bind-Value="@Model2.Name"></Display>
                </BootstrapInputGroup>
            </div>
            <div class="col-12 col-sm-6">
                <BootstrapInputNumber @bind-Value="@Model2.Count" />
            </div>
            <div class="col-12 col-sm-6">
                <DateTimePicker @bind-Value="@Model2.DateTime" />
            </div>
            <div class="col-12 col-sm-6">
                <Select @bind-Value="@Model2.Education" />
            </div>
            <div class="col-12">
                <CheckboxList @bind-Value="@Model2.Hobby" Items="@Hobbies2" />
            </div>
            <div class="col-12">
                <Button ButtonType="@ButtonType.Submit" Icon="fa-fw fa-solid fa-floppy-disk" IsAsync="true" Text="@Localizer["ValidateFormsSubmitButtonText"]" />
            </div>
        </div>
    </ValidateForm>
```

### 基本用法

```razor
<ValidateForm @ref="FooForm" Model="@Model3" OnValidSubmit="@OnValidSetError">
        <div class="row g-3">
            <div class="col-12 col-sm-6">
                <BootstrapInput @bind-Value="@Model3.Name" />
            </div>
            <div class="col-12 col-sm-6">
                <BootstrapInputNumber @bind-Value="@Model3.Count" />
            </div>
            <div class="col-12 col-sm-6">
                <DateTimePicker @bind-Value="@Model3.DateTime" />
            </div>
            <div class="col-12 col-sm-6">
                <Select @bind-Value="@Model3.Education" />
            </div>
            <div class="col-12">
                <CheckboxList @bind-Value="@Model3.Hobby" Items="@Hobbies3" />
            </div>
            <div class="col-12">
                <Button ButtonType="@ButtonType.Submit" Text="@Localizer["ValidateFormsSubmitButtonText"]" />
            </div>
        </div>
    </ValidateForm>
```

### 基本用法

```razor
<ValidateForm Model="@Model4" OnInvalidSubmit="@OnInvalidSubmitAddress"
                  ValidateAllProperties="true">
        <div class="row g-3">
            <div class="col-12 col-sm-6">
                <BootstrapInput @bind-Value="@Model4.Name" />
            </div>
            <div class="col-12 col-sm-6">
                <BootstrapInputNumber @bind-Value="@Model4.Count" />
            </div>
            <div class="col-12 col-sm-6">
                <DateTimePicker @bind-Value="@Model4.DateTime" />
            </div>
            <div class="col-12 col-sm-6">
                <Select @bind-Value="@Model4.Education" />
            </div>
            <div class="col-12">
                <CheckboxList @bind-Value="@Model4.Hobby" Items="@Hobbies4" />
            </div>
            <div class="col-12">
                <Button ButtonType="@ButtonType.Submit" Text="@Localizer["ValidateFormsSubmitButtonText"]" />
            </div>
        </div>
    </ValidateForm>
```

### 基本用法

```razor
<ValidateForm @ref="ComplexForm" Model="@ComplexModel" OnInvalidSubmit="@OnInvalidComplexModel"
                  OnValidSubmit="@OnValidComplexModel">
        <div class="row g-3">
            <div class="col-12 col-sm-6">
                <BootstrapInput @bind-Value="@ComplexModel.Name" />
            </div>
            <div class="col-12 col-sm-6">
                <BootstrapInput @bind-Value="@ComplexModel.Dummy.Dummy2.Name" />
            </div>
            <div class="col-12">
                <Button ButtonType="@ButtonType.Submit" Text="@Localizer["ValidateFormsSubmitButtonText"]" />
            </div>
        </div>
    </ValidateForm>
```
