# AutoFill 自动填充组件

## 概述

`AutoFill` 是一个自动填充组件，通过智能感应提示选项，选中后自动填充表单。适用于需要在输入框中输入信息并快速选择预设值来自动填充表单的场景。

**命名空间**: `BootstrapBlazor.Components`

**泛型参数**: `TValue` - 值类型

**在线演示**: [https://www.blazor.zone/auto-fill](https://www.blazor.zone/auto-fill)

## 使用场景

### 1. 基本用法

填充表单：录入 Name 姓名智能提示，选择提示项后自动填充下方表单。

```razor
<AutoFill @bind-Value="Model.Name" Items="Items" 
           IsLikeMatch="true" 
           OnGetDisplayText="OnGetDisplayText">
    <ItemTemplate>
        <div class="d-flex">
            <div>
                <img src="@GetAvatarUrl(context.Id)" class="bb-avatar" />
            </div>
            <div class="ps-2">
                <div>@context.Name</div>
                <div class="bb-sub">@context.Title</div>
            </div>
        </div>
    </ItemTemplate>
</AutoFill>

@code {
    [NotNull]
    private List<Person>? Items { get; set; }

    private Person Model { get; set; } = new();

    private string OnGetDisplayText(Person item)
    {
        return item.Name;
    }

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<Person>
        {
            new Person { Id = 1, Name = "张三", Title = "经理" },
            new Person { Id = 2, Name = "李四", Title = "工程师" },
            new Person { Id = 3, Name = "王五", Title = "设计师" }
        };
    }
}
```

**说明**:
- 输入时智能提示匹配的选项
- 支持键盘 `Enter`、`Esc` 键操作
- 选中后自动填充绑定值

### 2. 自定义过滤条件

通过设置自定义过滤条件回调委托 `OnCustomFilter` 过滤数据。

```razor
<AutoFill @bind-Value="Model.Name" Items="Items" 
           OnCustomFilter="OnCustomFilter"
           OnGetDisplayText="OnGetDisplayText">
    <ItemTemplate>
        <div class="d-flex">
            <div>
                <img src="@GetAvatarUrl(context.Id)" class="bb-avatar" />
            </div>
            <div class="ps-2">
                <div>@context.Name</div>
                <div class="bb-sub">@context.Title</div>
            </div>
        </div>
    </ItemTemplate>
</AutoFill>

@code {
    private Task<IEnumerable<Person>> OnCustomFilter(string searchText)
    {
        // 自定义过滤逻辑：Name 包含输入字符串 并且 Id 大于 50
        var items = Items.Where(i => i.Name.Contains(searchText) && i.Id > 50);
        return Task.FromResult(items.AsEnumerable());
    }
}
```

**说明**:
- `OnCustomFilter` 返回过滤后的数据集合
- 可以实现复杂的过滤逻辑
- 当前示例过滤条件为：Name 包含输入字符串 并且 Id 大于 50

### 3. 关闭自动展开下拉框

通过设置 `ShowDropdownListOnFocus="false"` 参数，关闭组件获得焦点后自动展开候选项下拉框的特性。

```razor
<AutoFill @bind-Value="Model.Name" Items="Items" 
           ShowDropdownListOnFocus="false"
           OnGetDisplayText="OnGetDisplayText">
    <ItemTemplate>
        <div class="d-flex">
            <div>
                <img src="@GetAvatarUrl(context.Id)" class="bb-avatar" />
            </div>
            <div class="ps-2">
                <div>@context.Name</div>
                <div class="bb-sub">@context.Title</div>
            </div>
        </div>
    </ItemTemplate>
</AutoFill>
```

**说明**:
- `ShowDropdownListOnFocus` 默认值为 `true`
- 设置为 `false` 后，只有输入内容时才会显示下拉框
- 适用于不需要一开始就用下拉框打扰用户的场景

### 4. 虚拟滚动

通过设置 `IsVirtualize` 参数开启组件虚拟功能特性。组件虚拟滚动支持两种形式：通过 `Items` 或者 `OnQueryAsync` 回调方法提供数据。

```razor
<!-- 方式 1：使用 OnQueryAsync 作为数据源 -->
<AutoFill @bind-Value="Model.Name" 
           OnQueryAsync="OnQueryAsync"
           IsVirtualize="true" 
           RowHeight="58f"
           OnGetDisplayText="OnGetDisplayText">
    <ItemTemplate>
        <div class="d-flex">
            <div>
                <img src="@GetAvatarUrl(context.Id)" class="bb-avatar" />
            </div>
            <div class="ps-2">
                <div>@context.Name</div>
                <div class="bb-sub">@context.Title</div>
            </div>
        </div>
    </ItemTemplate>
</AutoFill>

<!-- 方式 2：使用 Items 作为数据源 -->
<AutoFill @bind-Value="Model.Name" 
           Items="Items"
           IsVirtualize="true" 
           RowHeight="58f"
           OnGetDisplayText="OnGetDisplayText">
    <ItemTemplate>
        <div class="d-flex">
            <div>
                <img src="@GetAvatarUrl(context.Id)" class="bb-avatar" />
            </div>
            <div class="ps-2">
                <div>@context.Name</div>
                <div class="bb-sub">@context.Title</div>
            </div>
        </div>
    </ItemTemplate>
</AutoFill>

@code {
    private async Task<QueryData<Person>> OnQueryAsync(VirtualizeQueryOption option)
    {
        // 虚拟滚动加载数据
        var items = await DataService.GetItemsAsync(option.StartIndex, option.Count);
        return new QueryData<Person>(items, items.Count());
    }
}
```

**说明**:
- `IsVirtualize="true"` 开启虚拟滚动
- `RowHeight="58f"` 设置行高（像素）
- 适用于大数据量场景，提升性能

## 参数

### AutoFill 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `ClearIcon` | 获得/设置 右侧清除图标，默认为 `fa-solid fa-angle-up` | `string` | `fa-solid fa-angle-up` |
| `Color` | 获得/设置 按钮颜色 | `Color` | - |
| `CustomClass` | 获得/设置 自定义样式，默认 `null` | `string` | `null` |
| `Debounce` | 获得/设置 防抖时间，默认为 0 即不开启 | `int` | `0` |
| `DisplayCount` | 获得/设置 匹配数据时显示的数量，默认为 `null` | `int?` | `null` |
| `DisplayText` | 获得/设置 显示名称 | `string` | `null` |
| `FormatString` | 获得/设置 格式字符串，例如 `"yyyy-MM-dd"` 用于日期类型 | `string` | `null` |
| `Formatter` | 获得/设置 格式化函数 | `Func<TValue, string>` | - |
| `Icon` | 获得/设置 图标 | `string` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `IgnoreCase` | 获得/设置 匹配时是否忽略大小写，默认为 `true` | `bool` | `true` |
| `IsAutoClearWhenInvalid` | 获得/设置 输入框内容无效时是否自动清空内容，默认 `false` | `bool` | `false` |
| `IsAutoFocus` | 获得/设置 是否自动获取焦点，默认值为 `false` | `bool` | `false` |
| `IsClearable` | 获得/设置 选择组件是否可清除，默认为 `false` | `bool` | `false` |
| `IsDisabled` | 获得/设置 是否禁用，默认为 `false` | `bool` | `false` |
| `IsLikeMatch` | 获得/设置 是否开启模糊搜索，默认为 `false` | `bool` | `false` |
| `IsPopover` | 获得/设置 是否使用 Popover 渲染下拉框，默认 `false` | `bool` | `false` |
| `IsSelectAllTextOnEnter` | 获得/设置 是否在按下回车键时自动选择所有文本，默认值为 `false` | `bool` | `false` |
| `IsSelectAllTextOnFocus` | 获得/设置 是否在获取焦点时自动选择所有文本，默认值为 `false` | `bool` | `false` |
| `IsTrim` | 获得/设置 是否自动去除空格，默认值为 `false` | `bool` | `false` |
| `IsVirtualize` | 获得/设置 是否开启虚拟滚动，默认为 `false` | `bool` | `false` |
| `Items` | 获得/设置 组件数据集合 | `IEnumerable<TValue>` | `null` |
| `ItemTemplate` | 获得/设置 候选项模板，默认 `null` | `RenderFragment<TValue>` | `null` |
| `LoadingIcon` | 获得/设置 加载图标 | `string` | - |
| `NoDataTip` | 获得/设置 无匹配数据时显示提示信息，默认提示"无匹配数据" | `string` | - |
| `Offset` | 获得/设置 弹窗偏移量，默认 `[0, 10]` | `string` | `[0, 10]` |
| `OnBlurAsync` | 获得/设置 失去焦点时的回调方法，默认值为 `null` | `Func<TValue, Task>` | `null` |
| `OnClearAsync` | 获得/设置 点击清除按钮回调方法，默认为 `null` | `Func<Task>` | `null` |
| `OnCustomFilter` | 获得/设置 自定义集合过滤规则 | `Func<string, Task<IEnumerable<TValue>>>` | - |
| `OnEnterAsync` | 获得/设置 回车键按下时的回调方法，默认值为 `null` | `Func<TValue, Task>` | `null` |
| `OnEscAsync` | 获得/设置 Esc 键按下时的回调方法，默认值为 `null` | `Func<TValue, Task>` | `null` |
| `OnGetDisplayText` | 获得/设置 获取显示文本方法，默认为使用 `ToString()` 方法 | `Func<TValue, string>` | - |
| `OnQueryAsync` | 获得/设置 虚拟滚动加载回调方法 | `Func<VirtualizeQueryOption, Task<QueryData<TValue>>>` | - |
| `OnSelectedItemChanged` | 获得/设置 下拉菜单选择回调方法，默认 `null` | `Func<TValue, Task>` | `null` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<TValue, Task>` | - |
| `OverscanCount` | 获得/设置 虚拟滚动预加载行数，默认为 3 | `int` | `3` |
| `ParsingErrorMessage` | 获得/设置 类型转化失败格式化字符串，默认为 `null` | `string` | `null` |
| `PlaceHolder` | 获得/设置 占位符属性值 | `string` | - |
| `Placement` | 获得/设置 弹窗位置，默认为 `Bottom` | `Placement` | `Bottom` |
| `RequiredErrorMessage` | 获得/设置 必填项错误文本，默认为 `null` 未设置 | `string` | `null` |
| `RowHeight` | 获得/设置 虚拟滚动行高，默认为 `50f` | `float` | `50f` |
| `ScrollIntoViewBehavior` | 获得/设置 滚动行为 | `ScrollIntoViewBehavior` | - |
| `ShowDropdownListOnFocus` | 获得/设置 获得焦点时是否展开下拉候选菜单，默认为 `true` | `bool` | `true` |
| `ShowLabel` | 获得/设置 是否显示前置标签，默认值为 `null`，为空时不显示标签 | `bool?` | `null` |
| `ShowLabelTooltip` | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 `null` | `bool?` | `null` |
| `ShowNoDataTip` | 获得/设置 是否显示无匹配数据选项，默认为 `true` | `bool` | `true` |
| `ShowRequired` | 获得/设置 是否显示必填项标记，默认为 `null` 未设置 | `bool?` | `null` |
| `ShowShadow` | 获得/设置 是否显示阴影，默认 `true` | `bool` | `true` |
| `SkipEnter` | 获得/设置 是否跳过 Enter 按键处理，默认 `false` | `bool` | `false` |
| `SkipEsc` | 获得/设置 是否跳过 Esc 按键处理，默认 `false` | `bool` | `false` |
| `SkipValidate` | 获得/设置 是否不进行验证，默认为 `false` | `bool` | `false` |
| `ValidateRules` | 获得/设置 自定义验证集合 | `List<IValidator>` | - |
| `Value` | 获得/设置 输入组件的值，支持双向绑定 | `TValue` | - |
| `ValueChanged` | 获得/设置 用于更新绑定值的回调 | `EventCallback<TValue>` | - |
| `ValueExpression` | 获得/设置 标识绑定值的表达式 | `Expression<Func<TValue>>` | - |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `ValueChanged` | 获得/设置 用于更新绑定值的回调 | `EventCallback<TValue>` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<TValue, Task>` |
| `OnSelectedItemChanged` | 获得/设置 下拉菜单选择回调方法 | `Func<TValue, Task>` |
| `OnCustomFilter` | 获得/设置 自定义集合过滤规则 | `Func<string, Task<IEnumerable<TValue>>>` |
| `OnQueryAsync` | 获得/设置 虚拟滚动加载回调方法 | `Func<VirtualizeQueryOption, Task<QueryData<TValue>>>` |
| `OnClearAsync` | 获得/设置 点击清除按钮回调方法 | `Func<Task>` |
| `OnBlurAsync` | 获得/设置 失去焦点时的回调方法 | `Func<TValue, Task>` |
| `OnEnterAsync` | 获得/设置 回车键按下时的回调方法 | `Func<TValue, Task>` |
| `OnEscAsync` | 获得/设置 Esc 键按下时的回调方法 | `Func<TValue, Task>` |

## 最佳实践

### 1. 使用 @bind-Value 简化绑定

推荐使用 `@bind-Value` 实现双向绑定，简化代码。

```razor
<!-- 推荐：使用 @bind-Value -->
<AutoFill @bind-Value="Model.Name" Items="Items" />

@code {
    private Person Model { get; set; } = new();
}

<!-- 不推荐：手动处理 ValueChanged -->
<AutoFill Value="Model.Name" ValueChanged="OnValueChanged" Items="Items" />

@code {
    private Person Model { get; set; } = new();

    private void OnValueChanged(Person value)
    {
        Model.Name = value;
        StateHasChanged();
    }
}
```

### 2. 设置 OnGetDisplayText 自定义显示文本

当 `TValue` 是复杂类型时，必须通过 `OnGetDisplayText` 指定如何获取显示文本。

```razor
<!-- 正确：设置 OnGetDisplayText -->
<AutoFill @bind-Value="Model.Person" 
           Items="Persons" 
           OnGetDisplayText="GetPersonName">

@code {
    private string GetPersonName(Person p) => p.Name;
}

<!-- 错误：未设置 OnGetDisplayText，显示的是 Person.ToString() -->
<AutoFill @bind-Value="Model.Person" Items="Persons" />
```

### 3. 虚拟滚动用于大数据量

当数据量超过 100 条时，建议使用虚拟滚动提升性能。

```razor
<AutoFill @bind-Value="Model.Item" 
           OnQueryAsync="LoadItems" 
           IsVirtualize="true" 
           RowHeight="50f">
    <ItemTemplate>
        <div>@context.Name</div>
    </ItemTemplate>
</AutoFill>

@code {
    private async Task<QueryData<Item>> LoadItems(VirtualizeQueryOption option)
    {
        // 分批加载数据
        var items = await DataService.GetPagedItems(option.StartIndex, option.Count);
        return new QueryData<Item>(items, totalCount);
    }
}
```

### 4. 防抖提升性能

当数据源较大或需要远程查询时，建议设置 `Debounce` 防抖时间。

```razor
<AutoFill @bind-Value="Model.Name" 
           OnQueryAsync="SearchAsync" 
           Debounce="300">
    <ItemTemplate>
        <div>@context.Name</div>
    </ItemTemplate>
</AutoFill>

@code {
    private async Task<QueryData<Person>> SearchAsync(VirtualizeQueryOption option)
    {
        // 输入停止 300ms 后才触发查询，避免频繁请求
        await Task.Delay(300);
        return await DataService.Search(option.SearchText);
    }
}
```

## 常见问题

### 1. 下拉框不显示

**问题**: 输入内容后，下拉框不显示候选项。

**原因**: 可能是 `Items` 未设置，或者 `IsLikeMatch="true"` 未开启模糊搜索。

**解决方案**:
- 确保已设置 `Items` 或 `OnQueryAsync`
- 如果需要模糊搜索，设置 `IsLikeMatch="true"`

```razor
<!-- 错误：缺少 Items -->
<AutoFill @bind-Value="Model.Name" />

<!-- 正确：设置 Items 并开启模糊搜索 -->
<AutoFill @bind-Value="Model.Name" Items="Items" IsLikeMatch="true" />
```

### 2. 选中后显示的是对象名称

**问题**: 选中选项后，输入框显示的是 `Person` 或 `MyClass` 而不是期望的名称。

**原因**: 未设置 `OnGetDisplayText`，默认使用 `ToString()` 方法。

**解决方案**: 设置 `OnGetDisplayText` 返回期望的显示文本。

```razor
<AutoFill @bind-Value="Model.Person" 
           Items="Persons" 
           OnGetDisplayText="p => p.Name" />
```

### 3. 虚拟滚动不工作

**问题**: 设置了 `IsVirtualize="true"` 但滚动时性能仍然很差。

**原因**: 可能是未正确实现 `OnQueryAsync`，或者 `RowHeight` 设置不正确。

**解决方案**:
- 确保使用 `OnQueryAsync` 分批加载数据
- 确保 `RowHeight` 与实际行高一致

```razor
<AutoFill @bind-Value="Model.Item" 
           OnQueryAsync="LoadItems" 
           IsVirtualize="true" 
           RowHeight="60f">  <!-- 与实际行高一致 -->
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | AutoFill 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 `IsVirtualize` 虚拟滚动支持；新增 `Debounce` 防抖参数 |
| 8.0.0 | 2024-11-10 | 新增 `OnCustomFilter` 自定义过滤；优化键盘操作逻辑 |

## 参考链接

- [Bootstrap Blazor 官方文档 - AutoFill](https://www.blazor.zone/auto-fill)
- [Bootstrap Blazor API - AutoFill](https://www.blazor.zone/api/AutoFill)
- [Bootstrap Blazor 官方文档 - AutoComplete](https://www.blazor.zone/auto-complete) (类似组件)
