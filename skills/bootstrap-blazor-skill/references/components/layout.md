# Layout

## 概述

Layout 组件

> Layout Component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/layout](https://www.blazor.zone/layout)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `string` | `Func<string?,` | `}` | 获得/设置 Tab 标签头文本本地化回调方法 |
| `TabStyle` | `TabStyle` | `}` | 获得/设置 the tab 样式. 默认为 <see cref="TabStyle.Default"/> |
| `ShowToolbar` | `bool` | `}` | 获得/设置 是否 show the toolbar. 默认为 false |
| `ToolbarTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 the 模板 of the toolbar 按钮. 默认为 null |
| `ShowFullscreenToolbarButton` | `bool` | `true` | 获得/设置 是否 show the full screen 按钮. 默认为 true |
| `FullscreenToolbarButtonIcon` | `string?` | `}` | 获得/设置 the full screen toolbar 按钮 图标 string. 默认为 null |
| `FullscreenToolbarTooltipText` | `string?` | `}` | 获得/设置 the full screen toolbar 按钮 tooltip string. 默认为 null |
| `ShowRefreshToolbarButton` | `bool` | `true` | 获得/设置 是否 show the full screen 按钮. 默认为 true |
| `RefreshToolbarButtonIcon` | `string?` | `}` | 获得/设置 the refresh toolbar 按钮 图标 string. 默认为 null |
| `RefreshToolbarTooltipText` | `string?` | `}` | 获得/设置 the refresh toolbar 按钮 tooltip string. 默认为 null |
| `OnToolbarRefreshCallback` | `Func<Task>?` | `}` | 获得/设置 the refresh toolbar 按钮 click event 回调. 默认为 null |
| `Task` | `Func<TabItem,` | `}` | - |
| `IsCollapsed` | `bool` | `}` | 获得/设置 侧边栏状态 |
| `IsAccordion` | `bool` | `}` | 获得/设置 菜单手风琴效果 |
| `CollapseBarTemplate` | `RenderFragment?` | `}` | 获得/设置 收起展开按钮模板 |
| `Header` | `RenderFragment?` | `}` | 获得/设置 Header 模板 |
| `Footer` | `RenderFragment?` | `}` | 获得/设置 Footer 模板 |
| `MenuBarIcon` | `string?` | `}` | 获得/设置 MenuBar 图标 |
| `Side` | `RenderFragment?` | `}` | 获得/设置 Side 模板 |
| `ShowSplitBar` | `bool` | `}` | 获得/设置 是否显示分割栏 默认 false 不显示 仅在 左右布局时有效 |
| `ShowSplitebar` | `bool` | `}` | 获得/设置 是否显示分割栏 默认 false 不显示 仅在 左右布局时有效 |
| `SidebarMinWidth` | `int?` | `}` | 获得/设置 侧边栏最小宽度 默认 null 未设置 |
| `SidebarMaxWidth` | `int?` | `}` | 获得/设置 侧边栏最大宽度 默认 null 未设置 |
| `NotAuthorized` | `RenderFragment?` | `}` | 获得/设置 NotAuthorized 模板 默认 null NET6.0/7.0 有效 |
| `NotFound` | `RenderFragment?` | `}` | 获得/设置 NotFound 模板 默认 null NET6.0/7.0 有效 |
| `NotFoundTabText` | `string?` | `}` | 获得/设置 NotFound 标签文本 默认 null NET6.0/7.0 有效 |
| `SideWidth` | `string?` | `}` | 获得/设置 侧边栏宽度，支持百分比，设置 0 时关闭宽度功能 默认值 300 |
| `Main` | `RenderFragment?` | `}` | 获得/设置 Main 模板 |
| `IsFullSide` | `bool` | `}` | 获得/设置 侧边栏是否占满整个左侧 默认为 false |
| `IsPage` | `bool` | `}` | - |
| `Menus` | `IEnumerable<MenuItem>?` | `}` | 获得/设置 侧边栏菜单集合 |
| `UseTabSet` | `bool` | `}` | 获得/设置 是否右侧使用 Tab 组件 默认为 false 不使用 |
| `IsFixedTabHeader` | `bool` | `}` | 获得/设置 是否固定多标签 Header 默认 false |
| `IsOnlyRenderActiveTab` | `bool` | `}` | 获得/设置 是否仅渲染 Active 标签 |
| `AllowDragTab` | `bool` | `true` | 获得/设置 是否允许拖动标签页 默认 true |
| `IsFixedFooter` | `bool` | `}` | 获得/设置 是否固定 Footer 组件 |
| `IsFixedHeader` | `bool` | `}` | 获得/设置 是否固定 Header 组件 |
| `ShowCollapseBar` | `bool` | `}` | 获得/设置 是否显示收缩展开 Bar 默认 false |
| `ShowFooter` | `bool` | `}` | 获得/设置 是否显示 Footer 模板 默认 false |
| `ShowGotoTop` | `bool` | `}` | 获得/设置 是否显示返回顶端按钮 默认为 false 不显示 |
| `TabDefaultUrl` | `string` | `""` | 获得/设置 默认标签页 关闭所有标签页时自动打开此地址 默认 null 未设置 |
| `ShowTabItemClose` | `bool` | `true` | 获得/设置 标签是否显示关闭按钮 默认 true |
| `ShowTabExtendButtons` | `bool` | `true` | 获得/设置 标签是否显示扩展按钮 默认 true |
| `ClickTabToNavigation` | `bool` | `true` | 获得/设置 点击标签页是否切换地址栏 默认 true |
| `NotAuthorizeUrl` | `string` | `"/Account/Login"` | 获得/设置 未授权导航地址 默认为 "/Account/Login" Cookie 模式登录页 |
| `ShowTabContextMenu` | `bool` | `}` | 获得/设置 是否 enable tab context menu. 默认为 false |
| `BeforeTabContextMenuTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 the 模板 of before tab context menu. 默认为 null |
| `TabContextMenuTemplate` | `RenderFragment<Tab>?` | `}` | 获得/设置 the 模板 of tab context menu. 默认为 null |
| `TabContextMenuRefreshIcon` | `string?` | `}` | 获得/设置 the 图标 of tab item context menu refresh 按钮. 默认为 null |
| `TabContextMenuCloseIcon` | `string?` | `}` | 获得/设置 the 图标 of tab item context menu close 按钮. 默认为 null |
| `TabContextMenuCloseOtherIcon` | `string?` | `}` | 获得/设置 the 图标 of tab item context menu close other 按钮. 默认为 null |
| `TabContextMenuCloseAllIcon` | `string?` | `}` | 获得/设置 the 图标 of tab item context menu close all 按钮. 默认为 null |
| `ShowTabInHeader` | `bool` | `}` | 获得/设置 是否 show the tab in header. 默认为 false |
| `SkipAuthenticate` | `bool` | `}` | 获得/设置 是否跳过认证逻辑 默认 false |
| `ExcludeUrls` | `IEnumerable<string>?` | `}` | 获得/设置 排除地址支持通配符 |
| `AdditionalAssemblies` | `IEnumerable<Assembly>?` | `}` | 获得/设置 额外的程序集集合，这些程序集将被搜索以匹配 URI 的组件 |
| `TooltipText` | `string?` | `}` | 获得/设置 鼠标悬停提示文字信息 |
| `Resource` | `object?` | `}` | 获得/设置 AuthorizeRouteView 参数 |
| `EnableErrorLogger` | `bool?` | `}` | 获得/设置 是否开启全局异常捕获 默认 null 使用 <see cref="BootstrapBlazorOptions.EnableErrorLogger"/> 设置值 |
| `EnableErrorLoggerILogger` | `bool?` | `}` | 获得/设置 是否记录异常到 <see cref="ILogger"/> 默认 null 使用 <see cref="BootstrapBlazorOptions.EnableErrorLoggerILogger"/> 设置值 |
| `ShowErrorLoggerToast` | `bool?` | `}` | 获得/设置 是否显示 Error 提示弹窗 默认 null 使用 <see cref="BootstrapBlazorOptions.ShowErrorLoggerToast"/> 设置值 |
| `ErrorLoggerToastTitle` | `string?` | `}` | 获得/设置 错误日志 <see cref="Toast"/> 弹窗标题 默认 null |
| `Exception` | `Func<ILogger,` | `}` | 获得/设置 自定义错误处理回调方法 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `IsCollapsedChanged` | `EventCallback<bool>` | 获得/设置 侧边栏状态 |

