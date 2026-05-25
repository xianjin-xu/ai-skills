# Toast (轻量弹窗)

## 概述

`Toast` 组件用于显示**系统级被动提醒通知**。与 `Message` 的区别是 `Message` 更多用于主动操作后的反馈提示，而 `Toast` 更多用于系统级通知的被动提醒。

`Toast` 是**浮层通知**，通常从页面角落出现，一段时间后自动消失。

**主要特性**：
- 支持 4 种通知类型（Success、Info、Warning、Danger）
- 支持 6 种显示位置（TopRight、TopLeft、BottomRight、BottomLeft、TopCenter、BottomCenter）
- 可设置自动关闭延时（Duration）
- 可显示标题（Title）
- 可显示内容（Content）
- 可显示图标（Icon）
- 支持通过 `ToastService` 服务动态显示通知

**在线演示**: https://www.blazor.zone/toast

---

## 使用场景

### 1. 基础用法（注入 ToastService 并显示通知）

`Toast` 组件通常通过 `ToastService` 服务来显示通知。

```razor
@inject ToastService ToastService

<!-- 显示成功通知 -->
<Button OnClick="ShowSuccessToast">显示成功通知</Button>

@code {
    private async Task ShowSuccessToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "成功",
            Content = "操作已完成"
        });
    }
}
```

**说明**：通知从右上角出现，4.5 秒后自动消失。

---

### 2. 设置显示位置（Placement）

通过 `ToastOption` 的 `Placement` 参数设置通知显示的位置。

```razor
@inject ToastService ToastService

<!-- 右上角显示（默认） -->
<Button OnClick="ShowTopRightToast">右上角</Button>

<!-- 左上角显示 -->
<Button OnClick="ShowTopLeftToast">左上角</Button>

<!-- 右下角显示 -->
<Button OnClick="ShowBottomRightToast">右下角</Button>

<!-- 左下角显示 -->
<Button OnClick="ShowBottomLeftToast">左下角</Button>

@code {
    private async Task ShowTopRightToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "右上角通知",
            Placement = Placement.TopRight
        });
    }

    private async Task ShowTopLeftToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "左上角通知",
            Placement = Placement.TopLeft
        });
    }

    private async Task ShowBottomRightToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "右下角通知",
            Placement = Placement.BottomRight
        });
    }

    private async Task ShowBottomLeftToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "左下角通知",
            Placement = Placement.BottomLeft
        });
    }
}
```

---

### 3. 不同颜色的通知（Color）

通过设置 `ToastOption` 的 `Color` 属性，更改通知颜色。

```razor
@inject ToastService ToastService

<!-- Success 通知 -->
<Button OnClick="ShowSuccessToast">Success</Button>

<!-- Info 通知 -->
<Button OnClick="ShowInfoToast">Info</Button>

<!-- Warning 通知 -->
<Button OnClick="ShowWarningToast">Warning</Button>

<!-- Danger 通知 -->
<Button OnClick="ShowDangerToast">Danger</Button>

@code {
    private async Task ShowSuccessToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "成功",
            Content = "操作成功完成",
            Color = Color.Success
        });
    }

    private async Task ShowInfoToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "信息",
            Content = "这是一条信息通知",
            Color = Color.Info
        });
    }

    private async Task ShowWarningToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "警告",
            Content = "请注意此警告",
            Color = Color.Warning
        });
    }

    private async Task ShowDangerToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "错误",
            Content = "操作失败，请重试",
            Color = Color.Danger
        });
    }
}
```

---

### 4. 带图标的通知（Icon）

通过设置 `ToastOption` 的 `Icon` 属性，更改通知左侧图标。

```razor
@inject ToastService ToastService

<!-- 带自定义图标 -->
<Button OnClick="ShowIconToast">带图标通知</Button>

@code {
    private async Task ShowIconToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "这是一条带图标的通知",
            Icon = "fa fa-info-circle"
        });
    }
}
```

---

### 5. 设置自动关闭延时（Duration）

通过 `ToastOption` 的 `Duration` 参数设置通知自动关闭的延时（毫秒）。

```razor
@inject ToastService ToastService

<!-- 3秒后自动关闭 -->
<Button OnClick="ShowShortToast">短延时（3秒）</Button>

<!-- 6秒后自动关闭 -->
<Button OnClick="ShowLongToast">长延时（6秒）</Button>

<!-- 不自动关闭 -->
<Button OnClick="ShowNoAutoCloseToast">不自动关闭</Button>

@code {
    private async Task ShowShortToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "3秒后自动关闭",
            Duration = 3000
        });
    }

    private async Task ShowLongToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "6秒后自动关闭",
            Duration = 6000
        });
    }

    private async Task ShowNoAutoCloseToast()
    {
        await ToastService.Show(new ToastOption()
        {
            Title = "提示",
            Content = "不会自动关闭",
            Duration = 0
        });
    }
}
```

---

## 参数 (Parameters)

### Toast 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Placement` | `Placement` | `Placement.TopRight` | 获得/设置显示位置 默认为 TopRight |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

### ToastOption 参数

通过 `ToastService.Show(ToastOption)` 方法显示通知时，需要传递 `ToastOption` 对象。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Title` | `string?` | `null` | 获得/设置通知标题 |
| `Content` | `string?` | `null` | 获得/设置通知内容 |
| `Color` | `Color` | `Color.Success` | 获得/设置通知颜色主题 |
| `Duration` | `int` | `4500` | 获得/设置自动关闭延时（毫秒），0 表示不自动关闭 |
| `Icon` | `string?` | `null` | 获得/设置通知图标 |
| `Placement` | `Placement` | `Placement.TopRight` | 获得/设置通知显示位置 |
| `ClassName` | `string?` | `null` | 获得/设置通知 CSS 类名 |

---

## 服务 (Services)

### ToastService

`ToastService` 是用于显示通知的服务，需要通过依赖注入获取。

**注册服务**：
```csharp
// Program.cs
builder.Services.AddBootstrapBlazor();
```

**注入服务**：
```razor
@inject ToastService ToastService
```

或

```csharp
[Inject]
private ToastService? ToastService { get; set; }
```

**使用方法**：
```csharp
// 显示通知
await ToastService.Show(new ToastOption()
{
    Title = "标题",
    Content = "内容",
    Color = Color.Success
});

// 关闭所有通知
await ToastService.Clear();
```

---

## 最佳实践

1. **使用 ToastService**：推荐通过 `ToastService` 服务来显示通知，而不是直接在页面中使用 `Toast` 组件
2. **合理设置 Duration**：短暂提示设置 3000-5000 毫秒，重要提示设置 0（不自动关闭）
3. **合理使用颜色**：`Success` 用于成功操作，`Info` 用于一般信息，`Warning` 用于注意事项，`Danger` 用于错误
4. **选择合适的 Placement**：系统通知通常使用 `Placement.TopRight`（默认），避免遮挡页面主要内容
5. **提供标题和内容**：`Title` 用于简短标题，`Content` 用于详细描述
6. **与 Message 组件的区别**：`Toast` 是系统级被动提醒（如后台任务完成通知），`Message` 是主动操作后的反馈提示（如表单提交成功）
