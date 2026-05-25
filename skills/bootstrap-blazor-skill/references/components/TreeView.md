# TreeView (树形视图)

## 概述

`TreeView` 组件是**高级树形视图控件**，相比 `Tree` 组件支持更多功能，如拖拽、编辑、右键菜单等。

**主要特性**：
- 支持展开/折叠节点
- 支持单选/多选
- 支持复选框
- 支持拖拽排序
- 支持节点编辑
- 支持右键菜单
- 可自定义节点内容
- 支持搜索过滤

**在线演示**: https://www.blazor.zone/tree-view

---

## 使用场景

### 1. 基础用法（简单树形视图）

`TreeView` 组件可以通过 `Items` 参数绑定树形数据。

```razor
<!-- 基础树形视图 -->
<TreeView Items="TreeViewItems" />

@code {
    private List<TreeViewItem> TreeViewItems { get; set; } = new List<TreeViewItem>
    {
        new TreeViewItem("1", "节点 1")
        {
            Items = new List<TreeViewItem>
            {
                new TreeViewItem("1-1", "节点 1-1"),
                new TreeViewItem("1-2", "节点 1-2")
            }
        },
        new TreeViewItem("2", "节点 2"),
        new TreeViewItem("3", "节点 3")
    };
}
```

---

### 2. 选择模式（SelectionMode）

通过 `SelectionMode` 参数设置选择模式。

```razor
<!-- 单选模式 -->
<TreeView Items="TreeViewItems" SelectionMode="TreeSelectionMode.Single" @bind-Value="SelectedValue" />

<!-- 多选模式 -->
<TreeView Items="TreeViewItems" SelectionMode="TreeSelectionMode.Multiple" @bind-Values="SelectedValues" />

@code {
    private string? SelectedValue { get; set; }
    private List<string> SelectedValues { get; set; } = new List<string>();
}
```

**选择模式**：
- `TreeSelectionMode.None` - 不可选择
- `TreeSelectionMode.Single` - 单选
- `TreeSelectionMode.Multiple` - 多选

---

### 3. 复选框（ShowCheckbox）

通过设置 `ShowCheckbox="true"` 显示复选框。

```razor
<!-- 带复选框的树形视图 -->
<TreeView Items="TreeViewItems" ShowCheckbox="true" @bind-Values="CheckedValues" />

@code {
    private List<string> CheckedValues { get; set; } = new List<string>();
}
```

---

### 4. 拖拽排序（AllowDrag）

通过设置 `AllowDrag="true"` 启用拖拽排序功能。

```razor
<!-- 可拖拽的树形视图 -->
<TreeView Items="TreeViewItems" AllowDrag="true" OnDragComplete="OnDragComplete" />

@code {
    private List<TreeViewItem> TreeViewItems { get; set; } = new List<TreeViewItem>
    {
        new TreeViewItem("1", "节点 1"),
        new TreeViewItem("2", "节点 2")
    };

    private void OnDragComplete(TreeViewItem draggedItem, TreeViewItem? targetItem)
    {
        // 处理拖拽完成逻辑
        Console.WriteLine($"拖拽 {draggedItem.Text} 到 {targetItem?.Text}");
    }
}
```

---

### 5. 节点编辑（AllowEdit）

通过设置 `AllowEdit="true"` 启用节点编辑功能。

```razor
<!-- 可编辑的树形视图 -->
<TreeView Items="TreeViewItems" AllowEdit="true" OnEditComplete="OnEditComplete" />

@code {
    private List<TreeViewItem> TreeViewItems { get; set; } = new List<TreeViewItem>
    {
        new TreeViewItem("1", "节点 1"),
        new TreeViewItem("2", "节点 2")
    };

    private void OnEditComplete(TreeViewItem item, string newText)
    {
        // 处理编辑完成逻辑
        item.Text = newText;
    }
}
```

---

### 6. 右键菜单（ContextMenuItems）

通过 `ContextMenuItems` 参数设置右键菜单项。

