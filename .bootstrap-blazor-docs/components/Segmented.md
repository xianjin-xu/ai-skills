# Segmented 分段控制器

## 概述

`Segmented` 是一个分段控制器组件，用于展示多个选项并允许用户选择其中单个选项。常用于在多个互斥选项之间进行切换，如时间维度切换（日/周/月/季/年）或视图模式切换。

**命名空间**: `BootstrapBlazor.Components`

**泛型参数**: `TValue` - 选项值类型

## 使用场景

### 1. 基本用法

通过 `Items` 参数设置组件数据源，最简单的用法是直接绑定选项集合。

```razor
<Segmented TValue="string" Items="Items" Value="Value" ValueChanged="OnValueChanged" />

@code {
    [NotNull]
    private IEnumerable<SegmentedOption<string>>? Items { get; set; }

    private string Value { get; set; } = "";

    private Task OnValueChanged(string value)
    {
        Value = value;
        StateHasChanged();
        return Task.CompletedTask;
    }

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "Daily", Value = "Daily" },
            new SegmentedOption<string> { Text = "Weekly", Value = "Weekly" },
            new SegmentedOption<string> { Text = "Monthly", Value = "Monthly" },
            new SegmentedOption<string> { Text = "Quarterly", Value = "Quarterly" },
            new SegmentedOption<string> { Text = "Yearly", Value = "Yearly" }
        };
    }
}
```

### 2. 不可用状态

通过 `IsDisabled` 参数或选项级别的 `Disabled` 属性，可以禁用整个组件或单个选项。

```razor
<Segmented TValue="string" Items="Items" Value="Value" IsDisabled="false" />

@code {
    [NotNull]
    private IEnumerable<SegmentedOption<string>>? Items { get; set; }

    private string Value { get; set; } = "1";

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "123", Value = "1" },
            new SegmentedOption<string> { Text = "456", Value = "2" },
            new SegmentedOption<string> { Text = "789", Value = "3", Disabled = true },
            new SegmentedOption<string> { Text = "long-text-long-text-long-text", Value = "4" }
        };
    }
}
```

**说明**:
- 设置 `IsDisabled="true"` 禁用整个组件
- 设置选项的 `Disabled = true` 禁用单个选项（该选项不可点击）

### 3. Block 充满父容器

通过 `IsBlock` 参数可将组件充满父容器，适用于需要组件宽度占满可用空间的场景。

```razor
<div style="width: 500px; border: 1px solid #ccc; padding: 10px;">
    <Segmented TValue="string" Items="Items" Value="Value" IsBlock="true" />
</div>

@code {
    [NotNull]
    private IEnumerable<SegmentedOption<string>>? Items { get; set; }

    private string Value { get; set; } = "Daily";

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "Daily", Value = "Daily" },
            new SegmentedOption<string> { Text = "Weekly", Value = "Weekly" },
            new SegmentedOption<string> { Text = "Monthly", Value = "Monthly" },
            new SegmentedOption<string> { Text = "Quarterly", Value = "Quarterly" },
            new SegmentedOption<string> { Text = "Yearly", Value = "Yearly" }
        };
    }
}
```

**说明**:
- `IsBlock="true"` 时组件宽度充满父容器
- 适用于响应式布局或需要组件占满整行的场景

### 4. 自定义渲染

使用 `ItemTemplate` 参数自定义选项的渲染模板，可以实现复杂的选项展示效果。

```razor
<Segmented TValue="string" Items="Items" Value="Value" ItemTemplate="ItemTemplate" />

@code {
    [NotNull]
    private IEnumerable<SegmentedOption<string>>? Items { get; set; }

    private string Value { get; set; } = "1";

    private RenderFragment<SegmentedOption<string>> ItemTemplate => item => builder =>
    {
        builder.OpenElement(0, "div");
        builder.AddContent(1, item.Text);
        builder.CloseElement();
    };

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "123", Value = "1" },
            new SegmentedOption<string> { Text = "456", Value = "2" },
            new SegmentedOption<string> { Text = "789", Value = "3" }
        };
    }
}
```

**说明**:
- `ItemTemplate` 是 `RenderFragment<SegmentedOption<TValue>>` 类型
- 可以完全自定义选项的 HTML 结构和样式
- 适用于需要显示图标、徽章或其他复杂内容的场景

### 5. 图标

通过设置选项的 `Icon` 参数，可以在选项中显示图标。

```razor
<Segmented TValue="string" Items="Items" Value="Value" />

@code {
    [NotNull]
    private IEnumerable<SegmentedOption<string>>? Items { get; set; }

    private string Value { get; set; } = "List";

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "List", Value = "List", Icon = "fa-solid fa-list" },
            new SegmentedOption<string> { Text = "Chart", Value = "Chart", Icon = "fa-solid fa-chart-bar" }
        };
    }
}
```

