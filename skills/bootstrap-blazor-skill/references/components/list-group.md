# ListGroup

## 概述

ListGroup 组件

> ListGroup Component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/list-group](https://www.blazor.zone/list-group)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `List<TItem>?` | `}` | 获得/设置 数据源集合 |
| `HeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 Header 模板 默认 null |
| `HeaderText` | `string?` | `}` | 获得/设置 Header 文字 默认 null |
| `ItemTemplate` | `RenderFragment<TItem>?` | `}` | 获得/设置 Item 模板 默认 null |
| `Task` | `Func<TItem,` | `}` | 获得/设置 点击 List 项目回调方法 |
| `string` | `Func<TItem,` | `}` | 获得/设置 获得条目显示文本内容回调方法 |

## 代码示例

### 基本用法

```razor
<ListGroup TItem="Foo" Items="Items" Value="Value" GetItemDisplayText="@GetItemDisplayText"></ListGroup>
```

### 基本用法

```razor
<ListGroup TItem="Foo" Items="Items" Value="Value" GetItemDisplayText="@GetItemDisplayText" HeaderText="@Localizer["HeaderText"]">
        </ListGroup>
```

### 基本用法

```razor
<ListGroup Items="Items" @bind-Value="Value" GetItemDisplayText="@GetItemDisplayText">
            <HeaderTemplate>
                <div class="list-group-header">
                    <div class="flex-fill">列表框</div>
                    <button class="btn btn-primary btn-xs">按钮</button>
                </div>
            </HeaderTemplate>
        </ListGroup>
```
