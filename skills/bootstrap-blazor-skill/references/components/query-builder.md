# QueryBuilder

## 概述

QueryBuilder 组件

> QueryBuilder Component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/query-builder](https://www.blazor.zone/query-builder)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `FilterKeyValueAction?` | `}` | 获得/设置 过滤模型 <see cref="FilterKeyValueAction"/> 实例值 |
| `Logic` | `FilterLogic` | `}` | 获得/设置 逻辑运算符 |
| `ChildContent` | `RenderFragment<TModel>?` | `}` | 获得/设置 模板 |
| `ShowHeader` | `bool` | `true` | 获得/设置 是否显示 Header 区域，默认为 true |
| `HeaderTemplate` | `RenderFragment<FilterKeyValueAction>?` | `}` | 获得/设置 Header 模板，默认为 null |
| `PlusIcon` | `string?` | `}` | 获得/设置 增加过滤条件图标 |
| `RemoveIcon` | `string?` | `}` | 获得/设置 移除过滤条件图标 |
| `MinusIcon` | `string?` | `}` | 获得/设置 减少过滤条件图标 |
| `GroupText` | `string?` | `}` | 获得/设置 组合过滤条件文本 |
| `ItemText` | `string?` | `}` | 获得/设置 过滤条件文本 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<FilterKeyValueAction>` | 获得/设置 Filter 回调方法，支持双向绑定 |

## 代码示例

### 基本用法

```razor
<QueryBuilder TModel="Foo" @bind-Value="_filter1">
        <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>

        <QueryGroup Logic="@FilterLogic.Or">
            <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains"></QueryColumn>
            <QueryColumn @bind-Field="@context.Education" Operator="@FilterAction.Equal"></QueryColumn>
        </QueryGroup>

        <QueryColumn @bind-Field="@context.Complete" Operator="@FilterAction.Equal"></QueryColumn>
        <QueryColumn @bind-Field="@context.DateTime" Operator="@FilterAction.GreaterThanOrEqual"></QueryColumn>
    </QueryBuilder>
<QueryBuilder TModel="Foo" @bind-Value="_filter2" class="mt-3">
        <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>

        <QueryGroup Logic="@FilterLogic.Or">
            <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains"></QueryColumn>
            <QueryColumn @bind-Field="@context.Education" Operator="@FilterAction.Equal"></QueryColumn>

            <QueryGroup Logic="@FilterLogic.And">
                <QueryColumn @bind-Field="@context.DateTime" Operator="@FilterAction.GreaterThanOrEqual"></QueryColumn>
                <QueryColumn @bind-Field="@context.Complete" Operator="@FilterAction.Equal"></QueryColumn>
            </QueryGroup>
        </QueryGroup>
    </QueryBuilder>
```

### 基本用法

```razor
<QueryBuilder TModel="Foo" @bind-Value="_filter3" ShowHeader="false">
        <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>

        <QueryGroup Logic="@FilterLogic.Or">
            <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains"></QueryColumn>
            <QueryColumn @bind-Field="@context.Education" Operator="@FilterAction.Equal"></QueryColumn>

            <QueryGroup Logic="@FilterLogic.And">
                <QueryColumn @bind-Field="@context.DateTime" Operator="@FilterAction.GreaterThanOrEqual"></QueryColumn>
                <QueryColumn @bind-Field="@context.Complete" Operator="@FilterAction.Equal"></QueryColumn>
            </QueryGroup>
        </QueryGroup>
    </QueryBuilder>
```
