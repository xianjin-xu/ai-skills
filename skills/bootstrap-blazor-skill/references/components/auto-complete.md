# AutoComplete

## 概述

AutoComplete 组件

> AutoComplete component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/auto-complete](https://www.blazor.zone/auto-complete)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<string>?` | `}` | 获得/设置 通过输入字符串获得的匹配数据集合 |
| `Task` | `Func<string,` | `}` | 获得/设置 自定义集合过滤规则 默认为 null |
| `Icon` | `string?` | `}` | 获得/设置 图标 |
| `LoadingIcon` | `string?` | `}` | 获得/设置 加载图标 |
| `DisplayCount` | `int?` | `}` | 获得/设置 匹配数据时显示的数量 |
| `IsLikeMatch` | `bool` | `}` | 获得/设置 是否开启模糊搜索 默认为 false |
| `IgnoreCase` | `bool` | `true` | 获得/设置 匹配时是否忽略大小写 默认为 true |
| `ShowDropdownListOnFocus` | `bool` | `true` | 获得/设置 获得焦点时是否展开下拉候选菜单 默认为 true |
| `ShowNoDataTip` | `bool` | `true` | 获得/设置 是否显示无匹配数据选项 默认为 true |
| `SkipMatch` | `bool` | `}` | 获得/设置 是否不进行匹配操作 默认为 false |

## 代码示例

### 基本用法

```razor
<AutoComplete Value="@_value" Items="@StaticItems" IsSelectAllTextOnFocus="true" IsClearable></AutoComplete>
```

### 基本用法

```razor
<AutoComplete Items="@StaticItems" OnSelectedItemChanged="OnSelectedItemChanged"></AutoComplete>
```

### 基本用法

```razor
<AutoComplete Items="@StaticItems">
        <ItemTemplate>
            <div class="d-flex align-items-center">
                <i class="fa-solid fa-bell"></i>
                <span class="flex-fill ms-2">@context</span>
            </div>
        </ItemTemplate>
    </AutoComplete>
```

### 基本用法

```razor
<AutoComplete Items="@StaticItems" OnSelectedItemChanged="GroupOnSelectedItemChanged"></AutoComplete>
<AutoComplete Items="@StaticItems" OnSelectedItemChanged="GroupOnSelectedItemChanged"></AutoComplete>
<AutoComplete Items="@StaticItems" OnSelectedItemChanged="GroupOnSelectedItemChanged"></AutoComplete>
```

### 基本用法

```razor
<AutoComplete Items="@StaticItems" IsPopover="true"></AutoComplete>
```
