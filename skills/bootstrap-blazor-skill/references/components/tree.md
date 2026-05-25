# Tree (树形控件)

## 概述

`Tree` 组件用于**以树形结构展示数据**，支持展开/折叠、选择、复选等功能。

**主要特性**：
- 支持展开/折叠节点
- 支持单选/多选
- 支持复选框
- 可自定义节点内容
- 支持搜索过滤
- 支持拖拽排序

**在线演示**: https://www.blazor.zone/tree

---

## 使用场景

### 1. 基础用法（简单树形）

`Tree` 组件可以通过 `Items` 参数绑定树形数据。

```razor
<!-- 基础树形 -->
<Tree Items="TreeItems" />

@code {
    private List<TreeItem> TreeItems { get; set; } = new List<TreeItem>
    {
        new TreeItem("1", "节点 1")
        {
            Items = new List<TreeItem>
            {
                new TreeItem("1-1", "节点 1-1"),
                new TreeItem("1-2", "节点 1-2")
            }
        },
        new TreeItem("2", "节点 2"),
        new TreeItem("3", "节点 3")
    };
}
```

---

### 2. 选择模式（SelectionMode）

通过 `SelectionMode` 参数设置选择模式。

```razor
<!-- 单选模式 -->
<Tree Items="TreeItems" SelectionMode="TreeSelectionMode.Single" @bind-Value="SelectedValue" />

<!-- 多选模式 -->
<Tree Items="TreeItems" SelectionMode="TreeSelectionMode.Multiple" @bind-Values="SelectedValues" />

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
<!-- 带复选框的树形 -->
<Tree Items="TreeItems" ShowCheckbox="true" @bind-Values="CheckedValues" />

@code {
    private List<string> CheckedValues { get; set; } = new List<string>();
}
```

---

### 4. 搜索过滤（ShowSearch）

通过设置 `ShowSearch="true"` 启用搜索过滤功能。

```razor
<!-- 带搜索的树形 -->
<Tree Items="TreeItems" ShowSearch="true" />

@code {
    private List<TreeItem> TreeItems { get; set; } = new List<TreeItem>
    {
        new TreeItem("1", "节点 1"),
        new TreeItem("2", "节点 2"),
        new TreeItem("3", "节点 3")
    };
}
```

---

### 5. 自定义节点内容（ItemTemplate）

通过 `ItemTemplate` 参数自定义节点显示内容。

```razor
<!-- 自定义节点 -->
<Tree Items="TreeItems">
    <ItemTemplate>
        <div>
            <i class="fa fa-folder"></i>
            <span>@context.Text</span>
            <small>(@context.Value)</small>
        </div>
    </ItemTemplate>
</Tree>

@code {
    private List<TreeItem> TreeItems { get; set; } = new List<TreeItem>
    {
        new TreeItem("1", "节点 1"),
        new TreeItem("2", "节点 2")
    };
}
```

---

## 参数 (Parameters)

### Tree 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TreeItem>?` | `null` | 获得/设置树形数据 |
| `Value` | `string?` | `null` | 获得/设置选中的值（单选） |
| `Values` | `List<string>?` | `null` | 获得/设置选中的值（多选） |
| `SelectionMode` | `TreeSelectionMode` | `TreeSelectionMode.None` | 获得/设置选择模式 |
| `ShowCheckbox` | `bool` | `false` | 获得/设置是否显示复选框 |
| `ShowSearch` | `bool` | `false` | 获得/设置是否显示搜索框 |
| `ExpandAll` | `bool` | `false` | 获得/设置是否展开所有节点 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<string?>` | 选中值变化回调（单选） |
| `ValuesChanged` | `EventCallback<List<string>?>` | 选中值变化回调（多选） |
| `OnExpand` | `Func<TreeItem, Task>?` | 节点展开回调 |
| `OnCollapse` | `Func<TreeItem, Task>?` | 节点折叠回调 |

---

## 数据类 (TreeItem)

`TreeItem` 类定义树形节点的数据。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置节点值 |
| `Text` | `string?` | `null` | 获得/设置节点文本 |
| `Icon` | `string?` | `null` | 获得/设置节点图标 |
| `Items` | `List<TreeItem>?` | `null` | 获得/设置子节点 |
| `IsExpanded` | `bool` | `false` | 获得/设置是否展开 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用 |
| `CssClass` | `string?` | `null` | 获得/设置 CSS 类名 |

---

## 最佳实践

1. **使用 Items 绑定数据**：推荐通过 `Items` 参数绑定数据，而不是在 Razor 中手动编写 `<TreeItem>` 标签
2. **合理设置 SelectionMode**：根据需求选择 `Single`（单选）或 `Multiple`（多选），不需要选择时使用 `None`
3. **提供搜索功能**：对于大量数据，设置 `ShowSearch="true"` 提供搜索功能，提升用户体验
4. **处理 ValueChanged 事件**：对于需要在选中值变化时执行逻辑的场景，处理 `ValueChanged` 或 `ValuesChanged` 事件
5. **自定义节点内容**：对于复杂内容，使用 `ItemTemplate` 自定义节点显示
6. **与 TreeView 组件的区别**：`Tree` 是简单树形控件，`TreeView` 是高级树形视图（可能支持更多功能如拖拽、编辑等）
