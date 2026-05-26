# AnchorLink 锚点链接

## 概述

`AnchorLink` 是一个锚点链接组件，应用于标题带 Hash 的锚点链接，点击可拷贝锚点链接到剪贴板，方便分享。适用于需要在页面中快速定位和分享特定章节的场景。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/anchor-link](https://www.blazor.zone/anchor-link)

## 使用场景

### 1. 普通用法

放置 `AnchorLink` 标签后，点击即可拷贝锚点链接到粘贴板。

```razor
<h2>
    <AnchorLink Id="section1" Text="第一章 介绍" />
    第一章 介绍
</h2>
<p>章节内容...</p>

<h2>
    <AnchorLink Id="section2" Text="第二章 使用方法" />
    第二章 使用方法
</h2>
<p>章节内容...</p>
```

**说明**:
- `Id` 为必填项，不填写时不提供拷贝锚点链接功能
- 点击 `AnchorLink` 图标后，页面 URL 会添加 `#section1` 哈希值，同时链接被复制到剪贴板
- 用户可以通过分享带有哈希值的 URL 直接定位到特定章节

### 2. 自定义图标

组件锚点图标可通过 `Icon` 参数进行自定义，默认为 `fa-solid fa-link`。

```razor
<h2>
    <AnchorLink Id="section1" Text="第一章" Icon="fa-solid fa-hashtag" />
    第一章 介绍
</h2>
```

**说明**:
- 默认图标：`fa-solid fa-link`（链接图标）
- 可自定义为其他 Font Awesome、Bootstrap 或 Material Design 图标
- 例如：`fa-solid fa-hashtag`（井号图标）、`fa-solid fa-chain`（链条图标）

### 3. 自定义提示信息

参数 `TooltipText` 用于设置拷贝地址后的提示信息，默认 `null` 不弹出提示信息。

```razor
<h2>
    <AnchorLink Id="section1" Text="第一章" TooltipText="链接已复制到剪贴板！" />
    第一章 介绍
</h2>
```

**说明**:
- `TooltipText="null"`（默认值）- 不显示提示信息
- `TooltipText="自定义提示"` - 拷贝成功后显示提示信息
- 提示信息以 Tooltip 形式显示在页面上

## 参数

### AnchorLink 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `Icon` | 获得/设置 锚点图标，默认 `fa-solid fa-link` | `string` | `fa-solid fa-link` |
| `Id` | 获得/设置 组件 id 属性（必填项） | `string` | `null` |
| `Text` | 获得/设置 组件 Text 显示文字 | `string` | `null` |
| `TooltipText` | 获得/设置 组件拷贝成功后显示文字 | `string` | `null` |

## 事件回调

AnchorLink 组件暂无事件回调参数。

## 最佳实践

### 1. 确保 Id 参数唯一

`Id` 参数必须为页面中唯一的值，否则锚点定位可能不准确。

```razor
<!-- 推荐：使用有意义的唯一 ID -->
<AnchorLink Id="introduction" Text="介绍" />
<AnchorLink Id="installation" Text="安装" />
<AnchorLink Id="usage" Text="使用方法" />

<!-- 不推荐：ID 重复 -->
<AnchorLink Id="section" Text="介绍" />
<AnchorLink Id="section" Text="安装" />  <!-- ID 重复，锚点定位会出错 -->
```

### 2. 与 Anchor 组件配合使用

`AnchorLink` 通常与 `Anchor` 组件配合使用，`Anchor` 提供导航菜单，`AnchorLink` 提供章节标题的锚点链接。

```razor
<!-- Anchor 组件提供导航 -->
<Anchor Container="content">
    <AnchorLink Id="intro" Text="介绍" />
    <AnchorLink Id="install" Text="安装" />
    <AnchorLink Id="usage" Text="使用方法" />
</Anchor>

<!-- 内容区域 -->
<div id="content" style="height: 500px; overflow-y: auto;">
    <h2><AnchorLink Id="intro" Text="介绍" />介绍</h2>
    <p>内容...</p>
    
    <h2><AnchorLink Id="install" Text="安装" />安装</h2>
    <p>内容...</p>
    
    <h2><AnchorLink Id="usage" Text="使用方法" />使用方法</h2>
    <p>内容...</p>
</div>
```

### 3. 合理设置 TooltipText

根据用户需要决定是否显示提示信息。

```razor
<!-- 场景 1：不需要提示（默认） -->
<AnchorLink Id="section1" Text="章节一" />
<!-- 点击后无提示，链接已复制到剪贴板 -->

<!-- 场景 2：需要提示 -->
<AnchorLink Id="section1" Text="章节一" TooltipText="链接已复制，可直接粘贴分享！" />
<!-- 点击后显示 Tooltip 提示 -->
```

## 常见问题

### 1. 点击 AnchorLink 无反应

**问题**: 点击 `AnchorLink` 图标后，没有任何反应，链接也没有被复制。

**原因**: 可能是 `Id` 参数未设置，或者浏览器不支持 Clipboard API。

**解决方案**:
- 确保已设置 `Id` 参数（必填项）
- 检查浏览器是否支持 Clipboard API（现代浏览器都支持）
- 检查浏览器控制台是否有错误信息

```razor
<!-- 错误示例：缺少 Id -->
<AnchorLink Text="章节一" />  <!-- 无反应 -->

<!-- 正确示例：设置 Id -->
<AnchorLink Id="section1" Text="章节一" />  <!-- 点击后复制链接 -->
```

### 2. 锚点定位不准确

**问题**: 点击导航或分享链接后，页面滚动位置不准确。

**原因**: 可能是 CSS 的 `scroll-padding` 或 `scroll-margin` 设置不当，或者页面有固定头部的偏移。

**解决方案**: 在 CSS 中设置 `scroll-margin-top` 来调整锚点定位的偏移量。

```css
/* 调整锚点定位偏移（如果有固定头部） */
h2 {
    scroll-margin-top: 60px;  /* 固定头部的高度 */
}
```

### 3. Tooltip 不显示

**问题**: 设置了 `TooltipText` 但点击后没有显示提示信息。

**原因**: 可能是 `TooltipText` 值为 `null` 或空字符串。

**解决方案**: 确保 `TooltipText` 有非空值。

```razor
<!-- 错误：TooltipText 为 null -->
<AnchorLink Id="s1" Text="章节" TooltipText="null" />  <!-- 不显示 -->

<!-- 正确：设置提示文字 -->
<AnchorLink Id="s1" Text="章节" TooltipText="链接已复制！" />  <!-- 显示提示 -->
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | AnchorLink 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 TooltipText 参数；优化复制逻辑 |

## 参考链接

- [Bootstrap Blazor 官方文档 - AnchorLink](https://www.blazor.zone/anchor-link)
- [Bootstrap Blazor API - AnchorLink](https://www.blazor.zone/api/AnchorLink)
- [Bootstrap Blazor 官方文档 - Anchor](https://www.blazor.zone/anchor) (配合使用的导航组件)