**说明**:
- 使用 `Icon` 属性为选项添加图标（支持 Font Awesome、Bootstrap、Material Design 图标）
- 图标显示在选项文本左侧
- 适用于需要增强视觉识别的场景

### 6. 大小

组件定义了三种尺寸（大、默认、小），高度分别为 40px、32px 和 24px。通过 `Size` 参数控制组件大小。

```razor
<Segmented TValue="string" Items="Items" Value="Value" Size="Size.Large" />
<br />
<Segmented TValue="string" Items="Items" Value="Value" Size="Size.Medium" />
<br />
<Segmented TValue="string" Items="Items" Value="Value" Size="Size.Small" />

@code {
    [NotNull]
    private IEnumerable<SegmentedOption<string>>? Items { get; set; }

    private string Value { get; set; } = "Daily";

    protected override void OnInitialized()
    {
        base.OnInitialized();
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "Daily", Value = "Daily" },
            new SegmentedOption<string> { Text = "Weekly", Value = "Weekly" },
            new SegmentedOption<string> { Text = "Monthly", Value = "Monthly" },
            new SegmentedOption<string> { Text = "Quarterly", Value = "Quarterly" },
            new SegmentedOption<string> { Text = "Yearly", Value = "Yearly" }
        };
    }
}
```

**说明**:
- `Size.Large` - 大尺寸，高度 40px
- `Size.Medium` - 默认尺寸，高度 32px
- `Size.Small` - 小尺寸，高度 24px

### 7. SegmentItem 组件

可在 Razor 页面中直接使用 `SegmentItem` 组件添加数据源，无需在代码后台定义 `Items` 集合。

```razor
<Segmented TValue="string" Value="Value" ValueChanged="OnValueChanged">
    <SegmentItem Text="Daily" Value="Daily" />
    <SegmentItem Text="Weekly" Value="Weekly" />
    <SegmentItem Text="Monthly" Value="Monthly" />
    <SegmentItem Text="Quarterly" Value="Quarterly" />
    <SegmentItem Text="Yearly" Value="Yearly" />
</Segmented>

@code {
    private string Value { get; set; } = "Daily";

    private Task OnValueChanged(string value)
    {
        Value = value;
        StateHasChanged();
        return Task.CompletedTask;
    }
}
```

**说明**:
- 使用 `SegmentItem` 子组件可以直接在 Razor 标记中定义选项
- 每个 `SegmentItem` 可以设置 `Text`、`Value`、`Icon`、`Disabled` 等属性
- 这种方式更直观，适合选项较少且固定的场景

## 参数

### Segmented 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `ChildContent` | 获得/设置 组件内容（用于放置 SegmentItem 子组件） | `RenderFragment` | `null` |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `IsBlock` | 获得/设置 是否充满父元素 | `bool` | `false` |
| `IsDisabled` | 获得/设置 是否禁用 | `bool` | `false` |
| `Items` | 获得/设置 选项集合 | `IEnumerable<SegmentedOption<TValue>>` | `null` |
| `ItemTemplate` | 获得/设置 候选项模板 | `RenderFragment<SegmentedOption<TValue>>` | `null` |
| `ShowTooltip` | 获得/设置 是否自动显示 Tooltip | `bool` | `false` |
| `Size` | 获得/设置 组件大小 | `Size` | `Size.Medium` |
| `Value` | 获得/设置 选中值 | `TValue` | `null` |

### SegmentedOption 选项参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Text` | 获得/设置 选项显示文本 | `string` | `null` |
| `Value` | 获得/设置 选项值 | `TValue` | `null` |
| `Icon` | 获得/设置 选项图标 | `string` | `null` |
| `Disabled` | 获得/设置 是否禁用此选项 | `bool` | `false` |
| `Tooltip` | 获得/设置 选项提示文本 | `string` | `null` |

### SegmentItem 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Text` | 获得/设置 选项显示文本 | `string` | `null` |
| `Value` | 获得/设置 选项值 | `TValue` | `null` |
| `Icon` | 获得/设置 选项图标 | `string` | `null` |
| `Disabled` | 获得/设置 是否禁用此选项 | `bool` | `false` |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `ValueChanged` | 获得/设置 选中值回调委托 | `EventCallback<TValue>` |
| `OnValueChanged` | 获得/设置 选中值改变后回调委托方法 | `Func<TValue, Task>` |

**说明**:
- `ValueChanged` 是标准的 Blazor 双向绑定事件，可与 `@bind-Value` 配合使用
- `OnValueChanged` 是自定义回调，在值改变后执行，适合执行异步操作

## 最佳实践

### 1. 选项数量控制

Segmented 组件适合选项数量较少（2-5 个）的场景。如果选项过多，应考虑使用 Dropdown 或 Select 组件。

```razor
<!-- 推荐：选项数量适中 -->
<Segmented TValue="string" Items="TimeItems" />

<!-- 不推荐：选项过多，UI 拥挤 -->
<Segmented TValue="string" Items="TooManyItems" />
```

