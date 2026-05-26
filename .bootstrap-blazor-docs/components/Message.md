# Message (消息提示)

## 概述

`Message` 组件常用于**主动操作后的反馈提示**。与 `Toast` 的区别是后者更多用于系统级通知的被动提醒。

`Message` 是**浮层消息通知**，从顶部出现，4 秒后自动消失。

**主要特性**：
- 支持 6 种消息颜色（Primary、Secondary、Success、Danger、Warning、Info）
- 支持 2 种显示位置（Top、Bottom）
- 可设置自动关闭延时（Duration）
- 可显示关闭按钮（ShowDismiss）
- 可显示图标（Icon）
- 可显示左侧边框（ShowBar）
- 支持显示模式（ShowMode）
- 支持自定义模板（ChildContent）
- 支持通过 `MessageService` 服务动态显示消息

**在线演示**: https://www.blazor.zone/message

---

## 使用场景

### 1. 基础用法（注入 MessageService 并显示消息）

`Message` 组件通常通过 `MessageService` 服务来显示消息。

```razor
@inject MessageService MessageService

<!-- 显示提示消息 -->
<Button OnClick="ShowMessage">显示消息</Button>

@code {
    private async Task ShowMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "这是一条提示消息"
        });
    }
}
```

**说明**：消息从顶部出现，4 秒后自动消失。

---

### 2. 设置显示位置（Placement）

通过 `MessageOption` 的 `Placement` 参数设置消息显示的位置（Top 或 Bottom）。

```razor
@inject MessageService MessageService

<!-- 顶部显示（默认） -->
<Button OnClick="ShowTopMessage">顶部显示</Button>

<!-- 底部显示 -->
<Button OnClick="ShowBottomMessage">底部显示</Button>

@code {
    private async Task ShowTopMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "顶部消息",
            Placement = Placement.Top
        });
    }

    private async Task ShowBottomMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "底部消息",
            Placement = Placement.Bottom
        });
    }
}
```

---

### 3. 带图标的消息框（Icon）

通过设置 `MessageOption` 的 `Icon` 属性，更改消息框左侧小图标。

```razor
@inject MessageService MessageService

<!-- 带自定义图标 -->
<Button OnClick="ShowIconMessage">带图标消息</Button>

@code {
    private async Task ShowIconMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "这是一条带图标的消息",
            Icon = "fa fa-info-circle"
        });
    }
}
```

---

### 4. 带关闭按钮的消息框（ShowDismiss）

通过设置 `MessageOption` 的 `ShowDismiss` 属性，更改消息框右侧出现关闭按钮。

```razor
@inject MessageService MessageService

<!-- 带关闭按钮 -->
<Button OnClick="ShowDismissMessage">带关闭按钮</Button>

@code {
    private async Task ShowDismissMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "这是一条带关闭按钮的消息",
            ShowDismiss = true
        });
    }
}
```

---

### 5. 左侧带边框的消息框（ShowBar）

通过设置 `MessageOption` 的 `ShowBar` 属性，更改消息框左侧边框样式。

```razor
@inject MessageService MessageService

<!-- 左侧带边框 -->
<Button OnClick="ShowBarMessage">左侧带边框</Button>

@code {
    private async Task ShowBarMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "这是一条左侧带边框的消息",
            ShowBar = true
        });
    }
}
```

---

### 6. 不同颜色的消息框（Color）

通过设置 `MessageOption` 的 `Color` 属性，更改消息框颜色。

```razor
@inject MessageService MessageService

<!-- Primary 消息 -->
<Button OnClick="ShowPrimaryMessage">Primary 消息</Button>

<!-- Success 消息 -->
<Button OnClick="ShowSuccessMessage">Success 消息</Button>

<!-- Info 消息 -->
<Button OnClick="ShowInfoMessage">Info 消息</Button>

<!-- Danger 消息 -->
<Button OnClick="ShowDangerMessage">Danger 消息</Button>

<!-- Warning 消息 -->
<Button OnClick="ShowWarningMessage">Warning 消息</Button>

<!-- Secondary 消息 -->
<Button OnClick="ShowSecondaryMessage">Secondary 消息</Button>

@code {
    private async Task ShowPrimaryMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "Primary 消息",
            Color = Color.Primary
        });
    }

    private async Task ShowSuccessMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "Success 消息",
            Color = Color.Success
        });
    }

    private async Task ShowInfoMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "Info 消息",
            Color = Color.Info
        });
    }

    private async Task ShowDangerMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "Danger 消息",
            Color = Color.Danger
        });
    }

    private async Task ShowWarningMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "Warning 消息",
            Color = Color.Warning
        });
    }

    private async Task ShowSecondaryMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "Secondary 消息",
            Color = Color.Secondary
        });
    }
}
```

---

### 7. 显示模式（ShowMode）

通过设置 `ShowMode` 参数，指定显示模式（如只显示最后一条消息）。

