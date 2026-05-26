# Row (行布局组件)

## 概述

`Row` 组件用于**简单设置一行显示的组件数量**，将自己的组件放到 Row 内部即可。

`Row` 是布局组件，常用于在 `ValidateForm` 内自动生成 Label 标签。

**主要特性**：
- 支持设置一行显示组件数量（ItemsPerRow）
- 支持两种布局模式（Normal、Inline）
- 支持跨列功能（ColSpan）
- 支持嵌套使用
- 在 ValidateForm 内自动生成 Label

**在线演示**: https://www.blazor.zone/row

---

## 使用场景

### 1. 基础用法（放置普通控件）

`Row` 组件内部直接放置组件即可，通过 `ItemsPerRow` 设置一行显示几个组件。

```razor
<!-- 一行显示 3 个组件 -->
<Row ItemsPerRow="ItemsPerRow.Three">
    <BootstrapInput @bind-Value="Value1" PlaceHolder="输入框 1" />
    <BootstrapInput @bind-Value="Value2" PlaceHolder="输入框 2" />
    <BootstrapInput @bind-Value="Value3" PlaceHolder="输入框 3" />
</Row>

@code {
    private string? Value1 { get; set; }
    private string? Value2 { get; set; }
    private string? Value3 { get; set; }
}
```

---

### 2. 放置表单控件（Inline 模式）

当放置表单控件时，可以指定 `RowType` 为 `Inline`，会将 Label 显示在左边，控件充满剩余空间。

本例中 Row 组件内置于 ValidateForm 组件内，自动增加前置 Label 标签。

```razor
<ValidateForm Model="Model">
    <Row ItemsPerRow="ItemsPerRow.Two" RowType="RowType.Inline">
        <BootstrapInput @bind-Value="Model.Name" />
        <BootstrapInput @bind-Value="Model.Address" />
        <DateTimePicker @bind-Value="Model.DateTime" />
        <BootstrapInputNumber @bind-Value="Model.Count" />
        <Switch @bind-Value="Model.Complete" />
        <Select @bind-Value="Model.Education" />
    </Row>
</ValidateForm>

@code {
    private DemoModel Model { get; set; } = new DemoModel();
    
    public class DemoModel
    {
        public string? Name { get; set; }
        public string? Address { get; set; }
        public DateTime? DateTime { get; set; }
        public int Count { get; set; }
        public bool Complete { get; set; }
        public string? Education { get; set; }
    }
}
```

---

### 3. 放置表单控件（Normal 模式）

当放置表单控件时，可以指定 `RowType` 为 `Normal`，会将 Label 显示在上边，控件充满。

```razor
<ValidateForm Model="Model">
    <Row ItemsPerRow="ItemsPerRow.Two" RowType="RowType.Normal">
        <BootstrapInput @bind-Value="Model.Name" />
        <BootstrapInput @bind-Value="Model.Address" />
        <DateTimePicker @bind-Value="Model.DateTime" />
        <BootstrapInputNumber @bind-Value="Model.Count" />
        <Switch @bind-Value="Model.Complete" />
        <Select @bind-Value="Model.Education" />
    </Row>
</ValidateForm>
```

---

### 4. 嵌套使用

`Row` 组件支持嵌套使用，比如下面最外层的 Row 设置一行显示两个控件，第一个是 TextBox，第二个还是 Row，第二个 Row 继续设置显示两个控件。

```razor
<ValidateForm Model="NestedModel">
    <Row ItemsPerRow="ItemsPerRow.Two">
        <BootstrapInput @bind-Value="NestedModel.Name" />
        <Row ItemsPerRow="ItemsPerRow.Two">
            <Switch @bind-Value="NestedModel.Complete" />
            <BootstrapInput @bind-Value="NestedModel.Address" />
        </Row>
    </Row>
</ValidateForm>

@code {
    private NestedModel NestedModel { get; set; } = new NestedModel();
    
    public class NestedModel
    {
        public string? Name { get; set; }
        public string? Address { get; set; }
        public bool Complete { get; set; }
    }
}
```

---

### 5. 跨列功能（ColSpan）

Row 组件可以通过指定 `ColSpan` 值设置跨列数，组合这些功能可以实现复杂布局。

#### 5.1 行显示 4 个

