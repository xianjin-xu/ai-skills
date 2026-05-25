# Tab (标签页)

## 概述

`Tab` 是一个标签页组件，提供多标签页管理功能，支持卡片样式、关闭按钮、全屏、拖拽等配置。

> Tab component

**分类**: 导航  
**在线演示**: [https://www.blazor.zone/tab](https://www.blazor.zone/tab)

## 使用场景

### 1. 基本用法

```razor
<Tab>
    <TabItem Text="标签1" Url="/page1">
        <h3>标签1内容</h3>
    </TabItem>
    <TabItem Text="标签2" Url="/page2">
        <h3>标签2内容</h3>
    </TabItem>
</Tab>
```

### 2. 卡片样式

```razor
<Tab IsCard="true">
    <TabItem Text="标签1">
        <h3>标签1内容</h3>
    </TabItem>
</Tab>
```

### 3. 显示关闭按钮

```razor
<Tab ShowClose="true">
    <TabItem Text="标签1" Closable="true">
        <h3>标签1内容</h3>
    </TabItem>
</Tab>
```

### 4. 显示全屏按钮

```razor
<Tab ShowFullScreen="true">
    <TabItem Text="标签1">
        <h3>标签1内容</h3>
    </TabItem>
</Tab>
```

### 5. 标签位置

```razor
<Tab Placement="Placement.Bottom">
    <TabItem Text="标签1">
        <h3>标签1内容</h3>
    </TabItem>
</Tab>
```

### 6. 懒加载

```razor
<Tab IsLazyLoadTabItem="true">
    <TabItem Text="标签1" Url="/page1" />
    <TabItem Text="标签2" Url="/page2" />
</Tab>
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsCard` | `bool` | `false` | 获得/设置是否为卡片样式 |
| `IsBorderCard` | `bool` | `false` | 获得/设置是否为边框卡片样式 |
| `IsOnlyRenderActiveTab` | `bool` | `false` | 获得/设置是否仅渲染活动标签 |
| `IsLazyLoadTabItem` | `bool` | `false` | 获得/设置是否懒加载 TabItem |
| `Height` | `int` | `0` | 获得/设置组件高度（0 为自动） |
| `Placement` | `Placement` | `Placement.Top` | 获得/设置标签显示位置 |
| `ShowClose` | `bool` | `false` | 获得/设置是否显示关闭按钮 |
| `ShowFullScreen` | `bool` | `false` | 获得/设置是否显示全屏按钮 |
| `ShowExtendButtons` | `bool` | `false` | 获得/设置是否显示扩展功能按钮 |
| `ShowNavigatorButtons` | `bool` | `true` | 获得/设置是否显示前后导航按钮 |
| `IsLoopSwitchTabItem` | `bool` | `true` | 获得/设置是否自动重置标签项索引 |
| `ShowActiveBar` | `bool` | `true` | 获得/设置是否显示活动标签栏 |
| `ClickTabToNavigation` | `bool` | `false` | 获得/设置点击 TabItem 时是否自动导航 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnCloseTabItemAsync` | 关闭标签页前触发 |
| `OnTabHeaderTextLocalizer` | Tab 标签头文本本地化回调 |

## 最佳实践

1. **基本结构**: 使用 `TabItem` 定义标签页，设置 `Text` 和 `Url` 属性
2. **卡片样式**: 设置 `IsCard="true"` 启用卡片样式
3. **关闭功能**: 设置 `ShowClose="true"` 显示关闭按钮，设置 `TabItem.Closable="true"` 允许关闭
4. **全屏功能**: 设置 `ShowFullScreen="true"` 显示全屏按钮
5. **懒加载**: 设置 `IsLazyLoadTabItem="true"` 懒加载标签页内容
6. **拖拽功能**: 组件支持拖拽标签页重新排序（自动启用）

## 常见问题

### Q: 如何创建基本标签页？
A: 使用 `Tab` 组件，内部使用 `TabItem` 定义标签页，设置 `Text` 和 `Url` 属性。

### Q: 如何启用卡片样式？
A: 设置 `IsCard="true"` 启用卡片样式标签页。

### Q: 如何允许关闭标签页？
A: 设置 `ShowClose="true"` 显示关闭按钮，设置 `TabItem.Closable="true"` 允许该标签页被关闭。

### Q: 如何启用懒加载？
A: 设置 `IsLazyLoadTabItem="true"` 懒加载标签页内容，首次不渲染。

### Q: 如何设置标签位置？
A: 使用 `Placement` 参数设置位置，可选 `Top`、`Bottom`、`Left`、`Right`。

## 子组件

`Tab` 组件包含以下子组件：
- `TabItem` - 标签页项
- `TabItemText` - 标签页文本模板
- `TabContent` - 标签页内容区域
