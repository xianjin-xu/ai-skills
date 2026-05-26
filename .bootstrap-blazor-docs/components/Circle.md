# Circle (进度环)

## 概述

`Circle` 组件是**图表类组件**。一般有两种用途：
- 显示某项任务进度的百分比
- 统计某些指标的占比

**主要特性**：
- 支持设置进度值（Value）
- 支持设置进度条颜色（Color）
- 支持设置进度条宽度（StrokeWidth）
- 支持显示/隐藏进度百分比（ShowProgress）
- 支持自定义显示内容（ChildContent）

**在线演示**: https://www.blazor.zone/circle

---

## 使用场景

### 1. 基础用法（设置进度）

通过设置 `Value` 属性设定圆形进度（0-100）。

```razor
<!-- 基础进度环 -->
<Circle Value="25" />

<!-- 动态控制进度 -->
<Circle Value="ProgressValue" />
<Button @onclick="() => ProgressValue += 10">增加 10</Button>
<Button @onclick="() => ProgressValue -= 10">减少 10</Button>

@code {
    private int ProgressValue { get; set; } = 25;
}
```

---

### 2. 设置颜色（Color）

通过设置 `Color` 属性设定圆形进度条颜色。

```razor
<!-- 主要颜色 -->
<Circle Value="30" Color="Color.Primary" />

<!-- 成功颜色 -->
<Circle Value="50" Color="Color.Success" />

<!-- 危险颜色 -->
<Circle Value="70" Color="Color.Danger" />

<!-- 警告颜色 -->
<Circle Value="90" Color="Color.Warning" />
```

---

### 3. 设置进度条宽度（StrokeWidth）

通过设置 `StrokeWidth` 属性设定圆形进度条宽度（默认为 2）。

```razor
<!-- 细进度条 -->
<Circle Value="60" StrokeWidth="4" />

<!-- 粗进度条 -->
<Circle Value="60" StrokeWidth="8" />

<!-- 超粗进度条 -->
<Circle Value="60" StrokeWidth="12" />
```

---

### 4. 显示/隐藏进度百分比（ShowProgress）

通过设置 `ShowProgress` 控制是否显示进度百分比文字（默认显示）。

```razor
<!-- 显示百分比（默认） -->
<Circle Value="75" ShowProgress="true" />

<!-- 隐藏百分比 -->
<Circle Value="75" ShowProgress="false" />
```

---

### 5. 自定义显示内容（ChildContent）

通过自定义子组件自定义显示内容（默认显示百分比，可自定义为其他内容）。

```razor
<!-- 自定义内容：显示数字 -->
<Circle Value="75">
    <ChildContent>
        <div class="text-center">
            <h3>75%</h3>
            <p class="text-muted">已完成</p>
        </div>
    </ChildContent>
</Circle>

<!-- 自定义内容：显示图标 -->
<Circle Value="42">
    <ChildContent>
        <div class="text-center">
            <i class="fa fa-users fa-2x"></i>
            <p>消费人群</p>
        </div>
    </ChildContent>
</Circle>
```

---

## 参数 (Parameters)

### Circle 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `int` | `0` | 获得/设置 当前值（0-100） |
| `Color` | `Color` | `Color.Primary` | 获得/设置 组件进度条颜色 |
| `StrokeWidth` | `int` | `2` | 获得/设置 进度条宽度 默认为 2 |
| `ShowProgress` | `bool` | `true` | 获得/设置 是否显示进度百分比 默认显示 |
| `Width` | `int` | `120` | 获得/设置 组件宽度（像素） |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件 |

---

## 最佳实践

1. **Value 范围 0-100**：`Value` 表示百分比，范围 0-100，不是 0-1 或 0-100%
2. **合理设置 Color**：根据进度状态选择颜色（`< 30` 用 `Danger`，`30-70` 用 `Warning`，`> 70` 用 `Success`）
3. **控制 StrokeWidth**：细进度条（2-4）适合小尺寸，粗进度条（6-12）适合大尺寸
4. **自定义内容**：通过 `ChildContent` 自定义显示内容（如添加图标、描述文字）
5. **与 Progress 的区别**：`Circle` 是圆形进度，`Progress` 是线性进度条
6. **性能考虑**：频繁更新 `Value` 时（如实时进度），考虑使用 `Task` 延迟更新 UI
