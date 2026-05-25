# Switch (开关)

## 概述

Switch 组件是 Bootstrap Blazor 中提供最普通的开关应用的组件。用于切换两种状态（开/关）。

**主要功能特性**：
- 支持单向/双向数据绑定
- 支持禁用状态（IsDisabled）
- 支持颜色设置（OnColor、OffColor）
- 支持内置文字显示（ShowInnerText、OnInnerText、OffInnerText）
- 支持自定义文本（OnText、OffText）
- 支持可为空类型（DefaultValueWhenNull）
- 支持宽度和高度设置（Width、Height）
- 支持客户端验证（ValidateForm）

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/switch](https://www.blazor.zone/switch)

## 使用场景

### 1. 基础用法

提供最普通的开关应用，点击按钮切换状态。

```razor
<Switch @bind-Value="Model.IsEnabled" />
```

**功能说明**：
- 点击第一个开关有值输出日志
- 开启/关闭状态切换

---

### 2. 禁用状态

通过设置 `IsDisabled` 属性控制组件不可用状态。

```razor
<Switch @bind-Value="Model.IsEnabled" IsDisabled="true" />
```

**功能说明**：
- 关闭状态下的禁用

---

### 3. 开关颜色

通过设置 `OnColor`、`OffColor` 属性值，设置开关状态颜色。

```razor
<Switch @bind-Value="Model.IsEnabled" OnColor="Color.Success" OffColor="Color.Secondary" />
```

**功能说明**：
- 关闭状态的颜色设置

---

### 4. 双向绑定

绑定组件内变量，数据自动同步。

```razor
<Switch @bind-Value="Model.IsEnabled" />
```

**说明**：
- Switch 组件开启双向绑定时，会根据绑定的 Model 属性值去自动获取 `DisplayName` 标签值并且显示为前置 Label
- 通过 `DisplayText` 属性可以自定义显示前置标签
- 或者通过 `ShowLabel` 属性关闭前置标签是否显示

**前置标签显示规则与 BootstrapInput 组件一致**。

---

### 5. 自定义标签

设置 `DisplayText` 值为"自定义标签"。

```razor
<Switch @bind-Value="Model.IsEnabled" DisplayText="启用通知" />
```

**标签显示规则**：
- 无论是否设置 `DisplayText` 值，当 `ShowLabel="true"` 时均显示
- 无论是否设置 `DisplayText` 值，当 `ShowLabel="false"` 时均不显示

---

### 6. 显示内置文字

通过设置 `ShowInnerText` 属性控制组件显示内置文字。

```razor
<Switch @bind-Value="Model.IsEnabled" ShowInnerText="true" />
```

**功能说明**：
- 通过设置 `OnInnerText`、`OffInnerText` 属性更改内置文字
- 默认文字：开/关
- 自定义文字：自定义

---

### 7. 可为空类型的开关

通过设置 `DefaultValueWhenNull` 属性控制 Null 值的默认值，未设置时为 false。

```razor
<Switch @bind-Value="Model.IsEnabled" DefaultValueWhenNull="true" />
```

**功能说明**：
- 关闭状态下的可为空类型处理

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `bool` | `false` | 获得/设置输入组件的值，支持双向绑定 |
| `@bind-Value` | `bool` | `false` | 获得/设置组件值（双向绑定） |
| `DisplayText` | `string?` | `null` | 获得/设置显示名称（前置标签） |
| `ShowLabel` | `bool?` | `null` | 获得/设置是否显示前置标签，默认值为 null，为空时不显示标签 |
| `ShowLabelTooltip` | `bool?` | `null` | 获得/设置是否显示 Tooltip，多用于文字过长导致裁剪时使用，默认 null |
| `OnColor` | `Color` | `Color.Success` | 获得/设置开状态颜色 |
| `OffColor` | `Color` | `Color.Secondary` | 获得/设置关状态颜色 |
| `OnText` | `string?` | `null` | 获得/设置组件 On 时显示的文本 |
| `OffText` | `string?` | `null` | 获得/设置组件 Off 时显示的文本 |
| `OnInnerText` | `string?` | `null` | 获得/设置组件 On 时内置显示文本 |
| `OffInnerText` | `string?` | `null` | 获得/设置组件 Off 时内置显示文本 |
| `ShowInnerText` | `bool` | `false` | 获得/设置是否显示内置文字，默认 false 显示 |
| `IsDisabled` | `bool` | `false` | 获得/设置是否禁用，默认为 false |
| `DefaultValueWhenNull` | `bool` | `false` | 获得/设置 Null 值的默认值，未设置时为 false |
| `Width` | `int` | `40` | 获得/设置组件宽度，默认 40 |
| `Height` | `int` | `20` | 获得/设置控件高度，默认 20px |
| `OnValueChanged` | `Func<bool, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置类型转化失败格式化字符串，默认为 null |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置必填项错误文本，默认为 null 未设置 |
| `ShowRequired` | `bool?` | `null` | 获得/设置是否显示必填项标记，默认为 null 未设置 |
| `SkipValidate` | `bool` | `false` | 获得/设置是否不进行验证，默认为 false |
| `ValidateRules` | `List<IValidator>?` | `null` | 获得/设置自定义验证集合 |
| `ValueChanged` | `EventCallback<bool>` | - | 获得/设置用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<bool>>?` | `null` | 获得/设置标识绑定值的表达式 |
| `Id` | `string?` | `null` | 获得/设置组件 id 属性 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置用户自定义属性 |

## 最佳实践

### 1. 数据绑定最佳实践

**推荐做法**：使用 `@bind-Value` 进行双向绑定。

```razor
<Switch @bind-Value="Model.IsEnabled" />
```

**标签显示规则**：
- 组件会自动查找模型属性的 `Display` 或 `DisplayName` 特性作为标签文本
- 可以通过 `DisplayText` 参数自定义标签文本
- 可以通过 `ShowLabel="false"` 隐藏标签

---

### 2. 自定义开/关文本最佳实践

**场景**：需要自定义开关状态的显示文本（如"是/否"、"启用/禁用"）。

**推荐做法**：使用 `OnText`、`OffText` 或 `OnInnerText`、`OffInnerText` 参数。

```razor
@* 方式1：显示外部文本 *@
<Switch @bind-Value="Model.IsEnabled" 
        OnText="启用" 
        OffText="禁用" />

@* 方式2：显示内部文字 *@
<Switch @bind-Value="Model.IsEnabled" 
        ShowInnerText="true"
        OnInnerText="是" 
        OffInnerText="否" />
```

---

### 3. 颜色设置最佳实践

**场景**：需要根据开关状态显示不同颜色。

**推荐做法**：使用 `OnColor`、`OffColor` 参数。

```razor
<Switch @bind-Value="Model.IsEnabled" 
        OnColor="Color.Success" 
        OffColor="Color.Danger" />
```

**常用颜色组合**：
- 成功/危险：`Color.Success` / `Color.Danger`
- 主要/次要：`Color.Primary` / `Color.Secondary`
- 警告/信息：`Color.Warning` / `Color.Info`

---

### 4. 可为空类型处理最佳实践

**场景**：绑定 `bool?` 类型时，需要处理 null 值。

**推荐做法**：使用 `DefaultValueWhenNull` 参数设置默认值。

```razor
<Switch @bind-Value="Model.IsEnabledNullable" DefaultValueWhenNull="false" />
```

**说明**：
- 当 `Value` 为 null 时，组件使用 `DefaultValueWhenNull` 作为默认值
- 未设置 `DefaultValueWhenNull` 时，默认值为 `false`

---

### 5. 常见错误

**错误 1**：未设置 `@bind-Value`，只设置了 `Value`

**解决方法**：使用 `@bind-Value` 进行双向绑定，或者同时设置 `Value` 和 `ValueChanged`。

**错误 2**：绑定 `bool?` 类型时，组件显示异常

**解决方法**：设置 `DefaultValueWhenNull="false"` 或 `DefaultValueWhenNull="true"` 明确指定 null 时的默认值。

**错误 3**：在 `ValidateForm` 中使用时未触发验证

**解决方法**：确保 `Value` 正确绑定，并在模型中使用数据注解进行验证。

---

## 相关组件

- `Toggle` - 开关组件（类似 Switch，但外观不同）
- `Checkbox` - 多选框组件（用于多选场景）
- `RadioList` - 单选框组件（用于单选场景）
- `ValidateForm` - 验证表单组件

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 Switch 组件的核心功能和使用方法。
