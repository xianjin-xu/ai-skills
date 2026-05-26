# IpAddress IP 地址组件#

## 概述

`IpAddress` 是一个 IP 地址组件，用于输入和验证 IP 地址的可重用组件。适用于需要输入 IPv4 或 IPv6 地址的场景。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/ip-address](https://www.blazor.zone/ip-address)

## 使用场景

### 1. 基础用法

分段录入并显示 IP 地址，例如：`192.168.1.1`。

```razor
<IpAddress @bind-Value="IpAddress" />

@code {
    private string? IpAddress { get; set; }
}
```

**说明**:
- 组件会自动分段显示 IP 地址（如 `192.168.1.1`）
- 支持 IPv4 和 IPv6 地址格式
- 使用 `@bind-Value` 实现双向绑定

### 2. 禁用

通过设置 `IsDisabled` 使组件处于不可用状态。

```razor
<IpAddress @bind-Value="IpAddress" IsDisabled="true" />
```

**说明**:
- `IsDisabled="false"`（默认值）- 组件可用
- `IsDisabled="true"` - 组件禁用，不可编辑

## 参数

### IpAddress 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `DisplayText` | 获得/设置 显示名称 | `string` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `IsDisabled` | 获得/设置 是否禁用，默认为 `false` | `bool` | `false` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<string, Task>` | - |
| `ParsingErrorMessage` | 获得/设置 类型转化失败格式化字符串，默认为 `null` | `string` | `null` |
| `RequiredErrorMessage` | 获得/设置 必填项错误文本，默认为 `null` 未设置 | `string` | `null` |
| `ShowLabel` | 获得/设置 是否显示前置标签，默认值为 `null`，为空时不显示标签 | `bool?` | `null` |
| `ShowLabelTooltip` | 获得/设置 是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 `null` | `bool?` | `null` |
| `ShowRequired` | 获得/设置 是否显示必填项标记，默认为 `null` 未设置 | `bool?` | `null` |
| `SkipValidate` | 获得/设置 是否不进行验证，默认为 `false` | `bool` | `false` |
| `ValidateRules` | 获得/设置 自定义验证集合 | `List<IValidator>` | - |
| `Value` | 获得/设置 输入组件的值，支持双向绑定 | `string` | - |
| `ValueChanged` | 获得/设置 用于更新绑定值的回调 | `EventCallback<string>` | - |
| `ValueExpression` | 获得/设置 标识绑定值的表达式 | `Expression<Func<string>>` | - |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `ValueChanged` | 获得/设置 用于更新绑定值的回调 | `EventCallback<string>` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<string, Task>` |

## 最佳实践

### 1. 使用 @bind-Value 简化绑定

推荐使用 `@bind-Value` 实现双向绑定，简化代码。

```razor
<!-- 推荐：使用 @bind-Value -->
<IpAddress @bind-Value="Model.ServerIp" />

@code {
    private ServerConfig Model { get; set; } = new();
}

<!-- 不推荐：手动处理 ValueChanged -->
<IpAddress Value="Model.ServerIp" ValueChanged="OnValueChanged" />

@code {
    private void OnValueChanged(string value)
    {
        Model.ServerIp = value;
        StateHasChanged();
    }
}
```

### 2. 配合表单验证使用

将 IpAddress 与 `EditForm` 配合使用，实现 IP 地址验证。

```razor
<EditForm Model="Model">
    <DataAnnotationsValidator />
    
    <div class="mb-3">
        <label>服务器 IP 地址</label>
        <IpAddress @bind-Value="Model.ServerIp" />
        <ValidationMessage For="() => Model.ServerIp" />
    </div>
    
    <button type="submit" class="btn btn-primary">保存</button>
</EditForm>

@code {
    private ServerConfig Model { get; set; } = new();

    public class ServerConfig
    {
        [Required(ErrorMessage = "服务器 IP 地址不能为空")]
        [RegularExpression(@"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", 
            ErrorMessage = "IP 地址格式不正确")]
        public string ServerIp { get; set; } = "";
    }
}
```

### 3. 自定义验证规则

通过 `ValidateRules` 添加自定义验证规则。

```razor
<IpAddress @bind-Value="IpAddress" ValidateRules="CustomRules" />

@code {
    private string? IpAddress { get; set; }
    
    private List<IValidator> CustomRules =>
        new List<IValidator>
        {
            new IPAddressValidator()  // 自定义验证器
        };
}
```

## 常见问题

### 1. IP 地址格式验证失败

**问题**: 输入 IP 地址后，验证提示格式不正确。

**原因**: 可能是输入的 IP 地址格式不符合 IPv4 标准（如 `192.168.1.256` 超出范围）。

**解决方案**:
- 检查 IP 地址格式是否正确（每段 0-255）
- 使用 `RegularExpression` 数据注解进行格式验证
- 设置 `ParsingErrorMessage` 自定义错误提示

```razor
<IpAddress @bind-Value="IpAddress" 
           ParsingErrorMessage="请输入有效的 IP 地址（如 192.168.1.1）" />

@code {
    private string? IpAddress { get; set; }
}
```

### 2. 组件不显示或显示异常

**问题**: IpAddress 组件不显示，或显示格式异常。

**原因**: 可能是 CSS 样式未正确引入，或组件版本不匹配。

**解决方案**:
- 确保已引入 Bootstrap Blazor 的 CSS 文件
- 检查 Bootstrap Blazor 版本是否支持 IpAddress 组件
- 使用浏览器开发者工具检查元素结构

```html
<!-- 确保在 _Host.cshtml 或 index.html 中引入了 CSS -->
<link rel="stylesheet" href="_content/BootstrapBlazor/css/bootstrap.blazor.bundle.min.css" />
```

### 3. 禁用状态不生效

**问题**: 设置 `IsDisabled="true"` 后，组件仍然可以编辑。

**原因**: 可能是组件未正确接收参数，或存在数据绑定冲突。

**解决方案**:
- 确保 `IsDisabled` 参数正确绑定
- 检查是否存在 `@bind-Value` 导致的数据绑定冲突
- 使用浏览器开发者工具检查组件属性

```razor
<IpAddress @bind-Value="IpAddress" IsDisabled="true" />

@code {
    private string? IpAddress { get; set; }
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 7.0.0 | 2024-01-15 | IpAddress 组件首次发布 |
| 8.0.0 | 2024-11-10 | 新增 `ShowLabelTooltip` 参数；优化 IPv6 支持 |

## 参考链接

- [Bootstrap Blazor 官方文档 - IpAddress](https://www.blazor.zone/ip-address)
- [Bootstrap Blazor API - IpAddress](https://www.blazor.zone/api/IpAddress)
- [RFC 791 - Internet Protocol](https://datatracker.ietf.org/doc/html/rfc791) (IPv4 协议标准)
