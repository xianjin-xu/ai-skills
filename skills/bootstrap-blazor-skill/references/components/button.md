# Button (按钮)

## 概述

`Button` 组件是 Bootstrap Blazor 中最常用的操作按钮组件。支持多种颜色主题、尺寸、风格（Outline、Block）、异步请求、禁用状态等。

**主要特性**：
- 支持 8 种颜色主题（Primary、Secondary、Success、Danger、Warning、Info、Dark、Light）
- 支持 3 种风格（Normal、Outline、Link）
- 支持 6 种尺寸（ExtraSmall、Small、Medium、Large、ExtraLarge、Block）
- 支持异步请求按钮（IsAsync）
- 支持按钮禁用状态（IsDisabled）
- 支持工具提示栏（TooltipText、TooltipPlacement）

**在线演示**: https://www.blazor.zone/button

---

## 使用场景

### 1. 基础用法（基础按钮样式）

基础的按钮用法，支持 8 种颜色主题。

```razor
<!-- 主要按钮 -->
<Button Color="Color.Primary">主要按钮</Button>

<!-- 次要按钮 -->
<Button Color="Color.Secondary">次要按钮</Button>

<!-- 成功按钮 -->
<Button Color="Color.Success">成功按钮</Button>

<!-- 危险按钮 -->
<Button Color="Color.Danger">危险按钮</Button>

<!-- 警告按钮 -->
<Button Color="Color.Warning">警告按钮</Button>

<!-- 信息按钮 -->
<Button Color="Color.Info">信息按钮</Button>

<!-- 黑暗按钮 -->
<Button Color="Color.Dark">黑暗按钮</Button>

<!-- 光亮按钮 -->
<Button Color="Color.Light">光亮按钮</Button>
```

---

### 2. 不同风格（ButtonStyle）

通过设置 `ButtonStyle` 来显示不同的按钮风格。

```razor
<!-- Outline 风格 -->
<Button Color="Color.Primary" ButtonStyle="ButtonStyle.Outline">主要按钮</Button>
<Button Color="Color.Secondary" ButtonStyle="ButtonStyle.Outline">次要按钮</Button>
<Button Color="Color.Success" ButtonStyle="ButtonStyle.Outline">成功按钮</Button>
<Button Color="Color.Danger" ButtonStyle="ButtonStyle.Outline">危险按钮</Button>
<Button Color="Color.Warning" ButtonStyle="ButtonStyle.Outline">警告按钮</Button>

<!-- Link 风格 -->
<Button Color="Color.Primary" ButtonStyle="ButtonStyle.Link">链接按钮</Button>
<Button Color="Color.Secondary" ButtonStyle="ButtonStyle.Link">链接按钮</Button>
```

---

### 3. 不同尺寸（Size）

Button 组件提供除了默认值以外的多种尺寸，通过设置 `Size` 属性可以在不同场景下选择合适的按钮尺寸。

```razor
<!-- 超小按钮 -->
<Button Color="Color.Primary" Size="Size.ExtraSmall">超小按钮</Button>

<!-- 小按钮 -->
<Button Color="Color.Primary" Size="Size.Small">小按钮</Button>

<!-- 正常按钮 -->
<Button Color="Color.Primary" Size="Size.Medium">正常按钮</Button>

<!-- 大按钮 -->
<Button Color="Color.Primary" Size="Size.Large">大按钮</Button>

<!-- 超大按钮 -->
<Button Color="Color.Primary" Size="Size.ExtraLarge">超大按钮</Button>

<!-- Block 按钮（占满宽度） -->
<Button Color="Color.Primary" Size="Size.Block">Block 按钮</Button>
```

---

### 4. 禁用状态（IsDisabled）

按钮不可用状态。通过设置 `IsDisabled` 属性。

```razor
<!-- 禁用状态的按钮 -->
<Button Color="Color.Primary" IsDisabled="true">禁用按钮</Button>
<Button Color="Color.Secondary" IsDisabled="true">禁用按钮</Button>
<Button Color="Color.Success" IsDisabled="true">禁用按钮</Button>
<Button Color="Color.Danger" IsDisabled="true">禁用按钮</Button>
```

**性能提示**：
- 使用 `IsDisabled` 属性设置时，需要显式手动调用 `StateHasChanged` 方法，会导致按钮所在组件整体刷新
- 建议使用**实例方法 `SetDisable`** 仅对按钮进行刷新，性能更好

```razor
<!-- 通过 OnClick 回调方法中设置自身 IsDisabled 属性 -->
<Button Color="Color.Primary" OnClick="@(e => OnDisableButton(e))">
    点击禁用我
</Button>

@code {
    private void OnDisableButton(MouseEventArgs e)
    {
        // 使用实例方法 SetDisable 仅刷新按钮，性能更好
        // buttonRef.SetDisable(true);
    }
    
    private ElementReference buttonRef;
}
```

---

### 5. 异步请求按钮（IsAsync）

通过设置 `IsAsync` 属性按钮是否为异步请求按钮，默认为 false。

当按钮为异步请求按钮时，点击按钮后**自身状态会改变为禁用状态**，同时显示 Loading 小图标，异步请求结束后恢复正常。

