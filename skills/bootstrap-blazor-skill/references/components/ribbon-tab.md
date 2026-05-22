# RibbonTab

## 概述

RibbonTab 组件

> RibbonTab Component

**分类**: 导航
**在线演示**: [https://www.blazor.zone/ribbon-tab](https://www.blazor.zone/ribbon-tab)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ShowFloatButton` | `bool` | `}` | 获得/设置 是否显示悬浮小箭头，默认为 false |
| `Task` | `Func<bool,` | `}` | 获得/设置 组件悬浮状态改变时的回调方法，默认为 null |
| `RibbonArrowUpIcon` | `string?` | `}` | 获得/设置 选项卡向上箭头图标 |
| `RibbonArrowDownIcon` | `string?` | `}` | 获得/设置 选项卡向下箭头图标 |
| `RibbonArrowPinIcon` | `string?` | `}` | 获得/设置 选项卡可固定图标 |
| `IsSupportAnchor` | `bool` | `}` | 获得/设置 是否开启 Url 锚点 |
| `string` | `Func<string,` | `}` | 获得/设置 编码锚点回调方法。第一参数是当前地址 Url，第二个参数是当前选项 Text 属性，返回值为地址全路径 |
| `Items` | `IEnumerable<RibbonTabItem>?` | `}` | 获得/设置 数据源 |
| `RightButtonsTemplate` | `RenderFragment?` | `}` | 获得/设置 右侧按钮模板 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 内容模板 |
| `IsBorder` | `bool` | `true` | 获得/设置 是否为带边框卡片样式，默认为 true |

## 代码示例

### 基本用法

```razor
<RibbonTab Items="@FloatItems" ShowFloatButton="true" OnFloatChanged="OnFloatChanged">
            @Localizer["RibbonTabsFloatContent"]
        </RibbonTab>
```

### 基本用法

```razor
<RibbonTab Items="@RightItems" ShowFloatButton="true">
        <RightButtonsTemplate>
            <div class="ribbon-button">
                <i class="fa-regular fa-circle-question"></i>
                <span>@Localizer["RibbonTabsRightButtonsTemplateContent"]</span>
            </div>
        </RightButtonsTemplate>
    </RibbonTab>
```

### 基本用法

```razor
<RibbonTab Items="@HeaderItems" OnMenuClickAsync="@OnMenuClickAsync">
        <div class="@FileClassString">@Localizer["RibbonTabsItemsText1"]</div>
        <div class="@EditClassString">@Localizer["RibbonTabsItemsText2"]</div>
    </RibbonTab>
```

### 基本用法

```razor
<RibbonTab Items="@AnchorItems" IsSupportAnchor="true" EncodeAnchorCallback="EncodeAnchorCallback" DecodeAnchorCallback="DecodeAnchorCallback"></RibbonTab>
```
