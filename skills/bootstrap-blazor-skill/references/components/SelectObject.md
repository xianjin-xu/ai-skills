# SelectObject 任意选择器

## 概述

SelectObject 任意选择器组件是下拉框为任意组件的选择器，用于展示复杂类型的选择需求。下拉框内可以放置任意组件，需要通过回调进行赋值或者关窗。

> SelectObject component is a dropdown selector for arbitrary components, used to display complex type selection requirements.

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/select-object](https://www.blazor.zone/select-object)

---

## 使用场景

### 1. 基本功能

内置 ListView 组件选择图片。可通过 `IsClearable` 控制是否显示清除小按钮，默认值为 `false`。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName">
    <ChildContent>
        <ListView TItem="Foo" Items="Foos" OnListViewChanged="OnFooSelected">
            <ListItemTemplate>
                <div class="d-flex align-items-center">
                    <img src="@context.Icon" width="40" height="40" class="me-2" />
                    <span>@context.Name</span>
                </div>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>

@code {
    private Foo? SelectedFoo { get; set; }
    private List<Foo> Foos { get; set; } = new();
    
    private string GetFooName(Foo foo)
    {
        return foo?.Name ?? "";
    }
    
    private async Task OnFooSelected(Foo foo)
    {
        SelectedFoo = foo;
        await Task.CompletedTask;
    }
    
    public class Foo
    {
        public string? Name { get; set; }
        public string? Icon { get; set; }
    }
}
```

### 2. 设置最小宽度

通过设置 `DropdownMinWidth` 值，来改变下拉框最小宽度。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName"
            DropdownMinWidth="300">
    <ChildContent>
        <ListView TItem="Foo" Items="Foos" OnListViewChanged="OnFooSelected">
            <ListItemTemplate>
                <div class="d-flex align-items-center">
                    <img src="@context.Icon" width="40" height="40" class="me-2" />
                    <span>@context.Name</span>
                </div>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>
```

### 3. 设置高度

通过设置 `Height` 值，来改变下拉框高度。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName"
            Height="300">
    <ChildContent>
        <ListView TItem="Foo" Items="Foos" OnListViewChanged="OnFooSelected">
            <ListItemTemplate>
                <div class="d-flex align-items-center">
                    <img src="@context.Icon" width="40" height="40" class="me-2" />
                    <span>@context.Name</span>
                </div>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>
```

### 4. 自定义组件

任意组件均可放入下拉框内，需要有一个回调进行赋值或者关窗即可。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName">
    <ChildContent>
        <div class="p-3">
            <h5>自定义内容</h5>
            <p>这里可以放置任意组件</p>
            <Button Text="选择此项" OnClick="() => OnSelectItem(foo1)" />
        </div>
    </ChildContent>
</SelectObject>

@code {
    private Foo? SelectedFoo { get; set; }
    private Foo foo1 = new Foo { Name = "选项1", Icon = "icon1.png" };
    
    private string GetFooName(Foo foo)
    {
        return foo?.Name ?? "";
    }
    
    private async Task OnSelectItem(Foo foo)
    {
        SelectedFoo = foo;
        // 关闭下拉框需要通过级联参数
        if (OnCloseAsync != null)
        {
            await OnCloseAsync.Invoke();
        }
    }
    
    [CascadingParameter(Name = "SelectObjectCloseAsync")]
    private Func<Task>? OnCloseAsync { get; set; }
    
    public class Foo
    {
        public string? Name { get; set; }
        public string? Icon { get; set; }
    }
}
```

### 5. 可清除

通过设置 `IsClearable="true"` 显示清除按钮，允许清空选择。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName"
            IsClearable="true"
            OnClearAsync="OnClear">
    <ChildContent>
        <ListView TItem="Foo" Items="Foos" OnListViewChanged="OnFooSelected">
            <ListItemTemplate>
                <div class="d-flex align-items-center">
                    <img src="@context.Icon" width="40" height="40" class="me-2" />
                    <span>@context.Name</span>
                </div>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>

@code {
    private Foo? SelectedFoo { get; set; }
    private List<Foo> Foos { get; set; } = new();
    
    private string GetFooName(Foo foo)
    {
        return foo?.Name ?? "";
    }
    
    private async Task OnClear()
    {
        SelectedFoo = null;
        await Task.CompletedTask;
    }
    
    private async Task OnFooSelected(Foo foo)
    {
        SelectedFoo = foo;
        await Task.CompletedTask;
    }
}
```

### 6. 禁用状态

通过设置 `IsDisabled="true"` 禁用选择器。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName"
            IsDisabled="true">
    <ChildContent>
        <div class="p-3">禁用状态</div>
    </ChildContent>
</SelectObject>
```

### 7. 显示标签

通过设置 `ShowLabel="true"` 显示前置标签。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName"
            ShowLabel="true"
            PlaceHolder="请选择">
    <ChildContent>
        <ListView TItem="Foo" Items="Foos" OnListViewChanged="OnFooSelected">
            <ListItemTemplate>
                <span>@context.Name</span>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>
```

### 8. 弹窗位置

通过设置 `Placement` 参数控制弹窗位置，可选值为 `Top`、`Bottom`、`Left`、`Right`。

```razor
<SelectObject TItem="Foo" 
            Value="SelectedFoo" 
            GetTextCallback="GetFooName"
            Placement="Placement.Top">
    <ChildContent>
        <ListView TItem="Foo" Items="Foos" OnListViewChanged="OnFooSelected">
            <ListItemTemplate>
                <span>@context.Name</span>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>
```

---

## 参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| AdditionalAttributes | 获得/设置 用户自定义属性 | IDictionary<string, Object> | — |
| ChildContent | 获得/设置 下拉列表内容模板 | RenderFragment<ISelectObjectContext<TItem>> | — |
| ClearIcon | 获得/设置 右侧清除图标 默认 fa-solid fa-angle-up | string | fa-solid fa-angle-up |
| Color | 获得/设置 颜色 默认 Color.None 无设置 | Color | Color.None |
| CustomClass | 获得/设置 自定义样式 参数 默认 null | string | null |
| DisplayText | 获得/设置 显示名称 | string | — |
| DropdownIcon | 获得/设置 右侧下拉箭头图标 默认 fa-solid fa-angle-up | string | fa-solid fa-angle-up |
| DropdownMinWidth | 获得/设置 弹窗最小宽度 默认为 null 未设置使用样式中的默认值 | Nullable<int> | null |
| GetTextCallback | 获得 显示文字回调方法 默认 null | Func<TItem, string> | null |
| Height | 获得/设置 弹窗高度 默认 486px | int | 486 |
| Id | 获得/设置 组件 id 属性 | string | — |
| IsClearable | 获得/设置 是否可清除 默认 false | bool | false |
| IsDisabled | 获得/设置 是否禁用 默认为 false | bool | false |
| OnClearAsync | 获得/设置 清除文本内容 OnClear 回调方法 默认 null | Func<Task> | null |
| OnValueChanged | 获得/设置 Value 改变时回调方法 | Func<TItem, Task> | — |
| ParsingErrorMessage | 获得/设置 类型转化失败格式化字符串 默认为 null | string | null |
| PlaceHolder | 获得 PlaceHolder 属性 | string | — |
| Placement | 获得/设置 弹窗位置 默认为 Bottom | Placement | Placement.Bottom |
| RequiredErrorMessage | 获得/设置 必填项错误文本 默认为 null 未设置 | string | null |
| ShowAppendArrow | 获得/设置 是否显示组件右侧扩展箭头 默认 true 显示 | bool | true |
| ShowLabel | 获得/设置 是否显示前置标签，默认值为 null，为空时不显示标签 | Nullable<bool> | null |
| ShowLabelTooltip | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null | Nullable<bool> | null |
| ShowRequired | 获得/设置 是否显示必填项标记 默认为 null 未设置 | Nullable<bool> | null |
| ShowShadow | 获得/设置 是否显示阴影 默认 true | bool | true |
| SkipValidate | 获得/设置 是否不进行验证 默认为 false | bool | false |
| Template | 获得/设置 Value 显示模板 默认 null | RenderFragment<TItem> | null |
| ValidateRules | 获得/设置 自定义验证集合 | List<IValidator> | — |
| Value | 获得/设置 输入组件的值，支持双向绑定 | TItem | — |
| ValueChanged | 获得/设置 用于更新绑定值的回调 | EventCallback<TItem> | — |
| ValueExpression | 获得/设置 标识绑定值的表达式 | Expression<Func<TItem>> | — |

---

## 事件回调

| 事件名称 | 说明 | 回调类型 |
|---------|------|---------|
| OnClearAsync | 清除文本内容时回调方法 | Func<Task> |
| OnValueChanged | Value 改变时回调方法 | Func<TItem, Task> |

---

## 最佳实践

### 与 ListView 配合使用

SelectObject 通常与 ListView 组件配合使用，实现复杂类型的选择：

```razor
<SelectObject TItem="Customer" 
            @bind-Value="SelectedCustomer"
            GetTextCallback="c => c.Name"
            DropdownMinWidth="400"
            Height="400">
    <ChildContent>
        <ListView TItem="Customer" Items="Customers">
            <ListItemTemplate>
                <div class="d-flex align-items-center p-2">
                    <img src="@context.Avatar" width="40" height="40" class="rounded-circle me-2" />
                    <div>
                        <div>@context.Name</div>
                        <small class="text-muted">@context.Email</small>
                    </div>
                </div>
            </ListItemTemplate>
        </ListView>
    </ChildContent>
</SelectObject>

@code {
    private Customer? SelectedCustomer { get; set; }
    private List<Customer> Customers { get; set; } = new();
    
    protected override async Task OnInitializedAsync()
    {
        // 加载客户数据
        Customers = await CustomerService.GetCustomersAsync();
    }
    
    public class Customer
    {
        public string? Name { get; set; }
        public string? Email { get; set; }
        public string? Avatar { get; set; }
    }
}
```

### 自定义显示模板

通过 `Template` 参数自定义选中后显示的内容：

```razor
<SelectObject TItem="Customer" 
            @bind-Value="SelectedCustomer"
            GetTextCallback="c => c.Name">
    <Template>
        @if (context != null)
        {
            <div class="d-flex align-items-center">
                <img src="@context.Avatar" width="20" height="20" class="rounded-circle me-1" />
                <span>@context.Name</span>
            </div>
        }
    </Template>
    <ChildContent>
        <!-- 下拉列表内容 -->
    </ChildContent>
</SelectObject>
```

---

## 常见问题

### 1. 如何获取选择的值？

通过 `Value` 属性或 `@bind-Value` 双向绑定获取选择的值。也可以通过 `OnValueChanged` 回调方法获取。

### 2. 如何自定义下拉框内容？

在 `ChildContent` 模板中放置任意组件，如 ListView、Table、Tree 等，实现复杂的下拉选择界面。

### 3. 如何在自定义组件中关闭下拉框？

通过级联参数获取 `SelectObjectCloseAsync` 方法，在自定义组件中调用此方法关闭下拉框：

```csharp
[CascadingParameter(Name = "SelectObjectCloseAsync")]
private Func<Task>? OnCloseAsync { get; set; }
```

### 4. 如何自定义显示文本？

通过 `GetTextCallback` 回调方法返回显示文本，或设置 `DisplayText` 属性直接指定显示文本。

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | SelectObject 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/select-object)
- [ListView 组件文档](https://www.blazor.zone/listview)
- [Table 组件文档](https://www.blazor.zone/table)
