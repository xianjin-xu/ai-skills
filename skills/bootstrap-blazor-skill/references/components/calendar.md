# Calendar

## 概述

日历框组件

> Calendar component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/calendar](https://www.blazor.zone/calendar)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `DateTime` | `}` | 获得/设置 组件值 |
| `Task` | `Func<DateTime,` | `}` | 获得/设置 值改变时回调委托 |
| `ViewMode` | `CalendarViewMode` | `}` | 获得/设置 是否显示周视图 默认为 <see cref="CalendarViewMode.Month"/> 月视图 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 周内容 <see cref="CalendarViewMode.Week"/> 时有效 |
| `HeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 列头模板 |
| `BodyTemplate` | `RenderFragment<BodyTemplateContext>?` | `}` | 获得/设置 Body 模板仅 <see cref="CalendarViewMode.Month"/> 有效 |
| `CellTemplate` | `RenderFragment<CalendarCellValue>?` | `}` | 获得/设置 单元格模板 |
| `ShowYearButtons` | `bool` | `true` | 获得/设置 是否显示年按钮 |
| `FirstDayOfWeek` | `DayOfWeek` | `DayOfWeek.Sunday` | 获得/设置 星期第一天 默认 <see cref="DayOfWeek.Sunday"/> |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<DateTime>` | 获得/设置 值改变时回调委托 |

## 代码示例

### 基本用法

```razor
<Calendar>
        <CellTemplate>
            <td class="@context.DefaultCss">
                <div class="calendar-day">
                    <div>@context.CellValue.Day</div>
                </div>
            </td>
        </CellTemplate>
    </Calendar>
```

### 基本用法

```razor
<Calendar ViewMode="HeaderTemplateViewMode">
        <HeaderTemplate>
            <CalendarHeaderTemplate ViewMode="HeaderTemplateViewMode"></CalendarHeaderTemplate>
        </HeaderTemplate>
        <BodyTemplate>
            <CalendarBodyTemplate Context="@context"></CalendarBodyTemplate>
        </BodyTemplate>
        <ChildContent>
            <CalendarChildContent></CalendarChildContent>
        </ChildContent>
    </Calendar>
```

### 基本用法

```razor
<Calendar ViewMode="CalendarViewMode.Week">
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td rowspan="4"><div class="less ch">@Localizer["Chinese"]</div></td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["Chinese"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["English"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td>@Localizer["Math"]</td>
            <td rowspan="3"><div class="less en">@Localizer["English"]</div></td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["English"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["English"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["English"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
        <tr>
            <td style="background-color: #f8f9fa;" colspan="7">午休</td>
        </tr>
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["Chinese"]</td>
            <td>@Localizer["English"]</td>
            <td>@Localizer["Math"]</td>
            <td>@Localizer["English"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
        <tr>
            <td class="none">@Localizer["None"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td>@Localizer["Study"]</td>
            <td class="none">@Localizer["None"]</td>
        </tr>
    </Calendar>
```

### 基本用法

```razor
<Calendar @bind-Value="CrewInfoValue">
        <CellTemplate>
            <td class="@context.DefaultCss">
                <CalendarCrewCell @bind-Value="@context" Crews="GetCrewsByDate(context.CellValue)" />
            </td>
        </CellTemplate>
    </Calendar>
```
