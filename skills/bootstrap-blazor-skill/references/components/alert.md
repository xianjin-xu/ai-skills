# Alert (警告框)

## 概述

`Alert` 组件用于在页面中展示重要的提示信息。它是一个**非浮层元素**，不会自动消失，需要用户手动关闭（如果显示关闭按钮）。

**主要特性**：
- 支持 8 种颜色主题（Primary、Secondary、Success、Danger、Warning、Info、Dark、Light）
- 可显示关闭按钮（ShowDismiss）
- 可显示边框效果（ShowBorder）
- 可显示阴影效果（ShowShadow）
- 可显示左侧指示条（ShowBar）

**在线演示**: https://www.blazor.zone/alert

---

## 使用场景

### 1. 基础用法（页面中的非浮层警告框）

警告框是**非浮层元素**，不会自动消失，常用于页面顶部提示重要信息。

```razor
<!-- 主要的警告框 -->
<Alert Color="Color.Primary">
    <Strong>重要提示！</Strong> 请仔细阅读以下内容。
</Alert>

<!-- 成功的警告框 -->
<Alert Color="Color.Success">
    <Strong>操作成功！</Strong> 数据已保存。
</Alert>

<!-- 危险的警告框 -->
<Alert Color="Color.Danger">
    <Strong>错误！</Strong> 无法完成操作。
</Alert>

<!-- 警告的警告框 -->
<Alert Color="Color.Warning">
    <Strong>注意！</Strong> 此操作不可撤销。
</Alert>

<!-- 信息的警告框 -->
<Alert Color="Color.Info">
    <Strong>信息</Strong> 这是一条提示信息。
</Alert>

<!-- 黑暗的警告框 -->
<Alert Color="Color.Dark">
    <Strong>深色主题</Strong> 使用深色背景。
</Alert>
```

---

### 2. 带关闭按钮（ShowDismiss）

提供关闭按钮的警告框，用户点击后警告框消失。

```razor
<!-- 带关闭按钮的警告框 -->
<Alert Color="Color.Primary" ShowDismiss="true">
    <Strong>可关闭的提示</Strong> 点击右侧 X 按钮关闭此警告框。
</Alert>

<Alert Color="Color.Success" ShowDismiss="true">
    <Strong>成功！</Strong> 操作已完成。
</Alert>

<Alert Color="Color.Danger" ShowDismiss="true">
    <Strong>错误！</Strong> 请稍后重试。
</Alert>
```

---

### 3. 带图标（Icon）

通过 `Icon` 参数设置图标，提升可读性。

```razor
<!-- 带图标的警告框 -->
<Alert Color="Color.Primary" Icon="fa fa-info-circle">
    <Strong>信息</Strong> 这是一条带图标的提示。
</Alert>

<Alert Color="Color.Success" Icon="fa fa-check">
    <Strong>成功</Strong> 操作已完成。
</Alert>

<Alert Color="Color.Danger" Icon="fa fa-exclamation-triangle">
    <Strong>危险</Strong> 请立即处理。
</Alert>
```

---

### 4. 边框效果（ShowBorder）

设置 `ShowBorder="true"` 开启边框效果。

```razor
<!-- 带边框的警告框 -->
<Alert Color="Color.Primary" ShowBorder="true">
    <Strong>带边框的提示</Strong> 使用边框突出显示。
</Alert>

<Alert Color="Color.Success" ShowBorder="true">
    <Strong>成功！</Strong> 数据已保存。
</Alert>
```

---

### 5. 阴影效果（ShowShadow）

设置 `ShowShadow="true"` 开启阴影效果。

```razor
<!-- 带阴影的警告框 -->
<Alert Color="Color.Primary" ShowShadow="true">
    <Strong>带阴影的提示</Strong> 使用阴影增加层次感。
</Alert>

<Alert Color="Color.Success" ShowShadow="true">
    <Strong>成功！</Strong> 操作已完成。
</Alert>
```

---

### 6. 显示左侧 Bar（ShowBar）

作为 Tip 使用，显示左侧指示条。

```razor
<!-- 带左侧 Bar 的警告框 -->
<Alert Color="Color.Info" ShowBar="true">
    <Strong>提示</Strong> 这是一条带左侧指示条的提示。
</Alert>

<Alert Color="Color.Success" ShowBar="true">
    <Strong>建议</Strong> 推荐采用此方案。
</Alert>
```

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.None` | 获得/设置警告框颜色主题 |
| `Icon` | `string?` | `null` | 获得/设置显示图标 |
| `ShowBar` | `bool` | `false` | 获得/设置是否显示左侧 Bar |
| `ShowBorder` | `bool` | `false` | 获得/设置是否显示边框 默认 false 不显示 |
| `ShowDismiss` | `bool` | `false` | 获得/设置是否显示关闭按钮 |
| `ShowShadow` | `bool` | `false` | 获得/设置是否显示阴影 默认 false 不显示 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnDismiss` | `Func<Task>?` | 关闭警告框回调方法 |

---

## 最佳实践

1. **非浮层使用**：`Alert` 是页面中的固定元素，不会自动消失，适合展示重要提示
2. **提供关闭按钮**：如果提示信息不需要一直显示，设置 `ShowDismiss="true"` 让用户可关闭
3. **合理使用颜色**：`Primary` 用于一般信息，`Success` 用于成功操作，`Danger` 用于错误，`Warning` 用于注意事项
4. **图标提升可读性**：通过 `Icon` 参数设置图标（如 `fa fa-info-circle`），让用户快速理解提示类型
5. **Bar 作为 Tip**：`ShowBar="true"` 适合用作 Tip 提示，左侧彩条很醒目
6. **避免嵌套在 `Toast` 中**：`Toast` 是浮层通知，`Alert` 是页面元素，不要混用
