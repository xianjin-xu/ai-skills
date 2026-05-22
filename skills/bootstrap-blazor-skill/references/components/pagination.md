# Pagination

## 概述

Pagination 组件

> Pagination Component

**分类**: 导航
**在线演示**: [https://www.blazor.zone/pagination](https://www.blazor.zone/pagination)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Alignment` | `Alignment` | `Alignment.Right` | 获得/设置 对齐方式，默认为 Alignment.Right |
| `PrevPageIcon` | `string?` | `}` | 获得/设置 上一页图标 |
| `PrevEllipsisPageIcon` | `string?` | `}` | 获得/设置 上一页省略号图标 |
| `NextPageIcon` | `string?` | `}` | 获得/设置 下一页图标 |
| `NextEllipsisPageIcon` | `string?` | `}` | 获得/设置 下一页省略号图标 |
| `PageIndex` | `int` | `1` | 获得/设置 当前页码 |
| `PageCount` | `int` | `}` | 获得/设置 页码总数 |
| `MaxPageLinkCount` | `int` | `5` | 获得/设置 Page up/down 页码数量 默认 5 |
| `Task` | `Func<int,` | `}` | 点击页码时回调方法 参数是当前页码 |
| `PageInfoText` | `string?` | `}` | 获得/设置 显示分页信息文字 默认为 null |
| `GotoTemplate` | `RenderFragment?` | `}` | 获得/设置 Goto 导航模板 默认 null |
| `ShowGotoNavigator` | `bool` | `}` | 获得/设置 是否显示 Goto 跳转导航器 默认 false |
| `GotoNavigatorLabelText` | `string?` | `}` | 获得/设置 Goto 导航标签显示文字 默认 导航到/Goto |
| `ShowPageInfo` | `bool` | `true` | 获得/设置 是否显示 分页信息 默认 true |
| `PageInfoTemplate` | `RenderFragment?` | `}` | 获得/设置 分页信息模板 默认 null |

## 代码示例

### 基本用法

```razor
<Pagination PageCount="@PageCount" ShowPageInfo="true" ShowGotoNavigator="true">
        <PageInfoTemplate>
            <div class="page-info me-2">@PageInfoText</div>
            <Select @bind-Value="PageItems" Items="PageItemsSource" />
        </PageInfoTemplate>
    </Pagination>
```