```razor
@inject MessageService MessageService

<!-- 只显示最后一条消息 -->
<Button OnClick="ShowSingleMessage">只显示最后一条</Button>

@code {
    private async Task ShowSingleMessage()
    {
        // 设置 ShowMode 为 ShowLast（只显示最后一条消息）
        // 注意：ShowMode 是 MessageService 的参数，需要在组件中设置
        await MessageService.Show(new MessageOption()
        {
            Content = "只显示最后一条消息",
            Color = Color.Info
        });
    }
}
```

---

### 8. 自定义模板（ChildContent）

通过设置 `ChildContent` 模板可以实现丰富的自定义样式与内容的提示信息。

```razor
@inject MessageService MessageService

<!-- 自定义模板消息 -->
<Button OnClick="ShowCustomMessage">自定义模板</Button>

@code {
    private async Task ShowCustomMessage()
    {
        await MessageService.Show(new MessageOption()
        {
            Content = "自定义内容",
            Color = Color.Success
        });
    }
}
```

**说明**：更复杂的自定义模板需要通过 `Message` 组件的 `ChildContent` 来实现，通常通过 `MessageService` 显示简单文本消息即可。

---

### 9. 线程阻塞通知（IsAsync）

通过设置按钮 `IsAsync` 参数，使用同一个 `MessageOption` 更新弹窗信息提示不同步骤时的信息。

```razor
@inject MessageService MessageService

<!-- 线程阻塞通知示例 -->
<Button OnClick="ShowProgressMessage" IsAsync="true">开始处理</Button>

@code {
    private async Task ShowProgressMessage()
    {
        // 显示初始消息
        var option = new MessageOption()
        {
            Content = "正在处理...",
            Color = Color.Info,
            ShowDismiss = false
        };
        
        await MessageService.Show(option);
        
        // 模拟长时间操作
        await Task.Delay(2000);
        
        // 更新消息内容
        option.Content = "处理完成！";
        option.Color = Color.Success;
    }
}
```

---

## 参数 (Parameters)

### Message 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `null` | 获得/设置用户自定义属性 |
| `Id` | `string?` | `null` | 获得/设置组件 id 属性 |
| `Placement` | `Placement` | `Placement.Top` | 获得/设置显示位置 默认为 Top |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

### MessageOption 参数

通过 `MessageService.Show(MessageOption)` 方法显示消息时，需要传递 `MessageOption` 对象。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Content` | `string?` | `null` | 获得/设置消息内容 |
| `Color` | `Color` | `Color.Success` | 获得/设置消息颜色主题 |
| `Duration` | `int` | `4000` | 获得/设置自动关闭延时（毫秒），0 表示不自动关闭 |
| `Icon` | `string?` | `null` | 获得/设置消息图标 |
| `ShowDismiss` | `bool` | `false` | 获得/设置是否显示关闭按钮 |
| `ShowBar` | `bool` | `false` | 获得/设置是否显示左侧边框 |
| `Placement` | `Placement` | `Placement.Top` | 获得/设置消息显示位置 |
| `ClassName` | `string?` | `null` | 获得/设置消息 CSS 类名 |
| `ChildContent` | `RenderFragment?` | `null` | 自定义模板内容 |

---

## 服务 (Services)

### MessageService

`MessageService` 是用于显示消息的服务，需要通过依赖注入获取。

**注册服务**：
```csharp
// Program.cs
builder.Services.AddBootstrapBlazor();
```

**注入服务**：
```razor
@inject MessageService MessageService
```

或

```csharp
[Inject]
private MessageService? MessageService { get; set; }
```

**使用方法**：
```csharp
// 显示消息
await MessageService.Show(new MessageOption()
{
    Content = "消息内容",
    Color = Color.Success
});

// 关闭所有消息
await MessageService.Clear();
```

---

## 最佳实践

1. **使用 MessageService**：推荐通过 `MessageService` 服务来显示消息，而不是直接在页面中使用 `Message` 组件
2. **合理设置 Duration**：短暂提示设置 3000-5000 毫秒，重要提示设置 0（不自动关闭）并显示关闭按钮
3. **合理使用颜色**：`Success` 用于成功操作，`Info` 用于一般信息，`Warning` 用于注意事项，`Danger` 用于错误，`Primary` 用于主要操作反馈
4. **选择合适的 Placement**：顶部消息使用 `Placement.Top`（默认），底部消息使用 `Placement.Bottom`
5. **避免频繁显示**：短时间内避免频繁显示消息，以免打扰用户
6. **与 Toast 组件的区别**：`Message` 是轻量级消息通知（通常单行显示，主动操作反馈），`Toast` 是重量级通知（可包含更多内容如标题、按钮等，系统级被动提醒）
7. **使用 ShowBar 突出重要性**：对于重要消息，设置 `ShowBar="true"` 显示左侧边框，增强视觉提示
8. **线程阻塞场景使用 IsAsync**：对于长时间操作，使用按钮的 `IsAsync="true"` 参数，在同一消息中更新进度信息
