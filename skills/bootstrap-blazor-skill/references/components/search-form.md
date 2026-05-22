# SearchForm

## 概述

搜索表单类

> Search Form Component

**分类**: 其他

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Task` | `Func<FilterKeyValueAction,` | `}` | 获得/设置 过滤器改变回调事件 Func 版本 |
| `ItemsPerRow` | `int?` | `}` | 获得/设置 每行显示组件数量 默认为 null |
| `RowType` | `RowType` | `}` | 获得/设置 设置行格式 默认 Row 布局 |
| `LabelAlign` | `Alignment` | `}` | 获得/设置 设置 <see cref="RowType" /> Inline 模式下标签对齐方式 默认 None 等效于 Left 左对齐 |
| `LabelWidth` | `int?` | `}` | 获得/设置 标签宽度 默认 null 未设置使用全局设置 <code>--bb-row-label-width</code> 值 |
| `Buttons` | `RenderFragment?` | `}` | 获得/设置 按钮模板 |
| `ShowLabel` | `bool?` | `}` | 获得/设置 是否显示前置标签 默认为 null 未设置时默认显示标签 |
| `ShowLabelTooltip` | `bool?` | `}` | 获得/设置 是否显示标签 Tooltip 多用于标签文字过长导致裁减时使用 默认 null |
| `Items` | `IEnumerable<ISearchItem>?` | `}` | 获得/设置 绑定字段信息集合 |
| `ShowUnsetGroupItemsOnTop` | `bool` | `}` | 获得/设置 未设置 GroupName 编辑项是否放置在顶部 默认 false |
| `GroupType` | `EditorFormGroupType` | `}` | 获得/设置 分组类型 默认 <see cref="EditorFormGroupType.GroupBox"/> |
| `SearchFormLocalizerOptions` | `SearchFormLocalizerOptions?` | `}` | 获得/设置 搜索表单本地化配置项 |
