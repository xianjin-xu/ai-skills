# Pagination 分页

## 概述

Pagination 分页组件用于当数据量过多时，将数据分解成多个页面展示。组件支持多种配置，如下拉框选择每页显示数量、对齐方式设置、跳转导航、分页信息显示等。

> Pagination component is used to decompose data into multiple pages when there is too much data.

**分类**: 导航组件  
**在线演示**: [https://www.blazor.zone/pagination](https://www.blazor.zone/pagination)

---

## 使用场景

### 1. 基础用法

可以通过下拉框选取每页显示数据数量。设置 `PageCount` 属性指定总页数，组件会自动渲染分页导航。

```razor
<Pagination PageCount="10" PageIndex="1" OnPageLinkClick="OnPageClick" />

@code {
    private async Task OnPageClick(int pageIndex)
    {
        // 处理页码点击事件
        Console.WriteLine($"点击了第 {pageIndex} 页");
        await Task.CompletedTask;
    }
}
```

### 2. 仅显示文本提示

只有一页时不显示切换页码组件，仅显示文本提示。通过设置 `ShowPageInfo` 参数为 `false` 可以隐藏分页信息。

```razor
<Pagination PageCount="1" PageIndex="1" ShowPageInfo="false" />
```

### 3. 仅显示分页组件

通过 `ShowPageInfo="false"` 设置不显示文本提示，只显示分页导航按钮。

```razor
<Pagination PageCount="20" PageIndex="1" ShowPageInfo="false" />
```

### 4. 对齐方式

设置 `Alignment` 参数控制页码对齐方式，可选值为 `Start`、`Center`、`End`（默认）。

```razor
<Pagination PageCount="20" PageIndex="1" Alignment="Alignment.Start" />
<Pagination PageCount="20" PageIndex="1" Alignment="Alignment.Center" />
<Pagination PageCount="20" PageIndex="1" Alignment="Alignment.End" />
```

### 5. 跳转导航

通过设置 `ShowGotoNavigator` 参数控制是否显示跳转导航，可以通过 `GotoTemplate` 自定义跳转组件。

```razor
<Pagination PageCount="20" PageIndex="1" ShowGotoNavigator="true" />
```

### 6. 分页信息

通过设置 `ShowPageInfo` 参数控制是否显示分页信息。可以配合 `PageInfoTemplate` 自定义分页信息模板。

```razor
<Pagination PageCount="20" PageIndex="1" ShowPageInfo="true">
    <PageInfoTemplate>
        <div class="page-info">共 @PageCount 页</div>
    </PageInfoTemplate>
</Pagination>
```

### 7. 自定义分页模板

通过 `PageInfoTemplate` 自定义分页信息区域的显示内容，可以实现如"每页 N 条 共 M 页"的自定义格式。

```razor
<Pagination PageCount="100" PageIndex="1" ShowPageInfo="true" ShowGotoNavigator="true">
    <PageInfoTemplate>
        <div class="page-info me-2">每页 2 条 共 @PageCount 页</div>
    </PageInfoTemplate>
</Pagination>
```

### 8. 自定义页码数量

通过设置 `MaxPageLinkCount` 参数控制显示的页码数量，默认值为 5。

```razor
<Pagination PageCount="20" PageIndex="1" MaxPageLinkCount="10" />
```

### 9. 自定义图标

通过设置 `PrevPageIcon`、`NextPageIcon`、`PrevEllipsisPageIcon`、`NextEllipsisPageIcon` 等参数自定义分页组件的图标。

```razor
<Pagination PageCount="20" 
           PageIndex="1" 
           PrevPageIcon="fa-solid fa-chevron-left"
           NextPageIcon="fa-solid fa-chevron-right" />
```

---

## 参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| AdditionalAttributes | 获得/设置 用户自定义属性 | IDictionary<string, Object> | — |
| Alignment | 获得/设置 对齐方式，默认为 Alignment.Right | Alignment | Alignment.Right |
| GotoNavigatorLabelText | 获得/设置 Goto 导航标签显示文字 默认 导航到/Goto | string | 导航到 |
| GotoTemplate | 获得/设置 Goto 导航模板 默认 null | RenderFragment | null |
| MaxPageLinkCount | 获得/设置 Page up/down 页码数量 默认 5 | int | 5 |
| NextEllipsisPageIcon | 获得/设置 下一页省略号图标 | string | — |
| NextPageIcon | 获得/设置 下一页图标 | string | — |
| OnPageLinkClick | 点击页码时回调方法 参数是当前页码 | Func<int, Task> | — |
| PageCount | 获得/设置 页码总数 | int | — |
| PageIndex | 获得/设置 当前页码 | int | 1 |
| PageInfoTemplate | 获得/设置 分页信息模板 默认 null | RenderFragment | null |
| PageInfoText | 获得/设置 显示分页信息文字 默认为 null | string | null |
| PrevEllipsisPageIcon | 获得/设置 上一页省略号图标 | string | — |
| PrevPageIcon | 获得/设置 上一页图标 | string | — |
| ShowGotoNavigator | 获得/设置 是否显示 Goto 跳转导航器 默认 false | bool | false |
| ShowPageInfo | 获得/设置 是否显示 分页信息 默认 true | bool | true |

---

## 事件回调

| 事件名称 | 说明 | 回调类型 |
|---------|------|---------|
| OnPageLinkClick | 点击页码时回调方法，参数是当前页码 | Func<int, Task> |

---

## 最佳实践

### 与表格组件配合使用

Pagination 组件通常与 Table 组件配合使用，实现服务端分页：

```razor
<Table TItem="BindItem" 
       Items="Items" 
       PageItems="PageItems" 
       TotalCount="TotalCount"
       OnPageClick="OnTablePageClick">
    <TableColumns>
        <TableColumn @bind-Field="context.Name" />
        <TableColumn @bind-Field="context.Education" />
    </TableColumns>
</Table>

@code {
    private List<BindItem> Items { get; set; } = new();
    private int PageItems { get; set; } = 10;
    private int TotalCount { get; set; }
    
    private async Task OnTablePageClick(int pageIndex)
    {
        // 根据页码加载数据
        Items = await LoadDataAsync(pageIndex, PageItems);
    }
    
    private async Task<List<BindItem>> LoadDataAsync(int pageIndex, int pageSize)
    {
        // 模拟数据加载
        await Task.Delay(100);
        return Enumerable.Range((pageIndex - 1) * pageSize, pageSize)
            .Select(i => new BindItem { Id = i, Name = $"Item {i}" })
            .ToList();
    }
}
```

### 自定义分页信息显示

通过 `PageInfoTemplate` 可以实现高度自定义的分页信息显示：

```razor
<Pagination PageCount="50" PageIndex="1" ShowPageInfo="true" ShowGotoNavigator="true">
    <PageInfoTemplate>
        <div class="d-flex align-items-center">
            <span class="me-2">每页</span>
            <Select @bind-Value="PageItems" Items="PageItemsSource" Style="width: 80px" />
            <span class="ms-2 me-2">条</span>
            <span>共 @PageCount 页</span>
        </div>
    </PageInfoTemplate>
</Pagination>

@code {
    private int PageItems { get; set; } = 10;
    private List<SelectedItem> PageItemsSource { get; set; } = new()
    {
        new SelectedItem("10", "10"),
        new SelectedItem("20", "20"),
        new SelectedItem("50", "50"),
        new SelectedItem("100", "100")
    };
}
```

---

## 常见问题

### 1. 如何动态更新总页数？

直接修改 `PageCount` 参数即可，组件会自动重新渲染分页导航。

### 2. 如何禁用上一页/下一页按钮？

Pagination 组件会根据 `PageIndex` 和 `PageCount` 自动禁用上一页/下一页按钮，无需手动控制。

### 3. 如何自定义页码点击事件？

通过 `OnPageLinkClick` 回调方法处理页码点击事件，可以在回调中执行数据加载等操作。

### 4. 如何实现服务端分页？

在服务端分页场景中，需要在 `OnPageLinkClick` 回调中根据 `pageIndex` 参数向服务器请求对应页的数据，然后更新页面显示的数据源。

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | Pagination 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/pagination)
- [Table 组件文档](https://www.blazor.zone/table)