## 代码示例

### 基本用法

```razor
<Layout ShowFooter="true" AdditionalAssemblies="[typeof(MainLayout).Assembly]">
            <Header>
                <div>Header</div>
            </Header>
            <Main>
                <div>Main</div>
            </Main>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
```

### 基本用法

```razor
<Layout ShowFooter="true" AdditionalAssemblies="[typeof(MainLayout).Assembly]">
            <Header>
                <div>Header</div>
            </Header>
            <Side>
                <div>Side</div>
            </Side>
            <Main>
                <div>Main</div>
            </Main>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
```

### 基本用法

```razor
<Layout ShowFooter="true" IsFullSide="true" AdditionalAssemblies="[typeof(MainLayout).Assembly]">
            <Header>
                <div>Header</div>
            </Header>
            <Side>
                <div>Side</div>
            </Side>
            <Main>
                <div>Main</div>
            </Main>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
```

### 基本用法

```razor
<Layout ShowFooter="true" SideWidth="200" AdditionalAssemblies="[typeof(MainLayout).Assembly]">
            <Header>
                <div>Header</div>
            </Header>
            <Side>
                <div>Side</div>
            </Side>
            <Main>
                <div>Main</div>
            </Main>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
```

### 基本用法

```razor
<Layout ShowFooter="true" SideWidth="160px" Menus="IconSideMenuItems1" AdditionalAssemblies="[typeof(MainLayout).Assembly]">
            <Header>
                <div>Header</div>
            </Header>
            <Side>
            </Side>
            <Main>
                <div>Main</div>
            </Main>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
<Layout ShowFooter="true" SideWidth="160px" Menus="IconSideMenuItems2" AdditionalAssemblies="[typeof(MainLayout).Assembly]">
            <Header>
                <div>Header</div>
            </Header>
            <Side>
            </Side>
            <Main>
                <div>Main</div>
            </Main>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
```
