# FloatingLabel 悬浮标签输入框

## 概述

`FloatingLabel` 是一个悬浮标签输入框组件，通过鼠标或键盘输入字符。当输入框获得焦点时，标签会浮动到输入框上方，提供更好的用户体验。适用于需要美观表单输入的场景。

**命名空间**: `BootstrapBlazor.Components`

**泛型参数**: `TValue` - 值类型

**在线演示**: [https://www.blazor.zone/floating-label](https://www.blazor.zone/floating-label)

## 使用场景

### 1. 基础用法

提供基本的文本录入组件。

```razor
<FloatingLabel @bind-Value="Text" PlaceHolder="请输入文字" />

@code {
    private string? Text { get; set; }
}
```

**说明**:
- `PlaceHolder` 设置占位符文本
- 当输入框获得焦点时，标签会浮动到上方
- 支持双向绑定 `@bind-Value`

### 2. 单向绑定数据

显示组件内变量值。

```razor
<FloatingLabel Value="Text" ValueChanged="OnValueChanged" />

@code {
    private string Text { get; set; } = "初始值";

    private void OnValueChanged(string value)
    {
        Text = value;
        StateHasChanged();
    }
}
```

**说明**:
- 使用 `Value` 和 `ValueChanged` 实现单向绑定
- 需要手动更新值和触发重新渲染

### 3. 客户端验证

根据自定义验证规则进行数据有效性检查并自动提示。

```razor
<EditForm Model="Model">
    <DataAnnotationsValidator />
    <FloatingLabel @bind-Value="Model.Name" PlaceHolder="请输入姓名">
        <Microsoft.AspNetCore.Components.Forms.ValidationMessage For="() => Model.Name" />
    </FloatingLabel>
</EditForm>

@code {
    private Person Model { get; set; } = new();

    public class Person
    {
        [Required(ErrorMessage = "姓名不能为空")]
        public string Name { get; set; } = "";
    }
}
```

**说明**:
- 配合 `EditForm` 和 `DataAnnotationsValidator` 使用
- 使用 `ValidationMessage` 显示验证错误信息
- 支持 `Required`、`StringLength` 等数据注解

### 4. 密码框

通过设置属性 `type` 值为 `password` 使输入文字后以 `*` 进行屏蔽的密码输入框。

```razor
<FloatingLabel @bind-Value="Password" type="password" PlaceHolder="请输入密码" />

@code {
    private string? Password { get; set; }
}
```

**说明**:
- `type="password"` - 密码输入框
- 为了支持更多的文本框属性，本组件可以直接写入 `type='email'`、`type='number'`、`type='phone'` 等 HTML5 新标准支持的全部属性值
- 组件未设置 `type` 值时使用默认的 `type='text'`

### 5. 泛型绑定

BootstrapInput 组件双向绑定值是泛型的，本例中双向绑定一个 `int` 类型数值。

```razor
<FloatingLabel @bind-Value="Age" type="number" PlaceHolder="请输入年龄" />

@code {
    private int Age { get; set; } = 0;
}
```

**说明**:
- `TValue` 可以是 `string`、`int`、`float`、`DateTime` 等类型
- 组件会自动处理类型转换
- 类型转换失败时会显示错误信息

### 6. 自定义格式

设置 `FormatString` 或 `Formatter` 自定义显示格式。

```razor
<!-- 方式 1：使用 FormatString -->
<FloatingLabel @bind-Value="Birthday" FormatString="yyyy-MM-dd" PlaceHolder="请选择生日" />

<!-- 方式 2：使用 Formatter -->
<FloatingLabel @bind-Value="Price" Formatter="FormatPrice" PlaceHolder="请输入价格" />

@code {
    private DateTime BirthDay { get; set; } = DateTime.Now;
    private decimal Price { get; set; } = 0;

    private string FormatPrice(decimal value)
    {
        return $"¥{value:N2}";
    }
}
```

**说明**:
- `FormatString` - 格式字符串（如 `"yyyy-MM-dd"` 用于日期类型）
- `Formatter` - 格式化函数（更灵活）
- `Formatter` 优先级高于 `FormatString`

### 7. 禁用

设置 `IsDisabled` 属性值为 `true` 时，组件禁止输入。

```razor
<FloatingLabel @bind-Value="Text" IsDisabled="true" PlaceHolder="禁用的输入框" />
```

**说明**:
- `IsDisabled="false"`（默认值）- 可输入
- `IsDisabled="true"` - 禁用输入

### 8. GroupBox 样式

设置 `IsGroupBox` 属性为 `true`，使用 GroupBox 样式。

```razor
<FloatingLabel @bind-Value="Text" IsGroupBox="true" PlaceHolder="GroupBox 样式" />
```

**说明**:
- `IsGroupBox="false"`（默认值）- 不使用 GroupBox 样式
- `IsGroupBox="true"` - 使用 GroupBox 边框样式

## 参数

### FloatingLabel 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `Color` | 获得/设置 按钮颜色 | `Color` | - |
| `DisplayText` | 获得/设置 显示名称 | `string` | - |
| `FormatString` | 获得/设置 格式字符串，例如 `"yyyy-MM-dd"` 用于日期类型 | `string` | `null` |
| `Formatter` | 获得/设置 格式化函数 | `Func<TValue, string>` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `IsAutoFocus` | 获得/设置 是否自动获取焦点，默认值为 `false` | `bool` | `false` |
| `IsDisabled` | 获得/设置 是否禁用，默认为 `false` | `bool` | `false` |
| `IsGroupBox` | 获得/设置 是否为 GroupBox 样式，默认 `false` | `bool` | `false` |
| `IsSelectAllTextOnEnter` | 获得/设置 是否在按下回车键时自动选择所有文本，默认值为 `false` | `bool` | `false` |
| `IsSelectAllTextOnFocus` | 获得/设置 是否在获取焦点时自动选择所有文本，默认值为 `false` | `bool` | `false` |
| `IsTrim` | 获得/设置 是否自动去除空格，默认值为 `false` | `bool` | `false` |
| `OnBlurAsync` | 获得/设置 失去焦点时的回调方法，默认值为 `null` | `Func<TValue, Task>` | `null` |
| `OnEnterAsync` | 获得/设置 回车键按下时的回调方法，默认值为 `null` | `Func<TValue, Task>` | `null` |
| `OnEscAsync` | 获得/设置 Esc 键按下时的回调方法，默认值为 `null` | `Func<TValue, Task>` | `null` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<TValue, Task>` | - |
| `ParsingErrorMessage` | 获得/设置 类型转化失败格式化字符串，默认为 `null` | `string` | `null` |
| `PlaceHolder` | 获得/设置 占位符属性值 | `string` | - |
| `RequiredErrorMessage` | 获得/设置 必填项错误文本，默认为 `null` 未设置 | `string` | `null` |
| `ShowLabel` | 获得/设置 是否显示前置标签，默认值为 `null`，为空时不显示标签 | `bool?` | `null` |
| `ShowLabelTooltip` | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 `null` | `bool?` | `null` |
| `ShowRequired` | 获得/设置 是否显示必填项标记，默认为 `null` 未设置 | `bool?` | `null` |
| `SkipValidate` | 获得/设置 是否不进行验证，默认为 `false` | `bool` | `false` |
| `ValidateRules` | 获得/设置 自定义验证集合 | `List<IValidator>` | - |
| `Value` | 获得/设置 输入组件的值，支持双向绑定 | `TValue` | - |
| `ValueChanged` | 获得/设置 用于更新绑定值的回调 | `EventCallback<TValue>` | - |
| `ValueExpression` | 获得/设置 标识绑定值的表达式 | `Expression<Func<TValue>>` | - |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `ValueChanged` | 获得/设置 用于更新绑定值的回调 | `EventCallback<TValue>` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<TValue, Task>` |
| `OnBlurAsync` | 获得/设置 失去焦点时的回调方法 | `Func<TValue, Task>` |
| `OnEnterAsync` | 获得/设置 回车键按下时的回调方法 | `Func<TValue, Task>` |
| `OnEscAsync` | 获得/设置 Esc 键按下时的回调方法 | `Func<TValue, Task>` |

## 最佳实践

### 1. 使用 @bind-Value 简化绑定

推荐使用 `@bind-Value` 实现双向绑定，简化代码。

```razor
<!-- 推荐：使用 @bind-Value -->
<FloatingLabel @bind-Value="Model.Name" PlaceHolder="请输入姓名" />

@code {
    private Person Model { get; set; } = new();
}

<!-- 不推荐：手动处理 ValueChanged -->
<FloatingLabel Value="Model.Name" ValueChanged="OnValueChanged" />

@code {
    private void OnValueChanged(string value)
    {
        Model.Name = value;
        StateHasChanged();
    }
}
```

### 2. 配合表单验证使用

将 FloatingLabel 与 `EditForm` 配合使用，实现表单验证。

```razor
<EditForm Model="Model" OnValidSubmit="OnValidSubmit">
    <DataAnnotationsValidator />
    
    <div class="mb-3">
        <FloatingLabel @bind-Value="Model.Email" type="email" PlaceHolder="请输入邮箱">
            <ValidationMessage For="() => Model.Email" />
        </FloatingLabel>
    </div>
    
    <div class="mb-3">
        <FloatingLabel @bind-Value="Model.Password" type="password" PlaceHolder="请输入密码">
            <ValidationMessage For="() => Model.Password" />
        </FloatingLabel>
    </div>
    
    <button type="submit" class="btn btn-primary">提交</button>
</EditForm>

@code {
    private LoginModel Model { get; set; } = new();

    private void OnValidSubmit()
    {
        // 表单提交逻辑
        Console.WriteLine($"登录: {Model.Email}");
    }

    public class LoginModel
    {
        [Required(ErrorMessage = "邮箱不能为空")]
        [EmailAddress(ErrorMessage = "邮箱格式不正确")]
        public string Email { get; set; } = "";

        [Required(ErrorMessage = "密码不能为空")]
        [MinLength(6, ErrorMessage = "密码至少 6 位")]
        public string Password { get; set; } = "";
    }
}
```

### 3. 使用 Formatter 自定义显示格式

当需要在输入框中显示自定义格式时，使用 `Formatter` 参数。

```razor
<FloatingLabel @bind-Value="Price" Formatter="FormatPrice" PlaceHolder="请输入价格" />

@code {
    private decimal Price { get; set; } = 0;

    private string FormatPrice(decimal value)
    {
        return $"¥{value:N2}";  // 显示格式：¥1,234.56
    }
}
```

### 4. 自动获取焦点

通过 `IsAutoFocus="true"` 让输入框自动获取焦点。

```razor
<FloatingLabel @bind-Value="Text" IsAutoFocus="true" PlaceHolder="自动获取焦点" />
```

**说明**:
- 页面加载后输入框自动获取焦点
- 适用于需要用户立即输入的场景（如搜索框）

## 常见问题

### 1. 标签不浮动

**问题**: 输入框获得焦点后，标签没有浮动到上方。

**原因**: 可能是 CSS 样式冲突，或者组件未正确渲染。

**解决方案**:
- 检查是否引入了 Bootstrap Blazor 的 CSS 文件
- 检查是否有自定义 CSS 覆盖了 FloatingLabel 的样式
- 使用浏览器开发者工具检查元素样式

```html
<!-- 确保在 _Host.cshtml 或 index.html 中引入了 CSS -->
<link rel="stylesheet" href="_content/BootstrapBlazor/css/bootstrap.blazor.bundle.min.css" />
```

### 2. 验证错误信息不显示

**问题**: 表单验证失败，但错误信息不显示。

**原因**: 可能是未添加 `ValidationMessage` 组件，或者验证未触发。

**解决方案**:
- 确保在 `EditForm` 中添加了 `DataAnnotationsValidator`
- 确保添加了 `ValidationMessage` 组件
- 检查模型属性的验证注解是否正确

```razor
<EditForm Model="Model">
    <DataAnnotationsValidator />  <!-- 重要：必须添加 -->
    <FloatingLabel @bind-Value="Model.Name">
        <ValidationMessage For="() => Model.Name" />  <!-- 显示验证错误 -->
    </FloatingLabel>
</EditForm>
```

### 3. 类型转换失败

**问题**: 输入内容后，提示类型转换失败。

**原因**: 可能是输入内容无法转换为 `TValue` 类型，或者 `ParsingErrorMessage` 未设置。

**解决方案**:
- 设置 `ParsingErrorMessage` 自定义错误提示
- 确保输入内容符合类型要求
- 使用 `OnValueChanged` 手动处理转换逻辑

```razor
<FloatingLabel @bind-Value="Age" 
           type="number" 
           ParsingErrorMessage="请输入有效的数字" 
           PlaceHolder="请输入年龄" />

@code {
    private int Age { get; set; } = 0;
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | FloatingLabel 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 `Formatter` 参数；优化验证逻辑 |
| 8.0.0 | 2024-11-10 | 新增 `IsGroupBox` 参数；支持 GroupBox 样式 |

## 参考链接

- [Bootstrap Blazor 官方文档 - FloatingLabel](https://www.blazor.zone/floating-label)
- [Bootstrap Blazor API - FloatingLabel](https://www.blazor.zone/api/FloatingLabel)
- [Bootstrap 官方文档 - Floating labels](https://getbootstrap.com/docs/5.3/forms/floating-labels/) (Bootstrap Floating Labels)
