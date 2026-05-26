# ContextMenu (右键菜单)

## 概述

`ContextMenu` 组件用于**用户点击鼠标右键时弹出的上下文关联菜单**。组件支持在指定区域内右键弹出菜单，并可以自定义菜单项、处理菜单项点击事件等。

**主要特性**：
- 支持在 `ContextMenuZone` 内区域右键弹出上下文菜单
- 支持自定义菜单项（`ContextMenuItem`）
- 支持菜单项图标和文本设置
- 支持菜单项点击事件（`OnClick`）
- 支持弹出前回调（`OnBeforeShowCallback`）
- 支持菜单项禁用回调（`OnDisabledCallback`）
- 支持在 Table 组件中使用
- 支持在 Tree 组件中使用

**在线演示**: https://www.blazor.zone/context-menu

---

## 使用场景

### 1. 基础用法（在 ContextMenuZone 内右键）

点击 `ContextMenuZone` 内区域右键，弹出上下文关联菜单。

```razor
<!-- 基础右键菜单 -->
<ContextMenuZone>
    <div class="border p-5">
        <p>张三 1000 - 上海市普陀区金沙江路 1747 弄</p>
    </div>
    <ContextMenu>
        <ContextMenuItem Icon="fa-solid fa-copy" Text="复制" OnClick="OnCopy" />
        <ContextMenuItem Icon="fa-solid fa-paste" Text="粘贴" OnClick="OnPaste" />
        <ContextMenuItem Icon="fa-solid fa-cut" Text="剪切" OnClick="OnCut" />
    </ContextMenu>
</ContextMenuZone>

@code {
    private void OnCopy()
    {
        // 处理复制逻辑
        Console.WriteLine("复制");
    }
    
    private void OnPaste()
    {
        // 处理粘贴逻辑
        Console.WriteLine("粘贴");
    }
    
    private void OnCut()
    {
        // 处理剪切逻辑
        Console.WriteLine("剪切");
    }
}
```

---

### 2. 自定义组件（点击 Li 弹出菜单）

点击 `Li` 弹出上下文关联菜单。

```razor
<!-- 自定义组件右键菜单 -->
<ContextMenuZone>
    <ul class="list-unstyled">
        <li>
            Test1
            <ContextMenu>
                <ContextMenuItem Icon="fa-solid fa-edit" Text="编辑" OnClick="() => OnEdit('Test1')" />
                <ContextMenuItem Icon="fa-solid fa-trash" Text="删除" OnClick="() => OnDelete('Test1')" />
            </ContextMenu>
        </li>
        <li>
            Test2
            <ContextMenu>
                <ContextMenuItem Icon="fa-solid fa-edit" Text="编辑" OnClick="() => OnEdit('Test2')" />
                <ContextMenuItem Icon="fa-solid fa-trash" Text="删除" OnClick="() => OnDelete('Test2')" />
            </ContextMenu>
        </li>
        <li>
            Test3
            <ContextMenu>
                <ContextMenuItem Icon="fa-solid fa-edit" Text="编辑" OnClick="() => OnEdit('Test3')" />
                <ContextMenuItem Icon="fa-solid fa-trash" Text="删除" OnClick="() => OnDelete('Test3')" />
            </ContextMenu>
        </li>
    </ul>
</ContextMenuZone>

@code {
    private void OnEdit(string item)
    {
        Console.WriteLine($"编辑: {item}");
    }
    
    private void OnDelete(string item)
    {
        Console.WriteLine($"删除: {item}");
    }
}
```

---

### 3. 在 Table 组件中使用

点击 Table 组件行数据右键，弹出上下文关联菜单。