```razor
<ValidateForm Model="SpanModel">
    <Row ItemsPerRow="ItemsPerRow.Four">
        <BootstrapInput @bind-Value="SpanModel.Name" />
        <BootstrapInput @bind-Value="SpanModel.Address" />
        <BootstrapInputNumber @bind-Value="SpanModel.Count" />
        <Select @bind-Value="SpanModel.Education" />
    </Row>
</ValidateForm>
```

#### 5.2 行显示 2 个

```razor
<ValidateForm Model="SpanModel">
    <Row ItemsPerRow="ItemsPerRow.Two">
        <BootstrapInput @bind-Value="SpanModel.Name" />
        <BootstrapInput @bind-Value="SpanModel.Address" />
    </Row>
</ValidateForm>
```

#### 5.3 行显示 4 个，Address 占 2 列

```razor
<ValidateForm Model="SpanModel">
    <Row ItemsPerRow="ItemsPerRow.Four">
        <BootstrapInput @bind-Value="SpanModel.Name" />
        <Row ColSpan="2">
            <BootstrapInput @bind-Value="SpanModel.Address" />
        </Row>
        <Select @bind-Value="SpanModel.Education" />
    </Row>
</ValidateForm>
```

#### 5.4 行显示 4 个，第二个组件 ColSpan 设置为 3

```razor
<ValidateForm Model="SpanModel">
    <Row ItemsPerRow="ItemsPerRow.Four">
        <BootstrapInput @bind-Value="SpanModel.Name" />
        <Row ColSpan="3">
            <BootstrapInput @bind-Value="SpanModel.Address" />
        </Row>
    </Row>
</ValidateForm>
```

#### 5.5 行显示 2 个，第一个组件 ColSpan 设置为 3

```razor
<ValidateForm Model="SpanModel">
    <Row ItemsPerRow="ItemsPerRow.Two">
        <Row ColSpan="3">
            <CheckboxList @bind-Value="SpanModel.Hobby" Items="Hobbies3" />
        </Row>
        <BootstrapInput @bind-Value="SpanModel.Address" />
    </Row>
</ValidateForm>
```

#### 5.6 行显示一个组件

```razor
<ValidateForm Model="SpanModel">
    <Row>
        <BootstrapInput @bind-Value="SpanModel.Address" />
    </Row>
</ValidateForm>
```

---

## 参数 (Parameters)

### Row 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ItemsPerRow` | `ItemsPerRow` | `ItemsPerRow.Three` | 获得/设置 设置一行显示多少个子组件 |
| `RowType` | `RowType` | `RowType.Normal` | 获得/设置 设置行格式 默认 Row 布局 |
| `ColSpan` | `int?` | `null` | 获得/设置 子 Row 跨父 Row 列数 默认为 null |
| `AdditionalAttributes` | `IDictionary<string, object>` | `null` | 获得/设置 用户自定义属性 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件 |

---

## 枚举 (Enums)

### ItemsPerRow 枚举

| 值 | 说明 |
|-----|------|
| `ItemsPerRow.One` | 一行显示 1 个组件 |
| `ItemsPerRow.Two` | 一行显示 2 个组件 |
| `ItemsPerRow.Three` | 一行显示 3 个组件（默认） |
| `ItemsPerRow.Four` | 一行显示 4 个组件 |
| `ItemsPerRow.Six` | 一行显示 6 个组件 |
| `ItemsPerRow.Twelve` | 一行显示 12 个组件 |

### RowType 枚举

| 值 | 说明 |
|-----|------|
| `RowType.Normal` | 普通模式，Label 显示在上边（默认） |
| `RowType.Inline` | 内联模式，Label 显示在左边 |

---

## 最佳实践

1. **直接放置组件**：将自己的组件直接放到 `Row` 内部即可，不需要 `Col` 包装
2. **合理设置 ItemsPerRow**：根据页面宽度和组件大小选择合适的 `ItemsPerRow` 值
3. **使用 RowType 控制布局**：表单场景使用 `RowType.Inline`（Label 在左）或 `RowType.Normal`（Label 在上）
4. **嵌套实现复杂布局**：对于复杂布局，使用嵌套 `Row` 和 `ColSpan` 实现
5. **在 ValidateForm 中使用**：`Row` 在 `ValidateForm` 内会自动生成 Label 标签
6. **与 Bootstrap 网格的区别**：Bootstrap Blazor 的 `Row` 不是传统的 12 列网格，而是通过 `ItemsPerRow` 控制每行组件数量
