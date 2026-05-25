# Table (表格)

## 概述

Table 组件是 Bootstrap Blazor 中最核心、最复杂的组件之一，用于展示多条结构类似的数据，可对数据进行排序、筛选、对比或其他自定义操作。

**主要功能特性**：
- 支持数据展示（表格、卡片视图）
- 支持分页、排序、筛选
- 支持行选中、行编辑
- 支持列设置、列拖动、列宽调整
- 支持明细行、树形数据
- 支持导出（Excel、CSV、PDF）
- 支持虚拟滚动
- 支持移动端适配

**分类**: 表格组件  
**在线演示**: [https://www.blazor.zone/table](https://www.blazor.zone/table)

## 小提示

> **表格功能比较多，参数也非常多，示例更多，各个功能详细用法建议查看下方视频讲解**  
> - 鞠佬 BootstrapBlazor Table 系列 [传送门](https://www.bilibili.com/video/BV1X44y1A7xE)  
> - 官网组件讲解合集 [传送门](https://www.blazor.zone/videos)

> **Table 组件已经支持移动端适配**，当屏幕小于 `RenderModeResponsiveWidth` 设定值时，组件渲染成卡片式方便查看数据，其默认值为 768

> **Table 组件有一个 `RenderMode` 属性**，其默认值为 `Auto` 其他值定义如下：
> - `Auto`: 当屏幕小于 768px 时使用 CardView 模式，否则使用 Table 模式
> - `Table`: 表格渲染模式，使用 table 元素进行数据渲染，适合宽屏幕下查看数据
> - `CardView`：卡片式渲染模式，使用 div 元素进行数据渲染，适合窄屏幕下查看数据

> **TableColumn 必须使用 `@bind-Field` 绑定了模型属性**，模型属性为复杂类型时，必须初始化此属性；想要绑定只读属性时，先绑定其他可写属性后利用模板显示只读属性

## 使用场景

### 1. 基础表格

基础的表格展示用法，通过设置 `Items` 参数绑定数据源。

```razor
<Table TItem="Foo" Items="Items">
    <TableColumns>
        <TableColumn @bind-Field="@context.DateTime" />
        <TableColumn @bind-Field="@context.Name" />
        <TableColumn @bind-Field="@context.Address" />
    </TableColumns>
</Table>
```

**效果**：显示日期、姓名、地址三列数据，支持点击按钮更新数据源。

---

### 2. 带斑马纹表格

使用带斑马纹的表格，可以更容易区分出不同行的数据。设置 `IsStriped=true` 即可。

```razor
<Table TItem="Foo" Items="Items" IsStriped="true">
    <TableColumns>
        <TableColumn @bind-Field="@context.DateTime" />
        <TableColumn @bind-Field="@context.Name" />
        <TableColumn @bind-Field="@context.Address" />
    </TableColumns>
</Table>
```

---

### 3. 带边框表格

通过设置 `IsBordered` 属性，增加表格表框效果。

```razor
<Table TItem="Foo" Items="Items" IsBordered="true">
    <TableColumns>
        <TableColumn @bind-Field="@context.DateTime" />
        <TableColumn @bind-Field="@context.Name" />
        <TableColumn @bind-Field="@context.Address" />
    </TableColumns>
</Table>
```

---

### 4. 紧凑型表格

通过设置 `TableSize` 属性，设定表格内间隙变小适合大数据展示。

`TableSize` 为表格大小枚举类型，默认值为 `Normal`，紧奏型值为 `Compact`。

```razor
<Table TItem="Foo" Items="Items" TableSize="TableSize.Compact">
    <TableColumns>
        <TableColumn @bind-Field="@context.DateTime" />
        <TableColumn @bind-Field="@context.Name" />
        <TableColumn @bind-Field="@context.Address" />
    </TableColumns>
</Table>
```

---

### 5. 表头样式

通过设置 `HeaderStyle` 属性控制表头样式。

`HeaderStyle` 为表格表头样式，默认值为 `None`。

**Light 表头模式**：
```razor
<Table TItem="Foo" Items="Items" HeaderStyle="TableHeaderStyle.Light">
    ...
</Table>
```

**Dark 表头模式**：
```razor
<Table TItem="Foo" Items="Items" HeaderStyle="TableHeaderStyle.Dark">
    ...
</Table>
```

---

## 重要参数分类

由于 Table 组件参数非常多（331个），这里按功能分类列出最重要的参数。完整参数列表请参考官方文档或源码。

### 数据相关参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TItem>` | `null` | 获得/设置数据集合，适用于无功能仅做数据展示使用，高级功能时请使用 `OnQueryAsync` 回调委托 |
| `OnQueryAsync` | `Func<QueryPageOptions, Task<QueryData<TItem>>>` | `null` | 异步查询回调方法，设置 `Items` 后无法触发此回调方法 |
| `DataService` | `IDataService<TItem>` | `null` | 获得/设置数据服务参数，组件采用就近原则：Items > OnQueryAsync > DataService > 全局注入的数据服务 `IDataService` |
| `IsPagination` | `bool` | `false` | 获得/设置是否分页，默认值为 false |
| `PageItems` | `int?` | `null` | 获得/设置默认每页数据数量，默认 null 使用 `PageItemsSource` 第一个值 |
| `PageItemsSource` | `IEnumerable<int>` | `null` | 获得/设置每页显示数据数量的外部数据源 |

### 外观相关参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsStriped` | `bool` | `false` | 获得/设置是否斑马线样式，默认为 false |
| `IsBordered` | `bool` | `false` | 获得/设置是否带边框样式，默认为 false |
| `TableSize` | `TableSize` | `TableSize.Normal` | 获得/设置表格组件大小，默认为 Normal 正常模式 |
| `HeaderStyle` | `TableHeaderStyle` | `TableHeaderStyle.None` | 获取/设置表格 thead 样式，默认为浅色 |
| `IsFixedHeader` | `bool` | `false` | 获得/设置固定表头，默认 false |
| `Height` | `int?` | `null` | 获得/设置 Table 高度，默认为 null（开启固定表头功能时生效） |
| `RenderMode` | `TableRenderMode` | `TableRenderMode.Auto` | 获得/设置组件布局方式，默认为 Auto |

### 功能相关参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsMultipleSelect` | `bool` | `false` | 获得/设置是否为多选模式，默认值为 false |
| `ClickToSelect` | `bool` | `false` | 获得/设置点击行即选中本行，默认为 false |
| `DoubleClickToEdit` | `bool` | `false` | 获得/设置单选模式下双击即编辑本行，默认为 false |
| `EditMode` | `EditMode` | `EditMode.PopupEditForm` | 获得/设置组件编辑模式，默认为弹窗编辑行数据 PopupEditForm |
| `IsAutoQueryFirstRender` | `bool` | `true` | 获得/设置首次加载时是否自动查询数据，默认 true（RemoteData 模式下此参数不起作用） |
| `IsTree` | `bool` | `false` | 获得/设置是否为树形数据，默认为 false |
| `IsDetails` | `bool?` | `null` | 获得/设置是否显示明细行，默认为 null 为空时使用 `DetailRowTemplate` 进行逻辑判断 |

### 工具栏相关参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ShowToolbar` | `bool` | `false` | 获得/设置是否显示工具栏，默认 false 不显示 |
| `ShowDefaultButtons` | `bool` | `true` | 获得/设置是否显示按钮列，默认为 true |
| `ShowAddButton` | `bool` | `true` | 获得/设置是否显示新建按钮，默认为 true 显示 |
| `ShowEditButton` | `bool` | `true` | 获得/设置是否显示编辑按钮，默认为 true |
| `ShowDeleteButton` | `bool` | `true` | 获得/设置是否显示删除按钮，默认为 true |
| `ShowSearch` | `bool` | `false` | 获得/设置是否显示搜索框，默认为 false 不显示搜索框 |
| `ShowExportButton` | `bool` | `false` | 获得/设置是否显示导出按钮，默认为 false 不显示 |

### 列设置相关参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AutoGenerateColumns` | `bool` | `false` | 获得/设置是否自动生成列信息，默认为 false |
| `AllowDragColumn` | `bool` | `false` | 获得/设置是否允许拖放标题栏更改栏位顺序，默认为 false |
| `AllowResizing` | `bool` | `false` | 获得/设置是否允许列宽度调整，默认 false（固定表头时此属性生效） |
| `ShowColumnList` | `bool` | `false` | 获得/设置是否显示列选择下拉框，默认为 false 不显示 |

## 最佳实践

### 1. 数据加载优先级

Table 组件数据加载遵循**就近原则**：
1. `Items` - 直接提供数据集合（适用于简单场景）
2. `OnQueryAsync` - 异步查询回调（适用于需要分页、排序、筛选的场景）
3. `DataService` - 数据服务（适用于封装好的数据访问层）
4. 全局注入的 `IDataService`（适用于整个应用统一的数据访问）

**推荐做法**：大多数场景下使用 `OnQueryAsync` 回调，它提供了最大的灵活性。

---

### 2. 编辑模式选择

Table 组件支持多种编辑模式（通过 `EditMode` 参数控制）：

- `PopupEditForm` - 弹窗编辑（默认）
- `EditForm` - 行内编辑
- `InCell` - 单元格编辑（Excel 模式）

**选择建议**：
- 字段较少时：使用 `PopupEditForm`（弹窗编辑）
- 字段较多时：使用 `EditForm`（行内编辑）
- 类似 Excel 操作时：使用 `InCell`（单元格编辑）

---

### 3. 性能优化

对于大数据量场景，建议：

1. **启用分页**：设置 `IsPagination="true"`
2. **使用服务端查询**：通过 `OnQueryAsync` 回调实现服务端分页、排序、筛选
3. **虚拟滚动**：设置 `ScrollMode="ScrollMode.Virtual"`（适用于超大数据集）
4. **延迟加载**：对于明细行、树形数据，使用懒加载模式

---

### 4. 移动端适配

Table 组件默认支持移动端适配：

- `RenderMode="TableRenderMode.Auto"`（默认）- 屏幕 < 768px 时自动切换为卡片视图
- `RenderModeResponsiveWidth` - 自定义切换阈值（默认 768）
- `ShowCardView="true"` - 手动启用卡片视图按钮

**建议**：保持默认的 `Auto` 模式，让组件自动适配不同屏幕尺寸。

---

### 5. 列定义最佳实践

**自动生成列 vs 手动定义列**：

- **简单场景**：使用 `AutoGenerateColumns="true"` 自动生成列
- **复杂场景**：手动定义 `TableColumn`，可以获得更多控制（排序、筛选、格式化等）

**手动定义列示例**：
```razor
<Table TItem="Foo" Items="Items">
    <TableColumns>
        <TableColumn @bind-Field="@context.Name" Sortable="true" Filterable="true" />
        <TableColumn @bind-Field="@context.Address" Sortable="true" />
    </TableColumns>
</Table>
```

---

### 6. 常见错误

**错误 1**：`TableColumn` 未使用 `@bind-Field` 绑定

**错误 2**：模型属性为复杂类型时未初始化

**错误 3**：在 `Items` 和 `OnQueryAsync` 之间混淆使用

**错误 4**：编辑模式下未正确配置 `EditModel` 或 `EditTemplate`

---

## 完整参数列表

由于 Table 组件参数非常多（331个），完整参数列表请参考：
- 官方文档：[https://www.blazor.zone/table](https://www.blazor.zone/table)
- 源码文件：`BootstrapBlazor/Components/Table/Table.razor.cs`

本文档列出了按功能分类的最重要参数，满足大多数使用场景。如需查看完整参数说明，请访问官方文档。

---

## 相关组件

- `TableColumn` - 表格列定义组件
- `Pagination` - 分页组件
- `Table<TItem>` - 表格泛型组件

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 Table 组件的核心功能和使用方法。由于 Table 组件非常复杂，本文档重点介绍了最常用的功能和参数，完整信息请参考官方文档。
