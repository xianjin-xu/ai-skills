# DateTimePicker

## 概述

DateTimePicker 组件

> DateTimePicker component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/datetime-picker](https://www.blazor.zone/datetime-picker)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsButton` | `bool` | `}` | 获得/设置 是否显示为按钮样式 默认 false |
| `PickerButtonText` | `string?` | `}` | 获得/设置 选择按钮文本 默认 null 读取资源文件 |
| `ButtonColor` | `Color` | `Color.Primary` | 获得/设置 选择按钮颜色 默认 <see cref="Color.Primary"/> |
| `Format` | `string?` | `-` | 获得/设置 时间格式化字符串 默认值为 null |
| `DateTimeFormat` | `string?` | `}` | 获得/设置 时间格式化字符串 默认值为 "yyyy-MM-dd HH:mm:ss" |
| `DateFormat` | `string?` | `}` | 获得/设置 时间格式化字符串 默认值为 "yyyy-MM-dd" |
| `TimeFormat` | `string?` | `}` | 获得/设置 时间格式化字符串 默认值为 "HH:mm:ss" |
| `FirstDayOfWeek` | `DayOfWeek` | `DayOfWeek.Sunday` | 获得/设置 星期第一天 默认 <see cref="DayOfWeek.Sunday"/> |
| `Icon` | `string?` | `}` | 获得/设置 组件图标 默认 fa-regular fa-calendar-days |
| `ShowIcon` | `bool` | `true` | 获得/设置 是否显示组件图标 默认 true 显示 |
| `Color` | `Color` | `Color.None` | 获得/设置  控件边框颜色样式 默认为 None 显示 |
| `ViewMode` | `DatePickerViewMode` | `DatePickerViewMode.Date` | 获得/设置 组件显示模式 默认为显示年月日模式 |
| `PickTimeMode` | `PickTimeMode` | `PickTimeMode.Dropdown` | 获得/设置 选择时间方式 默认使用 <see cref="PickTimeMode.Dropdown"/> |
| `ShowSidebar` | `bool` | `}` | 获得/设置 是否显示快捷侧边栏 默认不显示 |
| `Task` | `RenderFragment<Func<DateTime,` | `}` | 获得/设置 侧边栏模板 默认 null |
| `MaxValue` | `DateTime?` | `}` | 获得/设置 当前日期最大值 |
| `MinValue` | `DateTime?` | `}` | 获得/设置 当前日期最小值 |
| `AutoClose` | `bool` | `true` | 获得/设置 是否点击日期后自动关闭弹窗 默认 true |
| `IsEditable` | `bool` | `}` | 获得/设置 是否可以编辑内容 默认 false |
| `AutoToday` | `bool` | `true` | - |
| `DisplayMinValueAsEmpty` | `bool` | `true` | - |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件模板 |
| `DatePlaceHolderText` | `string?` | `}` | 获得/设置 日期占位符文本 默认 null 读取资源文件 |
| `DateTimePlaceHolderText` | `string?` | `}` | 获得/设置 日期时间占位符文本 默认 null 读取资源文件 |
| `DayTemplate` | `RenderFragment<DateTime>?` | `}` | 获得/设置 日单元格模板 |
| `DayDisabledTemplate` | `RenderFragment<DateTime>?` | `}` | 获得/设置 禁用日单元格模板 |
| `ShowLunar` | `bool` | `}` | 获得/设置 是否显示中国阴历历法 默认 false |
| `ShowSolarTerm` | `bool` | `}` | 获得/设置 是否显示中国 24 节气 默认 false |
| `ShowFestivals` | `bool` | `}` | 获得/设置 是否显示节日 默认 false |
| `ShowHolidays` | `bool` | `}` | 获得/设置 是否显示休假日 默认 false |
| `DateTime` | `Func<DateTime,` | `}` | 获取/设置 获得自定义禁用日期回调方法，默认 null 内部默认启用数据缓存 可通过 <see cref="EnableDisabledDaysCache"/> 参数关闭 |
| `EnableDisabledDaysCache` | `bool` | `true` | 获得/设置 是否启用获得年自定义禁用日期缓存 |
| `DisplayDisabledDayAsEmpty` | `bool` | `}` | 获得/设置 是否将禁用日期显示为空字符串 默认 false 开启后组件会频繁调用 <see cref="OnGetDisabledDaysCallback"/> 方法，建议外部使用缓存提高性能 |

## 代码示例

### 基本用法

```razor
<DateTimePicker ViewMode="DatePickerViewMode.DateTime" TimeFormat="hh\:mm" IsButton="_isButton"
					Value="@DateTimePickerValue" OnValueChanged="@TimePickerValueChanged">
		<TimePickerSetting ShowClockScale="true" IsAutoSwitch="false" />
	</DateTimePicker>
```

### 基本用法

```razor
<DateTimePicker TValue="DateTimeOffset ?" CustomClass="custom-picker">
		<DayTemplate>
			<span class="custom-cell">
				<span>@context.Day</span>
				<span class="@GetMarkByDay(context)"></span>
			</span>
		</DayTemplate>
	</DateTimePicker>
```

### 基本用法

```razor
<DateTimePicker ViewMode="DatePickerViewMode.DateTime" DisplayText="@Localizer["DisableDayCallbackAllowNullDisplayText"]"
							ShowLabel="true" @bind-Value="@_disabledNullValue" @ref="_picker1"
							OnGetDisabledDaysCallback="OnGetDisabledDaysCallback" DisplayDisabledDayAsEmpty="true">
			</DateTimePicker>
<DateTimePicker ViewMode="DatePickerViewMode.DateTime" DisplayText="@Localizer["DisableDayCallbackNotAllowNullDisplayText"]"
							ShowLabel="true" @bind-Value="@_disabledValue" @ref="_picker2"
							OnGetDisabledDaysCallback="OnGetDisabledDaysCallback">
			</DateTimePicker>
```
