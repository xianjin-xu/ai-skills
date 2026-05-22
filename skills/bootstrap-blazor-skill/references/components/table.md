# Table

## 概述

Table 组件基类

> Table Component Base Class

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/table](https://www.blazor.zone/table)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AutoSearchOnInput` | `bool` | `}` | 获得/设置 模糊搜索栏输入时是否自动搜索 默认值 false |
| `NotSupportedColumnFilterMessage` | `string?` | `}` | 获得/设置 不支持过滤类型提示信息 默认 null 读取资源文件内容 |
| `LoadingTemplate` | `RenderFragment?` | `}` | 获得/设置 Loading 模板 |
| `ColumnToolboxIcon` | `string?` | `}` | 获得/设置 列工具栏图标 fa-solid fa-gear |
| `DefaultFixedColumnWidth` | `int` | `200` | 获得/设置 默认固定列宽度 默认 200 单位 px |
| `IsGroupExtendButtons` | `bool` | `true` | 获得/设置 是否使用按钮组显示行内扩展按钮 默认 true |
| `ScrollWidth` | `int?` | `}` | 获得/设置 滚动条宽度 默认 null 未设置使用 <see cref="ScrollOptions"/> 配置类中的 <see cref="ScrollOptions.ScrollWidth"/> |
| `ScrollHoverWidth` | `int?` | `}` | 获得/设置 滚动条 hover 状态下宽度 默认 null 未设置使用 <see cref="ScrollOptions"/> 配置类中的 <see cref="ScrollOptions.ScrollHoverWidth"/> |
| `ColumnWidthTooltipPrefix` | `string?` | `}` | 获得/设置 列调整提示前缀文字 默认 null 未设置使用资源文件中文字 |
| `ShowColumnWidthTooltip` | `bool` | `}` | 获得/设置 是否显示列宽提示信息，默认 false 显示 |
| `Height` | `int?` | `}` | - |
| `IsFixedHeader` | `bool` | `}` | 获得/设置 固定表头 默认 false |
| `IsFixedFooter` | `bool` | `}` | 获得/设置 固定 Footer 默认 false |
| `MultiHeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 多表头模板 |
| `CopyColumnTooltipText` | `string?` | `}` | 获得/设置 列拷贝 Tooltip 文字 |
| `CopyColumnCopiedTooltipText` | `string?` | `}` | 获得/设置 列拷贝完毕后 Tooltip 文字 |
| `ShowCopyColumnTooltip` | `bool` | `true` | 获得/设置 CopyColumn Tooltip 默认 true |
| `IsExcel` | `bool` | `}` | 获得/设置 组件工作模式为 Excel 模式 默认 false |
| `EnableKeyboardNavigationCell` | `bool` | `true` | 获得/设置 是否启用 Excel 模式下的键盘导航功能 默认 true |
| `IsDetails` | `bool?` | `}` | 获得/设置 是否显示明细行 默认为 null 为空时使用 <see cref="DetailRowTemplate" /> 进行逻辑判断 |
| `IsHideFooterWhenNoData` | `bool` | `}` | 获得/设置 无数据时是否隐藏表格 Footer 默认为 false 不隐藏 |
| `EditDialogItemsPerRow` | `int` | `2` | 获得/设置 编辑弹窗每行显示组件数量 默认为 2 |
| `EditDialogRowType` | `RowType` | `RowType.Inline` | 获得/设置 设置行内组件布局格式 默认 Inline 布局 |
| `EditDialogLabelAlign` | `Alignment` | `}` | 获得/设置 设置 <see cref="EditDialogRowType" /> Inline 模式下标签对齐方式 默认 None 等效于 Left 左对齐 |
| `EditDialogLabelWidth` | `int?` | `}` | 获得/设置 编辑弹窗标签宽度 默认为 null 使用样式默认值 120 |
| `DisableAutoSubmitFormByEnter` | `bool?` | `}` | 获得/设置 是否禁用表单内回车自动提交功能 默认 null 未设置 |
| `DetailColumnWidth` | `int` | `}` | 获得/设置 明细行 Row Header 宽度 默认 24 |
| `ShowCheckboxTextColumnWidth` | `int` | `}` | 获得/设置 显示文字的复选框列宽度 默认 80 |
| `CheckboxColumnWidth` | `int` | `}` | 获得/设置 复选框宽度 默认 36 |
| `CheckboxColumnCompactWidth` | `int` | `}` | 获得/设置 紧凑模式下复选框宽度 默认 28 |
| `LineNoColumnWidth` | `int` | `}` | 获得/设置 行号列宽度 默认 60 |
| `LineNoColumnAlignment` | `Alignment` | `}` | 获得/设置 行号内容位置 |
| `OnBeforeRenderRow` | `Action<TItem>?` | `}` | 获得/设置 呈现每行之前的回调 |
| `bool` | `Func<Table<TItem>,` | `}` | 获得/设置 Table 组件渲染完毕回调 |
| `AutoScrollLastSelectedRowToView` | `bool` | `}` | 获得/设置 是否自动将选中行滚动到可视区域 默认 false |
| `AutoScrollVerticalAlign` | `ScrollToViewAlign` | `ScrollToViewAlign.Center` | 获得/设置 选中行滚动到可视区域对齐方式 默认 ScrollToViewAlign.Center |
| `ScrollIntoViewBehavior` | `ScrollIntoViewBehavior` | `ScrollIntoViewBehavior.Smooth` | 获得/设置 滚动行为，默认值为 <see cref="ScrollIntoViewBehavior.Smooth"/> |
| `TItem` | `Func<string,` | `}` | 获得/设置 双击单元格回调委托 |
| `IsPopoverToolbarDropdownButton` | `bool` | `}` | 获得/设置 工具栏下拉框按钮是否 IsPopover 默认 false |
| `ScrollMode` | `ScrollMode` | `}` | 获得/设置 数据滚动模式 |
| `RowHeight` | `float` | `38f` | - |
| `OverscanCount` | `int` | `10` | - |
| `IsTracking` | `bool` | `}` | 获得/设置 组件是否采用 Tracking 模式对编辑项进行直接更新 默认 false |
| `IsAccordion` | `bool` | `}` | 获得/设置 明细行手风琴效果 默认 false |
| `ColumnMinWidth` | `int?` | `}` | 获得/设置 列最小宽度 默认 null 未设置 可通过 <see cref="TableSettings.ColumnMinWidth"/> 统一设置 |
| `DetailRowTemplate` | `RenderFragment<TItem>?` | `}` | 获得/设置 明细行模板 <see cref="IsDetails" /> |
| `RowTemplate` | `RenderFragment<TableRowContext<TItem>>?` | `}` | 获得/设置 行模板 |
| `RowContentTemplate` | `RenderFragment<TableRowContext<TItem>>?` | `}` | 获得/设置 行内容模板 |
| `TableColumns` | `RenderFragment<TItem>?` | `}` | 获得/设置 TableHeader 实例 |
| `TableFooter` | `RenderFragment<IEnumerable<TItem>>?` | `}` | 获得/设置 TableFooter 实例 |
| `FooterTemplate` | `RenderFragment<IEnumerable<TItem>>?` | `}` | 获得/设置 Table Footer 模板 |
| `Items` | `IEnumerable<TItem>?` | `}` | 获得/设置 数据集合，适用于无功能仅做数据展示使用，高级功能时请使用 <see cref="OnQueryAsync"/> 回调委托 |
| `TableSize` | `TableSize` | `}` | 获得/设置 表格组件大小 默认为 Normal 正常模式 |
| `EmptyTemplate` | `RenderFragment?` | `}` | 获得/设置 无数据时显示模板 默认 null |
| `EmptyText` | `string?` | `}` | 获得/设置 无数据时显示文本 默认取资源文件 英文 NoData 中文 无数据 |
| `EmptyImage` | `string?` | `}` | 获得/设置 无数据时显示图片路径 默认 null 未设置 |
| `ShowEmpty` | `bool` | `}` | 获得/设置 是否显示无数据空记录 默认 false 不显示 |
| `ShowFilterHeader` | `bool` | `}` | 获得/设置 是否显示过滤表头 默认 false 不显示 |
| `ShowMultiFilterHeader` | `bool` | `}` | 获得/设置 是否显示过滤表头 默认 false 不显示 |
| `ShowFooter` | `bool` | `}` | 获得/设置 是否显示表脚 默认为 false |
| `AllowResizing` | `bool` | `}` | 获得/设置 是否允许列宽度调整 默认 false 固定表头时此属性生效 |
| `HeaderTextWrap` | `bool` | `}` | 获得/设置 是否表头允许折行 默认 false 不折行 此设置为 true 时覆盖 <see cref="ITableColumn.HeaderTextWrap"/> 参数值 |
| `IsStriped` | `bool` | `}` | - |
| `IsAutoQueryFirstRender` | `bool` | `true` | 获得/设置 首次加载时是否自动查询数据 默认 true <see cref="Items"/> 模式下此参数不起作用 |
| `IsBordered` | `bool` | `}` | 获得/设置 是否带边框样式 默认为 false |
| `IsAutoRefresh` | `bool` | `}` | 获得/设置 是否自动刷新表格 默认为 false |
| `AutoRefreshInterval` | `int` | `2000` | 获得/设置 自动刷新时间间隔 默认 2000 毫秒 |
| `HeaderStyle` | `TableHeaderStyle` | `TableHeaderStyle.None` | 获取/设置 表格 thead 样式 <see cref="TableHeaderStyle"/>，默认为浅色<see cref="TableHeaderStyle.None"/> |
| `Task` | `Func<TItem,` | `}` | 获得/设置 单击行回调委托方法 |
| `DynamicContext` | `IDynamicObjectContext?` | `}` | 获得/设置 动态数据上下文实例 |
| `UnsetText` | `string?` | `}` | 获得/设置 未设置排序时 tooltip 显示文字 默认点击升序 |
| `SortAscText` | `string?` | `}` | 获得/设置 升序排序时 tooltip 显示文字 默认点击降序 |
| `SortDescText` | `string?` | `}` | 获得/设置 降序排序时 tooltip 显示文字 默认取消排序 |
| `IEnumerable` | `Func<IEnumerable<ITableColumn>,` | `}` | - |
| `CustomKeyAttribute` | `Type?` | `typeof(KeyAttribute)` | 获得/设置 数据主键标识标签 默认为 <see cref="KeyAttribute"/><code><br /></code>用于判断数据主键标签，如果模型未设置主键时可使用 <see cref="ModelEqualityComparer"/> 参数自定义判断 <code><br /></code>数据模型支持联合主键 |
| `ClientTableName` | `string?` | `}` | 获得/设置 客户端表格名称 默认 null 用于客户端列宽与列顺序持久化功能 |
| `AlignLeftText` | `string?` | `}` | 获得/设置 左对齐显示文本 |
| `AlignLeftTooltipText` | `string?` | `}` | 获得/设置左对齐提示信息文本 |
| `AlignCenterText` | `string?` | `}` | 获得/设置 居中对齐显示文本 |
| `AlignCenterTooltipText` | `string?` | `}` | 获得/设置 居中对齐提示信息文本 |
| `AlignRightText` | `string?` | `}` | 获得/设置 右对齐显示文本 |
| `AlignRightTooltipText` | `string?` | `}` | 获得/设置 右对齐提示信息文本 |
| `IsAutoScrollTopWhenClickPage` | `bool` | `}` | 获得/设置 翻页时是否自动滚动到顶部 默认 false |
| `AllowDragColumn` | `bool` | `}` | 获得/设置 是否允许拖放标题栏更改栏位顺序，默认为 false |
| `float` | `Func<string,` | `}` | 获得/设置 设置列宽回调方法 |
| `TableColumnClientStatus` | `Func<string,` | `}` | 获得/设置 表格客户端状态调整回调方法 |
| `OnLoadTableColumnClientStatus` | `Func<Task<TableColumnClientStatus>>?` | `}` | 获得/设置 加载表格客户端状态回调方法，组件会在首次渲染时调用该方法获取列状态用于初始化表格显示状态 |
| `FitColumnWidthIncludeHeader` | `bool` | `true` | 获得/设置 列宽自适应时是否包含表头 默认 true |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ItemsChanged` | `EventCallback<IEnumerable<TItem>>` | 获得/设置 数据集合回调方法 |
