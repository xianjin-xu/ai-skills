# Nav (导航)

## 概述

`Nav` 是一个导航组件基类，提供水平/垂直导航菜单功能，支持对齐方式、胶囊样式等配置。

> NavMenu Component Base Class

**分类**: 导航  
**在线演示**: [https://www.blazor.zone/nav](https://www.blazor.zone/nav)

## 使用场景

### 1. 基本用法

```razor
<Nav Items="NavItems" />
```

```csharp
@code {
    List<NavLink> NavItems = new List<NavLink>
    {
        new NavLink("首页", "/") { Icon = "fa-solid fa-home" },
        new NavLink("关于", "/about") { Icon = "fa-solid fa-info-circle" }
    };
}
```

### 2. 垂直导航

```razor
<Nav Items="NavItems" IsVertical="true" />
```

### 3. 胶囊样式

```razor
<Nav Items="NavItems" IsPills="true" />
```

### 4. 填充样式

```razor
<Nav Items="NavItems" IsFill="true" />
```

### 5. 等宽样式

```razor
<Nav Items="NavItems" IsJustified="true" />
```

### 6. 右对齐

```razor
<Nav Items="NavItems" Alignment="Alignment.Right" />
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<NavLink>?` | `[]` | 获得/设置组件数据源 |
| `Alignment` | `Alignment` | `Alignment.Left` | 获得/设置组件对齐方式 |
| `IsVertical` | `bool` | `false` | 获得/设置是否垂直分布 |
| `IsPills` | `bool` | `false` | 获得/设置是否为胶囊样式 |
| `IsFill` | `bool` | `false` | 获得/设置是否填充 |
| `IsJustified` | `bool` | `false` | 获得/设置是否等宽 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnClick` | 点击导航项时触发 |

## 最佳实践

1. **数据绑定**: 使用 `Items` 参数提供 `NavLink` 集合
2. **垂直导航**: 设置 `IsVertical="true"` 启用垂直导航
3. **胶囊样式**: 设置 `IsPills="true"` 启用胶囊样式
4. **填充样式**: 设置 `IsFill="true"` 启用填充样式
5. **等宽样式**: 设置 `IsJustified="true"` 启用等宽样式
6. **对齐方式**: 使用 `Alignment` 参数设置对齐方式（`Left`、`Center`、`Right`）

## 常见问题

### Q: 如何绑定导航数据？
A: 使用 `Items` 参数提供 `NavLink` 集合，每个 `NavLink` 包含 `Text`、`Url`、`Icon` 等属性。

### Q: 如何启用垂直导航？
A: 设置 `IsVertical="true"` 启用垂直导航菜单。

### Q: 如何启用胶囊样式？
A: 设置 `IsPills="true"` 启用胶囊样式导航。

### Q: 如何设置对齐方式？
A: 使用 `Alignment` 参数设置对齐方式，例如 `Alignment="Alignment.Right"` 右对齐。

### Q: 如何处理点击事件？
A: 使用 `OnClick` 回调处理导航项点击事件。

## 子组件

`Nav` 组件有多个子组件：
- `NavLink` - 导航链接项
- `NavMenu` - 导航菜单（继承 `Nav`）
- `NavTab` - 导航标签页（继承 `Nav`）
