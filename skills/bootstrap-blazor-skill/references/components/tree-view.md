# TreeView

## 概述

Tree 组件

> Tree Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/tree-view](https://www.blazor.zone/tree-view)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ShowToolbar` | `bool` | `}` | 获得/设置 是否显示树视图项的工具栏，默认为 false |
| `Task` | `Func<TreeViewItem<TItem>,` | `}` | 获得/设置 确定是否显示树视图项工具栏的回调方法 |
| `IsDisabled` | `bool` | `}` | 获得/设置 整个组件是否被禁用，默认为 false |
| `CanExpandWhenDisabled` | `bool` | `}` | 获得/设置 组件被禁用时，节点是否可以展开或折叠，默认为 false |
| `IsAccordion` | `bool` | `}` | 获得/设置 树视图是否具有手风琴行为，默认为 false。虚拟滚动模式不支持手风琴行为 |
| `ClickToggleNode` | `bool` | `}` | 获得/设置 点击节点是否展开或折叠其子节点，默认为 false |
| `ClickToggleCheck` | `bool` | `}` | 获得/设置 点击节点是否切换其复选框状态，默认为 false。仅在 ShowCheckbox 为 true 时有效 |
| `ShowSkeleton` | `bool` | `}` | 获得/设置 是否显示加载骨架，默认为 false |
| `ShowSearch` | `bool` | `}` | 获得/设置 是否显示搜索栏，默认为 false |
| `ShowResetSearchButton` | `bool` | `true` | 获得/设置 是否显示重置搜索按钮，默认为 true |
| `SearchTemplate` | `RenderFragment?` | `}` | 获得/设置 搜索栏模板，默认为 null |
| `SearchIcon` | `string?` | `}` | 获得/设置 搜索图标，默认未设置，使用内置主题图标 |
| `ClearSearchIcon` | `string?` | `}` | 获得/设置 清除搜索图标，默认未设置，使用内置主题图标 |
| `Items` | `List<TreeViewItem<TItem>>?` | `}` | 获得/设置 分层数据集合 |
| `ShowCheckbox` | `bool` | `}` | 获得/设置 是否显示复选框，默认为 false |
| `MaxSelectedCount` | `int` | `}` | 获得/设置 最多选中项数 |
| `OnMaxSelectedCountExceed` | `Func<Task>?` | `}` | 获得/设置 超过最多选中项数时的回调方法 |
| `ShowIcon` | `bool` | `}` | 获得/设置 是否显示图标，默认为 false |
| `CustomKeyAttribute` | `Type` | `typeof(KeyAttribute)` | - |
| `TItem` | `Func<TItem,` | `}` | - |
| `LoadingIcon` | `string?` | `}` | 获得/设置 树节点的加载图标 |
| `NodeIcon` | `string?` | `}` | 获得/设置 树节点的图标 |
| `ExpandNodeIcon` | `string?` | `}` | 获得/设置 展开状态的树节点图标 |
| `EnableKeyboard` | `bool` | `}` | 获得/设置 是否启用键盘导航，默认为 false。 <para>ArrowLeft 收缩节点 |
| `IsAutoScrollIntoView` | `bool` | `}` | 获得/设置 是否将 active 选中节点自动滚动到可视状态 |
| `ScrollIntoViewOptions` | `ScrollIntoViewOptions?` | `}` | 获得/设置 键盘导航时的滚动至视图选项，默认为 null，使用 { behavior: "smooth", block: "nearest", inline: "start" } |
| `IsVirtualize` | `bool` | `}` | 获得/设置 是否启用虚拟滚动，默认为 false |
| `RowHeight` | `float` | `29f` | - |
| `OverscanCount` | `int` | `10` | - |
| `ToolbarTemplate` | `RenderFragment<TItem>?` | `}` | 获得/设置 工具栏内容模板，默认为 null |
| `ToolbarEditTitle` | `string?` | `}` | 获得/设置 弹出窗口标题，默认为 null |
| `ToolbarEditLabelText` | `string?` | `}` | 获得/设置 弹出窗口标签文本，默认为 null |
| `string` | `Func<TItem,` | `}` | 获得/设置 更新树文本值的回调，默认为 null. 如果返回 true 则更新树文本值，否则不更新 |
| `AutoCheckChildren` | `bool` | `}` | 获得/设置 节点状态变化时是否自动更新子节点，默认为 false |
| `AutoCheckParent` | `bool` | `}` | 获得/设置 节点状态变化时是否自动更新父节点，默认为 false |
| `AllowDrag` | `bool` | `}` | 获得/设置 是否允许拖放操作，默认为 false |

## 代码示例

### 基本用法

```razor
<TreeView Items="@NormalItems" OnTreeItemClick="@OnTreeItemClick" ShowToolbar="true"></TreeView>
```

### 基本用法

```razor
<TreeView Items="@CheckedItems" ShowCheckbox="true" OnTreeItemChecked="@OnTreeItemChecked" AutoCheckChildren="@AutoCheckChildren" AutoCheckParent="@AutoCheckParent"></TreeView>
```

### 基本用法

```razor
<TreeView Items="@DraggableItems" AllowDrag="true" OnDragItemEndAsync="OnDragItemEndAsync">
    </TreeView>
```

### 基本用法

```razor
<TreeView Items="@DisabledItems" ShowCheckbox="true" IsDisabled="@IsDisabled" CanExpandWhenDisabled="@DisableCanExpand"></TreeView>
```

### 基本用法

```razor
<TreeView Items="@AccordionItems" OnExpandNodeAsync="TreeFoo.OnExpandAccordionNodeAsync" ShowCheckbox="true" IsAccordion="true"></TreeView>
```
