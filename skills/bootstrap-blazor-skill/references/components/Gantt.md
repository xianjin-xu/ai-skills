# Gantt (甘特图)

## 概述

`Gantt` 组件用于**显示和管理项目任务的甘特图**。组件支持基础任务显示、视图模式切换、任务时间编辑、进度更新等功能。

**主要特性**：
- 支持基础任务显示（任务名称、开始时间、结束时间、进度）
- 支持视图模式切换（`Quarter Day`、`Half Day`、`Day`、`Week`、`Month`）
- 支持任务时间改变事件（`OnDataChanged`）
- 支持任务进度改变事件（`OnProgressChanged`）
- 支持任务点击事件（`OnClick`）
- 支持自定义甘特图配置（`Option`）
- 支持数据源绑定（`Items`）

**在线演示**: https://www.blazor.zone/gantt

---

## 使用场景

### 1. 基础用法（简单甘特图）

通过 `Items` 参数绑定数据源，显示基础甘特图。

```razor
<!-- 基础甘特图 -->
<Gantt Items="Tasks" />

@code {
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "2", 
            Name = "Write new content", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "3", 
            Name = "Apply new styles", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "4", 
            Name = "Review", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "5", 
            Name = "Deploy", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "6", 
            Name = "Go Live!", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
}
```

---

### 2. 改变视图模式（change_view_mode）

切换视图模式调用 `change_view_mode` 方法，支持 `Quarter Day`、`Half Day`、`Day`、`Week`、`Month` 等视图模式。

```razor
<!-- 改变视图模式 -->
<Gantt @ref="GanttRef" Items="Tasks" />

<div class="btn-group">
    <Button OnClick="() => ChangeViewMode(ViewMode.QuarterDay)">Quarter Day</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.HalfDay)">Half Day</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.Day)">Day</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.Week)">Week</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.Month)">Month</Button>
</div>

@code {
    private Gantt GanttRef { get; set; }
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
    
    private void ChangeViewMode(ViewMode mode)
    {
        GanttRef.ChangeViewMode(mode);
    }
}
```

**说明**：`ViewMode` 枚举值包括：
- `QuarterDay`：季度日视图
- `HalfDay`：半日视图
- `Day`：日视图
- `Week`：周视图
- `Month`：月视图

---

### 3. 任务点击事件（OnClick）

通过 `OnClick` 参数设置任务点击事件。

```razor
<!-- 任务点击事件 -->
<Gantt Items="Tasks" OnClick="OnTaskClick" />

@code {
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
    
    private async Task OnTaskClick(GanttItem item)
    {
        // 处理任务点击事件
        Console.WriteLine($"点击了任务：{item.Name}");
        await Task.CompletedTask;
    }
}
```

---

### 4. 任务时间改变事件（OnDataChanged）

通过 `OnDataChanged` 参数设置任务时间改变事件。

```razor
<!-- 任务时间改变事件 -->
<Gantt Items="Tasks" OnDataChanged="OnTaskDataChanged" />

@code {
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
    
    private async Task OnTaskDataChanged(GanttItem item, string startTime, string endTime)
    {
        // 处理任务时间改变事件
        Console.WriteLine($"任务 {item.Name} 时间改变：{startTime} - {endTime}");
        
        // 更新数据源
        item.Start = DateTime.Parse(startTime);
        item.End = DateTime.Parse(endTime);
        
        await Task.CompletedTask;
    }
}
```

---

### 5. 任务进度改变事件（OnProgressChanged）

通过 `OnProgressChanged` 参数设置任务进度改变事件。

```razor
<!-- 任务进度改变事件 -->
<Gantt Items="Tasks" OnProgressChanged="OnTaskProgressChanged" />

@code {
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
    
    private async Task OnTaskProgressChanged(GanttItem item, int progress)
    {
        // 处理任务进度改变事件
        Console.WriteLine($"任务 {item.Name} 进度改变：{progress}%");
        
        // 更新数据源
        item.Progress = progress;
        
        await Task.CompletedTask;
    }
}
```

---

### 6. 自定义甘特图配置（Option）

通过 `Option` 参数设置甘特图配置项。

```razor
<!-- 自定义甘特图配置 -->
<Gantt Items="Tasks" Option="GanttOption" />

@code {
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
    
    private GanttOption GanttOption { get; set; } = new GanttOption
    {
        // 配置甘特图选项
        // 例如：设置语言、日期格式等
    };
}
```

---

### 7. 完整示例（包含所有功能）

