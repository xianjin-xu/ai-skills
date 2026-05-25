# SelectTable (下拉表格选择器)

## 概述

`SelectTable` 是一个强大的下拉表格选择组件，结合了下拉选择和表格展示的功能，支持单选和多选模式，提供丰富的配置选项和事件回调。

> SelectTable component

**分类**: 表单组件
**在线演示**: [https://www.blazor.zone/select-table](https://www.blazor.zone/select-table)

## 使用场景

### 1. 基本用法

```razor
<SelectTable TItem="YourItemType" OnQueryAsync="OnQueryAsync" GetTextCallback="GetTextCallback" />
```

### 2. 多选模式

```razor
<SelectTable TItem="YourItemType" IsMultipleSelect="true" OnQueryAsync="OnQueryAsync" GetTextCallback="GetTextCallback" />
```

### 3. 显示工具栏

```razor
<SelectTable TItem="YourItemType" ShowToolbar="true" OnQueryAsync="OnQueryAsync" GetTextCallback="GetTextCallback">
    <ToolbarTemplate>
        <Button Text="自定义按钮" />
    </ToolbarTemplate>
</SelectTable>
```

### 4. 自定义表格列

```razor
<SelectTable TItem="YourItemType" OnQueryAsync="OnQueryAsync" GetTextCallback="GetTextCallback">
    <TableColumns>
        <TableColumn @bind-Field="context.Name" />
        <TableColumn @bind-Field="context.Age" />
    </TableColumns>
</SelectTable>
```

### 5. 可清除

```razor
<SelectTable TItem="YourItemType" IsClearable="true" OnQueryAsync="OnQueryAsync" GetTextCallback="GetTextCallback" />
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsMultipleSelect` | `bool` | `false` | 获得/设置是否为多选模式 |
| `MultiSelectedItemsMaxHeight` | `string?` | `null` | 获得/设置多选模式下组件最大高度 |
| `MultiSelectedItemsMaxDisplayCount` | `int` | `8` | 获得/设置多选模式下组件显示最大数量 |
| `MultiSelectedItemsMaxDisplayCountColor` | `Color` | `Color.None` | 获得/设置多选模式下组件显示最大数量标签颜色 |
| `SelectedItems` | `List<TItem>` | `[]` | 获得/设置多选模式下已选择项集合 |
| `SelectedItemsChanged` | `EventCallback<List<TItem>>` | - | 获得/设置多选模式下已选择项集合变化回调方法 |
| `TableColumns` | `RenderFragment<TItem>?` | `null` | 获得/设置 TableHeader 实例 |
| `OnQueryAsync` | `Func<QueryPageOptions, Task<QueryData<TItem>>>?` | `null` | 获得/设置异步查询回调方法 |
| `Color` | `Color` | `Color.None` | 获得/设置颜色 |
| `ShowAppendArrow` | `bool` | `true` | 获得/设置是否显示组件右侧扩展箭头 |
| `TableMinWidth` | `int?` | `null` | 获得/设置弹窗表格最小宽度 |
| `GetTextCallback` | `Func<TItem, string?>?` | `null` | 获得/设置显示文字回调方法 |
| `DropdownIcon` | `string?` | `fa-solid fa-angle-up` | 获得/设置右侧下拉箭头图标 |
| `IsClearable` | `bool` | `false` | 获得/设置是否可清除 |
| `ShowEmpty` | `bool` | `false` | 获得/设置是否显示无数据空记录 |
| `EmptyTemplate` | `RenderFragment?` | `null` | 获得/设置无数据时显示模板 |
| `MultiSelectedItemMaxWidth` | `string?` | `null` | 获得/设置多选模式下选中项最大宽度 |
| `ShowToolbar` | `bool` | `false` | 获得/设置是否显示工具栏 |
| `ToolbarTemplate` | `RenderFragment?` | `null` | 获得/设置表格 Toolbar 工具栏模板 |
| `TableExtensionToolbarTemplate` | `RenderFragment?` | `null` | 获得/设置表格 Toolbar 工具栏右侧按钮模板 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `SelectedItemsChanged` | 多选模式下已选择项集合变化时的回调 |
| `ValueChanged` | 值改变时触发 |

## 最佳实践

1. **数据查询**: 必须实现 `OnQueryAsync` 回调方法，返回表格数据
2. **文本显示**: 必须实现 `GetTextCallback` 回调方法，返回显示文本
3. **多选模式**: 设置 `IsMultipleSelect="true"` 启用多选
4. **表格列**: 使用 `TableColumns` 模板自定义表格列
5. **工具栏**: 设置 `ShowToolbar="true"` 显示工具栏，使用 `ToolbarTemplate` 自定义工具栏内容
6. **性能优化**: 对于大数据量，建议启用分页和虚拟滚动

## 常见问题

### Q: 如何绑定选中值？
A: 使用 `Value` 参数绑定选中值，或使用 `SelectedItems` 参数绑定多选模式的选中项集合。

### Q: 如何自定义表格列？
A: 使用 `TableColumns` 模板，内部使用 `TableColumn` 组件定义列。

### Q: 如何触发查询？
A: 实现 `OnQueryAsync` 回调方法，组件会自动调用该方法获取表格数据。

### Q: 如何显示工具栏？
A: 设置 `ShowToolbar="true"`，并使用 `ToolbarTemplate` 自定义工具栏内容。

### Q: 如何清除选中值？
A: 设置 `IsClearable="true"` 显示清除按钮，点击可清除选中值。
