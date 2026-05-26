# Tag (标签)

## 概述!

`Tag` 是一个标签组件，提供标签显示和关闭功能，支持颜色、图标、可关闭等配置。

> Tag Component!

**分类**: 基础组件  
**在线演示**: [https://www.blazor.zone/tag](https://www.blazor.zone/tag)

## 使用场景!

### 1. 基本用法!

```razor
<Tag Color="Color.Primary">标签1</Tag>
```

### 2. 不同颜色!

```razor
<Tag Color="Color.Success">成功</Tag>
<Tag Color="Color.Danger">危险</Tag>
<Tag Color="Color.Warning">警告</Tag>
<Tag Color="Color.Info">信息</Tag>
```

### 3. 可关闭!

```razor
<Tag Color="Color.Primary" ShowDismiss="true" OnDismiss="OnTagDismiss">
    标签1
</Tag>
```

```csharp
@code {
    async Task OnTagDismiss()
    {
        // 处理标签关闭逻辑
    }
}
```

### 4. 显示图标!

```razor
<Tag Color="Color.Success" Icon="fa-solid fa-check">成功</Tag>
```

### 5. 自定义内容!

```razor
<Tag Color="Color.Primary">
    <i class="fa-solid fa-star"></i>
    <span>自定义标签</span>
</Tag>
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.None` | 获得/设置标签颜色 |
| `Icon` | `string?` | `null` | 获得/设置标签图标 |
| `ShowDismiss` | `bool` | `false` | 获得/设置是否显示关闭按钮 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置标签内容 |
| `AdditionalAttributes` | `Dictionary<string, object>?` | `null` | 获得/设置额外属性 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnDismiss` | 关闭标签时触发 |

## 最佳实践!

1. **基本用法**: 在 `ChildContent` 中放置标签文本或内容
2. **颜色设置**: 使用 `Color` 参数设置标签颜色（`Primary`、`Success`、`Danger` 等）
3. **关闭功能**: 设置 `ShowDismiss="true"` 显示关闭按钮，使用 `OnDismiss` 处理关闭逻辑
4. **图标设置**: 使用 `Icon` 参数设置标签图标
5. **自定义样式**: 通过 `AdditionalAttributes` 添加自定义 HTML 属性
6. **动态控制**: 使用条件渲染控制标签显示/隐藏

## 常见问题!

### Q: 如何创建基本标签？
A: 使用 `Tag` 组件，在 `ChildContent` 中放置标签文本，使用 `Color` 参数设置颜色。

### Q: 如何设置标签颜色？
A: 使用 `Color` 参数设置颜色，例如 `Color="Color.Success"`。

### Q: 如何启用关闭功能？
A: 设置 `ShowDismiss="true"` 显示关闭按钮，使用 `OnDismiss` 回调处理关闭逻辑。

### Q: 如何添加图标？
A: 使用 `Icon` 参数设置图标类名，例如 `Icon="fa-solid fa-check"`。

### Q: 如何控制标签显示/隐藏？
A: 使用条件渲染（如 `@if (showTag)`）控制标签显示/隐藏。