```razor
<!-- 带右键菜单的树形视图 -->
<TreeView Items="TreeViewItems" ContextMenuItems="ContextMenuItems" OnContextMenuClick="OnContextMenuClick" />

@code {
    private List<TreeViewItem> TreeViewItems { get; set; } = new List<TreeViewItem>
    {
        new TreeViewItem("1", "节点 1"),
        new TreeViewItem("2", "节点 2")
    };

    private List<ContextMenuItem> ContextMenuItems { get; set; } = new List<ContextMenuItem>
    {
        new ContextMenuItem("编辑", "fa fa-edit"),
        new ContextMenuItem("删除", "fa fa-trash")
    };

    private void OnContextMenuClick(TreeViewItem item, ContextMenuItem menuItem)
    {
        // 处理右键菜单点击逻辑
        Console.WriteLine($"对 {item.Text} 执行 {menuItem.Text}");
    }
}
```

---

## 参数 (Parameters)

### TreeView 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TreeViewItem>?` | `null` | 获得/设置树形数据 |
| `Value` | `string?` | `null` | 获得/设置选中的值（单选） |
| `Values` | `List<string>?` | `null` | 获得/设置选中的值（多选） |
| `SelectionMode` | `TreeSelectionMode` | `TreeSelectionMode.None` | 获得/设置选择模式 |
| `ShowCheckbox` | `bool` | `false` | 获得/设置是否显示复选框 |
| `AllowDrag` | `bool` | `false` | 获得/设置是否允许拖拽 |
| `AllowEdit` | `bool` | `false` | 获得/设置是否允许编辑 |
| `ShowSearch` | `bool` | `false` | 获得/设置是否显示搜索框 |
| `ExpandAll` | `bool` | `false` | 获得/设置是否展开所有节点 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<string?>` | 选中值变化回调（单选） |
| `ValuesChanged` | `EventCallback<List<string>?>` | 选中值变化回调（多选） |
| `OnExpand` | `Func<TreeViewItem, Task>?` | 节点展开回调 |
| `OnCollapse` | `Func<TreeViewItem, Task>?` | 节点折叠回调 |
| `OnDragComplete` | `Func<TreeViewItem, TreeViewItem?, Task>?` | 拖拽完成回调 |
| `OnEditComplete` | `Func<TreeViewItem, string, Task>?` | 编辑完成回调 |
| `OnContextMenuClick` | `Func<TreeViewItem, ContextMenuItem, Task>?` | 右键菜单点击回调 |

---

## 数据类 (TreeViewItem)

`TreeViewItem` 类定义树形节点的数据。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置节点值 |
| `Text` | `string?` | `null` | 获得/设置节点文本 |
| `Icon` | `string?` | `null` | 获得/设置节点图标 |
| `Items` | `List<TreeViewItem>?` | `null` | 获得/设置子节点 |
| `IsExpanded` | `bool` | `false` | 获得/设置是否展开 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用 |
| `CssClass` | `string?` | `null` | 获得/设置 CSS 类名 |

---

## 最佳实践

1. **与 Tree 组件的区别**：`TreeView` 是高级树形视图，支持拖拽、编辑、右键菜单等高级功能；`Tree` 是简单树形控件，适合基本场景
2. **合理使用选择模式**：根据需求选择 `Single`（单选）或 `Multiple`（多选），不需要选择时使用 `None`
3. **启用拖拽需谨慎**：拖拽功能会改变数据结构，确保在 `OnDragComplete` 事件中正确更新数据源
4. **启用编辑需验证**：编辑功能允许用户输入，确保在 `OnEditComplete` 事件中验证输入内容
5. **提供右键菜单**：对于复杂操作，通过 `ContextMenuItems` 提供右键菜单，提升用户体验
6. **处理事件回调**：对于需要在用户操作时执行逻辑的场景，处理相应的事件回调
7. **性能优化**：对于大量节点（>100），考虑虚拟滚动或分页，避免一次性渲染过多节点
