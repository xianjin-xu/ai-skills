# Menu (菜单)

## 概述

`Menu` 是一个菜单组件基类，提供垂直/水平菜单、手风琴效果、缩进等配置。

> Menu Component Base!

**分类**: 导航  
**在线演示**: [https://www.blazor.zone/menu](https://www.blazor.zone/menu)

## 使用场景

### 1. 基本用法

```razor
<Menu Items="MenuItems" OnClick="OnMenuItemClick" />
```

```csharp
@code {
    List<MenuItem> MenuItems = new List<MenuItem>
    {
        new MenuItem("菜单1") { Items = new List<MenuItem> { new MenuItem("子菜单1") } },
        new MenuItem("菜单2")
    };
    
    Task OnMenuItemClick(MenuItem item)
    {
        // 处理菜单项点击
        return Task.CompletedTask;
    }
}
```

### 2. 垂直菜单

```razor
<Menu Items="MenuItems" IsVertical="true" />
```

### 3. 手风琴效果

```razor
<Menu Items="MenuItems" IsVertical="true" IsAccordion="true" />
```

### 4. 展开所有

```razor
<Menu Items="MenuItems" IsVertical="true" IsExpandAll="true" />
```

### 5. 折叠状态

```razor
<Menu Items="MenuItems" IsVertical="true" IsCollapsed="true" />
```

### 6. 底部菜单

```razor
<Menu Items="BottomMenuItems" IsVertical="true" IsBottom="true" />
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<MenuItem>?` | `null` | 获得/设置菜单数据集合 |
| `IsAccordion` | `bool` | `false` | 获得/设置是否为手风琴效果 |
| `IsExpandAll` | `bool` | `false` | 获得/设置是否全部展开 |
| `IsCollapsed` | `bool` | `false` | 获得/设置侧栏是否收起 |
| `IsVertical` | `bool` | `false` | 获得/设置侧栏垂直模式 |
| `IsScrollIntoView` | `bool` | `true` | 获得/设置自动滚动到可视区域 |
| `IsBottom` | `bool` | `false` | 获得/设置侧边栏垂直模式在底部 |
| `IndentSize` | `int` | `16` | 获得/设置缩进大小（单位 px） |
| `DisableNavigation` | `bool` | `false` | 获得/设置是否禁止导航 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnClick` | 菜单项点击时触发 |

## 最佳实践

1. **数据绑定**: 使用 `Items` 参数提供 `MenuItem` 集合
2. **垂直菜单**: 设置 `IsVertical="true"` 启用垂直菜单
3. **手风琴**: 设置 `IsAccordion="true"` 启用手风琴效果（一次只展开一个）
4. **展开所有**: 设置 `IsExpandAll="true"` 展开所有菜单项
5. **缩进控制**: 使用 `IndentSize` 参数设置子菜单缩进大小
6. **点击处理**: 使用 `OnClick` 回调处理菜单项点击事件

## 常见问题

### Q: 如何绑定菜单数据？
A: 使用 `Items` 参数提供 `MenuItem` 集合，每个 `MenuItem` 可以包含子菜单项（`Items` 属性）。

### Q: 如何启用垂直菜单？
A: 设置 `IsVertical="true"` 启用垂直菜单模式。

### Q: 如何启用手风琴效果？
A: 设置 `IsAccordion="true"` 启用手风琴效果，一次只能展开一个顶级菜单项。

### Q: 如何展开所有菜单项？
A: 设置 `IsExpandAll="true"` 展开所有菜单项（手风琴模式时此参数不生效）。

### Q: 如何处理菜单项点击？
A: 使用 `OnClick` 回调处理菜单项点击事件，参数为点击的 `MenuItem` 对象。

## 子组件

`Menu` 组件有多个子组件：
- `SideMenu` - 侧边菜单（继承 `Menu`）
- `TopMenu` - 顶部菜单（继承 `Menu`）
- `ContextMenu` - 右键菜单（继承 `Menu`）
- `SubMenu` - 子菜单项
