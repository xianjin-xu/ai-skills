# MultiSelect 多项选择器

## 概述

MultiSelect 多项选择器组件用于进行多项选项时，使用下拉菜单展示并提供搜索多项选择内容。

> MultiSelect component is used for multi-option selection, using dropdown menu to display and provide search for multi-select content.

**分类**: 表单组件
**在线演示**: [https://www.blazor.zone/multi-select](https://www.blazor.zone/multi-select)

---

## 使用场景

### 1. 基础用法 - 颜色

提供各种颜色的多选下拉框。

```razor
<MultiSelect TValue="string" Items="Colors" @bind-Value="SelectedColor">
    <ItemTemplate>
        <div style="color: @context.Value">@context.Text</div>
    </ItemTemplate>
</MultiSelect>

@code {
    private string? SelectedColor { get; set; }
    private IEnumerable<SelectedItem> Colors { get; set; } = new List<SelectedItem>
    {
        new SelectedItem("primary", "Primary"),
        new SelectedItem("success", "Success"),
        new SelectedItem("warning", "Warning"),
        new SelectedItem("danger", "Danger")
    };
}
```

### 2. 单行显示

通过设置 `IsSingleLine="true"` 使组件始终渲染成一行。候选项过多时，组件横向布局，鼠标悬浮组件上时显示横向滚动条进行数据滚动。

```razor
<MultiSelect TValue="string" Items="Items" IsSingleLine="true" />
```

### 3. 双向绑定值 - 字符串

绑定一个逗号字符串分割的字符串。MultiSelect 组件数据源 `Items` 与选中值 `SelectedItemsValue` 均支持双向绑定。

```razor
<MultiSelect TValue="string" Items="Items" @bind-Value="SelectedStringValue" />

@code {
    private string? SelectedStringValue { get; set; }
    private IEnumerable<SelectedItem> Items { get; set; } = new List<SelectedItem>();
}
```

### 4. 双向绑定值 - 集合

绑定一个泛型 `IEnumerable<TValue>` 集合。

```razor
<MultiSelect TValue="SelectedItem" Items="Items" @bind-Value="SelectedArrayValues" />

@code {
    private IEnumerable<SelectedItem>? SelectedArrayValues { get; set; }
    private IEnumerable<SelectedItem> Items { get; set; } = new List<SelectedItem>();
}
```

### 5. 双向绑定值 - 数组

绑定一个数组 `int[]`。

```razor
<MultiSelect TValue="int" Items="IntItems" @bind-Value="SelectedIntArrayValues" />

@code {
    private int[]? SelectedIntArrayValues { get; set; }
    private IEnumerable<SelectedItem> IntItems { get; set; } = new List<SelectedItem>();
}
```

### 6. 双向绑定 - 枚举集合

绑定一个泛型 `IEnumerable<TValue>` 集合。本例中通过双向绑定 `SelectedEnumValues` 集合变量，通过下拉框选择更改其值。枚举类型时无需设置 `Items` 参数，额外功能是组件内部会尝试查找资源文件或者 `DisplayAttribute` 与 `DescriptionAttribute` 标签尝试进行本地化翻译工作。

```razor
<MultiSelect TValue="EnumType" Items="null" @bind-Value="SelectedEnumValues" />

@code {
    private IEnumerable<EnumType>? SelectedEnumValues { get; set; }

    public enum EnumType
    {
        [Display(Name = "小学")]
        Primary,
        [Display(Name = "中学")]
        Middle
    }
}
```

### 7. Flags 枚举

绑定值为 `Enum` 数据类型时，如果枚举有 `Flags` 标签时，自动支持多选模式。

```razor
<MultiSelect TValue="MultiSelectEnumFoo" @bind-Value="SelectedFlagsValue" />

@code {
    private MultiSelectEnumFoo SelectedFlagsValue { get; set; }

    [Flags]
    private enum MultiSelectEnumFoo
    {
        One = 1,
        Two = 2,
        Three = 4,
        Four = 8
    }
}
```

### 8. 搜索功能

通过设置 `ShowSearch` 值开启搜索功能。本例中设置搜索回调委托方法 `OnSearchTextChanged` 进行自定义搜索结果，如果未设置时内部使用显示文本进行模糊匹配。

```razor
<MultiSelect TValue="string" Items="Items" ShowSearch="true" OnSearchTextChanged="OnSearch" />

@code {
    private Task<IEnumerable<SelectedItem>> OnSearch(string searchText)
    {
        // 自定义搜索逻辑
        var items = Items.Where(i => i.Text.Contains(searchText));
        return Task.FromResult(items);
    }
}
```

### 9. 分组

通过设置 `GroupItemTemplate` 将下拉框中的备选项进行分组显示。

```razor
<MultiSelect TValue="string" Items="GroupedItems">
    <GroupItemTemplate>
        <div class="group-header">@context</div>
    </GroupItemTemplate>
</MultiSelect>
```

### 10. 禁用功能

通过设置 `IsDisabled` 值设置组件禁用状态。禁用状态时组件无任何响应。

```razor
<MultiSelect TValue="string" Items="Items" IsDisabled="true" />
```

### 11. 选项改变时事件

通过设置 `OnSelectedItemsChanged` 回调方法获取当前选中数据集合改变事件。

```razor
<MultiSelect TValue="string" Items="Items" OnSelectedItemsChanged="OnSelectedItemsChanged" />

@code {
    private Task OnSelectedItemsChanged(IEnumerable<SelectedItem> items)
    {
        // 处理选中项改变
        return Task.CompletedTask;
    }
}
```

### 12. 客户端验证

下拉框未选择时，点击提交按钮时拦截。内置到 `ValidateForm` 组件时，自动开启客户端验证功能，绑定模型拥有 `Required` 标签。

```razor
<ValidateForm>
    <MultiSelect TValue="string" Items="Items" @bind-Value="SelectedValue" />
    <Button Text="提交" ButtonType="ButtonType.Submit" />
</ValidateForm>
```

### 13. 显示标签

组件双向绑定时会根据条件自动判断是否显示标签文字。前置标签显示规则与 `BootstrapInput` 组件一致。

```razor
<MultiSelect TValue="string" Items="Items" @bind-Value="SelectedValue" ShowLabel="true" />
```

### 14. 自定义 DisplayText

通过 `OnGetDisplayText` 自定义显示文本。

```razor
<MultiSelect TValue="YourType" Items="Items" OnGetDisplayText="GetDisplayText" />

@code {
    private string GetDisplayText(YourType item)
    {
        return item.Name;
    }
}
```

### 15. 全选与反选按钮

通过参数 `ShowToolbar` 控制是否显示工具栏，通过参数 `ShowDefaultButtons` 控制是否显示内置的三个按钮，通过参数 `ShowSearch` 控制是否显示搜索栏。

```razor
<MultiSelect TValue="string" Items="Items" ShowToolbar="true" ShowDefaultButtons="true" ShowSearch="true" />
```

### 16. 设置选项最大数与最小数

通过设置 `Max`、`Min` 值设置组件可选项数量限制。

```razor
<!-- 最多可选择两个选项 -->
<MultiSelect TValue="string" Items="Items" Max="2" />

<!-- 最少选择两个选项 -->
<MultiSelect TValue="string" Items="Items" Min="2" />
```

### 17. 扩展工具栏按钮

通过设置 `ButtonTemplate` 自定义工具栏按钮实现自定义功能。

```razor
<MultiSelect TValue="string" Items="Items" ShowToolbar="true">
    <ButtonTemplate>
        <Button Text="自定义按钮" IsOutline="true" OnClick="OnCustomButtonClick" />
    </ButtonTemplate>
</MultiSelect>
```

### 18. 级联绑定

通过选择第一个下拉框不同选项，第二个下拉框动态填充内容。本例中点击第一个下拉框，可以通过异步方法获取第二个多选框的数据源，进行赋值后，调用 `StateHasChanged` 进行对多选框重新渲染。

```razor
<MultiSelect TValue="string" Items="FirstItems" @bind-Value="FirstValue" OnSelectedItemsChanged="OnFirstChanged" />
<MultiSelect TValue="string" Items="SecondItems" @bind-Value="SecondValue" />

@code {
    private async Task OnFirstChanged(IEnumerable<SelectedItem> items)
    {
        // 异步获取第二个下拉框的数据
        SecondItems = await GetSecondItemsAsync();
        StateHasChanged();
    }
}
```

### 19. 选项模板

通过设置 `ItemTemplate` 设置下拉框中选项模板，可以自定义样式。

```razor
<MultiSelect TValue="string" Items="Items">
    <ItemTemplate>
        <div class="custom-item">
            <i class="fa-solid fa-user"></i>
            <span>@context.Text</span>
        </div>
    </ItemTemplate>
</MultiSelect>
```

### 20. 显示模板

通过设置 `DisplayTemplate` 模板自定义显示样式。

```razor
<MultiSelect TValue="string" Items="Items">
    <DisplayTemplate>
        <div class="selected-display">
            @foreach (var item in context)
            {
                <span class="badge">@item.Text</span>
            }
        </div>
    </DisplayTemplate>
</MultiSelect>
```

### 21. 悬浮弹窗

通过设置 `IsPopover` 参数，组件使用 popover 渲染 UI 防止由于父容器设置 `overflow: hidden;` 使弹窗无法显示问题。

```razor
<MultiSelect TValue="string" Items="Items" IsPopover="true" />
```

### 22. 可编辑

通过设置 `IsEditable` 参数，使组件可编辑。通过设置 `EditSubmitKey` 参数可以指定通过 Enter 还是 Space 进行提交。

```razor
<MultiSelect TValue="string" Items="Items" IsEditable="true" EditSubmitKey="EditSubmitKey.Enter" />
```

### 23. 虚拟滚动

通过设置 `IsVirtualize` 参数开启组件虚拟功能特性。组件虚拟滚动支持两种形式：通过 `Items` 或者 `OnQueryAsync` 回调方法提供数据。

```razor
<!-- 1. 使用 OnQueryAsync 作为数据源 -->
<MultiSelect TValue="YourType" IsVirtualize="true" OnQueryAsync="OnQueryAsync" />

<!-- 2. 使用 Items 作为数据源 -->
<MultiSelect TValue="YourType" IsVirtualize="true" Items="LargeItems" />
```

---

## 参数 (Parameters)

### MultiSelect 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `ButtonTemplate` | `RenderFragment?` | `null` | 获得/设置 扩展按钮模板 |
| `ClearIcon` | `string?` | `fa-solid fa-angle-up` | 获得/设置 右侧清除图标 |
| `ClearText` | `string?` | `null` | 获得/设置 全选按钮显示文本 |
| `CloseButtonIcon` | `string?` | `null` | 获得/设置 关闭按钮图标 |
| `Color` | `Color` | `Color.None` | 获得/设置 颜色 |
| `CustomClass` | `string?` | `null` | 获得/设置 自定义样式 |
| `DefaultVirtualizeItemText` | `string?` | `null` | 获得/设置 默认虚拟滚动项文本 |
| `DisplayTemplate` | `RenderFragment<List<SelectedItem>>?` | `null` | 获得/设置 显示部分模板 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `DropdownIcon` | `string?` | `fa-solid fa-angle-up` | 获得/设置 下拉图标 |
| `EditSubmitKey` | `EditSubmitKey` | `EditSubmitKey.Enter` | 获得/设置 编辑提交按键 |
| `GroupItemTemplate` | `RenderFragment<string>?` | `null` | 获得/设置 分组项模板 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsClearable` | `bool` | `false` | 获得/设置 选择组件是否可以清除 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `IsEditable` | `bool` | `false` | 获得/设置 选择组件是否可编辑 |
| `IsFixedHeight` | `bool` | `false` | 获得/设置 是否固定高度 |
| `IsMarkupString` | `bool` | `false` | 获得/设置 内容是否为 MarkupString |
| `IsPopover` | `bool` | `false` | 获得/设置 是否使用 Popover 渲染下拉框 |
| `IsSingleLine` | `bool` | `false` | 获得/设置 是否为单行模式 |
| `IsVirtualize` | `bool` | `false` | 获得/设置 是否启用虚拟滚动 |
| `Items` | `IEnumerable<SelectedItem>?` | `null` | 获得/设置 项目集合 |
| `ItemTemplate` | `RenderFragment<SelectedItem>?` | `null` | 获得/设置 项目模板 |
| `Max` | `int` | `0` | 获得/设置 选项最大数，默认为 0 不限制 |
| `MaxErrorMessage` | `string?` | `null` | 获得/设置 设置最大值时错误消息文字 |
| `Min` | `int` | `0` | 获得/设置 选项最小数，默认为 0 不限制 |
| `MinErrorMessage` | `string?` | `null` | 获得/设置 设置最小值时错误消息文字 |
| `NoSearchDataText` | `string?` | `null` | 获得/设置 未找到搜索结果时显示的文本 |
| `Offset` | `string?` | `[0, 10]` | 获得/设置 弹窗偏移量 |
| `OnClearAsync` | `Func<Task>?` | `null` | 获得/设置 当清除按钮被点击时的回调方法 |
| `OnEditCallback` | `Func<string, Task<SelectedItem>>?` | `null` | 获得/设置 编辑模式下输入选项更新后回调方法 |
| `OnQueryAsync` | `Func<VirtualizeQueryOption, Task<QueryData<SelectedItem>>>?` | `null` | 获得/设置 加载虚拟化项目的回调方法 |
| `OnSearchTextChanged` | `Func<string, IEnumerable<SelectedItem>>?` | `null` | 获得/设置 搜索文本改变时的回调方法 |
| `OnSelectedItemsChanged` | `Func<IEnumerable<SelectedItem>, Task>?` | `null` | 获得/设置 选中项集合发生改变时回调委托方法 |
| `OnValueChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `OverscanCount` | `int` | `4` | 获得/设置 虚拟滚动的超限显示数量 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 |
| `PlaceHolder` | `string?` | `null` | 获得/设置 placeholder 文本 |
| `Placement` | `Placement` | `Placement.Bottom` | 获得/设置 弹窗位置 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 |
| `ReverseSelectText` | `string?` | `null` | 获得/设置 全选按钮显示文本 |
| `RowHeight` | `float` | `33` | 获得/设置 虚拟滚动的行高度 |
| `ScrollIntoViewBehavior` | `ScrollIntoViewBehavior` | `None` | 获得/设置 滚动行为 |
| `SearchIcon` | `string?` | `null` | 获得/设置 搜索图标 |
| `SearchLoadingIcon` | `string?` | `null` | 获得/设置 搜索加载图标 |
| `SelectAllText` | `string?` | `null` | 获得/设置 全选按钮显示文本 |
| `ShowCloseButton` | `bool` | `true` | 获得/设置 是否显示关闭按钮 |
| `ShowDefaultButtons` | `bool` | `true` | 获得/设置 是否显示默认功能按钮 |
| `ShowLabel` | `bool?` | `null` | 获得/设置 是否显示前置标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置 是否显示 Tooltip |
| `ShowRequired` | `bool?` | `null` | 获得/设置 是否显示必填项标记 |
| `ShowSearch` | `bool` | `false` | 获得/设置 是否显示搜索框 |
| `ShowShadow` | `bool` | `true` | 获得/设置 是否显示阴影 |
| `ShowToolbar` | `bool` | `false` | 获得/设置 是否显示功能按钮 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 |
| `StringComparison` | `StringComparison` | `StringComparison.OrdinalIgnoreCase` | 获得/设置 字符串比较规则 |
| `ValidateRules` | `List<IValidator>` | `{}` | 获得/设置 自定义验证集合 |
| `Value` | `TValue?` | `null` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<TValue>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<TValue>>?` | `null` | 获得/设置 标识绑定值的表达式 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnSelectedItemsChanged` | 选中项集合发生改变时的回调委托方法 |
| `OnValueChanged` | Value 改变时回调方法 |
| `OnClearAsync` | 当清除按钮被点击时的回调方法 |
| `OnEditCallback` | 编辑模式下输入选项更新后回调方法 |
| `OnQueryAsync` | 加载虚拟化项目的回调方法 |
| `OnSearchTextChanged` | 搜索文本改变时的回调方法 |

---

## 最佳实践

### 1. 数据源设置

MultiSelect 支持两种数据源设置方式：
- 使用 `Items` 参数直接提供数据集合
- 使用 `OnQueryAsync` 回调方法异步加载数据（推荐用于大数据量）

### 2. 双向绑定

支持多种绑定方式：
- 字符串：`@bind-Value="stringValue"` （逗号分隔）
- 集合：`@bind-Value="IEnumerable<T>"`
- 数组：`@bind-Value="T[]"`

### 3. 搜索功能

设置 `ShowSearch="true"` 开启搜索，可实现：
- 客户端搜索（默认使用显示文本模糊匹配）
- 服务端搜索（通过 `OnSearchTextChanged` 回调自定义搜索逻辑）

### 4. 验证集成

在 `ValidateForm` 中使用时，自动启用客户端验证。可通过以下方式自定义验证：
- 使用 `Required` 标签
- 使用 `ValidateRules` 参数添加自定义验证规则
- 使用 `Max`/`Min` 限制选择数量

### 5. 虚拟滚动

对于大数据量（>100 项），建议启用虚拟滚动：
```razor
<MultiSelect TValue="YourType" IsVirtualize="true" OnQueryAsync="OnQueryAsync" />
```

### 6. 级联选择

实现级联选择时，在第一个下拉框的 `OnSelectedItemsChanged` 中：
1. 异步加载第二个下拉框的数据
2. 更新 `Items` 集合
3. 调用 `StateHasChanged()` 重新渲染

---

## 常见问题 (FAQ)

### Q1: 如何获取选中的值？

**A**: 使用 `@bind-Value` 双向绑定选中值，或通过 `Value` 参数绑定。

```razor
<MultiSelect TValue="string" Items="Items" @bind-Value="SelectedValue" />

@code {
    private string? SelectedValue { get; set; }
}
```

### Q2: 如何限制选择数量？

**A**: 使用 `Max` 和 `Min` 参数限制选择数量。

```razor
<!-- 最多选择 3 项 -->
<MultiSelect TValue="string" Items="Items" Max="3" />

<!-- 最少选择 1 项 -->
<MultiSelect TValue="string" Items="Items" Min="1" />
```

### Q3: 如何自定义搜索逻辑？

**A**: 设置 `OnSearchTextChanged` 回调方法自定义搜索。

```razor
<MultiSelect TValue="string" Items="Items" ShowSearch="true" OnSearchTextChanged="OnSearch" />

@code {
    private Task<IEnumerable<SelectedItem>> OnSearch(string searchText)
    {
        var result = Items.Where(i => i.Text.Contains(searchText));
        return Task.FromResult(result);
    }
}
```

### Q4: 如何显示全选/反选按钮？

**A**: 设置 `ShowToolbar="true"` 和 `ShowDefaultButtons="true"`。

```razor
<MultiSelect TValue="string" Items="Items" ShowToolbar="true" ShowDefaultButtons="true" />
```

### Q5: 如何处理大数据量？

**A**: 启用虚拟滚动 `IsVirtualize="true"` 并使用 `OnQueryAsync` 异步加载。

```razor
<MultiSelect TValue="YourType" IsVirtualize="true" OnQueryAsync="OnQueryAsync" />

@code {
    private Task<QueryData<YourType>> OnQueryAsync(VirtualizeQueryOption option)
    {
        // 异步加载数据
        return Task.FromResult(new QueryData<YourType>());
    }
}
```

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 MultiSelect 组件 |
| 8.0 | 新增 `IsVirtualize` 虚拟滚动支持 |
| 8.0 | 新增 `IsPopover` 参数 |
