# ListView (列表视图)

## 概述

`ListView` 组件用于**提供规则排列控件，适用于大量重复的数据实现规则排列**。组件支持普通列表、分页显示、分组显示、分组折叠、分组手风琴等功能。

**主要特性**：
- 支持规则排列大量重复数据
- 支持点击图片触发 `OnListViewItemClick` 事件
- 支持分页显示（`Pageable`/`IsPagination`）
- 支持分组显示（`GroupName`）
- 支持分组排序（`GroupOrderCallback`）
- 支持分组折叠（`Collapsible`）
- 支持分组手风琴效果（`IsAccordion`）
- 支持自定义模板（`BodyTemplate`、`HeaderTemplate`、`FooterTemplate`、`EmptyTemplate`）
- 支持竖向排列（`IsVertical`）
- 支持异步查询（`OnQueryAsync`）

**在线演示**: https://www.blazor.zone/list-view

---

## 使用场景

### 1. 基础用法（普通列表）

适用于大量重复的数据实现规则排列。点击图片时触发 `OnListViewItemClick` 事件。

```razor
<!-- 基础列表视图 -->
<ListView Items="Products" OnListViewItemClick="OnItemClick">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
            <p>@context.Description</p>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg" },
        new Product { Name = "Pic2.jpg", ImageUrl = "/images/pic2.jpg" },
        new Product { Name = "Pic3.jpg", ImageUrl = "/images/pic3.jpg" },
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg" },
        new Product { Name = "Pic5.jpg", ImageUrl = "/images/pic5.jpg" },
        new Product { Name = "Pic6.jpg", ImageUrl = "/images/pic6.jpg" },
        new Product { Name = "Pic7.jpg", ImageUrl = "/images/pic7.jpg" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg" }
    };
    
    private async Task OnItemClick(Product item)
    {
        // 处理项目点击事件
        Console.WriteLine($"点击了：{item.Name}");
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Description { get; set; }
    }
}
```

---

### 2. 分页显示（Pageable/IsPagination）

设置 `Pageable` 或 `IsPagination` 显示分页组件。

```razor
<!-- 分页显示 -->
<ListView Items="Products" IsPagination="true" PageItems="4" OnListViewItemClick="OnItemClick">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg" },
        new Product { Name = "Pic2.jpg", ImageUrl = "/images/pic2.jpg" },
        new Product { Name = "Pic3.jpg", ImageUrl = "/images/pic3.jpg" },
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg" }
    };
    
    private async Task OnItemClick(Product item)
    {
        Console.WriteLine($"点击了：{item.Name}");
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

**说明**：`Pageable` 参数已弃用，请使用 `IsPagination` 参数。

---

### 3. 分组显示（GroupName）

设置 `GroupName` 数据进行分组显示，通过设置 `GroupOrderCallback` 参数细化分组排序规则。

```razor
<!-- 分组显示 -->
<ListView Items="Products" GroupName="GetGroupKey" GroupOrderCallback="GroupOrder">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic7.jpg", ImageUrl = "/images/pic7.jpg", Group = "Group4" },
        new Product { Name = "Pic3.jpg", ImageUrl = "/images/pic3.jpg", Group = "Group4" },
        new Product { Name = "Pic6.jpg", ImageUrl = "/images/pic6.jpg", Group = "Group3" },
        new Product { Name = "Pic2.jpg", ImageUrl = "/images/pic2.jpg", Group = "Group3" },
        new Product { Name = "Pic5.jpg", ImageUrl = "/images/pic5.jpg", Group = "Group2" },
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg", Group = "Group2" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" },
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    private IOrderedEnumerable<IGrouping<string, Product>> GroupOrder(IEnumerable<IGrouping<string, Product>> groups)
    {
        return groups.OrderBy(g => g.Key);
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

### 4. 分组折叠（Collapsible）

设置 `Collapsible="true"` 使分组信息可折叠。

```razor
<!-- 分组折叠 -->
<ListView Items="Products" GroupName="GetGroupKey" Collapsible="true">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" },
        new Product { Name = "Pic5.jpg", ImageUrl = "/images/pic5.jpg", Group = "Group2" },
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg", Group = "Group2" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

### 5. 分组手风琴（IsAccordion）

设置 `IsAccordion="true"` 使分组信息折叠手风琴效果。

```razor
<!-- 分组手风琴 -->
<ListView Items="Products" GroupName="GetGroupKey" Collapsible="true" IsAccordion="true">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" },
        new Product { Name = "Pic5.jpg", ImageUrl = "/images/pic5.jpg", Group = "Group2" },
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg", Group = "Group2" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

### 6. 自定义表头模板（HeaderTemplate）

通过 `HeaderTemplate` 参数设置列表头部内容。

```razor
<!-- 自定义表头 -->
<ListView Items="Products">
    <HeaderTemplate>
        <div class="list-view-header">
            <h3>产品列表</h3>
            <p>Copyright Bootstrap Blazor</p>
        </div>
    </HeaderTemplate>
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg" }
    };
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

---

### 7. 自定义页脚模板（FooterTemplate）

通过 `FooterTemplate` 参数设置列表页脚内容。设置值后，`Pageable` 参数不起作用，请自行实现分页功能。

```razor
<!-- 自定义页脚 -->
<ListView Items="Products">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
    <FooterTemplate>
        <div class="list-view-footer">
            <span>总计：@Products.Count() 个项目</span>
        </div>
    </FooterTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg" }
    };
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