```razor
<!-- 在 Table 中使用右键菜单 -->
<Table Items="Items">
    <TableColumns>
        <TableColumn @bind-Field="context.Date" />
        <TableColumn @bind-Field="context.Name" />
        <TableColumn @bind-Field="context.Address" />
    </TableColumns>
    <TableTemplate>
        <ContextMenu>
            <ContextMenuItem Icon="fa-solid fa-edit" Text="编辑" OnClick="() => OnEditItem(context)" />
            <ContextMenuItem Icon="fa-solid fa-trash" Text="删除" OnClick="() => OnDeleteItem(context)" />
        </ContextMenu>
    </TableTemplate>
</Table>

@code {
    private List<Customer> Items { get; set; } = new List<Customer>
    {
        new Customer { Date = DateTime.Parse("2026/5/26 03:41:48"), Name = "张三 0001", Address = "上海市普陀区金沙江路 1254 弄" },
        new Customer { Date = DateTime.Parse("2026/5/27 03:41:48"), Name = "张三 0002", Address = "上海市普陀区金沙江路 1870 弄" },
        new Customer { Date = DateTime.Parse("2026/5/28 03:41:48"), Name = "张三 0003", Address = "上海市普陀区金沙江路 1876 弄" }
    };
    
    private void OnEditItem(Customer item)
    {
        Console.WriteLine($"编辑: {item.Name}");
    }
    
    private void OnDeleteItem(Customer item)
    {
        Console.WriteLine($"删除: {item.Name}");
    }
    
    public class Customer
    {
        public DateTime Date { get; set; }
        public string Name { get; set; }
        public string Address { get; set; }
    }
}
```

---

### 4. 在 Tree 组件中使用

点击 Tree 组件行数据右键，弹出上下文关联菜单。

```razor
<!-- 在 Tree 中使用右键菜单 -->
<Tree Items="TreeItems">
    <TreeTemplate>
        <ContextMenu>
            <ContextMenuItem Icon="fa-solid fa-edit" Text="编辑" OnClick="() => OnEditNode(context)" />
            <ContextMenuItem Icon="fa-solid fa-trash" Text="删除" OnClick="() => OnDeleteNode(context)" />
        </ContextMenu>
    </TreeTemplate>
</Tree>

@code {
    private List<TreeItem> TreeItems { get; set; } = new List<TreeItem>
    {
        new TreeItem { Text = "Navigation one" },
        new TreeItem { Text = "Navigation two" },
        new TreeItem { Text = "Sub menu 1" },
        new TreeItem { Text = "Sub menu 2" },
        new TreeItem { Text = "Sub Menu One" },
        new TreeItem { Text = "Sub Menu Two" },
        new TreeItem { Text = "Sub Menu Three" },
        new TreeItem { Text = "Sub menu 3" },
        new TreeItem { Text = "Navigation three" }
    };
    
    private void OnEditNode(TreeItem item)
    {
        Console.WriteLine($"编辑节点: {item.Text}");
    }
    
    private void OnDeleteNode(TreeItem item)
    {
        Console.WriteLine($"删除节点: {item.Text}");
    }
    
    public class TreeItem
    {
        public string Text { get; set; }
    }
}
```

---

### 5. ContextMenu 回调（OnBeforeShowCallback）

通过设置 `ContextMenu` 组件参数 `OnBeforeShowCallback` 获得右键菜单弹出前回调事件，可用于数据准备工作，也可按需渲染菜单。

```razor
<!-- 弹出前回调 -->
<ContextMenuZone>
    <div class="border p-5">
        <p>右键点击此区域</p>
    </div>
    <ContextMenu OnBeforeShowCallback="OnBeforeShow">
        @if (SelectModel?.Id == "1020")
        {
            <ContextMenuItem Icon="fa-solid fa-copy" Text="复制" OnClick="OnCopy" />
            <ContextMenuItem Icon="fa-solid fa-paste" Text="粘贴" OnClick="OnPaste" />
        }
        else
        {
            <ContextMenuItem Icon="fa-solid fa-copy" Text="复制子项" OnClick="OnCopySub" />
        }
    </ContextMenu>
</ContextMenuZone>

@code {
    private Model SelectModel { get; set; }
    
    private Task OnBeforeShow(object sender)
    {
        // 弹出前的准备工作
        // sender 是触发右键的对象
        SelectModel = sender as Model;
        Console.WriteLine("菜单即将弹出");
        return Task.CompletedTask;
    }
    
    private void OnCopy()
    {
        Console.WriteLine("复制");
    }
    
    private void OnPaste()
    {
        Console.WriteLine("粘贴");
    }
    
    private void OnCopySub()
    {
        Console.WriteLine("复制子项");
    }
    
    public class Model
    {
        public string Id { get; set; }
    }
}
```

