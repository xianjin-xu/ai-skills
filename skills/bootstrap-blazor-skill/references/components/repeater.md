# Repeater

## 概述

Repeat 组件

> Repeater Component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/repeater](https://www.blazor.zone/repeater)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TItem>?` | `}` | 获得/设置 数据源 |
| `ShowLoading` | `bool` | `true` | 获得/设置 是否显示正在加载信息，默认为 true |
| `LoadingTemplate` | `RenderFragment?` | `}` | 获得/设置 正在加载模板 |
| `ShowEmpty` | `bool` | `true` | 获得/设置 是否显示无数据信息，默认为 true |
| `EmptyText` | `string?` | `}` | 获得/设置 无数据时提示信息，默认为 null |
| `EmptyTemplate` | `RenderFragment?` | `}` | 获得/设置 无数据时的模板 |
| `ContainerTemplate` | `RenderFragment<RenderFragment>?` | `}` | 获得/设置 容器模板 |
| `ItemTemplate` | `RenderFragment<TItem>?` | `}` | 获得/设置 项模板 |

## 代码示例

### 基本用法

```razor
<Repeater TItem="Foo" Items="Items">
        <ItemTemplate>
            <div class="d-flex">
                @context.Name
            </div>
        </ItemTemplate>
    </Repeater>
```

### 基本用法

```razor
<Repeater TItem="Foo" Items="Items">
        <ItemTemplate>
            <div class="d-flex">
                @context.Name
            </div>
        </ItemTemplate>
    </Repeater>
```

### 基本用法

```razor
<Repeater TItem="Foo" Items="EmptyItems" EmptyText="No Data">
    </Repeater>
```

### 基本用法

```razor
<Repeater TItem="Foo" Items="Items">
        <ContainerTemplate>
            <table class="table">
                <thead>
                    <tr><th>@FooLocalizer[nameof(Foo.Name)]</th><th>@FooLocalizer[nameof(Foo.Address)]</th><th></th></tr>
                </thead>
                <tbody>
                    @context
                </tbody>
            </table>
        </ContainerTemplate>
        <ItemTemplate>
            <tr>
                <td>@context.Name</td>
                <td>@context.Address</td>
                <td><Button Size="Size.ExtraSmall" Color="Color.Danger" Icon="fa-solid fa-xmark" Text="Delete" OnClick="() => OnDelete(context)"></Button></td>
            </tr>
        </ItemTemplate>
    </Repeater>
```
