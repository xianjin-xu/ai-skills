# CheckboxList 多选框组

## 概述

CheckboxList 多选框组组件用于创建多选的复选框组，支持数据绑定、双向绑定、项目模板、按钮样式、泛型支持等功能。

> CheckboxList component is used to create multi-select checkbox groups, supports data binding, two-way binding, item templates, button style, generic support and other features.

**分类**: 表单组件
**在线演示**: [https://www.blazor.zone/checkboxlist](https://www.blazor.zone/checkboxlist)

---

## 使用场景

### 1. 基础用法

通过数据绑定展现复选框组。通过 `@bind-Value` 设置双向绑定数据值，通过 `Items` 设置候选数据源，通过 `OnSelectedChanged` 回调方法获取改变项实例。

```razor
<CheckboxList TValue="string" Items="Hobbies" @bind-Value="BindValue">
    <ItemTemplate>
        <div>@context.Text</div>
    </ItemTemplate>
</CheckboxList>

@code {
    private string? BindValue { get; set; }
    private IEnumerable<SelectedItem> Hobbies { get; set; } = new List<SelectedItem>
    {
        new SelectedItem("1", "Item 1"),
        new SelectedItem("2", "Item 2"),
        new SelectedItem("3", "Item 3"),
        new SelectedItem("4", "Item 4")
    };
}
```

### 2. 客户端验证

内置于 `ValidateForm` 中使用。本例中绑定模型 `BindItem` 的 `Name` 字段，通过勾选项自动更改模型数据。由于内置于 `ValidateForm` 表单内，本例中增加了 `RequiredAttribute` 必选要求验证，当取消所有选项后提示验证结果。

```razor
<ValidateForm>
    <CheckboxList TValue="string" Items="Items" @bind-Value="BindValue">
        <ItemTemplate>
            <div>@context.Text</div>
        </ItemTemplate>
    </CheckboxList>
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>

@code {
    [Required(ErrorMessage = "请至少选择一项")]
    private string? BindValue { get; set; }
}
```

### 3. 双向绑定集合

绑定值为集合。`TValue` 设置为 `IEnumerable<int>` 泛型集合，绑定集合的 `ValueField` 指定字段必须与泛型类型一致。

```razor
<CheckboxList TValue="int" Items="Items" @bind-Value="BindValue" />

@code {
    private IEnumerable<int>? BindValue { get; set; }
    private IEnumerable<SelectedItem> Items { get; set; } = new List<SelectedItem>
    {
        new SelectedItem("9", "Item 9"),
        new SelectedItem("10", "Item 10"),
        new SelectedItem("11", "Item 11"),
        new SelectedItem("12", "Item 12")
    };
}
```

`TValue` 设置为 `IEnumerable<string>` 泛型集合：

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" />

@code {
    private IEnumerable<string>? BindValue { get; set; }
    private IEnumerable<SelectedItem> Items { get; set; } = new List<SelectedItem>
    {
        new SelectedItem("13", "Item 13"),
        new SelectedItem("14", "Item 14"),
        new SelectedItem("15", "Item 15"),
        new SelectedItem("16", "Item 16")
    };
}
```

### 4. 项目模板

通过设置 `ItemTemplate` 自定义显示 UI。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue">
    <ItemTemplate>
        <div class="custom-checkbox-item">
            <i class="@(context.Selected ? "fa-solid fa-check-square" : "fa-regular fa-square")"></i>
            <span>@context.Text</span>
        </div>
    </ItemTemplate>
</CheckboxList>
```

### 5. 双向绑定枚举

绑定值为枚举。当 CheckboxList 绑定一个枚举集合时，`Items` 不需要指定，`Items` 会被自动设置成枚举里面所有的值，如果需要绑定部分值时，请自行提供枚举集合 `Items`。

```razor
<CheckboxList TValue="EnumType" Items="null" @bind-Value="BindValue" />

@code {
    private IEnumerable<EnumType>? BindValue { get; set; }

    public enum EnumType
    {
        [Display(Name = "小学")]
        Primary,
        [Display(Name = "中学")]
        Middle
    }
}
```

### 6. 无边框

通过设置 `ShowBorder="false"` 不显示边框。当验证失败时显示红色边框。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" ShowBorder="false" />
```

### 7. 竖向排列

通过设置 `IsVertical="true"` 使checkbox 竖向排列。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" IsVertical="true" />
```

### 8. 最大选择数量

通过设置 `MaxSelectedCount` 属性控制最大可选数量，通过 `OnMaxSelectedCountExceed` 回调处理逻辑。选中节点超过 2 个时，弹出 Toast 提示栏。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" MaxSelectedCount="2" OnMaxSelectedCountExceed="OnExceed" />

@code {
    private Task OnExceed()
    {
        // 处理超过最大选择数量的业务逻辑
        return Task.CompletedTask;
    }
}
```

### 9. 禁用

通过设置 `IsDisabled="true"` 禁用。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" IsDisabled="true" />
```

### 10. 按钮复选框

设置 `IsButton="true"`，将复选框样式改为按钮样式。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" IsButton="true" />
```

### 11. 泛型支持

通过 `CheckboxList<TValue>` 组件和 `SelectedItem<TValue>` 开启泛型支持。

```razor
<CheckboxList TValue="YourType" Items="Items" @bind-Value="BindValue" />

@code {
    private IEnumerable<YourType>? BindValue { get; set; }
    private IEnumerable<SelectedItem> Items { get; set; } = new List<SelectedItem>();
}
```

---

## 参数 (Parameters)

### CheckboxList 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `CheckboxItemClass` | `string?` | `null` | 获得/设置 Checkbox 组件布局样式 |
| `Color` | `Color` | `Color.None` | 获得/设置 按钮颜色 默认为 None 未设置 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsButton` | `bool` | `false` | 获得/设置 是否为按钮样式 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `IsVertical` | `bool` | `false` | 获得/设置 是否为竖向排列 |
| `Items` | `IEnumerable<SelectedItem>?` | `null` | 获得/设置 数据源 |
| `ItemTemplate` | `RenderFragment<SelectedItem>?` | `null` | 获得/设置 项模板 |
| `MaxSelectedCount` | `int` | `0` | 获得/设置 最多选中数量，0 表示不限制 |
| `OnMaxSelectedCountExceed` | `Func<Task>?` | `null` | 获得/设置 超过最大选中数量时回调委托 |
| `OnSelectedChanged` | `Func<IEnumerable<SelectedItem>, TValue, Task>?` | `null` | 获得/设置 SelectedItemChanged 方法 |
| `OnValueChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 |
| `ShowBorder` | `bool` | `true` | 获得/设置 非按钮模式下是否显示组件边框 |
| `ShowButtonBorderColor` | `bool` | `false` | 获得/设置 是否显示按钮边框颜色 |
| `ShowLabel` | `Nullable<bool>` | `null` | 获得/设置 是否显示前置标签 |
| `ShowLabelTooltip` | `Nullable<bool>` | `null` | 获得/设置 是否显示 Tooltip |
| `ShowRequired` | `Nullable<bool>` | `null` | 获得/设置 是否显示必填项标记 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 |
| `ValidateRules` | `List<IValidator>` | `{}` | 获得/设置 自定义验证集合 |
| `Value` | `TValue?` | `null` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<TValue>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<TValue>>?` | `null` | 获得/设置 标识绑定值的表达式 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnSelectedChanged` | 选中项发生改变时的回调方法 |
| `OnValueChanged` | Value 改变时回调方法 |
| `OnMaxSelectedCountExceed` | 超过最大选中数量时回调委托 |

---

## 最佳实践

### 1. 数据类型选择

CheckboxList 支持多种数据类型：
- **字符串**: `TValue="string"` - 逗号分隔的字符串
- **集合**: `TValue="IEnumerable<int>"` 或 `TValue="IEnumerable<string>"`
- **枚举**: `TValue="EnumType"` - 自动加载枚举值

### 2. 验证集成

在 `ValidateForm` 中使用时，自动启用客户端验证：
```razor
<ValidateForm>
    <CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" />
</ValidateForm>

@code {
    [Required(ErrorMessage = "请至少选择一项")]
    private string? BindValue { get; set; }
}
```

### 3. 按钮样式

设置 `IsButton="true"` 可将复选框改为按钮样式，适合多选标签场景：
```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" IsButton="true" />
```

### 4. 最大选择限制

通过 `MaxSelectedCount` 限制最多选择数量：
```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" MaxSelectedCount="3" />
```

### 5. 自定义模板

通过 `ItemTemplate` 自定义每个选项的显示样式：
```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue">
    <ItemTemplate>
        <div class="custom-item">@context.Text</div>
    </ItemTemplate>
</CheckboxList>
```

---

## 常见问题 (FAQ)

### Q1: 如何获取选中的值？

**A**: 使用 `@bind-Value` 双向绑定选中值。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" />

@code {
    private string? BindValue { get; set; }
}
```

### Q2: 如何限制最多选择数量？

**A**: 使用 `MaxSelectedCount` 参数。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" MaxSelectedCount="3" />
```

### Q3: 如何显示为按钮样式？

**A**: 设置 `IsButton="true"`。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue" IsButton="true" />
```

### Q4: 如何绑定枚举类型？

**A**: 设置 `TValue` 为枚举类型，`Items` 设为 `null`（自动加载）。

```razor
<CheckboxList TValue="EnumType" Items="null" @bind-Value="BindValue" />

@code {
    public enum EnumType { Primary, Middle }
}
```

### Q5: 如何自定义选项显示？

**A**: 使用 `ItemTemplate` 模板。

```razor
<CheckboxList TValue="string" Items="Items" @bind-Value="BindValue">
    <ItemTemplate>
        <div>@context.Text - Custom</div>
    </ItemTemplate>
</CheckboxList>
```

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 CheckboxList 组件 |
| 8.0 | 新增 `MaxSelectedCount` 和 `OnMaxSelectedCountExceed` 参数 |