---

### 6. 禁用回调方法（OnDisabledCallback）

通过设置 `ContextMenuItem` 组件参数 `OnDisabledCallback` 回调方法可用于设置当前右键选项是否禁用逻辑。

```razor
<!-- 禁用回调 -->
<ContextMenuZone>
    <div class="border p-5">
        <p>右键点击此区域</p>
    </div>
    <ContextMenu>
        <ContextMenuItem Icon="fa-solid fa-copy" Text="复制" OnClick="OnCopy" OnDisabledCallback="OnCopyDisabled" />
        <ContextMenuItem Icon="fa-solid fa-paste" Text="粘贴" OnClick="OnPaste" OnDisabledCallback="OnPasteDisabled" />
    </ContextMenu>
</ContextMenuZone>

@code {
    private bool OnCopyDisabled()
    {
        // 返回 true 表示禁用此菜单项
        return false; // 不禁用
    }
    
    private bool OnPasteDisabled()
    {
        // 返回 true 表示禁用此菜单项
        return true; // 禁用粘贴
    }
    
    private void OnCopy()
    {
        Console.WriteLine("复制");
    }
    
    private void OnPaste()
    {
        Console.WriteLine("粘贴");
    }
}
```

---

### 7. 完整示例（包含所有功能）

```razor
<!-- 完整右键菜单示例 -->
<ContextMenuZone>
    <Table Items="Items">
        <TableColumns>
            <TableColumn @bind-Field="context.Date" />
            <TableColumn @bind-Field="context.Name" />
            <TableColumn @bind-Field="context.Address" />
        </TableColumns>
        <TableTemplate>
            <ContextMenu OnBeforeShowCallback="OnBeforeShow">
                <ContextMenuItem Icon="fa-solid fa-edit" Text="编辑" OnClick="() => OnEditItem(context)" OnDisabledCallback="() => false" />
                <ContextMenuItem Icon="fa-solid fa-trash" Text="删除" OnClick="() => OnDeleteItem(context)" OnDisabledCallback="() => context.Name.Contains('0003')" />
                <ContextMenuItem Icon="fa-solid fa-eye" Text="查看" OnClick="() => OnViewItem(context)" />
            </ContextMenu>
        </TableTemplate>
    </Table>
</ContextMenuZone>

@code {
    private List<Customer> Items { get; set; } = new List<Customer>
    {
        new Customer { Date = DateTime.Parse("2026/5/26 03:41:48"), Name = "张三 0001", Address = "上海市普陀区金沙江路 1254 弄" },
        new Customer { Date = DateTime.Parse("2026/5/27 03:41:48"), Name = "张三 0002", Address = "上海市普陀区金沙江路 1870 弄" },
        new Customer { Date = DateTime.Parse("2026/5/28 03:41:48"), Name = "张三 0003", Address = "上海市普陀区金沙江路 1876 弄" }
    };
    
    private Task OnBeforeShow(object sender)
    {
        Console.WriteLine("菜单即将弹出");
        return Task.CompletedTask;
    }
    
    private void OnEditItem(Customer item)
    {
        Console.WriteLine($"编辑: {item.Name}");
    }
    
    private void OnDeleteItem(Customer item)
    {
        Console.WriteLine($"删除: {item.Name}");
    }
    
    private void OnViewItem(Customer item)
    {
        Console.WriteLine($"查看: {item.Name}");
    }
    
    public class Customer
    {
        public DateTime Date { get; set; }
        public string Name { get; set; }
        public string Address { get; set; }
    }
}
```

---

## 参数 (Parameters)

### ContextMenu 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件 |
| `ShowShadow` | `bool` | `true` | 获得/设置 是否显示阴影 默认 true |
| `OnBeforeShowCallback` | `Func<object?, Task>?` | `null` | 获得/设置 弹出前回调方法 默认 null |

---

