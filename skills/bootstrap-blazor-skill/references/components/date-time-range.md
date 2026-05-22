# DateTimeRange

## 概述

DateTimeRange 时间范围组件

> DateTimeRange component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/datetime-range](https://www.blazor.zone/datetime-range)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsEditable` | `bool` | `}` | 获得/设置 是否可以编辑内容 默认 false |
| `AutoCloseClickSideBar` | `bool` | `}` | 获得/设置 是否点击快捷侧边栏自动关闭弹窗 默认 false |
| `AutoClose` | `bool` | `}` | 获得/设置 是否 to automatically close the popup after a date range is selected. 默认为 false |
| `ShowSelectedValue` | `bool` | `}` | 获得/设置 是否 show the selected value. 默认为 false |
| `ClearButtonText` | `string?` | `}` | 获得/设置 清空按钮文字 |
| `ClearIcon` | `string?` | `}` | 获得/设置 清空图标 默认 fa-solid fa-circle-xmark |
| `ViewMode` | `DatePickerViewMode` | `DatePickerViewMode.Date` | 获得/设置 组件显示模式 默认为显示年月日模式 |
| `RenderMode` | `DateTimeRangeRenderMode` | `DateTimeRangeRenderMode.Double` | 获得/设置 组件显示模式 默认为显示年月日模式 |
| `TodayButtonText` | `string?` | `}` | 获得/设置 今天按钮文字 |
| `ConfirmButtonText` | `string?` | `}` | 获得/设置 确定按钮文字 |
| `MaxValue` | `DateTime` | `DateTime.MaxValue` | 获得/设置 最大值 |
| `MinValue` | `DateTime` | `DateTime.MinValue` | 获得/设置 最小值 |
| `AllowNull` | `bool` | `-` | 获得/设置 是否允许为空 默认为 true |
| `ShowClearButton` | `bool` | `true` | 获得/设置 是否显示清空按钮 默认 true |
| `Icon` | `string?` | `}` | 获得/设置 组件图标 |
| `ShowToday` | `bool` | `}` | 获得/设置 是否显示今天按钮 默认为 false |
| `ShowSidebar` | `bool` | `}` | 获得/设置 是否显示快捷侧边栏 默认不显示 |
| `SidebarItems` | `List<DateTimeRangeSidebarItem>?` | `}` | 获得/设置 侧边栏快捷选项集合 |
| `Task` | `Func<DateTimeRangeValue,` | `}` | 点击确认按钮回调委托方法 |
| `TimeFormat` | `string?` | `}` | 获得/设置 时间格式化字符串 默认值为 "HH:mm:ss" |
| `DateFormat` | `string?` | `}` | 获得/设置 时间格式化字符串 默认值为 "yyyy-MM-dd" |
| `DateTimeFormat` | `string?` | `}` | 获得/设置 时间格式化字符串 默认值为 "yyyy-MM-dd HH:mm:ss" |
| `ShowLunar` | `bool` | `}` | 获得/设置 是否显示中国阴历历法 默认 false |
| `ShowSolarTerm` | `bool` | `}` | 获得/设置 是否显示中国 24 节气 默认 false |
| `ShowFestivals` | `bool` | `}` | 获得/设置 是否显示节日 默认 false |
| `ShowHolidays` | `bool` | `}` | 获得/设置 是否显示休假日 默认 false |

## 代码示例

### 基本用法

```razor
<DateTimeRange @bind-Value="@NormalDateTimeRangeValue" OnConfirm="OnNormalConfirm" ShowSidebar="true" ViewMode="DatePickerViewMode.Year" IsEditable="true" DateFormat="yyyy">
        <TimePickerSetting ShowClockScale="true" IsAutoSwitch="false" />
    </DateTimeRange>
```

### 基本用法

```razor
<DateTimeRange @bind-Value="@BindValueDemoDateTimeRangeValue" OnValueChanged="v => BindValueDemoOnValueChanged(v, 1)"
                           ShowLunar="_showLunar" ShowSolarTerm="_showSolarTerm"
                           ShowFestivals="_showFestivals" ShowHolidays="_showHolidays"
                           ShowSelectedValue="true" AutoClose="true"></DateTimeRange>
```

### 基本用法

```razor
<DateTimeRange Value="@SidebarDateTimeRangeValue" ShowSidebar="true"></DateTimeRange>
```

### 基本用法

```razor
<DateTimeRange @bind-Value="@YearRangeValue" ViewMode="DatePickerViewMode.Year" DateFormat="yyyy">
            </DateTimeRange>
<DateTimeRange @bind-Value="@MonthRangeValue" ViewMode="DatePickerViewMode.Month" DateFormat="yyyy-MM">
            </DateTimeRange>
```
