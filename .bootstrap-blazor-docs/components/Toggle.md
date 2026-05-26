# Toggle (开关)

## 概述

`Toggle` 组件用于**在两种状态之间切换**，类似于 `Switch` 组件，但外观和交互可能不同。

**主要特性**：
- 支持开/关两种状态
- 可显示文本（OnText、OffText）
- 可设置颜色（Color）
- 支持只读（Readonly）
- 支持禁用（Disabled）
- 支持不同尺寸（Size）

**在线演示**: https://www.blazor.zone/toggle

---

## 使用场景

### 1. 基础用法（开关切换）

`Toggle` 组件可以通过 `@bind-Value` 绑定开关状态。

```razor
<!-- 基础开关 -->
<Toggle @bind-Value="IsToggled" />

<p>开关状态: @IsToggled</p>

@code {
    private bool IsToggled { get; set; }
}
```

---

### 2. 显示文本（OnText、OffText）

通过 `OnText` 和 `OffText` 参数设置开关显示的文本。

```razor
<!-- 带文本的开关 -->
<Toggle @bind-Value="IsToggled" OnText="开" OffText="关" />

@code {
    private bool IsToggled { get; set; }
}
```

---

### 3. 设置颜色（Color）

通过 `Color` 参数设置开关颜色。

```razor
<!-- 主要颜色开关 -->
<Toggle @bind-Value="IsToggled" Color="Color.Primary" />

<!-- 成功颜色开关 -->
<Toggle @bind-Value="IsToggled" Color="Color.Success" />

<!-- 危险颜色开关 -->
<Toggle @bind-Value="IsToggled" Color="Color.Danger" />

@code {
    private bool IsToggled { get; set; }
}
```

---

### 4. 只读模式（Readonly）

通过设置 `Readonly="true"` 使开关只读。

```razor
<!-- 只读开关 -->
<Toggle @bind-Value="IsToggled" Readonly="true" />

@code {
    private bool IsToggled { get; set; } = true;
}
```

---

### 5. 禁用状态（Disabled）

通过设置 `Disabled="true"` 禁用开关。

```razor
<!-- 禁用开关 -->
<Toggle @bind-Value="IsToggled" Disabled="true" />

@code {
    private bool IsToggled { get; set; } = true;
}
```

---

### 6. 不同尺寸（Size）

通过 `Size` 参数设置开关尺寸。

```razor
<!-- 小尺寸开关 -->
<Toggle @bind-Value="IsToggled" Size="Size.Small" />

<!-- 中尺寸开关（默认） -->
<Toggle @bind-Value="IsToggled" Size="Size.Medium" />

<!-- 大尺寸开关 -->
<Toggle @bind-Value="IsToggled" Size="Size.Large" />

@code {
    private bool IsToggled { get; set; }
}
```

---

## 参数 (Parameters)

### Toggle 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `bool` | `false` | 获得/设置开关状态 |
| `OnText` | `string?` | `null` | 获得/设置开状态文本 |
| `OffText` | `string?` | `null` | 获得/设置关状态文本 |
| `Color` | `Color` | `Color.Primary` | 获得/设置开关颜色 |
| `Size` | `Size` | `Size.Medium` | 获得/设置开关尺寸 |
| `Readonly` | `bool` | `false` | 获得/设置是否只读 |
| `Disabled` | `bool` | `false` | 获得/设置是否禁用 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<bool>` | 开关状态变化回调 |

---

## 最佳实践

1. **使用 @bind-Value 双向绑定**：推荐使用 `@bind-Value` 实现双向绑定，简化代码
2. **提供明确的文本**：通过 `OnText` 和 `OffText` 提供明确的开/关文本，提升用户体验
3. **合理使用颜色**：`Primary` 用于一般开关，`Success` 用于启用状态，`Danger` 用于危险操作
4. **处理 ValueChanged 事件**：对于需要在开关状态变化时执行逻辑的场景，处理 `ValueChanged` 事件
5. **与 Switch 组件的区别**：`Toggle` 和 `Switch` 都是开关组件，但外观和交互可能不同，根据具体设计选择
6. **避免频繁切换**：对于需要确认的操作，在 `ValueChanged` 事件中先确认再更新状态，避免误操作
