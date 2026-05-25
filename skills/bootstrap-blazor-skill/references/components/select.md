# Select (选择器)

## 概述

Select 组件是 Bootstrap Blazor 中用于下拉选择的组件。当选项过多时，使用下拉菜单展示并选择内容。

**主要功能特性**：
- 支持单向/双向数据绑定
- 支持泛型绑定（TValue）
- 支持静态数据、枚举数据、动态数据
- 支持分组显示
- 支持搜索功能（ShowSearch）
- 支持可编辑模式（IsEditable）
- 支持虚拟滚动（IsVirtualize）
- 支持清除按钮（IsClearable）
- 支持确认弹窗（ShowSwal）
- 支持自定义选项模板（ItemTemplate）
- 支持悬浮弹窗（IsPopover）

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/select](https://www.blazor.zone/select)

## 使用场景

### 1. 基础用法

提供各种颜色的下拉选择框。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" />
```

**功能说明**：
- 第一个下拉框没有进行 Value 双向绑定，所以选择不同选项时仅自己变化
- 其余下拉框共用同一数据源 Items 并且双向绑定 Value 值，选择不同选项时一同变化

---

### 2. 禁用下拉框

选择器不可用状态。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" IsDisabled="true" />
```

**功能说明**：下拉框内选项禁用示例。

---

### 3. 双向绑定

通过 Select 组件绑定 `Model.Name` 属性，改变下拉框选项时，文本框内的数值随之改变。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" />
```

---

### 4. 双向绑定 SelectItem

通过 Select 组件绑定 `SelectItem` 属性，改变下拉框选项时，文本框内的数值随之改变。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-SelectedItem="SelectedItem" />
```

---

### 5. 级联绑定

通过选择第一个下拉框不同选项，第二个下拉框动态填充内容。

```razor
<BootstrapSelect TValue="string" Items="Provinces" @bind-Value="SelectedProvince" />
<BootstrapSelect TValue="string" Items="Cities" @bind-Value="SelectedCity" />
```

**弹窗中级联示例**：在弹窗中使用级联选择。

---

### 6. 客户端验证

下拉框未选择时，点击提交按钮时拦截。

```razor
<ValidateForm Model="Model" OnValidSubmit="OnValidSubmit">
    <BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

---

### 7. 分组

备选项进行分组展示。

```razor
<BootstrapSelect TValue="string" Items="GroupedItems" @bind-Value="Model.Name" />
```

---

### 8. 绑定泛型为 Guid 结构

组件绑定值为 Guid 结构体示例。

```razor
<BootstrapSelect TValue="Guid" Items="Items" @bind-Value="Model.Id" />
```

---

### 9. 显示标签

组件双向绑定时会根据条件自动判断是否显示标签文字。

**前置标签显示规则与 BootstrapInput 组件一致**：
- 双向绑定显示标签
- 双向绑定不显示标签（设置 `ShowLabel="false"`）
- 自定义 `DisplayText`

```razor
@* 双向绑定显示标签 *@
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" />

@* 双向绑定不显示标签 *@
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" ShowLabel="false" />

@* 自定义 DisplayText *@
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" DisplayText="自定义城市" />
```

---

### 10. 静态数据

直接在 Select 组件内部进行硬编码书写，适用于静态数据下拉框。

```razor
<BootstrapSelect TValue="string" @bind-Value="Model.Name">
    <SelectItem Text="北京" Value="beijing" />
    <SelectItem Text="上海" Value="shanghai" />
    <SelectItem Text="广州" Value="guangzhou" />
</BootstrapSelect>
```

---

### 11. 枚举数据

Select 组件绑定枚举类型示例。

```razor
<BootstrapSelect TValue="EnumEducation?" @bind-Value="Model.Education" />
```

**功能说明**：
- 当绑定值为可为空枚举类型时，组件内部自动通过 PlaceHolder 值添加首选项
- 未设置 PlaceHolder 值时，使用资源文件中的"请选择..."作为首选项
- 本示例绑定 `EnumEducation` 枚举类型
- 绑定值为枚举类型时，设置 PlaceHolder 无效

---

### 12. 绑定可为空类型

Select 组件绑定 `int?` 类型示例。

```razor
<BootstrapSelect TValue="int?" Items="Items" @bind-Value="Model.NullableInt" />
```

**功能说明**：选中第一个选项时，绑定值 `SelectedIntItem` 为 null。

---

### 13. 绑定可为空布尔类型

Select 组件绑定 `bool?` 类型示例。

```razor
<BootstrapSelect TValue="bool?" Items="Items" @bind-Value="Model.NullableBool" />
```

**功能说明**：
- 可为空布尔类型多用于条件搜索框中
- 选中第一个选项时，绑定值 `SelectedIntItem` 为 null

---

### 14. 自定义选项模板

通过设置 `ItemTemplate` 可以自定义选项渲染样式。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name">
    <ItemTemplate>
        <div class="custom-item">
            <i class="fa-solid fa-map-pin"></i>
            @context.Text
        </div>
    </ItemTemplate>
</BootstrapSelect>
```

---

### 15. 带搜索框的下拉框

通过设置 `ShowSearch` 属性控制是否显示搜索框，默认为 false 不显示搜索框。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" ShowSearch="true" />
```

**功能说明**：
- 可以通过设置 `IsAutoClearSearchTextWhenCollapsed` 参数控制下拉框收起后是否自动清空搜索框内文字
- 默认值为 false 不清空

---

### 16. 可清空单选

包含清空按钮，可将选择器清空为初始状态。

```razor
<BootstrapSelect TValue="string?" Items="Items" @bind-Value="Model.Name" IsClearable="true" />
```

**功能说明**：
- 不可为空整形设置 `IsClearable` 无效，其默认值为 0
- string?、int? 等可为空类型支持清空

---

### 17. 带确认的下拉框

通过设置 `OnBeforeSelectedItemChange` 委托或者设置 `ShowSwal` 参数值为 true，阻止当前值的改变。

```razor
@* 方式1：使用 OnBeforeSelectedItemChange 回调 *@
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" 
              OnBeforeSelectedItemChange="OnBeforeChange" />

@code {
    private async Task<bool> OnBeforeChange(SelectedItem item)
    {
        // 弹窗确认是否更改值
        return await SwalService.Confirm("确认", $"确定要改为 {item.Text} 吗？");
    }
}

@* 方式2：使用 ShowSwal 参数 *@
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" 
              ShowSwal="true" SwalTitle="确认" SwalContent="确定要更改选择吗？" />
```

---

### 18. 悬浮弹窗

通过设置 `IsPopover` 参数，组件使用 popover 渲染 UI 防止由于父容器设置 `overflow: hidden;` 使弹窗无法显示问题。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" IsPopover="true" />
```

---

### 19. 可编辑

通过设置 `IsEditable="true"` 使组件可录入。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" IsEditable="true" />
```

**功能说明**：
- 开启可编辑功能后，输入值如果候选项中没有时，可以通过 `TextConvertToValueCallback` 回调方法返回新值
- 可以通过 `OnInputChangedCallback` 回调对 Items 数据源进行更新，防止页面刷新后输入值丢失

---

### 20. 虚拟滚动

通过设置 `IsVirtualize` 参数开启组件虚拟功能特性。

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" IsVirtualize="true" />
```

**功能说明**：
- 组件虚拟滚动支持两种形式：通过 `Items` 或者 `OnQueryAsync` 回调方法提供数据
- 如果数据源使用 `OnQueryAsync` 回调获得时，只有当下拉框展开时才会触发
- 如果数据源使用 `Items` 时，由于性能问题（有些开发会把几百万条数据给 Items），内部并没有进行查找选中项，所以需要设置 `DefaultVirtualizeItemText` 值应对首次加载时不知道如何显示问题

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TValue` | `default` | 获得/设置组件值 |
| `@bind-Value` | `TValue` | `default` | 获得/设置组件值（双向绑定） |
| `@bind-SelectedItem` | `SelectedItem` | `null` | 获得/设置选中项（双向绑定） |
| `Items` | `IEnumerable<SelectedItem>` | `null` | 获得/设置数据源 |
| `DisplayText` | `string?` | `null` | 获得/设置显示名称（前置标签） |
| `ShowLabel` | `bool?` | `null` | 获得/设置是否显示标签 |
| `Color` | `Color` | `Color.None` | 获得/设置颜色 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用 |
| `IsClearable` | `bool` | `false` | 获得/设置是否显示清除按钮 |
| `ClearIcon` | `string?` | `null` | 获得/设置右侧清除图标 |
| `DropdownIcon` | `string?` | `"fa-solid fa-angle-up"` | 获得/设置下拉图标 |
| `ShowSearch` | `bool` | `false` | 获得/设置是否显示搜索框 |
| `IsAutoClearSearchTextWhenCollapsed` | `bool` | `false` | 获得/设置下拉框关闭时是否自动清空搜索文本 |
| `IsEditable` | `bool` | `false` | 获得/设置是否可编辑 |
| `IsVirtualize` | `bool` | `false` | 获得/设置是否启用虚拟滚动 |
| `DefaultVirtualizeItemText` | `string?` | `null` | 获得/设置虚拟化项目的默认文本 |
| `ShowSwal` | `bool` | `false` | 获得/设置是否显示确认弹窗 |
| `SwalTitle` | `string?` | `null` | 获得/设置确认弹窗标题 |
| `SwalContent` | `string?` | `null` | 获得/设置确认弹窗内容 |
| `IsPopover` | `bool` | `false` | 获得/设置是否使用悬浮弹窗 |
| `PlaceHolder` | `string?` | `null` | 获得/设置占位符文本 |
| `ShowInnerLabel` | `bool` | `false` | 获得/设置是否显示内部标签 |
| `ItemTemplate` | `RenderFragment<SelectedItem>?` | `null` | 获得/设置选项模板 |
| `DisplayTemplate` | `RenderFragment<SelectedItem>?` | `null` | 获得/设置显示模板 |
| `GroupItemTemplate` | `RenderFragment<string>?` | `null` | 获得/设置分组项模板 |
| `OnBeforeSelectedItemChange` | `Func<SelectedItem, Task<bool>>?` | `null` | 获得/设置选中前回调 |
| `OnSelectedItemChanged` | `Func<SelectedItem, Task>?` | `null` | 获得/设置选中后回调 |
| `OnInputChangedCallback` | `Func<string, Task<IEnumerable<SelectedItem>>>?` | `null` | 获得/设置输入变化回调 |
| `TextConvertToValueCallback` | `Func<string, TValue>?` | `null` | 获得/设置文本转值回调 |
| `Id` | `string?` | `null` | 获得/设置组件 id 属性 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |

## 最佳实践

### 1. 数据绑定最佳实践

**推荐做法**：根据数据类型选择合适的绑定方式。

**场景 1**：绑定简单类型（string、int、Guid 等）

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" />
```

**场景 2**：绑定枚举类型

```razor
<BootstrapSelect TValue="EnumEducation?" @bind-Value="Model.Education" />
```

**场景 3**：绑定复杂类型（需要获取选中项完整信息）

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-SelectedItem="SelectedItem" />

@code {
    private SelectedItem? SelectedItem { get; set; }
}
```

---

### 2. 大数据量处理最佳实践

**场景**：数据源有成千上万条记录。

**推荐做法**：使用虚拟滚动或远程查询。

**方式 1**：虚拟滚动（适合中等数据量）

```razor
<BootstrapSelect TValue="string" Items="Items" @bind-Value="Model.Name" 
              IsVirtualize="true" DefaultVirtualizeItemText="加载中..." />
```

**方式 2**：远程查询（适合大数据量）

```razor
<BootstrapSelect TValue="string" @bind-Value="Model.Name" 
              OnQueryAsync="OnQueryItems" ShowSearch="true" />

@code {
    private async Task<IEnumerable<SelectedItem>> OnQueryItems(string searchText)
    {
        // 从服务器查询数据
        return await ItemService.SearchAsync(searchText);
    }
}
```

---

### 3. 级联选择最佳实践

**场景**：第一个下拉框选择后，第二个下拉框选项随之变化。

**推荐做法**：在第一个下拉框的 `OnSelectedItemChanged` 回调中更新第二个下拉框的数据源。

```razor
<BootstrapSelect TValue="string" Items="Provinces" @bind-Value="SelectedProvince" 
              OnSelectedItemChanged="OnProvinceChanged" />
<BootstrapSelect TValue="string" Items="Cities" @bind-Value="SelectedCity" />

@code {
    private async Task OnProvinceChanged(SelectedItem item)
    {
        // 根据选中的省份加载城市数据
        Cities = await CityService.GetCitiesAsync(item.Value);
    }
}
```

---

### 4. 常见错误

**错误 1**：TValue 类型与 Items 中的 Value 类型不匹配

**解决方法**：确保 `TValue` 类型与 `SelectedItem.Value` 类型一致。

**错误 2**：绑定可为空类型时，未设置 `PlaceHolder` 或首次加载时显示异常

**解决方法**：设置 `PlaceHolder` 属性，或使用 `DefaultVirtualizeItemText`（虚拟滚动时）。

**错误 3**：在 `ValidateForm` 中使用时未触发验证

**解决方法**：确保 `SelectedItem` 或 `Value` 正确绑定，并在模型中使用数据注解进行验证。

---

## 相关组件

- `SelectedItem` - 选择项类
- `BootstrapSelectList` - 多选下拉组件
- `BootstrapMultiSelect` - 多项选择器组件
- `ValidateForm` - 验证表单组件

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 Select 组件的核心功能和使用方法。