```razor
<!-- 完整甘特图示例 -->
<Gantt 
    Items="Tasks" 
    Option="GanttOption"
    OnClick="OnTaskClick"
    OnDataChanged="OnTaskDataChanged"
    OnProgressChanged="OnTaskProgressChanged" />

<div class="btn-group mb-3">
    <Button OnClick="() => ChangeViewMode(ViewMode.QuarterDay)">Quarter Day</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.HalfDay)">Half Day</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.Day)">Day</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.Week)">Week</Button>
    <Button OnClick="() => ChangeViewMode(ViewMode.Month)">Month</Button>
</div>

@code {
    private Gantt GanttRef { get; set; }
    private List<GanttItem> Tasks { get; set; } = new List<GanttItem>
    {
        new GanttItem 
        { 
            Id = "1", 
            Name = "Redesign website", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "2", 
            Name = "Write new content", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "3", 
            Name = "Apply new styles", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "4", 
            Name = "Review", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "5", 
            Name = "Deploy", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        },
        new GanttItem 
        { 
            Id = "6", 
            Name = "Go Live!", 
            Start = new DateTime(2026, 9, 25), 
            End = new DateTime(2026, 10, 18),
            Progress = 0
        }
    };
    
    private GanttOption GanttOption { get; set; } = new GanttOption();
    
    private void ChangeViewMode(ViewMode mode)
    {
        GanttRef.ChangeViewMode(mode);
    }
    
    private async Task OnTaskClick(GanttItem item)
    {
        Console.WriteLine($"点击了任务：{item.Name}");
        await Task.CompletedTask;
    }
    
    private async Task OnTaskDataChanged(GanttItem item, string startTime, string endTime)
    {
        Console.WriteLine($"任务 {item.Name} 时间改变：{startTime} - {endTime}");
        item.Start = DateTime.Parse(startTime);
        item.End = DateTime.Parse(endTime);
        await Task.CompletedTask;
    }
    
    private async Task OnTaskProgressChanged(GanttItem item, int progress)
    {
        Console.WriteLine($"任务 {item.Name} 进度改变：{progress}%");
        item.Progress = progress;
        await Task.CompletedTask;
    }
}
```

---

## 参数 (Parameters)

### Gantt 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `Items` | `IEnumerable<GanttItem>?` | `null` | 获得或设置 甘特图数据源 |
| `OnClick` | `Func<GanttItem, Task>?` | `null` | 获得或设置 点击事件 |
| `OnDataChanged` | `Func<GanttItem, string, string, Task>?` | `null` | 获得或设置 任务时间改变事件 |
| `OnProgressChanged` | `Func<GanttItem, int, Task>?` | `null` | 获得或设置 任务进度改变事件 |
| `Option` | `GanttOption?` | `null` | 获得或设置 甘特图配置项 |

---

## 方法 (Methods)

### Gantt 组件方法

| 方法名 | 返回类型 | 说明 |
|--------|----------|------|
| `ChangeViewMode(ViewMode mode)` | `void` | 改变视图模式 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnClick` | `Func<GanttItem, Task>?` | 任务点击事件 |
| `OnDataChanged` | `Func<GanttItem, string, string, Task>?` | 任务时间改变事件 |
| `OnProgressChanged` | `Func<GanttItem, int, Task>?` | 任务进度改变事件 |

---

## 最佳实践

1. **绑定数据源**：通过 `Items` 参数绑定 `GanttItem` 类型的数据源，每个任务应包含 Id、Name、Start、End、Progress 等属性
2. **处理任务时间改变**：使用 `OnDataChanged` 事件处理任务时间改变，及时更新数据源
3. **处理任务进度改变**：使用 `OnProgressChanged` 事件处理任务进度改变，及时更新数据源
4. **视图模式切换**：通过 `ChangeViewMode` 方法切换视图模式，提供不同的时间粒度视图
5. **自定义配置**：通过 `Option` 参数自定义甘特图配置，例如语言、日期格式等
6. **任务点击处理**：使用 `OnClick` 事件处理任务点击，例如显示任务详情、编辑任务等
7. **数据持久化**：在 `OnDataChanged` 和 `OnProgressChanged` 事件中，将变更持久化到服务器或本地存储
8. **初始化数据**：确保 `GanttItem` 的 `Start` 和 `End` 属性有有效值，否则可能导致渲染错误

---

## 常见问题

### 1. 如何绑定甘特图数据？

**回答**：通过 `Items` 参数绑定 `IEnumerable<GanttItem>` 类型的数据源。每个 `GanttItem` 应包含 Id、Name、Start、End、Progress 等属性。

### 2. 如何切换视图模式？

**回答**：通过调用 `Gantt` 组件的 `ChangeViewMode(ViewMode mode)` 方法切换视图模式。视图模式包括：`QuarterDay`、`HalfDay`、`Day`、`Week`、`Month`。

### 3. 如何处理任务时间改变？

**回答**：使用 `OnDataChanged` 事件处理任务时间改变。该事件的参数为 `(GanttItem item, string startTime, string endTime)`。

### 4. 如何处理任务进度改变？

**回答**：使用 `OnProgressChanged` 事件处理任务进度改变。该事件的参数为 `(GanttItem item, int progress)`。

### 5. 如何处理任务点击？

**回答**：使用 `OnClick` 事件处理任务点击。该事件的参数为 `GanttItem item`。

### 6. 如何自定义甘特图配置？

**回答**：通过 `Option` 参数设置 `GanttOption` 类型的配置项，可以自定义语言、日期格式等。

### 7. GanttItem 需要哪些属性？

**回答**：`GanttItem` 通常需要以下属性：
- `Id`：任务唯一标识
- `Name`：任务名称
- `Start`：开始时间
- `End`：结束时间
- `Progress`：进度（0-100）

### 8. 如何获取 Gantt 组件实例？

**回答**：使用 `@ref` 指令获取 `Gantt` 组件实例，然后可以调用其方法，例如 `ChangeViewMode`。

### 9. 任务时间改变事件的参数类型是什么？

**回答**：`OnDataChanged` 事件的参数类型为 `(GanttItem item, string startTime, string endTime)`，其中 `startTime` 和 `endTime` 是字符串格式的日期。

### 10. 任务进度改变事件的参数类型是什么？

**回答**：`OnProgressChanged` 事件的参数类型为 `(GanttItem item, int progress)`，其中 `progress` 是整数类型的进度值（0-100）。
