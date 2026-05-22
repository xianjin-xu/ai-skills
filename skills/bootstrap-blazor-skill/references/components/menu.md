# Menu

## 概述

Menu 组件基类

> Menu Component Base

**分类**: 导航
**在线演示**: [https://www.blazor.zone/menu](https://www.blazor.zone/menu)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<MenuItem>?` | `}` | 获得/设置 菜单数据集合 |
| `IsAccordion` | `bool` | `}` | - |
| `IsExpandAll` | `bool` | `}` | - |
| `IsCollapsed` | `bool` | `}` | 获得/设置 侧栏是否收起 默认 false 未收起 |
| `IsVertical` | `bool` | `}` | 获得/设置 侧栏垂直模式 默认 false |
| `IsScrollIntoView` | `bool` | `true` | - |
| `IsBottom` | `bool` | `}` | 获得/设置 侧边栏垂直模式在底部 默认 false |
| `IndentSize` | `int` | `16` | 获得/设置 缩进大小 默认为 16 单位 px |
| `DisableNavigation` | `bool` | `}` | 获得/设置 是否禁止导航 默认为 false 允许导航 |
| `Task` | `Func<MenuItem,` | `}` | 获得/设置 菜单项点击回调委托 |

## 代码示例

### 基本用法

```razor
<Menu Items="@Items" DisableNavigation="true" OnClick="@OnClickMenu"></Menu>
```

### 基本用法

```razor
<Menu Items="@BottomItems" DisableNavigation="true" OnClick="@OnClickBottomMenu" IsBottom="true"></Menu>
```

### 基本用法

```razor
<Menu Items="@IconItems" DisableNavigation="true"></Menu>
```

### 基本用法

```razor
<Menu Items="@SideMenuItems" DisableNavigation="true" IsVertical="true" OnClick="@OnClickSideMenu" style="width:220px; border-right: 1px solid #e6e6e6; padding-right: 4px;"></Menu>
```

### 基本用法

```razor
<Menu Items="@IconSideMenuItems" DisableNavigation="true" IsVertical="true" IsAccordion="true" style="border-right: 1px solid #e6e6e6; width:220px;"></Menu>
```
