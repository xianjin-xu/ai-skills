# ValidateForm (验证表单)

## 概述

`ValidateForm` 组件用于**带数据验证的表单**，基于 `EditForm` 扩展，提供 Bootstrap 样式验证反馈。

**主要特性**：
- 支持数据注解验证（DataAnnotations）
- 显示验证消息
- 支持自定义验证样式
- 可禁用验证（DisableValidate）
- 支持提交时验证（ValidateOnSubmit）

**在线演示**: https://www.blazor.zone/validate-form

---

## 使用场景

### 1. 基础用法（简单验证表单）

`ValidateForm` 组件可以通过 `Model` 参数绑定验证模型。

```razor
<!-- 基础验证表单 -->
<ValidateForm Model="UserModel" OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="UserModel.Name" DisplayText="姓名" />
    <BootstrapInput @bind-Value="UserModel.Email" DisplayText="邮箱" />
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>

@code {
    private User UserModel { get; set; } = new User();

    private void OnValidSubmit()
    {
        // 表单验证通过，执行提交逻辑
        Console.WriteLine("表单提交成功");
    }

    public class User
    {
        [Required(ErrorMessage = "姓名不能为空")]
        public string? Name { get; set; }

        [Required(ErrorMessage = "邮箱不能为空")]
        [EmailAddress(ErrorMessage = "邮箱格式不正确")]
        public string? Email { get; set; }
    }
}
```

---

### 2. 自定义验证消息（ValidationMessage）

通过 `ValidationMessage` 组件显示验证消息。

```razor
<!-- 自定义验证消息 -->
<ValidateForm Model="UserModel" OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="UserModel.Name" DisplayText="姓名" />
    <ValidationMessage For="() => UserModel.Name" />
    
    <BootstrapInput @bind-Value="UserModel.Email" DisplayText="邮箱" />
    <ValidationMessage For="() => UserModel.Email" />
    
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>

@code {
    private User UserModel { get; set; } = new User();

    private void OnValidSubmit()
    {
        // 提交逻辑
    }

    public class User
    {
        [Required(ErrorMessage = "姓名不能为空")]
        public string? Name { get; set; }

        [Required(ErrorMessage = "邮箱不能为空")]
        [EmailAddress(ErrorMessage = "邮箱格式不正确")]
        public string? Email { get; set; }
    }
}
```

---

### 3. 禁用验证（DisableValidate）

通过设置 `DisableValidate="true"` 禁用验证。

```razor
<!-- 禁用验证的表单 -->
<ValidateForm Model="UserModel" OnValidSubmit="OnValidSubmit" DisableValidate="true">
    <BootstrapInput @bind-Value="UserModel.Name" DisplayText="姓名" />
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>

@code {
    private User UserModel { get; set; } = new User();

    private void OnValidSubmit()
    {
        // 提交逻辑（不验证）
    }

    public class User
    {
        public string? Name { get; set; }
    }
}
```

---

### 4. 提交时验证（ValidateOnSubmit）

通过设置 `ValidateOnSubmit="true"` 在提交时进行验证。

```razor
<!-- 提交时验证 -->
<ValidateForm Model="UserModel" OnValidSubmit="OnValidSubmit" ValidateOnSubmit="true">
    <BootstrapInput @bind-Value="UserModel.Name" DisplayText="姓名" />
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>

@code {
    private User UserModel { get; set; } = new User();

    private void OnValidSubmit()
    {
        // 提交逻辑
    }

    public class User
    {
        [Required(ErrorMessage = "姓名不能为空")]
        public string? Name { get; set; }
    }
}
```

---

### 5. 自定义验证样式（ValidCssClass、InvalidCssClass）

通过 `ValidCssClass` 和 `InvalidCssClass` 参数自定义验证样式。

```razor
<!-- 自定义验证样式 -->
<ValidateForm Model="UserModel" 
             ValidCssClass="is-valid" 
             InvalidCssClass="is-invalid"
             OnValidSubmit="OnValidSubmit">
    <BootstrapInput @bind-Value="UserModel.Name" DisplayText="姓名" />
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>

@code {
    private User UserModel { get; set; } = new User();

    private void OnValidSubmit()
    {
        // 提交逻辑
    }

    public class User
    {
        [Required(ErrorMessage = "姓名不能为空")]
        public string? Name { get; set; }
    }
}
```

---

## 参数 (Parameters)

### ValidateForm 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Model` | `object?` | `null` | 获得/设置验证模型 |
| `DisableValidate` | `bool` | `false` | 获得/设置是否禁用验证 |
| `ValidateOnSubmit` | `bool` | `false` | 获得/设置是否在提交时验证 |
| `ValidCssClass` | `string?` | `null` | 获得/设置验证通过的 CSS 类 |
| `InvalidCssClass` | `string?` | `null` | 获得/设置验证失败的 CSS 类 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnValidSubmit` | `EventCallback` | 验证通过时提交回调 |
| `OnInvalidSubmit` | `EventCallback` | 验证失败时提交回调 |

---

## 最佳实践

1. **使用 DataAnnotations 验证**：在模型类上使用 `[Required]`、`[EmailAddress]` 等数据注解进行验证
2. **处理 OnValidSubmit 事件**：在 `OnValidSubmit` 事件中执行提交逻辑，确保只有验证通过才会执行
3. **显示验证消息**：使用 `ValidationMessage` 组件显示字段验证消息，提升用户体验
4. **自定义验证样式**：通过 `ValidCssClass` 和 `InvalidCssClass` 自定义验证样式，与项目设计保持一致
5. **与 EditForm 的区别**：`ValidateForm` 是基于 `EditForm` 的扩展，提供 Bootstrap 样式验证反馈；`EditForm` 是 Blazor 原生表单组件
6. **避免过度验证**：对于简单表单，使用基础验证即可；对于复杂表单，考虑使用 FluentValidation 等高级验证库
7. **处理 OnInvalidSubmit 事件**：在 `OnInvalidSubmit` 事件中处理验证失败逻辑（如提示用户修正错误）
