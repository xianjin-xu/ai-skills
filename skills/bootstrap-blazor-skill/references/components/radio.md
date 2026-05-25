# Radio 单选框

## 概述

Radio 单选框组件用于在一组备选项中进行单选。由于选项默认可见，不宜过多，若选项过多，建议使用 Select 选择器。

> Radio component is used for single selection among a group of options.

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/radio](https://www.blazor.zone/radio)

---

## 使用场景

### 1. 基础用法

选项默认可见，不宜过多。通过 `Items` 参数设置单选选项。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" />

@code {
    private string? SelectedValue { get; set; }
    private List<SelectedItem> RadioItems { get; set; } = new()
    {
        new SelectedItem("选项一", "选项一"),
        new SelectedItem("选项二", "选项二")
    };
}
```

### 2. 自动选择第一候选项

通过设置 `AutoSelectFirstWhenValueIsNull` 参数控制 RadioList 候选项选中情况，参数默认值为 `true`，即如果组件当前值与候选项中值无一致值时，自动选中第一个候选项，设置为 `false` 后，候选项将全部为未选中状态。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" AutoSelectFirstWhenValueIsNull="false" />

@code {
    private string? SelectedValue { get; set; }
    private List<SelectedItem> RadioItems { get; set; } = new()
    {
        new SelectedItem("选项一", "选项一"),
        new SelectedItem("选项二", "选项二")
    };
}
```

### 3. 禁用单选框

通过 `IsDisabled="true"` 单选框不可用状态。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" IsDisabled="true" />
```

### 4. Label 文字

单选框显示文字。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" ShowLabel="true" />
```

### 5. 按钮组

通过设定 `IsButton` 值为 `True` 将候选项更改为按钮样式。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" IsButton="true" />
```

### 6. 竖向排列

通过设置 `IsVertical` 使组件内部竖向排列。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" IsVertical="true" />
```

### 7. 绑定枚举类型

通过双向绑定 `Value` 无需设置 `Items`。

```razor
<RadioList TValue="EnumEducation" @bind-Value="SelectedEducation" />

@code {
    private EnumEducation SelectedEducation { get; set; } = EnumEducation.Primary;
    
    public enum EnumEducation
    {
        [Description("小学")]
        Primary,
        [Description("中学")]
        Middle,
        [Description("大学")]
        University
    }
}
```

### 8. 自动添加空值

通过设置 `IsAutoAddNullItem` 自动添加空值选项，通过设置 `NullItemText` 自定义空值选项。

```razor
<RadioList TValue="EnumEducation?" @bind-Value="SelectedEducation" 
           IsAutoAddNullItem="true" 
           NullItemText="空值" />

@code {
    private EnumEducation? SelectedEducation { get; set; }
}
```

### 9. 项目模板

通过设置 `ItemTemplate` 自定义显示 UI。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue">
    <ItemTemplate>
        <div class="d-flex align-items-center">
            <i class="fa-solid fa-star me-1"></i>
            <span>@context.Text</span>
        </div>
    </ItemTemplate>
</RadioList>
```

### 10. 颜色

通过设置 `Color` 属性改变组件背景色。

```razor
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" Color="Color.Primary" />
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" Color="Color.Success" />
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" Color="Color.Danger" />
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" Color="Color.Warning" />
<RadioList TValue="string" Items="RadioItems" @bind-Value="SelectedValue" Color="Color.Info" />
```

### 11. 泛型支持

通过使用 `RadioListGeneric` 组件配合 `SelectedItem<TValue>` 开启泛型支持。

```razor
<RadioListGeneric TValue="int" Items="RadioItems" @bind-Value="SelectedValue" />

@code {
    private int SelectedValue { get; set; }
    private List<SelectedItem> RadioItems { get; set; } = new()
    {
        new SelectedItem("1", "Item1"),
        new SelectedItem("2", "Item2"),
        new SelectedItem("3", "Item3")
    };
}
```

---

## 参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| AdditionalAttributes | 获得/设置 用户自定义属性 | IDictionary<string, Object> | — |
| AutoSelectFirstWhenValueIsNull | 获得/设置 未设置选中项时是否自动选择第一项，默认为 true | bool | true |
| CheckboxItemClass | 获得/设置 Checkbox 组件布局样式 | string | — |
| Color | 获得/设置 按钮颜色 默认为 None 未设置 | Color | None |
| DisplayText | 获得/设置 显示名称 | string | — |
| Id | 获得/设置 组件 id 属性 | string | — |
| IsAutoAddNullItem | 获得/设置 值为可为空枚举类型时是否自动添加空值，默认为 false | bool | false |
| IsButton | 获得/设置 是否为按钮样式 默认 false | bool | false |
| IsDisabled | 获得/设置 是否禁用 默认为 false | bool | false |
| IsVertical | 获得/设置 是否为竖向排列 默认为 false | bool | false |
| Items | 获得/设置 数据源 | IEnumerable<SelectedItem> | — |
| ItemTemplate | 获得/设置 项模板 | RenderFragment<SelectedItem> | — |
| MaxSelectedCount | 获得/设置 最多选中数量 | int | — |
| NullItemText | 获得/设置 空值项显示文字，默认为 "" | string | — |
| OnMaxSelectedCountExceed | 获得/设置 超过最大选中数量时回调委托 | Func<Task> | — |
| OnSelectedChanged | 获得/设置 SelectedItemChanged 方法 | Func<IEnumerable<SelectedItem>, TValue, Task> | — |
| OnValueChanged | 获得/设置 Value 改变时回调方法 | Func<TValue, Task> | — |
| ParsingErrorMessage | 获得/设置 类型转化失败格式化字符串 默认为 null | string | null |
| RequiredErrorMessage | 获得/设置 必填项错误文本 默认为 null 未设置 | string | null |
| ShowBorder | 获得/设置 非按钮模式下是否显示组件边框 默认为 true | bool | true |
| ShowButtonBorderColor | 获得/设置 是否显示按钮边框颜色 默认为 false | bool | false |
| ShowLabel | 获得/设置 是否显示前置标签，默认值为 null，为空时不显示标签 | Nullable<bool> | null |
| ShowLabelTooltip | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null | Nullable<bool> | null |
| ShowRequired | 获得/设置 是否显示必填项标记 默认为 null 未设置 | Nullable<bool> | null |
| SkipValidate | 获得/设置 是否不进行验证 默认为 false | bool | false |
| ValidateRules | 获得/设置 自定义验证集合 | List<IValidator> | — |
| Value | 获得/设置 输入组件的值，支持双向绑定 | TValue | — |
| ValueChanged | 获得/设置 用于更新绑定值的回调 | EventCallback<TValue> | — |
| ValueExpression | 获得/设置 标识绑定值的表达式 | Expression<Func<TValue>> | — |

---

## 事件回调

| 事件名称 | 说明 | 回调类型 |
|---------|------|---------|
| OnMaxSelectedCountExceed | 超过最大选中数量时回调委托 | Func<Task> |
| OnSelectedChanged | SelectedItemChanged 方法 | Func<IEnumerable<SelectedItem>, TValue, Task> |
| OnValueChanged | Value 改变时回调方法 | Func<TValue, Task> |

---

## 最佳实践

### 与表单验证配合使用

RadioList 组件支持表单验证，可以通过 `ValidateRules` 设置验证规则：

```razor
<ValidateForm Model="Model">
    <RadioList TValue="string" 
             Items="RadioItems" 
             @bind-Value="Model.Education"
             ShowLabel="true"
             ShowRequired="true">
    </RadioList>
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>

@code {
    private Model Model { get; set; } = new();
    
    private List<SelectedItem> RadioItems { get; set; } = new()
    {
        new SelectedItem("小学", "小学"),
        new SelectedItem("中学", "中学"),
        new SelectedItem("大学", "大学")
    };
    
    public class Model
    {
        [Required(ErrorMessage = "请选择学历")]
        public string? Education { get; set; }
    }
}
```

### 按钮样式单选框

使用 `IsButton="true"` 可以将单选框渲染为按钮组样式：

```razor
<RadioList TValue="string" 
         Items="RadioItems" 
         @bind-Value="SelectedValue"
         IsButton="true"
         Color="Color.Primary">
    <ItemTemplate>
        <span>@context.Text</span>
    </ItemTemplate>
</RadioList>
```

---

## 常见问题

### 1. 如何绑定枚举类型？

直接设置 `TValue` 为枚举类型，无需设置 `Items` 参数，组件会自动根据枚举生成选项。

### 2. 如何实现竖向排列？

设置 `IsVertical="true"` 即可实现竖向排列。

### 3. 如何自定义选项显示？

使用 `ItemTemplate` 模板可以自定义每个选项的显示内容。

### 4. 如何添加空值选项？

设置 `IsAutoAddNullItem="true"` 和 `NullItemText="请选择"` 可以自动添加空值选项。

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | Radio 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/radio)
- [Select 组件文档](https://www.blazor.zone/select)
- [CheckboxList 组件文档](https://www.blazor.zone/checkbox-list)