### 2. 使用 @bind-Value 简化代码

对于简单的选中值绑定，推荐使用 `@bind-Value` 语法。

```razor
<!-- 推荐：使用 @bind-Value -->
<Segmented TValue="string" Items="Items" @bind-Value="SelectedValue" />

@code {
    private string SelectedValue { get; set; } = "Daily";
}

<!-- 传统方式：需要手动处理 ValueChanged -->
<Segmented TValue="string" Items="Items" Value="SelectedValue" ValueChanged="OnValueChanged" />

@code {
    private string SelectedValue { get; set; } = "Daily";

    private Task OnValueChanged(string value)
    {
        SelectedValue = value;
        StateHasChanged();
        return Task.CompletedTask;
    }
}
```

### 3. 选项文本简洁明了

选项文本应简洁明了，避免过长文本导致 UI 布局问题。

```razor
<!-- 推荐：文本简洁 -->
<SegmentedOption<string> Text="日" Value="day" />
<SegmentedOption<string> Text="周" Value="week" />
<SegmentedOption<string> Text="月" Value="month" />

<!-- 不推荐：文本过长 -->
<SegmentedOption<string> Text="long-text-long-text-long-text" Value="long" />
```

如果必须使用长文本，可考虑：
- 使用 `ItemTemplate` 自定义渲染，截断文本
- 设置 `ShowTooltip="true"` 显示完整文本提示
- 使用 `IsBlock="true"` 让组件自适应宽度

### 4. 禁用状态的视觉反馈

当选项被禁用时，用户应能清晰识别。可通过样式或 Tooltip 提供额外反馈。

```razor
<Segmented TValue="string" Items="Items" ShowTooltip="true" />

@code {
    protected override void OnInitialized()
    {
        Items = new List<SegmentedOption<string>>
        {
            new SegmentedOption<string> { Text = "可用", Value = "1" },
            new SegmentedOption<string> 
            { 
                Text = "已禁用", 
                Value = "2", 
                Disabled = true,
                Tooltip = "此选项暂时不可用" 
            }
        };
    }
}
```

## 常见问题

### 1. 选中值不更新

**问题**: 设置 `Value` 后，组件选中状态不更新。

**原因**: 可能是未触发 `ValueChanged` 回调或未调用 `StateHasChanged()`。

**解决方案**:
- 使用 `@bind-Value` 自动处理双向绑定
- 手动处理 `ValueChanged` 时，确保更新 `Value` 并调用 `StateHasChanged()`

```razor
<!-- 方案 1：使用 @bind-Value -->
<Segmented TValue="string" Items="Items" @bind-Value="SelectedValue" />

<!-- 方案 2：手动处理 -->
<Segmented TValue="string" Items="Items" Value="SelectedValue" ValueChanged="OnValueChanged" />

@code {
    private string SelectedValue { get; set; } = "";

    private Task OnValueChanged(string value)
    {
        SelectedValue = value;
        StateHasChanged();  // 重要：触发重新渲染
        return Task.CompletedTask;
    }
}
```

### 2. 选项显示异常

**问题**: 选项文本显示为空白或显示异常。

**原因**: 可能是 `Text` 属性未设置或 `ItemTemplate` 模板有问题。

**解决方案**:
- 检查 `SegmentedOption` 的 `Text` 属性是否正确设置
- 如果使用 `ItemTemplate`，确保模板正确渲染内容

```razor
<!-- 检查 Text 属性 -->
<SegmentedOption<string> Text="正确文本" Value="1" />

<!-- 检查 ItemTemplate -->
<ItemTemplate>
    <div>@context.Text</div>  <!-- 确保使用 context.Text -->
</ItemTemplate>
```

### 3. IsBlock 不生效

**问题**: 设置 `IsBlock="true"` 后，组件宽度未充满父容器。

**原因**: 父容器可能没有设置宽度或样式限制。

**解决方案**:
- 确保父容器有明确宽度或使用 flex 布局
- 检查父容器的 CSS 样式

```razor
<!-- 父容器设置宽度 -->
<div style="width: 100%;">
    <Segmented TValue="string" Items="Items" IsBlock="true" />
</div>

<!-- 或使用 flex 布局 -->
<div style="display: flex;">
    <Segmented TValue="string" Items="Items" IsBlock="true" />
</div>
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 7.0.0 | 2024-01-15 | Segmented 组件首次发布 |
| 7.5.0 | 2024-06-20 | 新增 SegmentItem 子组件支持 |
| 8.0.0 | 2024-11-10 | 新增 ShowTooltip 参数；优化 IsBlock 布局逻辑 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Segmented](https://www.blazor.zone/segmented)
- [Bootstrap Blazor API - Segmented](https://www.blazor.zone/api/Segmented)
