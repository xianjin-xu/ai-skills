# Display (显示组件)

## 概述

`Display` 组件用于**以只读格式显示数据**，通常用于表单的查看模式（与 `Input` 组件对应）。

**主要特性**：
- 支持多种数据类型显示
- 支持自定义格式
- 支持前缀/后缀文本
- 可显示图标

**在线演示**: https://www.blazor.zone/display

---

## 使用场景

### 1. 基础用法（简单显示）

`Display` 组件可以通过 `@bind-Value` 或 `Value` 参数绑定显示值。

```razor
<!-- 基础显示 -->
<Display Value="张三" />

<p>上方显示：张三</p>
```

---

### 2. 显示不同数据类型（DataType）

通过 `DataType` 参数设置数据类型，自动格式化显示。

```razor
<!-- 文本显示（默认） -->
<Display Value="这是一段文本" DataType="DisplayDataType.Text" />

<!-- HTML 显示 -->
<Display Value="<strong>加粗文本</strong>" DataType="DisplayDataType.Html" />

<!-- URL 显示 -->
<Display Value="https://www.example.com" DataType="DisplayDataType.Url" />

<!-- 邮件显示 -->
<Display Value="user@example.com" DataType="DisplayDataType.EmailAddress" />

<!-- 电话显示 -->
<Display Value="+86 138 0013 8000" DataType="DisplayDataType.PhoneNumber" />

<!-- 日期显示 -->
<Display Value="@DateTime.Now" DataType="DisplayDataType.Date" />

<!-- 时间显示 -->
<Display Value="@DateTime.Now" DataType="DisplayDataType.Time" />

<!-- 日期时间显示 -->
<Display Value="@DateTime.Now" DataType="DisplayDataType.DateTime" />
```

**DataType 选项**：
- `DisplayDataType.Text` - 文本（默认）
- `DisplayDataType.Html` - HTML 内容
- `DisplayDataType.Url` - URL 链接
- `DisplayDataType.EmailAddress` - 邮件地址
- `DisplayDataType.PhoneNumber` - 电话号码
- `DisplayDataType.Date` - 日期
- `DisplayDataType.Time` - 时间
- `DisplayDataType.DateTime` - 日期时间
- `DisplayDataType.Currency` - 货币
- `DisplayDataType.Password` - 密码（隐藏）

---

### 3. 自定义格式（Format）

通过 `Format` 参数设置自定义显示格式。

```razor
<!-- 日期格式 -->
<Display Value="@DateTime.Now" Format="yyyy-MM-dd" />

<!-- 数字格式 -->
<Display Value="@Price" Format="C2" />

<!-- 百分比格式 -->
<Display Value="@Progress" Format="P0" />

@code {
    private decimal Price { get; set; } = 1234.56m;
    private double Progress { get; set; } = 0.85;
}
```

**常用格式**：
- `yyyy-MM-dd` - 日期（2024-01-01）
- `HH:mm:ss` - 时间（14:30:00）
- `C2` - 货币（¥1,234.56）
- `P0` - 百分比（85%）
- `N0` - 数字（1,235）

---

### 4. 前缀/后缀文本（Prefix、Suffix）

通过 `Prefix` 和 `Suffix` 参数添加前缀或后缀文本。

```razor
<!-- 带前缀 -->
<Display Value="@Price" Prefix="¥" Format="N2" />

<!-- 带后缀 -->
<Display Value="@Progress" Suffix="%" Format="F0" />

@code {
    private decimal Price { get; set; } = 1234.56m;
    private double Progress { get; set; } = 85.0;
}
```

---

### 5. 显示图标（Icon）

通过 `Icon` 参数在显示值前添加图标。

```razor
<!-- 带图标 -->
<Display Value="张三" Icon="fa fa-user" />

<!-- 带状态图标 -->
<Display Value="已完成" Icon="fa fa-check-circle" Color="Color.Success" />
```

---

### 6. 与 Input 对比（EditMode vs DisplayMode）

`Display` 组件通常与 `Input` 组件配合，根据模式切换。

```razor
<!-- 查看模式：使用 Display -->
@if (IsViewMode)
{
    <Display Value="@UserModel.Name" />
    <Display Value="@UserModel.Email" DataType="DisplayDataType.EmailAddress" />
}
<!-- 编辑模式：使用 Input -->
else
{
    <BootstrapInput @bind-Value="@UserModel.Name" />
    <BootstrapInput @bind-Value="@UserModel.Email" />
}

<Button OnClick="() => IsViewMode = !IsViewMode">切换模式</Button>

@code {
    private bool IsViewMode { get; set; } = true;
    private UserModel UserModel { get; set; } = new UserModel();
    
    public class UserModel
    {
        public string Name { get; set; } = "张三";
        public string Email { get; set; } = "zhangsan@example.com";
    }
}
```

---

## 参数 (Parameters)

### Display 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `object?` | `null` | 获得/设置显示值 |
| `DataType` | `DisplayDataType` | `DisplayDataType.Text` | 获得/设置数据类型 |
| `Format` | `string?` | `null` | 获得/设置显示格式 |
| `Prefix` | `string?` | `null` | 获得/设置前缀文本 |
| `Suffix` | `string?` | `null` | 获得/设置后缀文本 |
| `Icon` | `string?` | `null` | 获得/设置图标 |
| `Color` | `Color` | `Color.None` | 获得/设置颜色 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 最佳实践

1. **与 Input 配合使用**：`Display` 用于查看模式，`Input` 用于编辑模式，根据场景切换
2. **合理设置 DataType**：根据数据类型设置 `DataType`，自动格式化显示（如 `EmailAddress` 会生成 `mailto:` 链接）
3. **使用 Format 控制格式**：对于日期、数字等，使用 `Format` 参数控制显示格式
4. **添加 Prefix/Suffix**：对于货币、百分比等，使用 `Prefix` 或 `Suffix` 增强可读性
5. **与 Label 的区别**：`Display` 显示数据值，`Label` 显示字段标签，通常配合使用
6. **避免过度格式化**：过度格式化会降低可读性，保持简洁明了

---

## 与 Input 组件对比

| 特性 | Display | Input |
|------|---------|-------|
| 用途 | 查看数据 | 编辑数据 |
| 交互性 | 无（只读） | 有（可编辑） |
| 数据类型 | 支持格式化显示 | 支持编辑各种类型 |
| 典型场景 | 详情页、查看模式 | 表单、编辑模式 |