### ContextMenuItem 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Icon` | `string?` | `null` | 获得/设置 菜单项图标 |
| `Text` | `string?` | `null` | 获得/设置 菜单项文本 |
| `OnClick` | `Action?` | `null` | 获得/设置 菜单项点击回调 |
| `OnDisabledCallback` | `Func<bool>?` | `null` | 获得/设置 禁用回调方法 默认 null |
| `Disabled` | `bool` | `false` | 获得/设置 是否禁用 默认 false |
| `CssClass` | `string?` | `null` | 获得/设置 自定义 CSS 类 |

---

## 事件回调 (EventCallbacks)

### ContextMenu 事件

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnBeforeShowCallback` | `Func<object?, Task>?` | 弹出前回调方法 |

### ContextMenuItem 事件

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnClick` | `Action?` | 菜单项点击回调 |
| `OnDisabledCallback` | `Func<bool>?` | 禁用回调方法 |

---

## 最佳实践

1. **使用 ContextMenuZone**：将 `ContextMenu` 放在 `ContextMenuZone` 内，限定右键菜单的触发区域
2. **合理设置菜单项**：根据上下文提供相关的菜单项，避免菜单项过多影响用户体验
3. **使用图标增强可读性**：通过 `Icon` 参数为菜单项添加图标，使菜单更直观
4. **处理弹出前回调**：使用 `OnBeforeShowCallback` 在菜单弹出前进行数据准备或条件判断
5. **动态渲染菜单项**：根据上下文状态在 `OnBeforeShowCallback` 中动态决定显示哪些菜单项
6. **禁用不适用的菜单项**：使用 `OnDisabledCallback` 或 `Disabled` 属性禁用当前上下文不适用的菜单项
7. **在 Table/Tree 中使用**：在 Table 或 Tree 组件中使用右键菜单时，通过 `TableTemplate` 或 `TreeTemplate` 定义菜单
8. **避免菜单项过多**：右键菜单应简洁明了，避免超过 10 个菜单项

---

## 常见问题

### 1. 如何限定右键菜单的触发区域？

**回答**：使用 `ContextMenuZone` 组件包裹触发区域，`ContextMenu` 组件放在 `ContextMenuZone` 内。只有在该区域内右键才会弹出菜单。

### 2. 如何在菜单弹出前执行逻辑？

**回答**：使用 `ContextMenu` 的 `OnBeforeShowCallback` 回调，在菜单弹出前执行逻辑，例如数据准备、条件判断等。

### 3. 如何动态显示不同的菜单项？

**回答**：在 `OnBeforeShowCallback` 回调中根据条件判断，然后在 `ContextMenu` 的子内容中使用 `@if` 或 `@switch` 语句动态渲染菜单项。

### 4. 如何禁用某个菜单项？

**回答**：有两种方式：
- 使用 `Disabled="true"` 静态禁用
- 使用 `OnDisabledCallback` 回调动态判断是否禁用

### 5. 如何在 Table 中使用右键菜单？

**回答**：在 `Table` 组件的 `TableTemplate` 中定义 `ContextMenu`，通过 `context` 访问当前行数据。

### 6. 如何在 Tree 中使用右键菜单？

**回答**：在 `Tree` 组件的 `TreeTemplate` 中定义 `ContextMenu`，通过 `context` 访问当前节点数据。

### 7. ContextMenu 的 OnBeforeShowCallback 参数类型是什么？

**回答**：`OnBeforeShowCallback` 的类型是 `Func<object?, Task>?`，参数为触发右键的对象（通常是数据项）。

### 8. 如何设置菜单项图标？

**回答**：使用 `ContextMenuItem` 的 `Icon` 参数设置图标，例如 `Icon="fa-solid fa-edit"`。

### 9. 如何处理菜单项点击？

**回答**：使用 `ContextMenuItem` 的 `OnClick` 参数设置点击事件处理程序，类型为 `Action?`。

### 10. 如何自定义菜单项样式？

**回答**：使用 `ContextMenuItem` 的 `CssClass` 参数添加自定义 CSS 类，然后通过 CSS 样式自定义外观。
