# Skeleton 骨架屏

## 概述

Skeleton 骨架屏组件在需要等待加载内容的位置提供一个占位图形组合。适用于网络较慢需要长时间等待加载处理的情况、图文信息内容较多的列表/卡片中、只在第一次加载数据的时候使用。

> Skeleton component provides a placeholder graphic combination at the position where content needs to be loaded. Suitable for slow network conditions, content-rich lists/cards, and first-time data loading.

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/skeleton](https://www.blazor.zone/skeleton)

---

## 何时使用

- 网络较慢，需要长时间等待加载处理的情况下
- 图文信息内容较多的列表/卡片中
- 只在第一次加载数据的时候使用
- 可以被 Spin 完全代替，但是在可用的场景下可以比 Spin 提供更好的视觉效果和用户体验

---

## 使用场景

### 1. 图片骨架屏

适用于头像、图片等类型加载时显示。通过设置 `Circle` 属性可以设置为圆形显示。

```razor
<!-- 矩形图片骨架屏 -->
<SkeletonAvatar />

<!-- 圆形图片骨架屏 -->
<SkeletonAvatar Circle="true" />
```

### 2. 段落骨架屏

适用于大段文字等类型加载时显示。默认段落骨架屏仅显示三行，如果需要多行占位，请放置多个 `SkeletonParagraph` 即可。

```razor
<!-- 段落骨架屏 -->
<SkeletonParagraph />

<!-- 多个段落骨架屏 -->
<SkeletonParagraph />
<SkeletonParagraph />
<SkeletonParagraph />
```

### 3. 表单骨架屏

适用于编辑表单加载时显示。

```razor
<EditForm Model="Model">
    <SkeletonEditor />
</EditForm>
```

### 4. 表格骨架屏

适用于编辑表格加载时显示。

```razor
<SkeletonTable Rows="7" Columns="3" ShowToolbar="true" />
```

### 5. 树骨架屏

适用于树组件加载时显示。

```razor
<SkeletonTable Rows="5" Columns="1" />
```

### 6. 组合使用

在实际使用中，通常会组合使用多个骨架屏组件。

```razor
<div class="skeleton-demo">
    <div class="row">
        <div class="col-2">
            <SkeletonAvatar Circle="true" />
        </div>
        <div class="col-10">
            <SkeletonParagraph />
        </div>
    </div>
</div>
```

### 7. 控制加载状态

通过 `Active` 参数控制是否显示动画效果。

```razor
<SkeletonAvatar Active="true" />
<SkeletonParagraph Active="true" />
```

### 8. 圆角控制

通过 `Round` 参数控制是否显示圆角，默认为 `true`。

```razor
<SkeletonAvatar Round="false" />
<SkeletonParagraph Round="false" />
```

---

## 参数 (Parameters)

### SkeletonAvatar 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Active` | `bool` | `true` | 获得/设置 是否显示动画 |
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `Circle` | `bool` | `false` | 获得/设置 是否为圆形 |
| `Round` | `bool` | `true` | 获得/设置 是否圆角 |

### SkeletonParagraph 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Active` | `bool` | `true` | 获得/设置 是否显示动画 |
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `Round` | `bool` | `true` | 获得/设置 是否圆角 |

### SkeletonEditor 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Active` | `bool` | `true` | 获得/设置 是否显示动画 |
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `Round` | `bool` | `true` | 获得/设置 是否圆角 |

### SkeletonTable 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Active` | `bool` | `true` | 获得/设置 是否显示动画 |
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `Columns` | `int` | `3` | 获得/设置 列数 |
| `Round` | `bool` | `true` | 获得/设置 是否圆角 |
| `Rows` | `int` | `7` | 获得/设置 行数 |
| `ShowToolbar` | `bool` | `false` | 获得/设置 是否显示工具栏 |

---

## 最佳实践

### 1. 加载状态管理

在实际应用中，通常通过加载状态控制骨架屏的显示与隐藏。

```razor
@if (IsLoading)
{
    <SkeletonAvatar Circle="true" />
    <SkeletonParagraph />
}
else
{
    <div class="user-info">
        <img src="avatar.jpg" class="avatar" />
        <div class="user-name">@UserName</div>
        <div class="user-desc">@UserDescription</div>
    </div>
}

@code {
    private bool IsLoading { get; set; } = true;
    private string? UserName { get; set; }
    private string? UserDescription { get; set; }

    protected override async Task OnInitializedAsync()
    {
        await Task.Delay(2000); // 模拟加载
        UserName = "张三";
        UserDescription = "这是用户描述";
        IsLoading = false;
    }
}
```

### 2. 组合使用

根据实际界面布局，组合使用不同的骨架屏组件。

```razor
<div class="card">
    <div class="card-body">
        @if (IsLoading)
        {
            <div class="row">
                <div class="col-3">
                    <SkeletonAvatar Circle="true" />
                </div>
                <div class="col-9">
                    <SkeletonParagraph />
                </div>
            </div>
        }
        else
        {
            <div class="row">
                <div class="col-3">
                    <img src="avatar.jpg" class="rounded-circle" width="60" />
                </div>
                <div class="col-9">
                    <h5>@UserName</h5>
                    <p>@UserDescription</p>
                </div>
            </div>
        }
    </div>
</div>
```

### 3. 动画效果

默认情况下骨架屏显示动画效果（`Active="true"`），加载完成后隐藏。

---

## 常见问题 (FAQ)

### Q1: 如何控制骨架屏的显示与隐藏？

**A**: 通过加载状态变量控制骨架屏与真实内容的切换。

```razor
@if (IsLoading)
{
    <SkeletonTable Rows="5" Columns="3" />
}
else
{
    <Table Items="Data" />
}
```

### Q2: 如何自定义骨架屏样式？

**A**: 通过 CSS 自定义骨架屏样式，或通过设置 `AdditionalAttributes` 添加自定义属性。

### Q3: 骨架屏和 Spin 有什么区别？

**A**: Spin 是简单的加载指示器，骨架屏是内容占位符。骨架屏提供更好的视觉效果和用户体验，特别是在内容结构已知的情况下。

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 Skeleton 组件 |
| 8.0 | 新增 `SkeletonTable` 组件 |
