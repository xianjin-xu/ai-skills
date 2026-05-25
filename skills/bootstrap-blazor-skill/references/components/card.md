# Card (卡片)

## 概述

`Card` 是一个卡片组件，提供卡片头部、主体、页脚模板，支持颜色、阴影、可折叠等配置。

> Card component!

**分类**: 基础组件  
**在线演示**: [https://www.blazor.zone/card](https://www.blazor.zone/card)

## 使用场景

### 1. 基本用法

```razor
<Card>
    <HeaderTemplate>
        <h5>卡片标题</h5>
    </HeaderTemplate>
    <BodyTemplate>
        <p>卡片内容</p>
        <Button Text="Go somewhere" />
    </BodyTemplate>
</Card>
```

### 2. 卡片颜色

```razor
<Card Color="Color.Primary">
    <HeaderTemplate>
        <h5>Primary 卡片</h5>
    </HeaderTemplate>
    <BodyTemplate>
        <p>卡片内容</p>
    </BodyTemplate>
</Card>
```

### 3. 显示阴影

```razor
<Card IsShadow="true">
    <BodyTemplate>
        <p>带阴影的卡片</p>
    </BodyTemplate>
</Card>
```

### 4. 可折叠

```razor
<Card IsCollapsible="true" Collapsed="false">
    <HeaderTemplate>
        <h5>可折叠卡片</h5>
    </HeaderTemplate>
    <BodyTemplate>
        <p>折叠内容</p>
    </BodyTemplate>
</Card>
```

### 5. 居中内容

```razor
<Card IsCenter="true">
    <BodyTemplate>
        <p>居中内容</p>
    </BodyTemplate>
</Card>
```

### 6. 自定义页脚

```razor
<Card>
    <BodyTemplate>
        <p>卡片内容</p>
    </BodyTemplate>
    <FooterTemplate>
        <small>卡片页脚</small>
    </FooterTemplate>
</Card>
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.None` | 获得/设置卡片颜色 |
| `IsCenter` | `bool` | `false` | 获得/设置是否居中 |
| `IsCollapsible` | `bool` | `false` | 获得/设置是否可折叠 |
| `Collapsed` | `bool` | `false` | 获得/设置是否折叠 |
| `IsShadow` | `bool` | `false` | 获得/设置是否显示阴影 |
| `HeaderPaddingY` | `string?` | `null` | 获得/设置头部高度 padding Y 轴值 |
| `CollapseIcon` | `string?` | `null` | 获得/设置收缩展开箭头图标 |
| `HeaderText` | `string?` | `null` | 获得/设置头部模板显示文本 |
| `HeaderTemplate` | `RenderFragment?` | `null` | 获得/设置头部模板 |
| `BodyTemplate` | `RenderFragment?` | `null` | 获得/设置主体模板 |
| `FooterTemplate` | `RenderFragment?` | `null` | 获得/设置页脚模板 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `CollapsedChanged` | 折叠状态改变时触发 |

## 最佳实践

1. **基本结构**: 使用 `HeaderTemplate`、`BodyTemplate`、`FooterTemplate` 定义卡片内容
2. **颜色设置**: 使用 `Color` 参数设置卡片颜色（如 `Color.Primary`）
3. **阴影效果**: 设置 `IsShadow="true"` 显示阴影效果
4. **折叠功能**: 设置 `IsCollapsible="true"` 启用折叠功能
5. **居中内容**: 设置 `IsCenter="true"` 居中卡片内容
6. **自定义样式**: 使用模板自定义卡片头部、主体、页脚内容

## 常见问题

### Q: 如何创建基本卡片？
A: 使用 `Card` 组件，在 `BodyTemplate` 模板中定义卡片主体内容。

### Q: 如何设置卡片颜色？
A: 使用 `Color` 参数设置颜色，例如 `Color="Color.Primary"`。

### Q: 如何启用折叠功能？
A: 设置 `IsCollapsible="true"` 启用折叠功能，使用 `Collapsed` 控制折叠状态。

### Q: 如何显示阴影？
A: 设置 `IsShadow="true"` 显示卡片阴影效果。

### Q: 如何自定义头部和页脚？
A: 使用 `HeaderTemplate` 和 `FooterTemplate` 模板自定义头部和页脚内容。

## 子组件

`Card` 组件包含以下模板区域：
- `HeaderTemplate` - 头部模板
- `BodyTemplate` - 主体模板
- `FooterTemplate` - 页脚模板
