# Layout (布局)

## 概述

`Layout` 是一个布局组件，提供侧边栏、标签页、工具栏等功能，用于构建应用程序的主布局。

> Layout Component

**分类**: 布局  
**在线演示**: [https://www.blazor.zone/layout](https://www.blazor.zone/layout)

## 使用场景

### 1. 基本用法

```razor
<Layout>
    <Side>
        <!-- 侧边栏内容 -->
    </Side>
    <Main>
        <!-- 主内容区域 -->
    </Main>
</Layout>
```

### 2. 显示标签页

```razor
<Layout UseTabSet="true">
    <Side>
        <!-- 侧边栏内容 -->
    </Side>
    <Main>
        <!-- 主内容区域 -->
    </Main>
</Layout>
```

### 3. 侧边栏可折叠

```razor
<Layout IsCollapsed="IsCollapsed" IsCollapsedChanged="OnCollapsedChanged">
    <Side>
        <!-- 侧边栏内容 -->
    </Side>
    <Main>
        <!-- 主内容区域 -->
    </Main>
</Layout>
```

```csharp
@code {
    bool IsCollapsed { get; set; } = false;
    
    void OnCollapsedChanged(bool value)
    {
        IsCollapsed = value;
    }
}
```

### 4. 显示工具栏

```razor
<Layout ShowToolbar="true" ShowRefreshToolbarButton="true">
    <ToolbarTemplate>
        <Button Text="自定义按钮" />
    </ToolbarTemplate>
    <Side>
        <!-- 侧边栏内容 -->
    </Side>
    <Main>
        <!-- 主内容区域 -->
    </Main>
</Layout>
```

### 5. 菜单手风琴效果

```razor
<Layout IsAccordion="true" Menus="MenuItems">
    <Side>
        <!-- 侧边栏内容 -->
    </Side>
    <Main>
        <!-- 主内容区域 -->
    </Main>
</Layout>
```

```csharp
@code {
    List<MenuItem> MenuItems = new List<MenuItem>
    {
        new MenuItem("菜单1") { Items = new List<MenuItem> { new MenuItem("子菜单1") } },
        new MenuItem("菜单2")
    };
}
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsCollapsed` | `bool` | `false` | 获得/设置侧边栏是否折叠 |
| `IsCollapsedChanged` | `EventCallback<bool>` | - | 获得/设置侧边栏折叠状态改变回调 |
| `IsAccordion` | `bool` | `false` | 获得/设置菜单是否手风琴效果 |
| `Menus` | `IEnumerable<MenuItem>?` | `null` | 获得/设置侧边栏菜单集合 |
| `UseTabSet` | `bool` | `false` | 获得/设置是否使用标签页 |
| `ShowToolbar` | `bool` | `false` | 获得/设置是否显示工具栏 |
| `ShowFullscreenToolbarButton` | `bool` | `true` | 获得/设置是否显示全屏按钮 |
| `ShowRefreshToolbarButton` | `bool` | `true` | 获得/设置是否显示刷新按钮 |
| `SideWidth` | `string?` | `"300"` | 获得/设置侧边栏宽度 |
| `SidebarMinWidth` | `int?` | `null` | 获得/设置侧边栏最小宽度 |
| `SidebarMaxWidth` | `int?` | `null` | 获得/设置侧边栏最大宽度 |
| `ShowSplitBar` | `bool` | `false` | 获得/设置是否显示分割栏 |
| `IsFullSide` | `bool` | `false` | 获得/设置侧边栏是否占满整个左侧 |
| `Header` | `RenderFragment?` | `null` | 获得/设置 Header 模板 |
| `Footer` | `RenderFragment?` | `null` | 获得/设置 Footer 模板 |
| `Side` | `RenderFragment?` | `null` | 获得/设置 Side 模板 |
| `Main` | `RenderFragment?` | `null` | 获得/设置 Main 模板 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `IsCollapsedChanged` | 侧边栏折叠状态改变时触发 |
| `OnToolbarRefreshCallback` | 刷新按钮点击时触发 |
| `OnCloseTabItemAsync` | 关闭标签页前触发 |

## 最佳实践

1. **基本布局**: 使用 `Side` 和 `Main` 模板定义侧边栏和主内容区域
2. **标签页**: 设置 `UseTabSet="true"` 启用标签页功能
3. **折叠功能**: 使用 `IsCollapsed` 和 `IsCollapsedChanged` 控制侧边栏折叠状态
4. **工具栏**: 设置 `ShowToolbar="true"` 显示工具栏，使用 `ToolbarTemplate` 自定义工具栏内容
5. **菜单**: 使用 `Menus` 参数提供菜单项集合，设置 `IsAccordion="true"` 启用手风琴效果
6. **宽度控制**: 使用 `SideWidth` 设置侧边栏宽度，使用 `SidebarMinWidth` 和 `SidebarMaxWidth` 限制宽度范围

## 常见问题

### Q: 如何创建基本布局？
A: 使用 `Layout` 组件，在 `Side` 模板中定义侧边栏内容，在 `Main` 模板中定义主内容区域。

### Q: 如何启用标签页？
A: 设置 `UseTabSet="true"` 启用标签页功能，页面会自动在标签页中打开。

### Q: 如何控制侧边栏折叠？
A: 使用 `IsCollapsed` 参数控制折叠状态，使用 `IsCollapsedChanged` 回调处理状态改变。

### Q: 如何自定义菜单？
A: 使用 `Menus` 参数提供 `MenuItem` 集合，每个 `MenuItem` 可以包含子菜单项。

### Q: 如何自定义工具栏？
A: 设置 `ShowToolbar="true"` 显示工具栏，使用 `ToolbarTemplate` 模板自定义工具栏内容。
