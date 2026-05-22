# ListView

## 概述

ListView 组件基类

> ListView Component Base

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/list-view](https://www.blazor.zone/list-view)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `HeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 CardHeader |
| `string` | `Func<object?,` | `}` | 获得/设置 获得 <see cref="CollapseItem.Text"/> 值 默认 null 使用分组 Key.ToString() 方法获取 |
| `TItem` | `Func<IEnumerable<IGrouping<object?,` | `}` | 获得/设置 组排序回调方法 默认 null 使用内置 |
| `BodyTemplate` | `RenderFragment<TItem>?` | `}` | 获得/设置 BodyTemplate |
| `FooterTemplate` | `RenderFragment?` | `}` | 获得/设置 FooterTemplate 默认 null 未设置 设置值后 <see cref="IsPagination"/> 参数不起作用，请自行实现分页功能 |
| `Items` | `IEnumerable<TItem>?` | `}` | 获得/设置 数据源 |
| `Pageable` | `bool` | `> IsPagination` | 获得/设置 是否分页 默认为 false 不分页 设置 <see cref="FooterTemplate"/> 时分页功能自动被禁用 |
| `IsPagination` | `bool` | `}` | 获得/设置 是否分页 默认为 false 不分页 设置 <see cref="FooterTemplate"/> 时分页功能自动被禁用 |
| `object` | `Func<TItem,` | `}` | 获得/设置 分组 Lambda 表达式 默认 null |
| `Collapsible` | `bool` | `}` | 获得/设置 是否可折叠 默认 false 需要开启分组设置 <see cref="GroupName"/> |
| `IsAccordion` | `bool` | `}` | 获得/设置 是否手风琴效果 默认 false 需要开启可收缩设置 <see cref="Collapsible"/> |
| `Task` | `Func<CollapseItem,` | `}` | 获得/设置 CollapseItem 展开收缩时回调方法 默认 false 需要开启可收缩设置 <see cref="Collapsible"/> |
| `bool` | `Func<object?,` | `}` | 获得/设置 首次渲染是否收缩回调委托 |
| `IsVertical` | `bool` | `}` | 获得/设置 是否为竖向排列 默认为 false |
| `PageItems` | `int` | `20` | 获得/设置 每页数据数量 默认 20 |
| `Height` | `string?` | `}` | 获得/设置 组件高度 默认 null 未设置高度 如：50% 100px 10rem 10vh 等 |
| `EmptyTemplate` | `RenderFragment?` | `}` | 获得/设置 无数据时模板 默认 null 未设置 |
| `EmptyText` | `string?` | `}` | 获得/设置 无数据时显示文字 默认 null 未设置使用资源文件设置文字 |

## 代码示例

### 基本用法

```razor
<ListView TItem="Product" Items="@Products" OnListViewItemClick="OnListViewItemClick" Height="620px">
        <HeaderTemplate>
            <div>@Localizer["ProductListText"]</div>
        </HeaderTemplate>
        <BodyTemplate>
            <Card>
                <BodyTemplate>
                    <img src="@context.ImageUrl" />
                    <div class="lv-demo-desc">@context.Description</div>
                </BodyTemplate>
            </Card>
        </BodyTemplate>
        <FooterTemplate>
            <div class="text-end">
                Copyright Bootstrap Blazor
            </div>
        </FooterTemplate>
    </ListView>
```

### 基本用法

```razor
<ListView TItem="Product" IsPagination="true" PageItems="4" OnQueryAsync="@OnQueryAsync" Height="620px">
        <HeaderTemplate>
            <div>@Localizer["ProductListText"]</div>
        </HeaderTemplate>
        <BodyTemplate>
            <Card>
                <BodyTemplate>
                    <img src="@context.ImageUrl" />
                    <div class="lv-demo-desc">@context.Description</div>
                </BodyTemplate>
            </Card>
        </BodyTemplate>
    </ListView>
```

### 基本用法

```razor
<ListView TItem="Product" GroupName="p => p.Category" GroupOrderCallback="GroupOrderCallback" GroupItemOrderCallback="GroupItemOrderCallback" OnQueryAsync="@OnQueryAsync" Height="620px">
        <HeaderTemplate>
            <div>@Localizer["ProductListText"]</div>
        </HeaderTemplate>
        <BodyTemplate>
            <Card>
                <BodyTemplate>
                    <img src="@context.ImageUrl" />
                    <div class="lv-demo-desc">@context.Description</div>
                </BodyTemplate>
            </Card>
        </BodyTemplate>
    </ListView>
```

### 基本用法

```razor
<ListView TItem="Product" GroupName="p => p.Category" OnQueryAsync="@OnQueryAsync" Collapsible="true" CollapsedGroupCallback="CollapsedGroupCallback" Height="620px">
        <HeaderTemplate>
            <div>@Localizer["ProductListText"]</div>
        </HeaderTemplate>
        <BodyTemplate>
            <Card>
                <BodyTemplate>
                    <img src="@context.ImageUrl" />
                    <div class="lv-demo-desc">@context.Description</div>
                </BodyTemplate>
            </Card>
        </BodyTemplate>
    </ListView>
```

### 基本用法

```razor
<ListView TItem="Product" GroupName="p => p.Category" OnQueryAsync="@OnQueryAsync" Collapsible="true" IsAccordion="true" Height="620px">
        <HeaderTemplate>
            <div>@Localizer["ProductListText"]</div>
        </HeaderTemplate>
        <BodyTemplate>
            <Card>
                <BodyTemplate>
                    <img src="@context.ImageUrl" />
                    <div class="lv-demo-desc">@context.Description</div>
                </BodyTemplate>
            </Card>
        </BodyTemplate>
    </ListView>
```
