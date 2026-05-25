# Timeline (时间线)

## 概述

`Timeline` 组件用于**按时间顺序展示信息**，常用于历史记录、项目进度、日志记录等场景。

**主要特性**：
- 支持自定义时间节点内容
- 支持不同颜色标识（Primary、Success、Info、Warning、Danger）
- 支持自定义图标
- 支持左右交替布局
- 支持通过 `Items` 参数绑定数据

**在线演示**: https://www.blazor.zone/timeline

---

## 使用场景

### 1. 基础用法（简单时间线）

`Timeline` 组件可以通过 `TimelineItems` 参数定义时间线节点。

```razor
<!-- 基础时间线 -->
<Timeline Items="TimelineItems" />

@code {
    private List<TimelineItem> TimelineItems { get; set; } = new List<TimelineItem>
    {
        new TimelineItem("2024-01-01", "项目启动", "项目正式启动，组建团队"),
        new TimelineItem("2024-02-01", "需求分析", "完成需求分析文档"),
        new TimelineItem("2024-03-01", "开发阶段", "进入开发阶段"),
        new TimelineItem("2024-04-01", "测试阶段", "开始系统测试"),
        new TimelineItem("2024-05-01", "项目上线", "项目成功上线")
    };
}
```

---

### 2. 自定义颜色（Color）

通过设置 `Color` 属性，为不同节点设置不同颜色。

```razor
<!-- 带颜色的时间线 -->
<Timeline Items="ColoredTimelineItems" />

@code {
    private List<TimelineItem> ColoredTimelineItems { get; set; } = new List<TimelineItem>
    {
        new TimelineItem("2024-01-01", "项目启动", "项目正式启动")
        {
            Color = Color.Primary
        },
        new TimelineItem("2024-02-01", "需求分析", "完成需求分析")
        {
            Color = Color.Info
        },
        new TimelineItem("2024-03-01", "开发阶段", "进入开发阶段")
        {
            Color = Color.Warning
        },
        new TimelineItem("2024-04-01", "测试阶段", "开始系统测试")
        {
            Color = Color.Success
        },
        new TimelineItem("2024-05-01", "项目上线", "项目成功上线")
        {
            Color = Color.Danger
        }
    };
}
```

---

### 3. 自定义图标（Icon）

通过设置 `Icon` 属性，为节点设置自定义图标。

```razor
<!-- 带图标的时间线 -->
<Timeline Items="IconTimelineItems" />

@code {
    private List<TimelineItem> IconTimelineItems { get; set; } = new List<TimelineItem>
    {
        new TimelineItem("2024-01-01", "项目启动", "项目正式启动")
        {
            Icon = "fa fa-flag"
        },
        new TimelineItem("2024-02-01", "需求分析", "完成需求分析")
        {
            Icon = "fa fa-file"
        },
        new TimelineItem("2024-03-01", "开发阶段", "进入开发阶段")
        {
            Icon = "fa fa-code"
        },
        new TimelineItem("2024-04-01", "测试阶段", "开始系统测试")
        {
            Icon = "fa fa-bug"
        },
        new TimelineItem("2024-05-01", "项目上线", "项目成功上线")
        {
            Icon = "fa fa-rocket"
        }
    };
}
```

---

### 4. 交替布局（IsAlternate）

通过设置 `IsAlternate="true"` 启用左右交替布局。

```razor
<!-- 交替布局时间线 -->
<Timeline Items="AlternateTimelineItems" IsAlternate="true" />

@code {
    private List<TimelineItem> AlternateTimelineItems { get; set; } = new List<TimelineItem>
    {
        new TimelineItem("2024-01-01", "项目启动", "项目正式启动"),
        new TimelineItem("2024-02-01", "需求分析", "完成需求分析"),
        new TimelineItem("2024-03-01", "开发阶段", "进入开发阶段"),
        new TimelineItem("2024-04-01", "测试阶段", "开始系统测试"),
        new TimelineItem("2024-05-01", "项目上线", "项目成功上线")
    };
}
```

---

### 5. 自定义模板（ChildContent）

通过 `ChildContent` 模板自定义节点内容。

```razor
<!-- 自定义模板时间线 -->
<Timeline Items="CustomTimelineItems">
    <ChildContent>
        <div class="timeline-custom">
            <h5>@context.Title</h5>
            <p>@context.Content</p>
            <small>@context.Time</small>
        </div>
    </ChildContent>
</Timeline>

@code {
    private List<TimelineItem> CustomTimelineItems { get; set; } = new List<TimelineItem>
    {
        new TimelineItem("2024-01-01", "项目启动", "项目正式启动"),
        new TimelineItem("2024-02-01", "需求分析", "完成需求分析"),
        new TimelineItem("2024-03-01", "开发阶段", "进入开发阶段")
    };
}
```

---

## 参数 (Parameters)

### Timeline 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TimelineItem>?` | `null` | 获得/设置时间线节点数据 |
| `IsAlternate` | `bool` | `false` | 获得/设置是否交替布局 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件/自定义模板 |

---

### TimelineItem 参数

`TimelineItem` 类定义时间线节点的数据。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Time` | `string?` | `null` | 获得/设置时间 |
| `Title` | `string?` | `null` | 获得/设置标题 |
| `Content` | `string?` | `null` | 获得/设置内容 |
| `Color` | `Color` | `Color.None` | 获得/设置颜色 |
| `Icon` | `string?` | `null` | 获得/设置图标 |
| `IsDone` | `bool` | `false` | 获得/设置是否已完成 |

---

## 最佳实践

1. **使用 Items 绑定数据**：推荐通过 `Items` 参数绑定数据，而不是在 Razor 中手动编写 `<TimelineItem>` 标签
2. **合理使用颜色**：使用不同颜色区分不同状态的节点（如 `Success` 表示已完成，`Warning` 表示进行中，`Danger` 表示有问题）
3. **提供有意义的时间**：`Time` 属性应提供用户可读的时间格式（如 "2024-01-01" 或 "2 小时前"）
4. **交替布局适合宽屏**：`IsAlternate="true"` 适合宽屏显示，窄屏建议使用默认布局
5. **自定义模板增强表现力**：对于复杂内容，使用 `ChildContent` 模板自定义节点样式和布局
6. **注意性能**：对于大量节点（>50），考虑分页或虚拟滚动，避免一次性渲染过多节点
