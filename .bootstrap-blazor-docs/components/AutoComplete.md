# AutoComplete (自动完成)

## 概述

`AutoComplete` 是一个自动完成组件，提供输入建议功能，支持自定义过滤、模糊搜索、忽略大小写等配置。

> AutoComplete component

**分类**: 表单输入  
**在线演示**: [https://www.blazor.zone/auto-complete](https://www.blazor.zone/auto-complete)

## 使用场景

### 1. 基本用法

```razor
<AutoComplete @bind-Value="SearchText" Items="SuggestItems" />
```

```csharp
@code {
    string SearchText { get; set; } = "";
    List<string> SuggestItems = new List<string> { "Apple", "Banana", "Cherry" };
}
```

### 2. 自定义过滤

```razor
<AutoComplete @bind-Value="SearchText" OnCustomFilter="CustomFilter" />
```

```csharp
@code {
    async Task<IEnumerable<string>> CustomFilter(string text)
    {
        // 自定义过滤逻辑
        return await Task.FromResult(SuggestItems.Where(i => i.Contains(text)));
    }
}
```

### 3. 模糊搜索

```razor
<AutoComplete @bind-Value="SearchText" Items="SuggestItems" IsLikeMatch="true" />
```

### 4. 忽略大小写

```razor
<AutoComplete @bind-Value="SearchText" Items="SuggestItems" IgnoreCase="true" />
```

### 5. 显示数量限制

```razor
<AutoComplete @bind-Value="SearchText" Items="SuggestItems" DisplayCount="5" />
```

### 6. 自定义模板

```razor
<AutoComplete @bind-Value="SearchText" Items="SuggestItems">
    <ItemTemplate>
        <div class="d-flex align-items-center">
            <i class="fa-solid fa-bell"></i>
            <span class="flex-fill ms-2">@context</span>
        </div>
    </ItemTemplate>
</AutoComplete>
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置组件值 |
| `Items` | `IEnumerable<string>?` | `null` | 获得/设置通过输入字符串获得的匹配数据集合 |
| `OnCustomFilter` | `Func<string, Task<IEnumerable<string>>>?` | `null` | 获得/设置自定义集合过滤规则 |
| `Icon` | `string?` | `null` | 获得/设置图标 |
| `LoadingIcon` | `string?` | `null` | 获得/设置加载图标 |
| `DisplayCount` | `int?` | `null` | 获得/设置匹配数据时显示的数量 |
| `IsLikeMatch` | `bool` | `false` | 获得/设置是否开启模糊搜索 |
| `IgnoreCase` | `bool` | `true` | 获得/设置匹配时是否忽略大小写 |
| `ShowDropdownListOnFocus` | `bool` | `true` | 获得/设置获得焦点时是否展开下拉候选菜单 |
| `ShowNoDataTip` | `bool` | `true` | 获得/设置是否显示无匹配数据选项 |
| `SkipMatch` | `bool` | `false` | 获得/设置是否不进行匹配操作 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `ValueChanged` | 值改变时触发 |
| `OnSelectedItemChanged` | 选中项改变时触发 |
| `OnBlurAsync` | 失去焦点时触发 |

## 最佳实践

1. **数据绑定**: 使用 `Items` 参数提供建议数据集合
2. **自定义过滤**: 使用 `OnCustomFilter` 回调实现自定义过滤逻辑
3. **模糊搜索**: 设置 `IsLikeMatch="true"` 启用模糊搜索
4. **忽略大小写**: 设置 `IgnoreCase="true"` 忽略大小写匹配
5. **显示数量**: 使用 `DisplayCount` 限制显示的建议数量
6. **自定义模板**: 使用 `ItemTemplate` 自定义建议项的显示方式

## 常见问题

### Q: 如何绑定输入值？
A: 使用 `Value` 参数绑定到字符串变量，支持双向绑定（`@bind-Value`）。

### Q: 如何提供建议数据？
A: 使用 `Items` 参数提供字符串集合，或使用 `OnCustomFilter` 回调动态过滤数据。

### Q: 如何启用模糊搜索？
A: 设置 `IsLikeMatch="true"` 启用模糊搜索模式。

### Q: 如何自定义建议项显示？
A: 使用 `ItemTemplate` 参数自定义建议项的显示模板。

### Q: 如何限制显示数量？
A: 使用 `DisplayCount` 参数设置最多显示的建议数量。
