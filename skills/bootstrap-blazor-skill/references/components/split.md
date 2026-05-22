# Split

## 概述

Split 组件

> Split component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/split](https://www.blazor.zone/split)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsCollapsible` | `bool` | `}` | 获取 是否开启折叠功能 默认 false |
| `ShowBarHandle` | `bool` | `true` | 获取 是否显示拖动条 默认 true |
| `IsKeepOriginalSize` | `bool` | `true` | 获得/设置 开启 <see cref="IsCollapsible"/> 后，恢复时是否保持原始大小 默认 true |
| `IsVertical` | `bool` | `}` | 获得/设置 是否垂直分割 |
| `Basis` | `string` | `"50%"` | 获得/设置 第一个窗格初始化位置占比 默认为 50% |
| `FirstPaneTemplate` | `RenderFragment?` | `}` | 获得/设置 第一个窗格模板 |
| `FirstPaneMinimumSize` | `string?` | `}` | 获得/设置 第一个窗格最小宽度 支持任意单位如 10px 20% 5em 1rem 未提供单位时默认为 px |
| `SecondPaneTemplate` | `RenderFragment?` | `}` | 获得/设置 第二个窗格模板 |
| `SecondPaneMinimumSize` | `string?` | `}` | 获得/设置 第二个窗格最小宽度 |
| `Task` | `Func<bool,` | `}` | 获得/设置 窗格折叠时回调方法 参数 bool 值为 true 是表示已折叠 值为 false 表示第二个已折叠 |

## 代码示例

### 基本用法

```razor
<Split ShowBarHandle="_showBarHandle" OnResizedAsync="OnResizedAsync" IsCollapsible="_isCollapsible">
            <FirstPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel1"]</div>
            </FirstPaneTemplate>
            <SecondPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel2"]</div>
            </SecondPaneTemplate>
        </Split>
```

### 基本用法

```razor
<Split Basis="40%">
            <FirstPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel1"]</div>
            </FirstPaneTemplate>
            <SecondPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel2"]</div>
            </SecondPaneTemplate>
        </Split>
```

### 基本用法

```razor
<Split IsVertical="true">
            <FirstPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel3"]</div>
            </FirstPaneTemplate>
            <SecondPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel4"]</div>
            </SecondPaneTemplate>
        </Split>
```

### 基本用法

```razor
<Split>
            <FirstPaneTemplate>
                <Split IsVertical="true">
                    <FirstPaneTemplate>
                        <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel5"]</div>
                    </FirstPaneTemplate>
                    <SecondPaneTemplate>
                        <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel6"]</div>
                    </SecondPaneTemplate>
                </Split>
```

### 基本用法

```razor
<Split IsCollapsible="true">
            <FirstPaneTemplate>
                <Split IsVertical="true" IsCollapsible="true">
                    <FirstPaneTemplate>
                        <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel8"]</div>
                    </FirstPaneTemplate>
                    <SecondPaneTemplate>
                        <div class="d-flex justify-content-center align-items-center h-100">@Localizer["SplitsPanel9"]</div>
                    </SecondPaneTemplate>
                </Split>
```
