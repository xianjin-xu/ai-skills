# Popover

## 概述

Popover 弹出窗组件

> Popover Component

**分类**: 反馈
**在线演示**: [https://www.blazor.zone/popover](https://www.blazor.zone/popover)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Content` | `string?` | `}` | 获得/设置 显示文字。复杂内容可通过 <see cref="Template"/> 自定义 |
| `ShowShadow` | `bool` | `true` | 获得/设置 是否显示阴影，默认为 true |
| `Template` | `RenderFragment?` | `}` | 获得/设置 内容模板，默认为 null。设置值后 <see cref="Content"/> 参数失效 |

## 代码示例

### 基本用法

```razor
<Popover Placement="Placement.Auto" Title="@Title" Content="@Content" IsHtml="true" Trigger="click">
        <Button Text="@Localizer["PopoversButtonButtonText"]" />
    </Popover>
```

### 基本用法

```razor
<Popover Placement="Placement.Top" Title="@_templateTitle" Trigger="click">
        <ChildContent>
            <Button Text="@Localizer["PopoversTemplateButtonText"]" />
        </ChildContent>
        <Template>
            <BootstrapInput TValue="string" />
        </Template>
    </Popover>
```

### 基本用法

```razor
<Popover Placement="Placement.Auto" Title="@Title" Content="@Content" IsHtml="true" Trigger="click" CustomClass="custom-popover">
        <Button Text="@Localizer["PopoversCssClassButtonText"]" />
    </Popover>
```

### 基本用法

```razor
<Popover Title="@Title" Content="@Content" IsHtml="true" Trigger="manual" @ref="_popover">
        <i class="fa-solid fa-flag" style="cursor: pointer;"></i>
    </Popover>
```
