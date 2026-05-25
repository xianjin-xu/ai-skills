# Popover 弹出窗组件

## 概述

Popover 弹出窗组件用于点击/鼠标移入元素，弹出气泡式的卡片浮层。Placement 设置弹出框的位置，二次点击时关闭弹出框。

> Popover component is used to click/hover over an element to pop up a bubble-style card overlay.

**分类**: 通知组件  
**在线演示**: [https://www.blazor.zone/popover](https://www.blazor.zone/popover)

---

## 使用场景

### 1. 基础用法

点击文本输入框弹出 Popover 弹出框，Placement 设置弹出框的位置，二次点击时关闭弹出框。

```razor
<Popover Placement="Placement.Bottom" Title="提示" Content="这是弹出窗内容">
    <Button Text="点击弹出" />
</Popover>

<Popover Placement="Placement.Top" Title="提示" Content="这是弹出窗内容">
    <Button Text="上方弹出" />
</Popover>

<Popover Placement="Placement.Left" Title="提示" Content="这是弹出窗内容">
    <Button Text="左侧弹出" />
</Popover>

<Popover Placement="Placement.Right" Title="提示" Content="这是弹出窗内容">
    <Button Text="右侧弹出" />
</Popover>
```

### 2. 按钮激活弹出框

点击按钮后弹出 Popover 弹出框。

```razor
<Popover Placement="Placement.Bottom" Title="提示" Content="点击按钮后弹出">
    <Button Text="按钮激活/关闭" OnClick="OnButtonClick" />
</Popover>

@code {
    private async Task OnButtonClick()
    {
        await Task.CompletedTask;
    }
}
```

### 3. 自定义模板

通过设置 `Template` 模板，自定义弹窗内容。

```razor
<Popover Placement="Placement.Bottom" Title="自定义内容">
    <Template>
        <div class="p-3">
            <h5>自定义模板</h5>
            <p>这里可以放置任意内容</p>
            <Button Text="确定" Color="Color.Primary" />
        </div>
    </Template>
    <Button Text="自定义模板" />
</Popover>
```

### 4. 自定义样式

通过设置 Popover 参数 `CustomClass` 对弹窗进行自定义样式。

```razor
<Popover Placement="Placement.Bottom" 
         Title="自定义样式" 
         Content="设置 CssClass 进行自定义样式"
         CustomClass="custom-popover">
    <Button Text="自定义样式按钮" />
</Popover>

<style>
    .custom-popover {
        --bs-popover-border-color: var(--bs-primary);
        --bs-popover-header-bg: var(--bs-primary);
        --bs-popover-header-color: var(--bs-white);
        --bs-popover-body-padding-x: 1rem;
        --bs-popover-body-padding-y: 1rem;
    }
</style>
```

### 5. 手动控制状态

通过设置 `Trigger="manual"` 使用代码控制提示栏状态。子组件使用级联参数得到 Popover 实例，然后调用其相应方法 Show、Hide、Toggle。通过 `@ref` 获得 Popover 实例调用其对应方法。

```razor
<Popover Placement="Placement.Bottom" 
         Title="手动控制" 
         Content="通过代码控制"
         Trigger="manual"
         @ref="PopoverInstance">
    <Button Text="显示" OnClick="OnShow" />
    <Button Text="隐藏" OnClick="OnHide" />
    <Button Text="切换" OnClick="OnToggle" />
</Popover>

@code {
    private Popover? PopoverInstance { get; set; }
    
    private async Task OnShow()
    {
        if (PopoverInstance != null)
        {
            await PopoverInstance.Show();
        }
    }
    
    private async Task OnHide()
    {
        if (PopoverInstance != null)
        {
            await PopoverInstance.Hide();
        }
    }
    
    private async Task OnToggle()
    {
        if (PopoverInstance != null)
        {
            await PopoverInstance.Toggle();
        }
    }
}
```

### 6. Trigger 触发方式

通过设置 `Trigger` 参数控制弹出框的触发方式，可选值为 `click`、`hover`、`focus`、`manual`。

```razor
<Popover Placement="Placement.Bottom" Title="点击触发" Content="点击触发" Trigger="click">
    <Button Text="点击触发" />
</Popover>

<Popover Placement="Placement.Bottom" Title="悬停触发" Content="悬停触发" Trigger="hover">
    <Button Text="悬停触发" />
</Popover>

<Popover Placement="Placement.Bottom" Title="焦点触发" Content="焦点触发" Trigger="focus">
    <Button Text="焦点触发" />
</Popover>

<Popover Placement="Placement.Bottom" Title="手动触发" Content="手动触发" Trigger="manual">
    <Button Text="手动触发" />
</Popover>
```

---

## 参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| AdditionalAttributes | 获得/设置 用户自定义属性 | IDictionary<string, Object> | — |
| ChildContent | 获得/设置 子组件 | RenderFragment | — |
| Content | 获得/设置 显示文字。复杂内容可通过 自定义 | string | — |
| CustomClass | 获得/设置 自定义样式 | string | — |
| Delay | 获得/设置 延迟显示时间（毫秒） | string | — |
| FallbackPlacements | 获得/设置 位置，默认为 null | String[] | null |
| GetTitleCallback | 获得/设置 获取显示内容的异步回调方法，默认 null | Func<Task<string>> | null |
| Id | 获得/设置 组件 id 属性 | string | — |
| IsHtml | 获得/设置 是否解析 HTML 内容 | bool | — |
| Offset | 获得/设置 偏移量，默认为 null | string | null |
| Placement | 获得/设置 弹出位置 | Placement | — |
| Sanitize | 获得/设置 是否对内容进行消毒处理 | bool | — |
| Selector | 获得/设置 选择器 | string | — |
| ShowShadow | 获得/设置 是否显示阴影，默认为 true | bool | true |
| Template | 获得/设置 内容模板，默认为 null。设置值后 Content 参数失效 | RenderFragment | null |
| Title | 获得/设置 标题 | string | — |
| Trigger | 获得/设置 触发方式 | string | click |

---

## 方法

| 方法名称 | 说明 | 参数 |
|---------|------|------|
| Show | 显示弹出框 | — |
| Hide | 隐藏弹出框 | — |
| Toggle | 切换弹出框显示状态 | — |

---

## 最佳实践

### 与按钮配合使用

Popover 通常与按钮配合使用，提供额外的信息或操作：

```razor
<Popover Placement="Placement.Top" 
         Title="操作确认" 
         Content="确定要执行此操作吗？">
    <Button Text="执行操作" Color="Color.Warning" />
</Popover>
```

### 通过代码控制显示

使用 `@ref` 获取 Popover 实例，通过代码控制显示/隐藏：

```razor
<Popover @ref="MyPopover" 
         Placement="Placement.Bottom" 
         Title="提示" 
         Content="通过代码控制">
    <ChildContent>
        <Button Text="显示弹窗" OnClick="ShowPopover" />
    </ChildContent>
</Popover>

@code {
    private Popover? MyPopover { get; set; }
    
    private async Task ShowPopover()
    {
        if (MyPopover != null)
        {
            await MyPopover.Show();
        }
    }
}
```

---

## 常见问题

### 1. 如何自定义弹出内容？

使用 `Template` 参数可以自定义弹出框的内容，实现复杂的布局和交互。

### 2. 如何控制弹出框位置？

通过 `Placement` 参数控制弹出框位置，可选值为 `Top`、`Bottom`、`Left`、`Right`。

### 3. 如何通过代码控制弹出框？

使用 `@ref` 获取 Popover 实例，然后调用 `Show()`、`Hide()`、`Toggle()` 方法。

### 4. 如何设置触发方式？

通过 `Trigger` 参数设置触发方式，可选值为 `click`、`hover`、`focus`、`manual`（手动控制）。

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | Popover 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/popover)
- [PopConfirm 组件文档](https://www.blazor.zone/popconfirm)
- [Tooltip 组件文档](https://www.blazor.zone/tooltip)
