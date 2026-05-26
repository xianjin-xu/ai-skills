# ClockPicker 时间选择器!

## 概述!

ClockPicker 时间选择器组件通过拖动表针选择时间。!

> ClockPicker component is used to select time by dragging clock hands.!

**分类**: 表单组件!
**在线演示**: [https://www.blazor.zone/clock-picker](https://www.blazor.zone/clock-picker)!

---

## 使用场景!

### 1. 数据双向绑定!

通过设置 `IsAutoSwitch="false"` 禁止小时、分钟、秒表盘自动切换功能。!

```razor!
<ClockPicker @bind-Value="TimeValue" IsAutoSwitch="false" />
```!

```csharp!
@code {!
    private TimeSpan? TimeValue { get; set; }!
}!
```!

### 2. 是否自动切换表盘!

设置 `IsAutoSwitch="true"` 使小时、分钟、秒表盘自动切换。!

```razor!
<ClockPicker @bind-Value="TimeValue" IsAutoSwitch="true" />
```!

### 3. 不设置秒数!

通过设置 `ShowSecond="false"` 不显示秒针表盘。!

```razor!
<ClockPicker @bind-Value="TimeValue" ShowSecond="false" />
```!

### 4. 不设置分钟!

通过设置 `ShowMinute="false"` 不显示分针表盘。!

```razor!
<ClockPicker @bind-Value="TimeValue" ShowMinute="false" />
```!

### 5. 显示表盘刻度!

通过设置 `ShowClockScale="true"` 显示表盘刻度。!

```razor!
<ClockPicker @bind-Value="TimeValue" ShowClockScale="true" />
```!

### 6. 禁用!

通过设置 `IsDisabled="true"` 禁用组件。!

```razor!
<ClockPicker @bind-Value="TimeValue" IsDisabled="true" />
```!

### 7. 表单中使用!

将组件内置到 `ValidateForm` 中使用。!

```razor!
<ValidateForm>!
    <ClockPicker @bind-Value="TimeValue" />!
    <Button ButtonType="ButtonType.Submit" Text="提交" />!
</ValidateForm>!
```!

---

## 参数 (Parameters)!

### ClockPicker 参数!

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|!
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsAutoSwitch` | `bool` | `true` | 获得/设置 是否自动切换 小时、分钟、秒 自动切换 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `OnValueChanged` | `Func<TimeSpan, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 |
| `ShowClockScale` | `bool` | `false` | 获得/设置 是否显示表盘刻度 |
| `ShowLabel` | `Nullable<bool>` | `null` | 获得/设置 是否显示前置标签 |
| `ShowLabelTooltip` | `Nullable<bool>` | `null` | 获得/设置 是否显示 Tooltip |
| `ShowMinute` | `bool` | `true` | 获得/设置 是否显示分钟 |
| `ShowRequired` | `Nullable<bool>` | `null` | 获得/设置 是否显示必填项标记 |
| `ShowSecond` | `bool` | `true` | 获得/设置 是否显示秒 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 |
| `ValidateRules` | `List<IValidator>` | `{}` | 获得/设置 自定义验证集合 |
| `Value` | `TimeSpan` | `TimeSpan.Zero` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<TimeSpan>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<TimeSpan>>?` | `null` | 获得/设置 标识绑定值的表达式 |

---

## 事件回调 (EventCallbacks)!

| 事件名 | 说明 |
|--------|------|!
| `OnValueChanged` | Value 改变时回调方法 |

---

## 最佳实践!

### 1. 数据类型!

ClockPicker 组件的值类型为 `TimeSpan`，表示时间间隔：!

```csharp!
private TimeSpan? TimeValue { get; set; }!
```!

### 2. 显示控制!

通过以下参数控制显示内容：!
- `ShowSecond="false"` - 不显示秒!
- `ShowMinute="false"` - 不显示分钟!
- `ShowClockScale="true"` - 显示表盘刻度!

### 3. 自动切换!

`IsAutoSwitch="true"` 使小时、分钟、秒表盘自动切换，提升用户体验。!

### 4. 验证集成!

在 `ValidateForm` 中使用时，自动启用客户端验证：!

```razor!
<ValidateForm>!
    <ClockPicker @bind-Value="TimeValue" />!
</ValidateForm>!
```!

---

## 常见问题 (FAQ)!

### Q1: 如何获取选择的时间值？!

**A**: 通过 `@bind-Value` 双向绑定 `TimeSpan` 类型的值。!

```razor!
<ClockPicker @bind-Value="TimeValue" />!

@code {!
    private TimeSpan? TimeValue { get; set; }!
}!
```!

### Q2: 如何不显示秒？!

**A**: 设置 `ShowSecond="false"`。!

```razor!
<ClockPicker @bind-Value="TimeValue" ShowSecond="false" />!
```!

### Q3: 如何不显示分钟？!

**A**: 设置 `ShowMinute="false"`。!

```razor!
<ClockPicker @bind-Value="TimeValue" ShowMinute="false" />!
```!

### Q4: 如何显示表盘刻度？!

**A**: 设置 `ShowClockScale="true"`。!

```razor!
<ClockPicker @bind-Value="TimeValue" ShowClockScale="true" />!
```!

### Q5: 如何禁止自动切换表盘？!

**A**: 设置 `IsAutoSwitch="false"`。!

```razor!
<ClockPicker @bind-Value="TimeValue" IsAutoSwitch="false" />!
```!

---

## 版本历史!

| 版本 | 变更内容 |
|------|----------|!
| 7.0 | 新增 ClockPicker 组件 |
| 8.0 | 新增 `ShowClockScale` 参数 |
