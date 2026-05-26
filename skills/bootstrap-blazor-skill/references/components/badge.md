# Badge (徽章)

## 概述

`Badge` 是一个徽章组件，提供数字或文本标签功能，支持颜色、胶囊样式等配置。

> Badge component!

**分类**: 基础组件  
**在线演示**: [https://www.blazor.zone/badge](https://www.blazor.zone/badge)

## 使用场景!

### 1. 基本用法

```razor
<Badge Color="Color.Primary">1</Badge>
```

### 2. 不同颜色

```razor
<Badge Color="Color.Success">2</Badge>
<Badge Color="Color.Danger">3</Badge>
<Badge Color="Color.Warning">4</Badge>
<Badge Color="Color.Info">5</Badge>
```

### 3. 胶囊样式

```razor
<Badge Color="Color.Primary" IsPill="true">1</Badge>
```

### 4. 自定义内容

```razor
<Badge Color="Color.Success">
    <i class="fa-solid fa-check"></i>
    <span>成功</span>
</Badge>
```

### 5. 数字徽章

```razor
<Badge Color="Color.Danger">@NotificationCount</Badge>
```

```csharp
@code {
    int NotificationCount { get; set; } = 5;
}
```

### 6. 链接徽章

```razor
<a class="btn btn-primary" href="#">
    消息 <Badge Color="Color.Secondary">4</Badge>
</a>
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.Primary` | 获得/设置徽章颜色 |
| `IsPill` | `bool` | `false` | 获得/设置徽章是否显示为胶囊形式 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置子组件内容 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnClick` | 点击徽章时触发 |

## 最佳实践!

1. **基本用法**: 在 `ChildContent` 中放置文本或数字
2. **颜色设置**: 使用 `Color` 参数设置徽章颜色（`Primary`、`Success`、`Danger` 等）
3. **胶囊样式**: 设置 `IsPill="true"` 启用胶囊样式
4. **自定义内容**: 在 `ChildContent` 中放置图标、文本等
5. **动态内容**: 绑定变量动态显示内容（如 `@NotificationCount`）
6. **链接使用**: 在 `<a>` 标签中使用徽章显示通知数量

## 常见问题!

### Q: 如何创建基本徽章？
A: 使用 `Badge` 组件，在 `ChildContent` 中放置文本或数字。

### Q: 如何设置徽章颜色？
A: 使用 `Color` 参数设置颜色，例如 `Color="Color.Success"`。

### Q: 如何启用胶囊样式？
A: 设置 `IsPill="true"` 启用胶囊样式徽章。

### Q: 如何显示动态内容？
A: 在 `ChildContent` 中使用变量，例如 `<Badge>@Count</Badge>`。

### Q: 如何在链接中使用徽章？
A: 将 `Badge` 放在 `<a>` 标签内，例如 `<a class="btn">消息 <Badge>4</Badge></a>`。
