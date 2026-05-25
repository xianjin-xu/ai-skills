# Tooltip (工具提示)

## 概述

`Tooltip` 组件用于**在鼠标悬停时显示提示信息**，提供额外的上下文说明。

**主要特性**：
- 支持 4 个方向（Top、Bottom、Left、Right）
- 支持自定义内容
- 支持延迟显示
- 支持 HTML 内容

**在线演示**: https://www.blazor.zone/tooltip

---

## 使用场景

### 1. 基础用法（简单提示）

`Tooltip` 组件可以包裹任何元素，鼠标悬停时显示提示。

```razor
<!-- 基础提示 -->
<Tooltip Text="这是一个提示">
    <Button>悬停查看提示</Button>
</Tooltip>
```

---

### 2. 设置方向（Placement）

通过 `Placement` 参数设置提示显示方向。

```razor
<!-- 上方提示（默认） -->
<Tooltip Text="上方提示" Placement="Placement.Top">
    <Button>上方</Button>
</Tooltip>

<!-- 下方提示 -->
<Tooltip Text="下方提示" Placement="Placement.Bottom">
    <Button>下方</Button>
</Tooltip>

<!-- 左侧提示 -->
<Tooltip Text="左侧提示" Placement="Placement.Left">
    <Button>左侧</Button>
</Tooltip>

<!-- 右侧提示 -->
<Tooltip Text="右侧提示" Placement="Placement.Right">
    <Button>右侧</Button>
</Tooltip>
```

---

### 3. 自定义内容（ChildContent）

通过 `ChildContent` 自定义提示内容（支持 HTML）。

```razor
<!-- 自定义提示内容 -->
<Tooltip>
    <ChildContent>
        <div>
            <strong>自定义提示</strong>
            <p>这是一段<em>富文本</em>提示内容</p>
        </div>
    </ChildContent>
    <ChildElement>
        <Button>悬停查看</Button>
    </ChildElement>
</Tooltip>
```

---

### 4. 延迟显示（Delay）

通过 `Delay` 参数设置延迟显示时间（毫秒）。

```razor
<!-- 延迟 500ms 显示 -->
<Tooltip Text="延迟显示" Delay="500">
    <Button>悬停（延迟 500ms）</Button>
</Tooltip>

<!-- 立即显示 -->
<Tooltip Text="立即显示" Delay="0">
    <Button>悬停（立即显示）</Button>
</Tooltip>
```

---

### 5. 触发方式（Trigger）

通过 `Trigger` 参数设置触发方式。

```razor
<!-- 悬停触发（默认） -->
<Tooltip Text="悬停触发" Trigger="TooltipTrigger.Hover">
    <Button>悬停</Button>
</Tooltip>

<!-- 点击触发 -->
<Tooltip Text="点击触发" Trigger="TooltipTrigger.Click">
    <Button>点击</Button>
</Tooltip>

<!-- 焦点触发 -->
<Tooltip Text="焦点触发" Trigger="TooltipTrigger.Focus">
    <BootstrapInput @bind-Value="@Value" />
</Tooltip>
```

**Trigger 选项**：
- `TooltipTrigger.Hover` - 悬停（默认）
- `TooltipTrigger.Click` - 点击
- `TooltipTrigger.Focus` - 焦点
- `TooltipTrigger.Manual` - 手动

---

## 参数 (Parameters)

### Tooltip 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置提示文本 |
| `Placement` | `Placement` | `Placement.Top` | 获得/设置提示方向 |
| `Delay` | `int` | `0` | 获得/设置延迟显示时间（毫秒） |
| `Trigger` | `TooltipTrigger` | `TooltipTrigger.Hover` | 获得/设置触发方式 |
| `Html` | `bool` | `false` | 获得/设置是否支持 HTML |
| `ChildContent` | `RenderFragment?` | `null` | 提示内容 |
| `ChildElement` | `RenderFragment?` | `null` | 触发元素 |

---

## 最佳实践

1. **简洁明了**：提示文本应简洁明了，避免过长
2. **合理设置方向**：根据页面布局选择合适方向，避免提示被遮挡
3. **避免过度使用**：过多提示会干扰用户，只在必要时使用
4. **延迟显示**：设置 `Delay="500"` 避免快速移动鼠标时频繁显示提示
5. **与 Popover 的区别**：`Tooltip` 是简单文本提示，`Popover` 是丰富内容弹出框
6. **无障碍访问**：确保提示内容对有障碍用户可访问（使用 ARIA 属性）
