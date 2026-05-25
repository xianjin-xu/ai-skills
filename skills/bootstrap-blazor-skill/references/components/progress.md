# Progress (进度条)

## 概述

`Progress` 组件用于**显示任务进度或操作状态**，是线性进度指示器。

**主要特性**：
- 支持设置进度值（Value）
- 支持不同颜色（Color）
- 支持条纹效果（IsStriped）
- 支持动画效果（IsAnimated）
- 支持显示进度值（IsShowValue）
- 支持自定义文本（Text）

**在线演示**: https://www.blazor.zone/progress)

---

## 使用场景

### 1. 基础用法（设置进度）

通过设置 `Value` 参数设置进度（0-100）。

```razor
<!-- 基础进度条 -->
<Progress Value="25" />

<!-- 动态控制进度 -->
<Progress Value="ProgressValue" />
<Button @onclick="() => ProgressValue += 10">增加 10</Button>
<Button @onclick="() => ProgressValue -= 10">减少 10</Button>

@code {
    private double ProgressValue { get; set; } = 25;
}
```

---

### 2. 设置颜色（Color）

通过设置 `Color` 参数设置进度条颜色。

```razor
<!-- 主要颜色 -->
<Progress Value="30" Color="Color.Primary" />

<!-- 成功颜色 -->
<Progress Value="50" Color="Color.Success" />

<!-- 危险颜色 -->
<Progress Value="70" Color="Color.Danger" />

<!-- 警告颜色 -->
<Progress Value="90" Color="Color.Warning" />
```

---

### 3. 条纹效果（IsStriped）

通过设置 `IsStriped="true"` 启用条纹效果。

```razor
<!-- 条纹进度条 -->
<Progress Value="60" IsStriped="true" />

<!-- 条纹 + 颜色 -->
<Progress Value="60" Color="Color.Success" IsStriped="true" />
```

---

### 4. 动画效果（IsAnimated）

通过设置 `IsAnimated="true"` 启用条纹动画（条纹会动）。

```razor
<!-- 动画条纹进度条 -->
<Progress Value="60" IsStriped="true" IsAnimated="true" />
```

---

### 5. 显示进度值（IsShowValue）

通过设置 `IsShowValue="true"` 显示进度百分比文本。

```razor
<!-- 显示进度值 -->
<Progress Value="75" IsShowValue="true" />

<!-- 自定义文本 -->
<Progress Value="75" Text="75%" />
```

---

### 6. 自定义高度（Height）

通过 `Height` 参数设置进度条高度（像素）。

```razor
<!-- 低进度条 -->
<Progress Value="50" Height="8" />

<!-- 中进度条 -->
<Progress Value="50" Height="16" />

<!-- 高进度条 -->
<Progress Value="50" Height="24" />
```

---

## 参数 (Parameters)

### Progress 组件参数#

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `double` | `0` | 获得/设置 组件进度值（0-100） |
| `Color` | `Color` | `Color.Primary` | 获得/设置 颜色，默认为 Color.Primary |
| `IsShowValue` | `bool` | `false` | 获得/设置 是否显示进度值 |
| `IsStriped` | `bool` | `false` | 获得/设置 是否显示条纹效果 |
| `IsAnimated` | `bool` | `false` | 获得/设置 是否显示动画效果 |
| `Height` | `int?` | `null` | 获得/设置 控件高度，默认为 null 未设置 |
| `Text` | `string?` | `null` | 获得/设置 进度标签文本 |
| `Round` | `int` | `0` | 获得/设置 进度值修约小数位数，默认为 0（即保留为整数） |
| `MidpointRounding` | `MidpointRounding` | `MidpointRounding.AwayFromZero` | 获得/设置 保留小数点模式，默认为 AwayFromZero |

---

## 最佳实践

1. **Value 范围 0-100**：`Value` 表示百分比，范围 0-100，不是 0-1 或 0-100%。
2. **合理设置 Color**：根据进度状态选择颜色（`< 30` 用 `Danger`，`30-70` 用 `Warning`，`> 70` 用 `Success`）。
3. **使用 IsShowValue**：需要显示具体进度值时设置 `IsShowValue="true"`，否则用户不知道进度多少。
4. **性能考虑**：频繁更新 `Value` 时（如实时进度），考虑使用 `Task` 延迟更新 UI，避免过度渲染。
5. **与 Circle 的区别**：`Progress` 是线性进度条，`Circle` 是圆形进度环。
6. **与 Mask 的区别**：`Progress` 是进度指示器（不阻止交互），`Mask` 是遮罩层（阻止交互）。

---

## 常见问题

### Q: 如何动态更新进度？
A: 通过绑定 `Value` 参数并调用 `StateHasChanged()` 或使用 `@bind-Value` 双向绑定。

### Q: 如何显示自定义文本（如 “上传中...”）？
A: 使用 `Text` 参数，如 `Text="上传中..."`。

### Q: 进度条不动画？
A: 确保同时设置了 `IsStriped="true"` 和 `IsAnimated="true"`。

### Q: 如何设置进度条高度？
A: 使用 `Height` 参数，如 `Height="20"`（单位：像素）。