---

### 8. 自定义空数据模板（EmptyTemplate）

通过 `EmptyTemplate` 参数设置无数据时显示的内容。

```razor
<!-- 自定义空数据模板 -->
<ListView Items="EmptyProducts">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
    <EmptyTemplate>
        <div class="list-view-empty">
            <p>暂无数据</p>
        </div>
    </EmptyTemplate>
</ListView>

@code {
    private List<Product> EmptyProducts { get; set; } = new List<Product>();
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

---

### 9. 竖向排列（IsVertical）

通过 `IsVertical` 参数控制是否为竖向排列，默认为 `false`（横向排列）。

```razor
<!-- 竖向排列 -->
<ListView Items="Products" IsVertical="true">
    <BodyTemplate>
        <div class="list-view-item-vertical">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg" }
    };
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

---

### 10. 设置组件高度（Height）

通过 `Height` 参数设置组件高度。

```razor
<!-- 设置高度为 500px -->
<ListView Items="Products" Height="500px">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg" }
    };
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

---

### 11. 异步查询（OnQueryAsync）

通过 `OnQueryAsync` 参数实现异步查询。

```razor
<!-- 异步查询 -->
<ListView Items="Products" OnQueryAsync="OnQuery">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>();
    
    private async Task<QueryData<Product>> OnQuery(QueryPageOptions options)
    {
        // 模拟异步查询
        await Task.Delay(500);
        
        // 返回查询数据
        return new QueryData<Product>
        {
            Items = Products.Skip((options.PageIndex - 1) * options.PageItems).Take(options.PageItems).ToList(),
            TotalCount = Products.Count
        };
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
    }
}
```

---

### 12. 分组折叠回调（CollapsedGroupCallback）

通过 `CollapsedGroupCallback` 参数设置首次渲染是否收缩回调委托。

```razor
<!-- 首次渲染时部分分组收缩 -->
<ListView Items="Products" GroupName="GetGroupKey" Collapsible="true" CollapsedGroupCallback="CollapsedGroup">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" },
        new Product { Name = "Pic5.jpg", ImageUrl = "/images/pic5.jpg", Group = "Group2" },
        new Product { Name = "Pic1.jpg", ImageUrl = "/images/pic1.jpg", Group = "Group2" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    private bool CollapsedGroup(object groupKey)
    {
        // 返回 true 表示该分组首次渲染时收缩
        return groupKey.ToString() == "Group2";
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

### 13. 分组头部文本回调（GroupHeaderTextCallback）

通过 `GroupHeaderTextCallback` 参数设置分组头部显示文本。

```razor
<!-- 自定义分组头部文本 -->
<ListView Items="Products" GroupName="GetGroupKey" GroupHeaderTextCallback="GetGroupHeaderText">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    private string GetGroupHeaderText(object groupKey)
    {
        return $"分组：{groupKey}";
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

### 14. 组内项目排序回调（GroupItemOrderCallback）

通过 `GroupItemOrderCallback` 参数设置组内项目排序规则。

```razor
<!-- 组内项目排序 -->
<ListView Items="Products" GroupName="GetGroupKey" GroupItemOrderCallback="GroupItemOrder">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    private IOrderedEnumerable<Product> GroupItemOrder(IGrouping<string, Product> group)
    {
        return group.OrderBy(p => p.Name);
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

### 15. 折叠状态变化回调（OnCollapseChanged）

通过 `OnCollapseChanged` 参数设置 CollapseItem 展开收缩时回调方法。

```razor
<!-- 折叠状态变化回调 -->
<ListView Items="Products" GroupName="GetGroupKey" Collapsible="true" OnCollapseChanged="OnCollapseChanged">
    <BodyTemplate>
        <div class="list-view-item">
            <img src="@context.ImageUrl" alt="@context.Name" />
            <h4>@context.Name</h4>
        </div>
    </BodyTemplate>
</ListView>

@code {
    private List<Product> Products { get; set; } = new List<Product>
    {
        new Product { Name = "Pic4.jpg", ImageUrl = "/images/pic4.jpg", Group = "Group1" },
        new Product { Name = "Pic8.jpg", ImageUrl = "/images/pic8.jpg", Group = "Group1" }
    };
    
    private string GetGroupKey(Product item)
    {
        return item.Group;
    }
    
    private async Task OnCollapseChanged(CollapseItem item)
    {
        // 处理折叠状态变化
        Console.WriteLine($"分组 {item.Text} 折叠状态：{item.IsCollapsed}");
    }
    
    public class Product
    {
        public string Name { get; set; }
        public string ImageUrl { get; set; }
        public string Group { get; set; }
    }
}
```

---

## 参数 (Parameters)

### ListView 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `BodyTemplate` | `RenderFragment<TItem>?` | `null` | 获得/设置 BodyTemplate |
| `CollapsedGroupCallback` | `Func<object, bool>?` | `null` | 获得/设置 首次渲染是否收缩回调委托 |
| `Collapsible` | `bool` | `false` | 获得/设置 是否可折叠 默认 false 需要开启分组设置 |
| `EmptyTemplate` | `RenderFragment?` | `null` | 获得/设置 无数据时模板 默认 null 未设置 |
| `EmptyText` | `string?` | `null` | 获得/设置 无数据时显示文字 默认 null 未设置使用资源文件设置文字 |
| `FooterTemplate` | `RenderFragment?` | `null` | 获得/设置 FooterTemplate 默认 null 未设置 设置值后 参数不起作用，请自行实现分页功能 |
| `GroupHeaderTextCallback` | `Func<object, string>?` | `null` | 获得/设置 获得 值 默认 null 使用分组 Key.ToString() 方法获取 |
| `GroupItemOrderCallback` | `Func<IGrouping<object, TItem>, IOrderedEnumerable<TItem>>?` | `null` | 获得/设置 组内项目排序回调方法 默认 null |
| `GroupName` | `Func<TItem, object>?` | `null` | 获得/设置 分组 Lambda 表达式 默认 null |
| `GroupOrderCallback` | `Func<IEnumerable<IGrouping<object, TItem>>, IOrderedEnumerable<IGrouping<object, TItem>>>?` | `null` | 获得/设置 组排序回调方法 默认 null 使用内置 |
| `HeaderTemplate` | `RenderFragment?` | `null` | 获得/设置 CardHeader |
| `Height` | `string?` | `null` | 获得/设置 组件高度 默认 null 未设置高度 如：50% 100px 10rem 10vh 等 |
| `IsAccordion` | `bool` | `false` | 获得/设置 是否手风琴效果 默认 false 需要开启可收缩设置 |
| `IsPagination` | `bool` | `false` | 获得/设置 是否分页 默认为 false 不分页 设置 时分页功能自动被禁用 |
| `IsVertical` | `bool` | `false` | 获得/设置 是否为竖向排列 默认为 false |
| `Items` | `IEnumerable<TItem>?` | `null` | 获得/设置 数据源 |
| `OnCollapseChanged` | `Func<CollapseItem, Task>?` | `null` | 获得/设置 CollapseItem 展开收缩时回调方法 默认 false 需要开启可收缩设置 |
| `OnListViewItemClick` | `Func<TItem, Task>?` | `null` | 获得/设置 ListView组件元素点击时回调委托 |
| `OnQueryAsync` | `Func<QueryPageOptions, Task<QueryData<TItem>>>?` | `null` | 异步查询回调方法 |
| `Pageable` | `bool` | `false` | **已弃用** 获得/设置 是否分页 默认为 false 不分页 设置 时分页功能自动被禁用 |
| `PageItems` | `int` | `20` | 获得/设置 每页数据数量 默认 20 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnListViewItemClick` | `Func<TItem, Task>?` | ListView组件元素点击时回调委托 |
| `OnQueryAsync` | `Func<QueryPageOptions, Task<QueryData<TItem>>>?` | 异步查询回调方法 |
| `OnCollapseChanged` | `Func<CollapseItem, Task>?` | CollapseItem 展开收缩时回调方法 |

---

## 最佳实践

1. **使用 Items 绑定数据**：推荐通过 `Items` 参数绑定数据，而不是在 Razor 中手动编写 item
2. **分页显示大量数据**：对于大量数据，使用 `IsPagination="true"` 启用分页功能，避免一次性加载过多数据
3. **分组显示相关数据**：使用 `GroupName` 参数对相关数据分组显示，提高可读性
4. **分组排序**：通过 `GroupOrderCallback` 参数细化分组排序规则，确保分组顺序符合业务需求
5. **分组折叠**：对于分组较多的场景，设置 `Collapsible="true"` 使分组可折叠，减少页面占用空间
6. **手风琴效果**：设置 `IsAccordion="true"` 使分组折叠具有手风琴效果，一次只能展开一个分组
7. **自定义空数据模板**：通过 `EmptyTemplate` 参数自定义无数据时显示的内容，提升用户体验
8. **异步查询**：对于需要服务器端分页的场景，使用 `OnQueryAsync` 参数实现异步查询
9. **竖向排列**：根据布局需求，通过 `IsVertical` 参数控制列表排列方向
10. **Pageable 已弃用**：注意 `Pageable` 参数已弃用，请使用 `IsPagination` 参数

---

## 常见问题

### 1. Pageable 参数已弃用，应该用什么？

**回答**：`Pageable` 参数已弃用，请使用 `IsPagination` 参数来启用分页功能。

### 2. 如何实现分组显示？

**回答**：使用 `GroupName` 参数设置分组 Lambda 表达式，例如 `GroupName="item => item.Category"`。

### 3. 如何自定义分组排序？

**回答**：使用 `GroupOrderCallback` 参数设置组排序回调方法，返回 `IOrderedEnumerable<IGrouping<object, TItem>>` 类型。

### 4. 如何实现分组折叠？

**回答**：设置 `Collapsible="true"` 使分组信息可折叠。需要开启分组设置（设置 `GroupName` 参数）。

### 5. 如何实现手风琴效果？

**回答**：设置 `IsAccordion="true"` 使分组信息折叠具有手风琴效果。需要开启可收缩设置（设置 `Collapsible="true"`）。

### 6. 如何自定义空数据显示？

**回答**：使用 `EmptyTemplate` 参数自定义无数据时显示的内容。

### 7. 如何实现异步查询？

**回答**：使用 `OnQueryAsync` 参数实现异步查询，返回 `Task<QueryData<TItem>>` 类型。

### 8. 如何设置每页数据数量？

**回答**：使用 `PageItems` 参数设置每页数据数量，默认值为 20。

### 9. 如何自定义分组头部文本？

**回答**：使用 `GroupHeaderTextCallback` 参数设置分组头部显示文本，返回 `string` 类型。

### 10. 如何控制首次渲染时分组是否收缩？

**回答**：使用 `CollapsedGroupCallback` 参数设置首次渲染是否收缩回调委托，返回 `bool` 类型，`true` 表示收缩，`false` 表示展开。
