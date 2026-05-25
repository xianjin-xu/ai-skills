# Transfer (穿梭框)

## 概述

`Transfer` 组件用于**在两个列表之间移动数据**，常用于权限分配、角色分配等场景。

**主要特性**：
- 支持搜索功能
- 支持单选/多选
- 可自定义显示内容
- 支持禁用状态
- 支持不同尺寸

**在线演示**: https://www.blazor.zone/transfer

---

## 使用场景

### 1. 基础用法（简单穿梭框）

`Transfer` 组件可以通过 `Items` 参数绑定数据源。

```razor
<!-- 基础穿梭框 -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues" />

@code {
    private List<TransferItem> TransferItems { get; set; } = new List<TransferItem>
    {
        new TransferItem("1", "选项 1"),
        new TransferItem("2", "选项 2"),
        new TransferItem("3", "选项 3"),
        new TransferItem("4", "选项 4"),
        new TransferItem("5", "选项 5")
    };

    private List<string> SelectedValues { get; set; } = new List<string>();
}
```

---

### 2. 搜索功能（ShowSearch）

通过设置 `ShowSearch="true"` 启用搜索功能。

```razor
<!-- 带搜索的穿梭框 -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues" ShowSearch="true" />

@code {
    private List<TransferItem> TransferItems { get; set; } = new List<TransferItem>
    {
        new TransferItem("1", "选项 1"),
        new TransferItem("2", "选项 2"),
        new TransferItem("3", "选项 3")
    };

    private List<string> SelectedValues { get; set; } = new List<string>();
}
```

---

### 3. 自定义显示内容（ItemTemplate）

通过 `ItemTemplate` 参数自定义选项显示内容。

```razor
<!-- 自定义显示 -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues">
    <ItemTemplate>
        <div>
            <strong>@context.Text</strong>
            <small>ID: @context.Value</small>
        </div>
    </ItemTemplate>
</Transfer>

@code {
    private List<TransferItem> TransferItems { get; set; } = new List<TransferItem>
    {
        new TransferItem("1", "选项 1"),
        new TransferItem("2", "选项 2")
    };

    private List<string> SelectedValues { get; set; } = new List<string>();
}
```

---

### 4. 禁用状态（Disabled）

通过设置 `Disabled="true"` 禁用穿梭框。

```razor
<!-- 禁用穿梭框 -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues" Disabled="true" />

@code {
    private List<TransferItem> TransferItems { get; set; } = new List<TransferItem>
    {
        new TransferItem("1", "选项 1"),
        new TransferItem("2", "选项 2")
    };

    private List<string> SelectedValues { get; set; } = new List<string>();
}
```

---

### 5. 不同尺寸（Size）

通过 `Size` 参数设置穿梭框尺寸。

```razor
<!-- 小尺寸 -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues" Size="Size.Small" />

<!-- 中尺寸（默认） -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues" Size="Size.Medium" />

<!-- 大尺寸 -->
<Transfer Items="TransferItems" @bind-Value="SelectedValues" Size="Size.Large" />

@code {
    private List<TransferItem> TransferItems { get; set; } = new List<TransferItem>
    {
        new TransferItem("1", "选项 1"),
        new TransferItem("2", "选项 2")
    };

    private List<string> SelectedValues { get; set; } = new List<string>();
}
```

---

## 参数 (Parameters)

### Transfer 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TransferItem>?` | `null` | 获得/设置数据源 |
| `Value` | `List<string>?` | `null` | 获得/设置选中的值 |
| `ShowSearch` | `bool` | `false` | 获得/设置是否显示搜索框 |
| `Disabled` | `bool` | `false` | 获得/设置是否禁用 |
| `Size` | `Size` | `Size.Medium` | 获得/设置尺寸 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<List<string>?>` | 选中值变化回调 |

---

## 数据类 (TransferItem)

`TransferItem` 类定义穿梭框选项的数据。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置选项值 |
| `Text` | `string?` | `null` | 获得/设置选项文本 |
| `Disabled` | `bool` | `false` | 获得/设置是否禁用 |
| `Group` | `string?` | `null` | 获得/设置分组名称 |

---

## 最佳实践

1. **使用 @bind-Value 双向绑定**：推荐使用 `@bind-Value` 实现双向绑定，简化代码
2. **提供搜索功能**：对于大量数据，设置 `ShowSearch="true"` 提供搜索功能，提升用户体验
3. **合理分组**：通过 `Group` 属性对选项进行分组，提升可读性
4. **处理 ValueChanged 事件**：对于需要在选中值变化时执行逻辑的场景，处理 `ValueChanged` 事件
5. **自定义显示内容**：对于复杂内容，使用 `ItemTemplate` 自定义选项显示
6. **与 Select 组件的区别**：`Transfer` 适合在两个列表间移动数据，`Select` 适合单选/多选下拉
