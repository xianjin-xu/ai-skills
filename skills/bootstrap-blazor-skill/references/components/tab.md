# Tab

## 概述

Tab 组件

> Tab component

**分类**: 导航
**在线演示**: [https://www.blazor.zone/tab](https://www.blazor.zone/tab)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsCard` | `bool` | `}` | 获得/设置 是否为卡片样式，默认为 false |
| `IsBorderCard` | `bool` | `}` | 获得/设置 是否为边框卡片样式，默认为 false |
| `IsOnlyRenderActiveTab` | `bool` | `}` | 获得/设置 是否仅渲染活动标签，默认为 false |
| `IsLazyLoadTabItem` | `bool` | `}` | 获得/设置 是否懒加载 TabItem，首次不渲染，默认为 false |
| `string` | `Func<string?,` | `}` | 获得/设置 Tab 标签头文本本地化回调方法 |
| `Height` | `int` | `}` | 获得/设置 组件高度，默认值为 0 自动高度 |
| `Placement` | `Placement` | `Placement.Top` | 获得/设置 组件标签显示位置，默认显示在 Top |
| `ShowClose` | `bool` | `}` | 获得/设置 是否显示关闭按钮，默认为 false |
| `ShowFullScreen` | `bool` | `}` | 获得/设置 是否显示全屏按钮，默认为 false |
| `ShowContextMenuFullScreen` | `bool` | `true` | 获得/设置 是否在右键菜单上显示全屏按钮，默认为 true |
| `Task` | `Func<TabItem,` | `}` | - |
| `ShowExtendButtons` | `bool` | `}` | 获得/设置 是否显示扩展功能按钮，默认为 false |
| `ShowNavigatorButtons` | `bool` | `true` | 获得/设置 是否显示前后导航按钮，默认为 true |
| `IsLoopSwitchTabItem` | `bool` | `true` | 获得/设置 是否自动重置标签项索引，默认为 true |
| `ShowActiveBar` | `bool` | `true` | 获得/设置 是否显示活动标签栏，默认为 true |
| `ClickTabToNavigation` | `bool` | `}` | 获得/设置 点击 TabItem 时是否自动导航，默认为 false |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 TabItems 模板 |
| `NotAuthorized` | `RenderFragment?` | `}` | 获得/设置 未授权模板，默认 null (NET6.0/7.0 有效) |
| `NotFound` | `RenderFragment?` | `}` | 获得/设置 未找到模板，默认 null (NET6.0/7.0 有效) |
| `NotFoundTabText` | `string?` | `}` | 获得/设置 未找到标签文本，默认 null (NET6.0/7.0 有效) |
| `Body` | `RenderFragment?` | `}` | 获得/设置 TabItems 主体模板 |
| `AdditionalAssemblies` | `IEnumerable<Assembly>?` | `}` | 获得/设置 应搜索的其他程序集的集合 |
| `ExcludeUrls` | `IEnumerable<string>?` | `}` | 获得/设置 排除地址，支持通配符 |
| `DefaultUrl` | `string?` | `}` | 获得/设置 默认标签页，关闭所有标签页时自动打开此地址，默认 null |
| `CloseCurrentTabText` | `string?` | `}` | 获得/设置 关闭当前 TabItem 菜单文本 |
| `CloseAllTabsText` | `string?` | `}` | 获得/设置 关闭所有 TabItem 菜单文本 |
| `CloseOtherTabsText` | `string?` | `}` | 获得/设置 关闭其他 TabItem 菜单文本 |
| `ButtonTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 按钮模板，默认 null |
| `ToolbarTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 工具栏按钮的模板，默认为 null |
| `BeforeNavigatorTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 导航器前置模板，默认 null (在向前移动标签页按钮前) |
| `AfterNavigatorTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 导航器后置模板，默认 null (在向后移动标签页按钮前) |
| `PreviousIcon` | `string?` | `}` | 获得/设置 上一个标签图标 |
| `NextIcon` | `string?` | `}` | 获得/设置 下一个标签图标 |
| `DropdownIcon` | `string?` | `}` | 获得/设置 下拉菜单图标 |
| `CloseIcon` | `string?` | `}` | 获得/设置 关闭标签图标 |
| `Menus` | `IEnumerable<MenuItem>?` | `}` | - |
| `AllowDrag` | `bool` | `}` | 获得/设置 是否允许拖放标题栏更改栏位顺序，默认为 false |
| `TabStyle` | `TabStyle` | `}` | 获得/设置 标签页样式，默认为 TabStyle.Default |
| `ShowToolbar` | `bool` | `}` | 获得/设置 是否显示工具栏，默认为 false |
| `ShowFullscreenToolbarButton` | `bool` | `true` | 获得/设置 是否显示全屏按钮，默认为 true |
| `FullscreenToolbarButtonIcon` | `string?` | `}` | 获得/设置 全屏工具栏按钮图标字符串，默认为 null |
| `FullscreenToolbarTooltipText` | `string?` | `}` | 获得/设置 全屏工具栏按钮提示字符串，默认为 null |
| `ShowRefreshToolbarButton` | `bool` | `true` | 获得/设置 是否显示刷新按钮，默认为 true |
| `RefreshToolbarButtonIcon` | `string?` | `}` | 获得/设置 刷新工具栏按钮图标字符串，默认为 null |
| `RefreshToolbarTooltipText` | `string?` | `}` | 获得/设置 刷新工具栏按钮提示字符串，默认为 null |
| `OnToolbarRefreshCallback` | `Func<Task>?` | `}` | 获得/设置 刷新工具栏按钮单击事件回调，默认为 null |
| `PrevTabNavLinkTooltipText` | `string?` | `}` | 获得/设置 上一个标签导航链接提示文本，默认为 null |
| `NextTabNavLinkTooltipText` | `string?` | `}` | 获得/设置 下一个标签导航链接提示文本，默认为 null |
| `CloseTabNavLinkTooltipText` | `string?` | `}` | 获得/设置 关闭标签导航链接提示文本，默认为 null |
| `ShowContextMenu` | `bool` | `}` | 获得/设置 是否启用标签页右键菜单，默认为 false |
| `BeforeContextMenuTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 右键菜单前置模板，默认为 null |
| `ContextMenuTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 右键菜单模板，默认为 null |
| `ContextMenuRefreshIcon` | `string?` | `}` | 获得/设置 标签项右键菜单刷新按钮的图标，默认为 null |
| `ContextMenuCloseIcon` | `string?` | `}` | 获得/设置 标签项右键菜单关闭按钮的图标，默认为 null |
| `ContextMenuCloseOtherIcon` | `string?` | `}` | 获得/设置 标签项右键菜单关闭其他按钮的图标，默认为 null |
| `ContextMenuCloseAllIcon` | `string?` | `}` | 获得/设置 标签项右键菜单关闭全部按钮的图标，默认为 null |
| `ContextMenuFullScreenIcon` | `string?` | `}` | 获得/设置 标签项右键菜单全屏按钮的图标，默认为 null |
| `TabHeader` | `ITabHeader?` | `}` | 获得/设置 ITabHeader 实例，默认为 null |
| `EnableErrorLogger` | `bool?` | `}` | 获得/设置 是否开启全局异常捕获，默认 null 读取配置文件 BootstrapBlazorOptions.EnableErrorLogger 值 |
| `EnableErrorLoggerILogger` | `bool?` | `}` | 获得/设置 是否记录异常到 ILogger，默认 null 使用 BootstrapBlazorOptions.EnableErrorLoggerILogger 设置值 |
| `ShowErrorLoggerToast` | `bool?` | `}` | 获得/设置 是否显示 Error 提示弹窗，默认 null 使用 BootstrapBlazorOptions.ShowErrorLoggerToast 设置值 |
| `ErrorLoggerToastTitle` | `string?` | `}` | 获得/设置 错误日志 Toast 弹窗标题，默认 null |
| `Exception` | `Func<ILogger,` | `}` | 获得/设置 自定义错误处理回调方法 |

## 代码示例

### 基本用法

```razor
<Tab>
        <TabItem Text="@Localizer["TabItem1Text"]">
            <div>@Localizer["TabItem1Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem2Text"]">
            <div>@Localizer["TabItem2Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem3Text"]">
            <div>@Localizer["TabItem3Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem4Text"]">
            <div>@Localizer["TabItem4Content"]</div>
        </TabItem>
    </Tab>
```

### 基本用法

```razor
<Tab IsCard="true">
        <TabItem Text="@Localizer["TabItem1Text"]">
            <div>@Localizer["TabItem1Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem2Text"]">
            <div>@Localizer["TabItem2Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem3Text"]">
            <div>@Localizer["TabItem3Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem4Text"]">
            <div>@Localizer["TabItem4Content"]</div>
        </TabItem>
    </Tab>
```

### 基本用法

```razor
<Tab IsBorderCard="true">
        <TabItem Text="@Localizer["TabItem1Text"]">
            <div>@Localizer["TabItem1Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem2Text"]">
            <div>@Localizer["TabItem2Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem3Text"]">
            <div>@Localizer["TabItem3Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem4Text"]">
            <div>@Localizer["TabItem4Content"]</div>
        </TabItem>
    </Tab>
```

### 基本用法

```razor
<Tab IsCard="true">
        <TabItem Text="@Localizer["TabItem1Text"]" Icon="fa-solid fa-user">
            <div>@Localizer["TabItem1Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem2Text"]" Icon="fa-solid fa-gauge-high">
            <div>@Localizer["TabItem2Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem3Text"]" Icon="fa-solid fa-sitemap">
            <div>@Localizer["TabItem3Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem4Text"]" Icon="fa-solid fa-building-columns">
            <div>@Localizer["TabItem4Content"]</div>
        </TabItem>
    </Tab>
```

### 基本用法

```razor
<Tab IsCard="true" ShowClose="true">
        <TabItem Text="@Localizer["TabItem1Text"]" Icon="fa-solid fa-user" Closable="false">
            <div>@Localizer["TabItem1Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem2Text"]" Icon="fa-solid fa-gauge-high">
            <div>@Localizer["TabItem2Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem3Text"]" Icon="fa-solid fa-sitemap">
            <div>@Localizer["TabItem3Content"]</div>
        </TabItem>
        <TabItem Text="@Localizer["TabItem4Text"]" Icon="fa-solid fa-building-columns">
            <div>@Localizer["TabItem4Content"]</div>
        </TabItem>
    </Tab>
```
