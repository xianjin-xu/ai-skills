# DateTimeRange 日期时间段选择器

## 概述

DateTimeRange 日期时间段选择器组件用于在同一个选择器里选择一段日期时间范围。

> DateTimeRange component is used to select a date-time range within the same picker.

**分类**: 表单组件
**在线演示**: [https://www.blazor.zone/datetime-range](https://www.blazor.zone/datetime-range)

---

## 使用场景

### 1. 基本功能

以「日」为基本单位，选择一段时间。

```razor
<DateTimeRange @bind-Value="StartEndTime" />
```

### 2. 数据双向绑定

点击确认按钮时间选择框值与文本框值一致，通过设置 `AutoClose="true"` 实现自动关闭功能，通过设置 `ShowSelectedValue="true"` 直接显示选中值。

```razor
<DateTimeRange @bind-Value="BindValue" 
           ShowSelectedValue="true" 
           AutoClose="true" />
```

### 3. 显示农历

显示农历、24节气、节日、法定假日功能体验区。需要先安装 `BootstrapBlazor.Holiday` 包并注册服务。

```csharp
// Program.cs
builder.Services.AddBootstrapHolidayService();
```

```razor
<DateTimeRange @bind-Value="RangeValue" 
           ShowLunar="true" 
           ShowSolarTerm="true" 
           ShowFestivals="true" 
           ShowHolidays="true" />
```

### 4. 时间范围 - 最大值和最小值

设置时间的取值范围。

```razor
<DateTimeRange @bind-Value="RangeValue" 
           MinValue="DateTime.Now.AddDays(-30)" 
           MaxValue="DateTime.Now.AddDays(30)" />
```

### 5. 禁用

设置 `IsDisabled` 属性值为 `true` 时，组件禁止输入。

```razor
<DateTimeRange @bind-Value="RangeValue" IsDisabled="true" />
```

### 6. 带快捷键侧边栏

设置 `ShowSidebar` 属性值为 `true` 时，组件显示快捷方式侧边栏。通过设置 `SidebarItems` 参数集合替换组件内置的默认快捷项。

```razor
<DateTimeRange @bind-Value="RangeValue" ShowSidebar="true">
    <SidebarItems>
        <DateTimeRangeSidebarItem Text="今天" Value="..." />
        <DateTimeRangeSidebarItem Text="昨天" Value="..." />
        <DateTimeRangeSidebarItem Text="最近7天" Value="..." />
    </SidebarItems>
</DateTimeRange>
```

### 7. 显示今天按钮

设置 `ShowToday` 属性值为 `true` 时，组件下方显示今天快捷按钮。点击 Today 今天按钮时，时间范围为 `yyyy-MM-dd 00:00:00` 到 `yyyy-MM-dd 23:59:59`。

```razor
<DateTimeRange @bind-Value="RangeValue" ShowToday="true" />
```

### 8. 单选模式

单选模式。

```razor
<DateTimeRange @bind-Value="RangeValue" RenderMode="DateTimeRangeRenderMode.Single" />
```

### 9. 表单中使用

将组件内置到 `ValidateForm` 中使用。

```razor
<ValidateForm>
    <DateTimeRange @bind-Value="RangeValue" />
    <Button ButtonType="ButtonType.Submit" Text="提交" />
</ValidateForm>
```

### 10. 自动关闭

点击侧边栏快捷方式自动关闭弹窗。

```razor
<DateTimeRange @bind-Value="RangeValue" 
           ShowSidebar="true" 
           AutoCloseClickSideBar="true" />
```

### 11. 显示模式

通过设置 `ViewMode="DatePickerViewMode.Year"` 使组件视图为年视图，设置 `ViewMode="DatePickerViewMode.Month"` 使组件视图为月视图。

```razor
<!-- 年视图 -->
<DateTimeRange @bind-Value="YearRange" 
           ViewMode="DatePickerViewMode.Year" 
           DateFormat="yyyy" />

<!-- 月视图 -->
<DateTimeRange @bind-Value="MonthRange" 
           ViewMode="DatePickerViewMode.Month" 
           DateFormat="yyyy-MM" />
```

---

## 参数 (Parameters)

### DateTimeRange 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `AllowNull` | `bool` | `true` | **已弃用** - 获得/设置 是否允许为空 |
| `AutoClose` | `bool` | `false` | 获得/设置 是否在选中日期范围后自动关闭弹窗 |
| `AutoCloseClickSideBar` | `bool` | `false` | 获得/设置 是否点击快捷侧边栏自动关闭弹窗 |
| `ClearButtonText` | `string?` | `null` | 获得/设置 清空按钮文字 |
| `ClearIcon` | `string?` | `fa-solid fa-circle-xmark` | 获得/设置 清空图标 |
| `ConfirmButtonText` | `string?` | `null` | 获得/设置 确定按钮文字 |
| `CustomClass` | `string?` | `null` | 获得/设置 自定义样式 参数 |
| `DateFormat` | `string?` | `yyyy-MM-dd` | 获得/设置 日期格式化字符串 |
| `DateTimeFormat` | `string?` | `yyyy-MM-dd HH:mm:ss` | 获得/设置 日期时间格式化字符串 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `Icon` | `string?` | `null` | 获得/设置 组件图标 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `IsEditable` | `bool` | `false` | 获得/设置 是否可以编辑内容 |
| `MaxValue` | `DateTime` | `DateTime.MaxValue` | 获得/设置 最大值 |
| `MinValue` | `DateTime` | `DateTime.MinValue` | 获得/设置 最小值 |
| `OnClearValue` | `Func<DateTimeRangeValue, Task>?` | `null` | 点击清空按钮回调委托方法 |
| `OnConfirm` | `Func<DateTimeRangeValue, Task>?` | `null` | 点击确认按钮回调委托方法 |
| `OnDateClick` | `Func<DateTime, Task>?` | `null` | 获得/设置 the date value changed event 回调 |
| `OnValueChanged` | `Func<DateTimeRangeValue, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 |
| `Placement` | `Placement` | `Placement.Bottom` | 获得/设置 弹窗位置 |
| `RenderMode` | `DateTimeRangeRenderMode` | `DateTimeRangeRenderMode.Double` | 获得/设置 组件渲染模式 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 |
| `ShowClearButton` | `bool` | `true` | 获得/设置 是否显示清空按钮 |
| `ShowFestivals` | `bool` | `false` | 获得/设置 是否显示节日 |
| `ShowHolidays` | `bool` | `false` | 获得/设置 是否显示休假日 |
| `ShowLabel` | `Nullable<bool>` | `null` | 获得/设置 是否显示前置标签 |
| `ShowLabelTooltip` | `Nullable<bool>` | `null` | 获得/设置 是否显示 Tooltip |
| `ShowLunar` | `bool` | `false` | 获得/设置 是否显示中国阴历历法 |
| `ShowRequired` | `Nullable<bool>` | `null` | 获得/设置 是否显示必填项标记 |
| `ShowSelectedValue` | `bool` | `false` | 获得/设置 是否显示选中的值 |
| `ShowShadow` | `bool` | `true` | 获得/设置 是否显示阴影 |
| `ShowSidebar` | `bool` | `false` | 获得/设置 是否显示快捷侧边栏 |
| `ShowSolarTerm` | `bool` | `false` | 获得/设置 是否显示中国24节气 |
| `ShowToday` | `bool` | `false` | 获得/设置 是否显示今天按钮 |
| `SidebarItems` | `List<DateTimeRangeSidebarItem>?` | `null` | 获得/设置 侧边栏快捷选项集合 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 |
| `TimeFormat` | `string?` | `HH:mm:ss` | 获得/设置 时间格式化字符串 |
| `TodayButtonText` | `string?` | `null` | 获得/设置 今天按钮文字 |
| `ValidateRules` | `List<IValidator>` | `{}` | 获得/设置 自定义验证集合 |
| `Value` | `DateTimeRangeValue?` | `null` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<DateTimeRangeValue>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<DateTimeRangeValue>>?` | `null` | 获得/设置 标识绑定值的表达式 |
| `ViewMode` | `DatePickerViewMode` | `DatePickerViewMode.Date` | 获得/设置 组件显示模式 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnConfirm` | 点击确认按钮回调委托方法 |
| `OnValueChanged` | Value 改变时回调方法 |
| `OnClearValue` | 点击清空按钮回调委托方法 |
| `OnDateClick` | 日期值改变事件回调 |

---

## 子组件

### TimePickerSetting

用于自定义时间选择器的行为。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ShowClockScale` | `bool` | `false` | 获得/设置 是否显示时钟刻度 |
| `IsAutoSwitch` | `bool` | `true` | 获得/设置 是否自动切换 |

---

## 最佳实践

### 1. 选择合适的数据类型

`DateTimeRange` 组件的值类型为 `DateTimeRangeValue`，包含 `Start` 和 `End` 两个 `DateTime?` 属性：

```csharp
public class DateTimeRangeValue
{
    public DateTime? Start { get; set; }
    public DateTime? End { get; set; }
}
```

### 2. 视图模式选择

根据需求选择合适的视图模式：
- `DatePickerViewMode.Date` - 日期选择（默认）
- `DatePickerViewMode.Year` - 年选择
- `DatePickerViewMode.Month` - 月选择

### 3. 格式化字符串

根据不同视图模式设置合适的格式化字符串：
- 日期模式：`DateFormat="yyyy-MM-dd"`
- 年月模式：`DateFormat="yyyy"`
- 月日模式：`DateFormat="MM-dd"`
- 日期时间模式：`DateTimeFormat="yyyy-MM-dd HH:mm:ss"`

### 4. 快捷侧边栏

通过 `ShowSidebar="true"` 显示快捷侧边栏，或自定义 `SidebarItems` 集合。

### 5. 自动关闭

在单选场景下，设置 `AutoClose="true"` 提升用户体验。

### 6. 显示农历和节日

需要先安装 `BootstrapBlazor.Holiday` 包并注册服务：

```csharp
// Program.cs
builder.Services.AddBootstrapHolidayService();
```

然后在组件中使用 `ShowLunar`、`ShowSolarTerm`、`ShowFestivals`、`ShowHolidays` 参数。

---

## 常见问题 (FAQ)

### Q1: 如何获取选中的开始和结束时间？

**A**: 通过 `DateTimeRangeValue.Start` 和 `DateTimeRangeValue.End` 属性获取：

```razor
<DateTimeRange @bind-Value="RangeValue" />

@code {
    private DateTimeRangeValue? RangeValue { get; set; }

    private void PrintRange()
    {
        if (RangeValue != null)
        {
            Console.WriteLine($"开始: {RangeValue.Start}, 结束: {RangeValue.End}");
        }
    }
}
```

### Q2: 如何限制可选择的时间范围？

**A**: 使用 `MinValue` 和 `MaxValue` 参数：

```razor
<DateTimeRange @bind-Value="RangeValue" 
           MinValue="DateTime.Now.AddDays(-7)" 
           MaxValue="DateTime.Now" />
```

### Q3: 如何自定义确认按钮文字？

**A**: 设置 `ConfirmButtonText` 参数：

```razor
<DateTimeRange @bind-Value="RangeValue" ConfirmButtonText="确定选择" />
```

### Q4: 如何显示中国阴历？

**A**: 需要先安装 `BootstrapBlazor.Holiday` 包并注册服务，然后设置 `ShowLunar="true"`：

```razor
<DateTimeRange @bind-Value="RangeValue" ShowLunar="true" />
```

### Q5: 如何自定义时间选择器？

**A**: 使用 `TimePickerSetting` 子组件：

```razor
<DateTimeRange @bind-Value="RangeValue">
    <TimePickerSetting ShowClockScale="true" IsAutoSwitch="false" />
</DateTimeRange>
```

### Q6: 如何实现单选模式？

**A**: 设置 `RenderMode="DateTimeRangeRenderMode.Single"`：

```razor
<DateTimeRange @bind-Value="RangeValue" RenderMode="DateTimeRangeRenderMode.Single" />
```

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 DateTimeRange 组件 |
| 8.0 | 新增 `ShowLunar`、`ShowSolarTerm`、`ShowFestivals`、`ShowHolidays` 参数 |
| 8.0 | 新增 `ShowSelectedValue` 参数 |
