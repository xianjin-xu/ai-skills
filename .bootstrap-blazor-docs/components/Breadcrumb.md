# Breadcrumb (面包屑)

## 概述

`Breadcrumb` 组件用于**显示当前页面的路径，快速返回之前的任意页面**。

**主要特性**：
- 显示页面导航路径
- 支持点击返回之前页面
- 支持设置当前页面（IsActive）
- 数据驱动（Value 绑定 BreadcrumbItem 列表）

**在线演示**: https://www.blazor.zone/breadcrumb

---

## 使用场景

### 1. 基础用法（简单面包屑）

适用广泛的基础用法，通过 `Value` 参数绑定面包屑数据。

```razor
<!-- 基础面包屑 -->
<Breadcrumb Value="BreadcrumbItems" />

@code {
    private List<BreadcrumbItem> BreadcrumbItems { get; set; } = new List<BreadcrumbItem>
    {
        new BreadcrumbItem("Home", "/"),
        new BreadcrumbItem("Library", "/library"),
        new BreadcrumbItem("Data", "/library/data") { IsActive = true }
    };
}
```

**显示效果**：Home / Library / Data

---

### 2. 设置当前页面（IsActive）

通过设置 `IsActive = true` 标记当前页面（通常最后一个为当前页面）。

```razor
<!-- 当前页面：Data -->
<Breadcrumb Value="BreadcrumbItems" />

@code {
    private List<BreadcrumbItem> BreadcrumbItems { get; set; } = new List<BreadcrumbItem>
    {
        new BreadcrumbItem("首页", "/"),
        new BreadcrumbItem("产品", "/products"),
        new BreadcrumbItem("详情", "/products/123") { IsActive = true }
    };
}
```

---

### 3. 动态生成面包屑（根据路由）

根据当前路由动态生成面包屑数据。

```razor
<!-- 动态面包屑 -->
<Breadcrumb Value="GetBreadcrumbItems()" />

@code {
    private List<BreadcrumbItem> GetBreadcrumbItems()
    {
        var items = new List<BreadcrumbItem>
        {
            new BreadcrumbItem("首页", "/")
        };
        
        // 根据当前路由添加面包屑项
        var currentPath = NavigationManager.Uri;
        if (currentPath.Contains("/products"))
        {
            items.Add(new BreadcrumbItem("产品", "/products"));
        }
        
        if (currentPath.Contains("/products/"))
        {
            items.Add(new BreadcrumbItem("详情", currentPath) { IsActive = true });
        }
        
        return items;
    }
    
    [Inject]
    private NavigationManager NavigationManager { get; set; } = null!;
}
```

---

## 参数 (Parameters)

### Breadcrumb 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `IEnumerable<BreadcrumbItem>?` | `null` | 获得/设置 数据集 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 数据类 (BreadcrumbItem)

`BreadcrumbItem` 类定义面包屑项的数据。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置 显示文本 |
| `Url` | `string?` | `null` | 获得/设置 链接地址 |
| `IsActive` | `bool` | `false` | 获得/设置 是否当前页面 |

---

## 最佳实践

1. **合理设置 IsActive**：最后一个面包屑项设置 `IsActive = true`，标记为当前页面
2. **URL 可点击**：`Url` 属性设置链接地址，点击可跳转（当前页面 IsActive=true 时不可点击）
3. **与导航配合**：通常在 `MainLayout` 中根据路由动态生成面包屑
4. **避免过度嵌套**：面包屑层级不宜过深（建议 ≤ 4 层），避免过长
5. **与 Menu 的区别**：`Breadcrumb` 是页面路径导航，`Menu` 是功能菜单导航
6. **SEO 友好**：面包屑有助于搜索引擎理解网站结构
