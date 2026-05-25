# InputGroup 输入组!

## 概述!

InputGroup 输入组组件可以在 Input 的前后可以增加与一些标签和按钮，拼成一组。其排版格式紧凑，非常适合单行多列的场景，比如搜索等。!

> InputGroup component allows adding labels and buttons before/after Input, grouped together. Its layout is compact, suitable for single-row multi-column scenarios like search.!

**分类**: 表单组件!
**在线演示**: [https://www.blazor.zone/input-group](https://www.blazor.zone/input-group)!

---

## 使用场景!

### 1. 基础用法!

在 Input 前增加标签，或者在 Input 后增加 Button。!

```razor!
<InputGroup>
    <Input AddOnButtonText="搜索" PlaceHolder="请输入用户名" />
</InputGroup>
```!

### 2. 自定义宽度!

通过设置 `Width` 参数，自定义标签宽度。!

```razor!
<InputGroup Width="100px">
    <Input PlaceHolder="自定义宽度" />
</InputGroup>
```!

### 3. 增加多个组件!

InputGroup 里面可以增加很多组件。!

```razor!
<InputGroup>
    <BootstrapInput PlaceHolder="距离" />
    <BootstrapInput PlaceHolder="单位" />
    <Button Text="确认" />
</InputGroup>
```!

### 4. 下拉框组合!

往 InputGroup 里面增加 Select。!

```razor!
<InputGroup>
    <Select TValue="string" Items="SelectItems" />
    <Input PlaceHolder="请输入内容" />
</InputGroup>
```!

### 5. 验证表单中!

内置到 `ValidateForm` 中使用。!

```razor!
<ValidateForm>
    <InputGroup>
        <Input PlaceHolder="姓名" @bind-Value="Name" />
        <Button Text="检查" />
    </InputGroup>
</ValidateForm>
```!

### 6. 复选框组合!

往 InputGroup 里面增加 Checkbox 或者 CheckboxList。!

```razor!
<InputGroup>
    <Checkbox Text="复选项目" />
    <Input PlaceHolder="请输入内容" />
</InputGroup>
```!

### 7. 单选框组合!

往 InputGroup 里面增加 RadioList。!

```razor!
<InputGroup>
    <RadioList Items="RadioItems" @bind-Value="RadioValue" />
    <Input PlaceHolder="请输入内容" />
</InputGroup>
```!

### 8. SlideButton 组合!

往 InputGroup 里面增加 SlideButton。!

```razor!
<InputGroup>
    <SlideButton Text="SlideButton Header" />
    <Input PlaceHolder="请输入内容" />
</InputGroup>
```!

### 9. DateTimePicker/Range 组合!

往 InputGroup 里面增加 DateTimePicker 或者 DateTimeRange。!

```razor!
<InputGroup>
    <DateTimePicker @bind-Value="DateTimeValue" />
    <Button Text="确认" />
</InputGroup>
```!

### 10. Dropdown 组合!

往 InputGroup 里面增加 Dropdown。!

```razor!
<InputGroup>
    <Dropdown Items="DropdownItems" />
    <Input PlaceHolder="请输入内容" />
</InputGroup>
```!

---

## 参数 (Parameters)!

### InputGroup 参数!

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|!
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件 |
| `Width` | `string?` | `null` | 获得/设置 标签宽度 |

---

## 子组件!

### InputGroup 可包含的子组件!

InputGroup 是一个容器组件，可以包含以下子组件：
- `Input` / `BootstrapInput` - 输入框
- `Button` - 按钮
- `Select` / `SelectTable` / `MultiSelect` - 选择器
- `Checkbox` / `CheckboxList` - 复选框
- `Radio` / `RadioList` - 单选框
- `DateTimePicker` / `DateTimeRange` - 日期选择器
- `Dropdown` - 下拉菜单
- `SlideButton` - 滑动按钮
- 其他任意 Blazor 组件!

---

## 最佳实践!

### 1. 布局特点!

InputGroup 的排版格式紧凑，所有子组件在同一行显示，适合搜索框、组合输入等场景。!

### 2. 常见组合!

**搜索框组合**：!
```razor!
<InputGroup>
    <Dropdown Items="SearchTypes" />
    <Input PlaceHolder="搜索关键词" @bind-Value="Keyword" />
    <Button Icon="fa-solid fa-search" OnClick="OnSearch" />
</InputGroup>
```!

**表单组合**：!
```razor!
<InputGroup>
    <BootstrapInput PlaceHolder="姓" @bind-Value="FirstName" />
    <BootstrapInput PlaceHolder="名" @bind-Value="LastName" />
    <Button Text="确认" ButtonType="ButtonType.Submit" />
</InputGroup>
```!

### 3. 验证集成!

在 `ValidateForm` 中使用时，自动启用客户端验证。!

---

## 常见问题 (FAQ)!

### Q1: 如何在 Input 前加标签？!

**A**: 直接在 InputGroup 中放置标签或按钮：!

```razor!
<InputGroup>
    <span class="input-group-text">用户名</span>
    <Input PlaceHolder="请输入用户名" />
</InputGroup>
```!

### Q2: 如何自定义标签宽度？!

**A**: 使用 `Width` 参数：!

```razor!
<InputGroup Width="120px">
    <span class="input-group-text">用户名</span>
    <Input PlaceHolder="请输入用户名" />
</InputGroup>
```!

### Q3: 如何组合多个组件？!

**A**: 在 InputGroup 中放置多个组件：!

```razor!
<InputGroup>
    <Select Items="Types" />
    <Input PlaceHolder="内容" />
    <Button Text="搜索" />
</InputGroup>
```!

### Q4: 如何使用日期选择器？!

**A**: 在 InputGroup 中放置 DateTimePicker：!

```razor!
<InputGroup>
    <DateTimePicker @bind-Value="DateValue" />
    <Button Text="确认" />
</InputGroup>
```!

### Q5: 如何验证表单？!

**A**: 放置在 `ValidateForm` 中：!

```razor!
<ValidateForm>
    <InputGroup>
        <Input @bind-Value="InputValue" />
    </InputGroup>
</ValidateForm>
```!

---

## 版本历史!

| 版本 | 变更内容 |
|------|----------|!
| 7.0 | 新增 InputGroup 组件 |
