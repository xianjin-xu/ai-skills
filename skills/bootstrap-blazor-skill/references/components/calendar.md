# Calendar (日历框)

## 概述

`Calendar` 组件是**按照日历形式展示数据的容器**。当数据是日期或按照日期划分时，例如日程、课表、价格日历等，可以使用日历框展示。

目前支持年/月切换。

**主要特性**：
- 支持月视图/周视图（ViewMode）
- 支持数据双向绑定（Value）
- 支持自定义单元格模板（CellTemplate）
- 支持自定义头部模板（HeaderTemplate）
- 支持自定义内容模板（BodyTemplate）
- 可设置星期第一天（FirstDayOfWeek）

**在线演示**: https://www.blazor.zone/calendar

---

## 使用场景

### 1. 基础用法（日历显示）

基础的日历显示，展示当前月份的日期。

```razor
<!-- 基础日历 -->
<Calendar Value="SelectedDate" />

@code {
    private DateTime SelectedDate { get; set; } = DateTime.Now;
}
```

---

### 2. 数据双向绑定（Value）

日历框选择时间时数据自动更新。

```razor
<!-- 双向绑定 -->
<Calendar @bind-Value="SelectedDate" />

<p>选择的日期：@SelectedDate.ToString("yyyy-MM-dd")</p>

@code {
    private DateTime SelectedDate { get; set; } = DateTime.Now;
}
```

---

### 3. 周视图（ViewMode）

通过设置 `ViewMode` 为 `CalendarViewMode.Week` 显示周视图。

```razor
<!-- 周视图 -->
<Calendar Value="SelectedDate" ViewMode="CalendarViewMode.Week" />

@code {
    private DateTime SelectedDate { get; set; } = DateTime.Now;
}
```

**ViewMode 选项**：
- `CalendarViewMode.Month` - 月视图（默认）
- `CalendarViewMode.Week` - 周视图

---

### 4. 自定义单元格模板（CellTemplate）

通过设置 `CellTemplate` 自定义单元格模板。

```razor
<!-- 自定义单元格 -->
<Calendar Value="SelectedDate">
    <CellTemplate>
        <div class="text-center">
            <div>@context.Date.Day</div>
            @if (context.Date.Day % 3 == 0)
            {
                <small class="text-muted">事件</small>
            }
        </div>
    </CellTemplate>
</Calendar>

@code {
    private DateTime SelectedDate { get; set; } = DateTime.Now;
}
```

**CellTemplateContext 属性**：
- `Date` (DateTime) - 当前单元格日期
- `IsCurrentMonth` (bool) - 是否当前月
- `IsToday` (bool) - 是否今天

---

### 5. 自定义头部模板（HeaderTemplate）

通过设置 `HeaderTemplate` 自定义头部模板。

```razor
<!-- 自定义头部 -->
<Calendar Value="SelectedDate">
    <HeaderTemplate>
        <div class="d-flex justify-content-between align-items-center p-2">
            <Button Size="Size.Small" @onclick="OnPrevMonth">上月</Button>
            <span>@context.Year 年 @context.Month 月</span>
            <Button Size="Size.Small" @onclick="OnNextMonth">下月</Button>
        </div>
    </HeaderTemplate>
</Calendar>

@code {
    private DateTime SelectedDate { get; set; } = DateTime.Now;
    
    private void OnPrevMonth()
    {
        SelectedDate = SelectedDate.AddMonths(-1);
    }
    
    private void OnNextMonth()
    {
        SelectedDate = SelectedDate.AddMonths(1);
    }
}
```

---

### 6. 自定义内容模板（BodyTemplate）

配合 `HeaderTemplate` 自定义呈现 UI。

```razor
<!-- 自定义内容 -->
<Calendar Value="SelectedDate" ViewMode="CalendarViewMode.Month">
    <HeaderTemplate>
        <div class="text-center p-2">
            <strong>@(SelectedDate.Year) 年 @(SelectedDate.Month) 月</strong>
        </div>
    </HeaderTemplate>
    <BodyTemplate>
        <div class="p-2">
            @foreach (var day in context.Days)
            {
                <div class="text-center">@day.Day</div>
            }
        </div>
    </BodyTemplate>
</Calendar>

@code {
    private DateTime SelectedDate { get; set; } = DateTime.Now;
}
```

---

## 参数 (Parameters)

### Calendar 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `DateTime` | `DateTime.Now` | 获得/设置 组件值 |
| `ViewMode` | `CalendarViewMode` | `CalendarViewMode.Month` | 获得/设置 是否显示周视图 默认为 月视图 |
| `FirstDayOfWeek` | `DayOfWeek` | `DayOfWeek.Sunday` | 获得/设置 星期第一天 默认 |
| `ShowYearButtons` | `bool` | `true` | 获得/设置 是否显示年按钮 |
| `CellTemplate` | `RenderFragment<CalendarCellValue>?` | `null` | 获得/设置 单元格模板 |
| `HeaderTemplate` | `RenderFragment?` | `null` | 获得/设置 列头模板 |
| `BodyTemplate` | `RenderFragment<BodyTemplateContext>?` | `null` | 获得/设置 Body 模板仅 有效 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 周内容 时有效 |
| `ValueChanged` | `EventCallback<DateTime>` | - | 获得/设置 值改变时回调委托 |
| `OnValueChanged` | `Func<DateTime, Task>?` | `null` | 获得/设置 值改变时回调委托 |

---

## 模板上下文 (Template Context)

### CalendarCellValue (CellTemplate 上下文)

| 属性名 | 类型 | 说明 |
|--------|------|------|
| `Date` | `DateTime` | 当前单元格日期 |
| `IsCurrentMonth` | `bool` | 是否当前月 |
| `IsToday` | `bool` | 是否今天 |

### BodyTemplateContext (BodyTemplate 上下文)

| 属性名 | 类型 | 说明 |
|--------|------|------|
| `Days` | `List<DateTime>` | 当前视图的所有日期 |
| `Year` | `int` | 当前年份 |
| `Month` | `int` | 当前月份 |

---

## 最佳实践

1. **选择合适的 ViewMode**：月视图用 `Month`（默认），周视图用 `Week`
2. **使用 Value 双向绑定**：通过 `@bind-Value` 实现日期选择双向绑定
3. **自定义单元格**：通过 `CellTemplate` 自定义单元格内容（如添加事件标记）
4. **自定义头部**：通过 `HeaderTemplate` 自定义头部（如添加切换按钮）
5. **与 DatePicker 的区别**：`Calendar` 是日历容器（展示数据），`DatePicker` 是日期选择器（表单输入）
6. **性能优化**：单元格模板避免过于复杂，大数据可考虑虚拟滚动
