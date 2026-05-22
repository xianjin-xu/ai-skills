# Divider

## 概述

Divider 组件

> Divider Component

**分类**: 基础组件
**在线演示**: [https://www.blazor.zone/divider](https://www.blazor.zone/divider)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsVertical` | `bool` | `}` | 获得/设置 是否为垂直显示 默认为 false |
| `Alignment` | `Alignment` | `Alignment.Center` | 获得/设置 组件对齐方式 默认为居中 |
| `Text` | `string?` | `}` | 获得/设置 文案显示文字 |
| `Icon` | `string?` | `}` | 获得/设置 文案显示图标 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子内容 |

## 代码示例

### 基本用法

```razor
<Divider IsVertical="true" />
        <span>@Localizer["VerticalContent2"]</span>
        <Divider IsVertical="true" />
        <span>@Localizer["VerticalContent3"]</span>
    </div>
    <Divider Text="@Localizer["VerticalDivider"]" />
    <div class="d-flex" style="height: 100px;">
        <div class="border border-primary" style="width:100px; height:100%;"></div>
        <Divider IsVertical="true" Alignment="Alignment.Left" />
        <div class="border border-success" style="width:100px; height:100%;"></div>
        <Divider IsVertical="true"></Divider>
```

### 基本用法

```razor
<Divider>
        <div class="text-danger">@((MarkupString)Localizer["DividerChildContent"].Value)</div>
    </Divider>
```