```razor
<!-- 异步请求按钮 -->
<Button Color="Color.Primary" IsAsync="true" OnClick="OnAsyncClick">
    异步请求
</Button>

@code {
    private async Task OnAsyncClick()
    {
        // 模拟异步请求（5秒）
        await Task.Delay(5000);
        
        // 异步请求结束后，按钮自动恢复正常状态
        // 如果需要保持禁用状态，设置 IsKeepDisabled="true"
    }
}
```

**特殊场景**：异步后需要按钮**继续保持禁用状态**，请通过 `IsKeepDisabled` 参数控制：

```razor
<Button Color="Color.Primary" 
        IsAsync="true" 
        IsKeepDisabled="true"
        OnClick="OnAsyncClickKeepDisabled">
    异步后保持禁用
</Button>
```

---

### 6. 带图标的按钮（Icon）

通过设置 `Icon` 属性对按钮图标进行设置，图标为字体字符串（如使用 font-awesome 图标时 `fa-solid fa-font-awesome`）。

```razor
<!-- 带图标的按钮 -->
<Button Color="Color.Primary" Icon="fa-solid fa-check">确认</Button>
<Button Color="Color.Success" Icon="fa-solid fa-save">保存</Button>
<Button Color="Color.Danger" Icon="fa-solid fa-trash">删除</Button>
<Button Color="Color.Warning" Icon="fa-solid fa-exclamation-triangle">警告</Button>
```

---

### 7. 按钮提示栏（TooltipText）

通过设置 `TooltipText`、`TooltipPlacement`、`TooltipTrigger` 快捷设置按钮提示栏信息、位置、触发方式。

```razor
<!-- 带提示的按钮 -->
<Button Color="Color.Primary" 
        TooltipText="点击此按钮保存数据" 
        TooltipPlacement="Placement.Top">
    保存
</Button>

<!-- 禁用按钮的提示仍然可用 -->
<Button Color="Color.Secondary" 
        IsDisabled="true"
        TooltipText="按钮已禁用">
    不可用
</Button>
```

---

### 8. 状态切换按钮（Toggle）

通过设置 `IsActiveChanged` 或者 `OnToggleAsync` 回调方法获得当前按钮 Toggle 状态。

```razor
<!-- Toggle 按钮 -->
<Button Color="Color.Primary" 
        IsActive="isActive"
        OnToggleAsync="OnToggle">
    Toggle: @isActive
</Button>

@code {
    private bool isActive = false;
    
    private Task OnToggle()
    {
        isActive = !isActive;
        return Task.CompletedTask;
    }
}
```

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.Primary` | 获得/设置按钮颜色 |
| `ButtonStyle` | `ButtonStyle` | `ButtonStyle.Normal` | 获得/设置按钮风格枚举（Normal/Outline/Link） |
| `ButtonType` | `ButtonType` | `ButtonType.Button` | 获得/设置按钮类型（Submit/Reset/Button） |
| `Size` | `Size` | `Size.Medium` | 获得/设置按钮尺寸 |
| `Icon` | `string?` | `null` | 获得/设置显示图标 |
| `Text` | `string?` | `null` | 获得/设置显示文字 |
| `IsAsync` | `bool` | `false` | 获得/设置是否为异步按钮，点击后禁用自身并显示 loading |
| `IsAutoFocus` | `bool` | `false` | 获得/设置是否自动获取焦点 |
| `IsBlock` | `bool` | `false` | 获得/设置 Block 模式 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用，默认为 false |
| `IsKeepDisabled` | `bool` | `false` | 获得/设置是否异步结束后是否保持禁用状态 |
| `IsOutline` | `bool` | `false` | 获得/设置 Outline 样式，默认 false |
| `LoadingIcon` | `string?` | `fa-solid fa-spinner` | 获得/设置正在加载动画图标 |
| `TooltipText` | `string?` | `null` | 获得/设置 Tooltip 显示文字，默认为 null |
| `TooltipPlacement` | `Placement` | `Placement.Top` | 获得/设置 Tooltip 显示位置，默认为 Top |
| `TooltipTrigger` | `string?` | `hover focus` | 获得/设置 Tooltip 触发方式 |
| `StopPropagation` | `bool` | `false` | 获得/设置点击事件是否向上传播，默认 false |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnClick` | `EventCallback<MouseEventArgs>` | 获得/设置 OnClick 事件 |
| `OnClickWithoutRender` | `EventCallback<Task>` | 获得/设置 OnClick 事件不刷新父组件 |

---

## 最佳实践

1. **性能优化**：禁用按钮时，优先使用**实例方法 `SetDisable(true)`** 而不是 `IsDisabled="true"` 属性，避免整个父组件刷新
2. **异步按钮**：使用 `IsAsync="true"` 时，按钮会自动显示 loading 状态，无需手动控制
3. **保持禁用状态**：异步请求后需要保持按钮禁用，设置 `IsKeepDisabled="true"`
4. **图标使用**：通过 `Icon` 属性设置 FontAwesome 图标（如 `fa-solid fa-check`），提升按钮可识别性
5. **Tooltip 设置**：为按钮添加 `TooltipText`，让用户理解按钮功能，提升用户体验
6. **Outline 风格**：在需要**次要操作**或**多个按钮并列**时，使用 `ButtonStyle="Outline"` 降低视觉权重
7. **Size 选择**：在**表单内**使用 `Size.Medium`（默认），在**工具栏**使用 `Size.Small`，在**主要操作区**使用 `Size.Large`
