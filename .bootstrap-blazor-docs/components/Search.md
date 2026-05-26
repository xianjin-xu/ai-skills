# Search 搜索框

## 概述

Search 搜索框组件用于数据搜索，支持输入部分数据进行搜索、显示清空按钮、模板自定义、键盘输入即时搜索等功能。

> Search component is used for data search, supports searching with partial data input, showing clear button, template customization, keyboard input instant search and other features.

**分类**: 表单组件
**在线演示**: [https://www.blazor.zone/search](https://www.blazor.zone/search)

---

## 使用场景

### 1. 基础用法

输入部分数据进行搜索，通过设置 `IsAutoFocus="true"` 开启自动获得焦点功能。

```razor
<Search IsAutoFocus="true"
        PlaceHolder="请输入关键词搜索"
        OnSearch="OnSearch"
        IsSelectAllTextOnFocus="true"></Search>

@code {
    private async Task<IEnumerable<string>> OnSearch(string? searchText)
    {
        // 模拟搜索逻辑
        await Task.Delay(100);
        return new List<string> { "结果1", "结果2", "结果3" };
    }
}
```

### 2. 显示清空按钮

通过设置 `ShowClearButton` 参数控制是否显示清空按钮。

```razor
<Search PlaceHolder="请输入关键词搜索"
        ShowClearButton="true"
        OnSearch="OnDisplaySearch"></Search>

@code {
    private async Task<IEnumerable<string>> OnDisplaySearch(string? searchText)
    {
        await Task.Delay(100);
        return new List<string> { "结果1", "结果2" };
    }
}
```

### 3. 模板自定义

通过设置 `ItemTemplate` 配合泛型数据可以做出自己想要的任何效果。本例中通过搜索任意关键字，后台调用任意第三方搜索结果并且进行展示，选中搜索项后通过 `OnSelectedItemChanged` 回调方法可以自行处理。

```razor
<Search PlaceHolder="请输入关键词搜索"
        OnGetDisplayText="OnGetDisplayText"
        OnSearch="OnSearchFoo">
    <ItemTemplate>
        <div class="search-result">
            <div class="search-result-avatar">
                <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" alt="avatar" />
            </div>
            <div class="search-result-main">
                <div class="search-result-name">@context.Name</div>
                <div class="search-result-address">@context.Address</div>
            </div>
            <div class="search-result-circle">
                <Circle Value="context.Count" Color="Color.Info" StrokeWidth="4" Width="60" />
            </div>
        </div>
    </ItemTemplate>
</Search>

@code {
    private string OnGetDisplayText(YourItemType item)
    {
        return item.Name;
    }

    private async Task<IEnumerable<YourItemType>> OnSearchFoo(string? searchText)
    {
        // 调用搜索API
        await Task.Delay(100);
        return new List<YourItemType>();
    }
}
```

### 4. 键盘输入即时搜索

通过设置 `IsTriggerSearchByInput` 参数控制是否实时进行搜索操作，组件默认输入时即进行搜索，可通过 `IsTriggerSearchByInput="false"` 关闭。

```razor
<Search PlaceHolder="请输入关键词搜索"
        IsTriggerSearchByInput="false"
        OnSearch="OnKeyboardSearch"></Search>

@code {
    private async Task<IEnumerable<string>> OnKeyboardSearch(string? searchText)
    {
        await Task.Delay(100);
        return new List<string> { "结果1", "结果2" };
    }
}
```

### 5. 验证表单内使用

内置于 `ValidateForm` 使用，输入中文时不会多次触发搜索功能。

```razor
<ValidateForm>
    <Search @bind-Value="Model.Name" OnSearch="OnModelSearch"></Search>
</ValidateForm>

@code {
    [Required]
    public string? Name { get; set; }

    private async Task OnModelSearch(string? searchText)
    {
        await Task.Delay(100);
        // 处理搜索逻辑
    }
}
```

### 6. 显示前缀图标

通过设置 `ShowPrefixIcon` 参数控制是否显示前缀图标。可以通过 `PrefixIconTemplate` 自定义前缀，本例中通过前缀模板使用 SVG 图标。

```razor
<Search PlaceHolder="请输入关键词搜索"
        ShowPrefixIcon="true"
        PrefixIcon="fa-solid fa-magnifying-glass">
</Search>
```

### 7. 图标模板

通过设置 `IconTemplate` 自定义组件显示的图标。搜索组件上下文 `SearchContext<TValue>` 提供了组件内部的 `OnClear` `OnSearch` 方法。

```razor
<Search PlaceHolder="请输入关键词搜索" OnSearch="OnSearch">
    <IconTemplate>
        <i class="fa-solid fa-search"></i>
    </IconTemplate>
</Search>
```

### 8. 按钮模板

通过设置 `ButtonTemplate` 自定义组件显示的按钮。通过设置 `PrefixButtonTemplate` 自定义组件前置显示的按钮。在自定义模板中可以通过关联参数调用 Search 组件内部的 `OnClear` `OnSearch` 方法。

```razor
<Search PlaceHolder="请输入关键词搜索" OnSearch="OnSearch">
    <ButtonTemplate>
        <Button Icon="fa-solid fa-search" IsOutline="true"
                OnClick="async () => await Context.OnSearchAsync()">
            搜索
        </Button>
    </ButtonTemplate>
</Search>

@code {
    private async Task<IEnumerable<string>> OnSearch(string? searchText)
    {
        await Task.Delay(100);
        return new List<string>();
    }
}
```

### 9. 可清除

通过设置 `IsClearable="true"` 显示清空小图标。

```razor
<Search PlaceHolder="请输入关键词搜索"
        IsClearable="true"
        OnSearch="OnSearch"></Search>
```

---

## 参数 (Parameters)

### Search 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `ButtonTemplate` | `RenderFragment<SearchContext<TValue>>?` | `null` | 获得/设置 按钮模板 |
| `ClearButtonColor` | `Color` | `Color.Primary` | 获得/设置 清空按钮的颜色 |
| `ClearButtonIcon` | `string?` | `null` | 获得/设置 清空按钮的图标 |
| `ClearButtonText` | `string?` | `null` | 获得/设置 清空按钮的文本 |
| `ClearIcon` | `string?` | `fa-solid fa-angle-up` | 获得/设置 右侧清除图标 |
| `Color` | `Color` | `Color.None` | 获得/设置 按钮颜色 |
| `CustomClass` | `string?` | `null` | 获得/设置 自定义样式 |
| `Debounce` | `int` | `0` | 获得/设置 防抖时间，默认为 0 即不开启 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `FormatString` | `string?` | `null` | 获得/设置 格式字符串 |
| `Formatter` | `Func<TValue, string>?` | `null` | 获得/设置 格式化函数 |
| `IconTemplate` | `RenderFragment<SearchContext<TValue>>?` | `null` | 获得/设置 图标模板 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsAutoClearAfterSearch` | `bool` | `false` | 获得/设置 搜索后是否自动清空搜索框（已弃用） |
| `IsAutoFocus` | `bool` | `false` | 获得/设置 是否自动获取焦点 |
| `IsClearable` | `bool` | `false` | 获得/设置 选择组件是否可清除 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `IsPopover` | `bool` | `false` | 获得/设置 是否使用 Popover 渲染下拉框 |
| `IsSelectAllTextOnEnter` | `bool` | `false` | 获得/设置 是否在按下回车键时自动选择所有文本 |
| `IsSelectAllTextOnFocus` | `bool` | `false` | 获得/设置 是否在获取焦点时自动选择所有文本 |
| `IsTriggerSearchByInput` | `bool` | `true` | 获得/设置 搜索是否由输入触发 |
| `IsTrim` | `bool` | `false` | 获得/设置 是否自动去除空格 |
| `ItemTemplate` | `RenderFragment<TValue>?` | `null` | 获得/设置 候选项模板 |
| `NoDataTip` | `string?` | `无匹配数据` | 获得/设置 无匹配数据时显示提示信息 |
| `Offset` | `string?` | `[0, 10]` | 获得/设置 弹窗偏移量 |
| `OnBlurAsync` | `Func<TValue, Task>?` | `null` | 获得/设置 失去焦点时的回调方法 |
| `OnClear` | `Func<Task>?` | `null` | 获得/设置 点击清空按钮时的事件回调（已弃用） |
| `OnEnterAsync` | `Func<TValue, Task>?` | `null` | 获得/设置 回车键按下时的回调方法 |
| `OnEscAsync` | `Func<TValue, Task>?` | `null` | 获得/设置 Esc 键按下时的回调方法 |
| `OnGetDisplayText` | `Func<TValue, string>?` | `null` | 获得/设置 获取显示文本的回调方法 |
| `OnSearch` | `Func<string, Task<IEnumerable<TValue>>>?` | `null` | 获得/设置 点击搜索按钮时的回调委托 |
| `OnSelectedItemChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 下拉菜单选择回调方法 |
| `OnValueChanged` | `Func<TValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 |
| `PlaceHolder` | `string?` | `null` | 获得/设置 占位符属性值 |
| `Placement` | `Placement` | `Placement.Bottom` | 获得/设置 弹窗位置 |
| `PrefixButtonTemplate` | `RenderFragment<SearchContext<TValue>>?` | `null` | 获得/设置 前缀按钮模板 |
| `PrefixIcon` | `string?` | `null` | 获得/设置 前缀图标 |
| `PrefixIconTemplate` | `RenderFragment<SearchContext<TValue>>?` | `null` | 获得/设置 前缀图标模板 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 |
| `ScrollIntoViewBehavior` | `ScrollIntoViewBehavior` | `None` | 获得/设置 滚动行为 |
| `SearchButtonColor` | `Color` | `Color.Primary` | 获得/设置 搜索按钮的颜色 |
| `SearchButtonIcon` | `string?` | `null` | 获得/设置 搜索按钮的图标 |
| `SearchButtonLoadingIcon` | `string?` | `null` | 获得/设置 搜索按钮的加载图标 |
| `SearchButtonText` | `string?` | `null` | 获得/设置 搜索按钮的文本 |
| `ShowClearButton` | `bool` | `false` | 获得/设置 是否显示清空按钮 |
| `ShowLabel` | `bool?` | `null` | 获得/设置 是否显示前置标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置 是否显示 Tooltip |
| `ShowPrefixIcon` | `bool` | `false` | 获得/设置 是否显示前缀图标 |
| `ShowRequired` | `bool?` | `null` | 获得/设置 是否显示必填项标记 |
| `ShowSearchButton` | `bool` | `true` | 获得/设置 是否显示搜索按钮 |
| `ShowShadow` | `bool` | `true` | 获得/设置 是否显示阴影 |
| `SkipEnter` | `bool` | `false` | 获得/设置 是否跳过 Enter 按键处理 |
| `SkipEsc` | `bool` | `false` | 获得/设置 是否跳过 Esc 按键处理 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 |
| `ValidateRules` | `List<IValidator>` | `{}` | 获得/设置 自定义验证集合 |
| `Value` | `TValue?` | `null` | 获得/设置 输入组件的值 |
| `ValueChanged` | `EventCallback<TValue>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<TValue>>?` | `null` | 获得/设置 标识绑定值的表达式 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnSearch` | 点击搜索按钮或输入搜索时的回调，返回搜索结果集合 |
| `OnSelectedItemChanged` | 下拉菜单选择项变化时的回调 |
| `OnValueChanged` | 值改变时触发 |
| `OnClear` | 点击清空按钮时的事件回调（已弃用） |
| `OnEnterAsync` | 回车键按下时的回调方法 |
| `OnEscAsync` | Esc 键按下时的回调方法 |
| `OnBlurAsync` | 失去焦点时的回调方法 |

---

## 最佳实践

### 1. 搜索回调实现

必须实现 `OnSearch` 回调方法，返回 `Task<IEnumerable<TValue>>` 类型的结果集合。

```csharp
private async Task<IEnumerable<YourItemType>> OnSearch(string? searchText)
{
    // 调用搜索API
    var result = await SearchService.SearchAsync(searchText);
    return result;
}
```

### 2. 显示文本回调

实现 `OnGetDisplayText` 回调方法，返回搜索项的显示文本。

```csharp
private string OnGetDisplayText(YourItemType item)
{
    return item.Name;
}
```

### 3. 防抖处理

对于实时搜索场景，建议设置 `Debounce` 参数避免频繁调用搜索接口。

```razor
<Search Debounce="300" OnSearch="OnSearch"></Search>
```

### 4. 中文输入优化

在 `ValidateForm` 中使用时，组件会自动处理中文输入，避免多次触发搜索。

### 5. 自定义模板

使用 `ItemTemplate` 自定义搜索结果展示，使用 `ButtonTemplate` 自定义搜索按钮。

---

## 常见问题 (FAQ)

### Q1: 如何绑定选中值？

**A**: 使用 `Value` 参数绑定选中值，或使用 `@bind-Value` 双向绑定。

```razor
<Search @bind-Value="SelectedValue" OnSearch="OnSearch"></Search>
```

### Q2: 如何自定义搜索结果展示？

**A**: 使用 `ItemTemplate` 模板自定义搜索结果项的展示。

```razor
<Search OnSearch="OnSearch">
    <ItemTemplate>
        <div>@context.Name - @context.Description</div>
    </ItemTemplate>
</Search>
```

### Q3: 如何控制搜索触发方式？

**A**: 使用 `IsTriggerSearchByInput` 控制是否输入时即时搜索，使用 `ShowSearchButton` 控制是否显示搜索按钮。

```razor
<!-- 输入时即时搜索 -->
<Search IsTriggerSearchByInput="true" OnSearch="OnSearch"></Search>

<!-- 点击按钮才搜索 -->
<Search IsTriggerSearchByInput="false" ShowSearchButton="true" OnSearch="OnSearch"></Search>
```

### Q4: 如何清除搜索框？

**A**: 设置 `IsClearable="true"` 显示清除图标，或设置 `ShowClearButton="true"` 显示清除按钮。

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 Search 组件 |
| 8.0 | 新增 `Debounce` 参数，优化中文输入体验 |
