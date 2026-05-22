# AutoFill

## 概述

AutoFill 组件

> AutoFill component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/auto-fill](https://www.blazor.zone/auto-fill)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TValue>?` | `}` | 获得/设置 组件数据集合 |
| `DisplayCount` | `int?` | `}` | 获得/设置 匹配数据时显示的数量 默认为 null |
| `IsLikeMatch` | `bool` | `}` | 获得/设置 是否开启模糊搜索 默认为 false |
| `IgnoreCase` | `bool` | `true` | 获得/设置 匹配时是否忽略大小写 默认为 true |
| `ShowDropdownListOnFocus` | `bool` | `true` | 获得/设置 获得焦点时是否展开下拉候选菜单 默认为 true |
| `string` | `Func<TValue?,` | `}` | 获得/设置 获取显示文本方法 默认为使用 ToString 方法 |
| `Icon` | `string?` | `}` | 获得/设置 图标 |
| `LoadingIcon` | `string?` | `}` | 获得/设置 加载图标 |
| `Task` | `Func<string,` | `}` | 获得/设置 自定义集合过滤规则 |
| `ShowNoDataTip` | `bool` | `true` | 获得/设置 是否显示无匹配数据选项 默认为 true |
| `Template` | `RenderFragment<TValue>?` | `> ItemTemplate` | 获得/设置 候选项模板 默认为 null |
| `IsVirtualize` | `bool` | `}` | 获得/设置 是否开启虚拟滚动 默认为 false |
| `RowHeight` | `float` | `50f` | - |
| `OverscanCount` | `int` | `3` | - |
| `OnClearAsync` | `Func<Task>?` | `}` | 获得/设置 点击清除按钮回调方法 默认为 null |
| `IsAutoClearWhenInvalid` | `bool` | `}` | 获得/设置 输入框内容无效时是否自动清空内容 默认 false |

## 代码示例

### 基本用法

```razor
<AutoFill @bind-Value="Model1" Items="Items1" IsAutoClearWhenInvalid="true"
              IsLikeMatch="true" OnGetDisplayText="OnGetDisplayText" IsSelectAllTextOnFocus="true">
        <ItemTemplate>
            <div class="d-flex">
                <div>
                    <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" class="bb-avatar" />
                </div>
                <div class="ps-2">
                    <div>@context.Name</div>
                    <div class="bb-sub">@Foo.GetTitle(context.Id)</div>
                </div>
            </div>
        </ItemTemplate>
    </AutoFill>
```

### 基本用法

```razor
<AutoFill @bind-Value="Model2" Items="Items2" OnCustomFilter="OnCustomFilter"
              OnGetDisplayText="OnGetDisplayText">
        <ItemTemplate>
            <div class="d-flex">
                <div>
                    <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" class="bb-avatar" />
                </div>
                <div class="ps-2">
                    <div>@context.Name</div>
                    <div class="bb-sub">@Foo.GetTitle(context.Id)</div>
                </div>
            </div>
        </ItemTemplate>
    </AutoFill>
```

### 基本用法

```razor
<AutoFill @bind-Value="Model3" Items="Items3" ShowDropdownListOnFocus="false" OnGetDisplayText="OnGetDisplayText">
        <ItemTemplate>
            <div class="d-flex">
                <div>
                    <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" class="bb-avatar" />
                </div>
                <div class="ps-2">
                    <div>@context.Name</div>
                    <div class="bb-sub">@Foo.GetTitle(context.Id)</div>
                </div>
            </div>
        </ItemTemplate>
    </AutoFill>
```

### 基本用法

```razor
<AutoFill @bind-Value="Model4" OnQueryAsync="OnQueryAsync" OnGetDisplayText="OnGetDisplayText"
                      IsSelectAllTextOnFocus="true" IsVirtualize="true" RowHeight="58f" IsClearable="_isClearable">
                <ItemTemplate>
                    <div class="d-flex">
                        <div>
                            <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" class="bb-avatar" />
                        </div>
                        <div class="ps-2">
                            <div>@context.Name</div>
                            <div class="bb-sub">@Foo.GetTitle(context.Id)</div>
                        </div>
                    </div>
                </ItemTemplate>
            </AutoFill>
<AutoFill @bind-Value="Model5" Items="Items5" OnGetDisplayText="OnGetDisplayText"
                      IsSelectAllTextOnFocus="true" OnCustomFilter="OnCustomVirtulizeFilter"
                      IsVirtualize="true" RowHeight="58f" IsClearable="_isClearable">
                <ItemTemplate>
                    <div class="d-flex">
                        <div>
                            <img src="@WebsiteOption.Value.GetAvatarUrl(context.Id)" class="bb-avatar" />
                        </div>
                        <div class="ps-2">
                            <div>@context.Name</div>
                            <div class="bb-sub">@Foo.GetTitle(context.Id)</div>
                        </div>
                    </div>
                </ItemTemplate>
            </AutoFill>
```
