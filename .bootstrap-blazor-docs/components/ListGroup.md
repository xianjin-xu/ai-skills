# ListGroup (列表组)

## 概述

`ListGroup` 是一个列表组组件，提供列表项展示功能，支持点击回调、双击回调、自定义模板等配置。

> ListGroup Component!

**分类**: 数据展示  
**在线演示**: [https://www.blazor.zone/list-group](https://www.blazor.zone/list-group)

## 使用场景!

### 1. 基本用法

```razor
<ListGroup TItem="DemoItem" Items="ListItems" />
```

```csharp
@code {
    List<DemoItem> ListItems = new List<DemoItem>
    {
        new DemoItem { Text = "Item 1" },
        new DemoItem { Text = "Item 2" },
        new DemoItem { Text = "Item 3" }
    };
}
```

### 2. 绑定选中值

```razor
<ListGroup TItem="DemoItem" Items="ListItems" @bind-Value="SelectedItem" />
```

```csharp
@code {
    DemoItem? SelectedItem { get; set; }
}
```

### 3. 自定义模板

```razor
<ListGroup TItem="DemoItem" Items="ListItems">
    <ItemTemplate>
        <i class="fa-solid fa-star"></i>
        <span>@context.Text</span>
    </ItemTemplate>
</ListGroup>
```

### 4. 点击回调

```razor
<ListGroup TItem="DemoItem" Items="ListItems" OnClickItem="OnItemClick" />
```

```csharp
@code {
    async Task OnItemClick(DemoItem item)
    {
        // 处理点击事件
    }
}
```

### 5. 双击回调

```razor
<ListGroup TItem="DemoItem" Items="ListItems" OnDoubleClickItem="OnItemDoubleClick" />
```

```csharp
@code {
    async Task OnItemDoubleClick(DemoItem item)
    {
        // 处理双击事件
    }
}
```

### 6. 自定义显示文本

```razor
<ListGroup TItem="DemoItem" Items="ListItems" GetItemDisplayText="GetDisplayText" />
```

```csharp
@code {
    string GetDisplayText(DemoItem item) => item.Text;
}
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `List<TItem>?` | `[]` | 获得/设置数据源集合 |
| `Value` | `TItem?` | `default` | 获得/设置当前选中项 |
| `HeaderTemplate` | `RenderFragment?` | `null` | 获得/设置头部模板 |
| `HeaderText` | `string?` | `null` | 获得/设置头部文字 |
| `ItemTemplate` | `RenderFragment<TItem>?` | `null` | 获得/设置列表项模板 |
| `OnClickItem` | `Func<TItem, Task>?` | `null` | 获得/设置点击列表项回调方法 |
| `OnDoubleClickItem` | `Func<TItem, Task>?` | `null` | 获得/设置双击列表项回调方法 |
| `GetItemDisplayText` | `Func<TItem, string>?` | `null` | 获得/设置获取条目显示文本内容回调方法 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `ValueChanged` | 值改变时触发 |
| `OnClickItem` | 点击列表项时触发 |
| `OnDoubleClickItem` | 双击列表项时触发 |

## 最佳实践!

1. **数据绑定**: 使用 `Items` 参数提供列表数据集合
2. **值绑定**: 使用 `Value` 参数绑定选中项，支持双向绑定（`@bind-Value`）
3. **点击处理**: 使用 `OnClickItem` 回调处理列表项点击事件
4. **双击处理**: 使用 `OnDoubleClickItem` 回调处理列表项双击事件
5. **自定义模板**: 使用 `ItemTemplate` 自定义列表项显示方式
6. **显示文本**: 使用 `GetItemDisplayText` 回调自定义列表项显示文本

## 常见问题

### Q: 如何绑定列表数据？
A: 使用 `Items` 参数提供列表数据集合，类型由 `TItem` 泛型参数指定。

### Q: 如何绑定选中项？
A: 使用 `Value` 参数绑定选中项，支持双向绑定（`@bind-Value`）。

### Q: 如何自定义列表项显示？
A: 使用 `ItemTemplate` 模板自定义列表项显示方式，使用 `GetItemDisplayText` 回调自定义显示文本。

### Q: 如何处理点击/双击事件？
A: 使用 `OnClickItem` 和 `OnDoubleClickItem` 回调处理点击和双击事件。

### Q: 如何自定义头部？
A: 使用 `HeaderTemplate` 模板或 `HeaderText` 参数自定义头部内容。
