# Search

## 概述

搜索组件

> Search component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/search](https://www.blazor.zone/search)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IconTemplate` | `RenderFragment<SearchContext<TValue>>?` | `}` | 获得/设置 图标模板，默认为 null |
| `ShowClearButton` | `bool` | `}` | 获得/设置 是否显示清空按钮，默认为 false |
| `ClearButtonIcon` | `string?` | `}` | 获得/设置 清空按钮的图标，默认为 null |
| `ClearButtonText` | `string?` | `}` | 获得/设置 清空按钮的文本，默认为 null |
| `ClearButtonColor` | `Color` | `Color.Primary` | 获得/设置 清空按钮的颜色，默认为 <see cref="Color.Primary"/> |
| `ShowSearchButton` | `bool` | `true` | 获得/设置 是否显示搜索按钮，默认为 true |
| `SearchButtonColor` | `Color` | `Color.Primary` | 获得/设置 搜索按钮的颜色，默认为 <see cref="Color.Primary"/> |
| `SearchButtonIcon` | `string?` | `}` | 获得/设置 搜索按钮的图标，默认为 null |
| `SearchButtonLoadingIcon` | `string?` | `}` | 获得/设置 搜索按钮的加载图标，默认为 null |
| `SearchButtonText` | `string?` | `}` | 获得/设置 搜索按钮的文本，默认为 null |
| `ButtonTemplate` | `RenderFragment<SearchContext<TValue>>?` | `}` | 获得/设置 按钮模板，默认为 null |
| `PrefixButtonTemplate` | `RenderFragment<SearchContext<TValue>>?` | `}` | 获得/设置 前缀按钮模板，默认为 null |
| `ShowPrefixIcon` | `bool` | `}` | 获得/设置 是否显示前缀图标，默认为 false |
| `PrefixIcon` | `string?` | `}` | 获得/设置 前缀图标，默认为 null |
| `PrefixIconTemplate` | `RenderFragment<SearchContext<TValue>>?` | `}` | 获得/设置 前缀图标模板，默认为 null |
| `IsAutoClearAfterSearch` | `bool` | `}` | 获得/设置 搜索后是否自动清空搜索框（已弃用） |
| `IsTriggerSearchByInput` | `bool` | `true` | 获得/设置 搜索是否由输入触发，默认为 true。如果为 false，必须点击搜索按钮来触发 |
| `Task` | `Func<string?,` | `}` | 获得/设置 点击搜索按钮时的回调委托 |
| `string` | `Func<TValue,` | `}` | 获得/设置 获取显示文本的回调方法，默认为 null，使用 ToString() 方法 |
| `OnClear` | `Func<Task>?` | `}` | 获得/设置 点击清空按钮时的事件回调，默认为 null（已弃用，已并入 OnSearch 方法中） |

## 代码示例

### 基本用法

```razor
<Search IsAutoFocus="true"
            PlaceHolder="@Localizer["SearchesPlaceHolder"]"
            OnSearch="@OnSearch"
            IsSelectAllTextOnFocus="true"></Search>
```

### 基本用法

```razor
<Search PlaceHolder="@Localizer["SearchesPlaceHolder"]"
            ShowClearButton="true"
            OnSearch="@OnDisplaySearch"></Search>
```

### 基本用法

```razor
<Search PlaceHolder="@Localizer["SearchesPlaceHolder"]"
            OnGetDisplayText="OnGetDisplayText"
            OnSearch="@OnSearchFoo">
        <ItemTemplate>
            <div class="search-result">
                <div class="search-result-avatar">
                    <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" alt="avatar" />
                </div>
                <div class="search-result-main">
                    <div class="search-result-name">@context.Name</div>
                    <div class="search-result-address">@context.Address</div>
                </div>
                <div class="search-result-circle">
                    <Circle Value="@context.Count" Color="Color.Info" StrokeWidth="4" Width="60" />
                </div>
            </div>
        </ItemTemplate>
    </Search>
```

### 基本用法

```razor
<Search PlaceHolder="@Localizer["SearchesPlaceHolder"]"
            IsTriggerSearchByInput="false"
            OnSearch="@OnKeyboardSearch"></Search>
```

### 基本用法

```razor
<Search @bind-Value="Model.Name" OnSearch="@OnModelSearch"></Search>
```
