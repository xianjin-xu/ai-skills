# Step (步骤条)

## 概述

`Step` 组件用于**引导用户完成多步骤流程**，如注册向导、 checkout 流程等。

**主要特性**：
- 支持水平/垂直布局（IsVertical）
- 支持步骤点击（OnStepClick）
- 支持自定义步骤内容（StepItem）
- 支持完成回调（OnFinishedCallback）

**在线演示**: https://www.blazor.zone/step

---

## 使用场景

### 1. 基础用法（简单步骤条）

`Step` 组件通过 `Items` 参数绑定步骤数据。

```razor
<Step Items="StepItems">
    <StepItem Text="步骤 1" Title="填写信息" />
    <StepItem Text="步骤 2" Title="确认订单" />
    <StepItem Text="步骤 3" Title="完成支付" />
</Step>

@code {
    private List<StepOption> StepItems { get; set; } = new List<StepOption>
    {
        new StepOption("步骤 1", "填写信息"),
        new StepOption("步骤 2", "确认订单"),
        new StepOption("步骤 3", "完成支付")
    };
}
```

---

### 2. 垂直布局（IsVertical）

通过设置 `IsVertical="true"` 垂直渲染步骤条。

```razor
<Step Items="StepItems" IsVertical="true">
    <StepItem Text="步骤 1" Title="填写信息" />
    <StepItem Text="步骤 2" Title="确认订单" />
    <StepItem Text="步骤 3" Title="完成支付" />
</Step>
```

---

### 3. 步骤点击回调（OnStepClick）

通过 `OnStepClick` 回调处理步骤点击事件。

```razor
<Step Items="StepItems" OnStepClick="OnStepClick">
    <StepItem Text="步骤 1" Title="填写信息" />
    <StepItem Text="步骤 2" Title="确认订单" />
    <StepItem Text="步骤 3" Title="完成支付" />
</Step>

@code {
    private List<StepOption> StepItems { get; set; } = new List<StepOption>
    {
        new StepOption("步骤 1", "填写信息"),
        new StepOption("步骤 2", "确认订单"),
        new StepOption("步骤 3", "完成支付")
    };

    private void OnStepClick(StepOption step)
    {
        Console.WriteLine($"点击了步骤: {step.Text}");
    }
}
```

---

### 4. 步骤完成回调（OnFinishedCallback）

当所有步骤完成时触发 `OnFinishedCallback` 回调。

```razor
<Step Items="StepItems" OnFinishedCallback="OnFinished">
    <StepItem Text="步骤 1" Title="填写信息" />
    <StepItem Text="步骤 2" Title="确认订单" />
    <StepItem Text="步骤 3" Title="完成支付" />
    <FinishedTemplate>
        <div class="alert alert-success">🎉️ 所有步骤已完成！</div>
    </FinishedTemplate>
</Step>

@code {
    private List<StepOption> StepItems { get; set; } = new List<StepOption>
    {
        new StepOption("步骤 1", "填写信息"),
        new StepOption("步骤 2", "确认订单"),
        new StepOption("步骤 3", "完成支付")
    };

    private void OnFinished()
    {
        Console.WriteLine("所有步骤已完成！");
    }
}
```

---

### 5. 动态更新步骤状态

通过 `@ref` 获取 `Step` 引用，调用方法更新状态。

```razor
<Step @ref="StepRef" Items="StepItems">
    <StepItem Text="步骤 1" Title="填写信息" />
    <StepItem Text="步骤 2" Title="确认订单" />
    <StepItem Text="步骤 3" Title="完成支付" />
</Step>

<button class="btn btn-primary" @onclick="GoNext">下一步</button>

@code {
    private Step? StepRef { get; set; }
    private List<StepOption> StepItems { get; set; } = new List<StepOption>>
    {
        new StepOption("步骤 1", "填写信息"),
        new StepOption("步骤 2", "确认订单"),
        new StepOption("步骤 3", "完成支付")
    };

    private void GoNext()
    {
        StepRef?.GoNext();
    }
}
```

---

## 参数 (Parameters)

### Step 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `List<StepOption>?` | `null` | 获得/设置 步骤集合 |
| `IsVertical` | `bool` | `false` | 获得/设置 是否垂直渲染 默认 false 水平渲染 |
| `StepIndex` | `int` | `0` | 获得/设置 当前步骤索引 默认 0 |
| `OnStepClick` | `Func<StepOption, Task>?` | `null` | 获得/设置 步骤点击回调 |
| `OnFinishedCallback` | `Func<Task>?` | `null` | 获得/设置 步骤全部完成时回调 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 组件内容实例 |

---

## 数据类 (StepOption)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置 步骤显示文本 |
| `Title` | `string?` | `null` | 获得/设置 步骤标题 |
| `Description` | `string?` | `null` | 获得/设置 步骤描述 |
| `IsActive` | `bool` | `false` | 获得/设置 是否当前步骤 |
| `IsCompleted` | `bool` | `false` | 获得/设置 是否已完成 |

---

## 最佳实践

1. **合理设置 StepIndex**：`StepIndex` 表示当前激活步骤索引（从 0 开始）
2. **使用 StepOption 绑定**：步骤数据通过 `List<StepOption>` 绑定，`StepOption` 支持 `Text`、`Title`、`Description`
3. **处理完成回调**：通过 `OnFinishedCallback` 处理流程完成逻辑
4. **与 Tabs 的区别**：`Step` 是线性流程（有顺序），`Tabs` 是选项卡（可随意切换）
5. **与 Wizard 的区别**：`Step` 是简化版步骤条，`Wizard` 可能支持更复杂布局
6. **响应式设计**：垂直模式（`IsVertical="true"`）在移动端更友好

---

## 常见问题

### Q: 如何动态切换步骤？
A: 通过 `@ref` 获取 `Step` 引用，调用 `GoNext()`、`GoPrevious()` 方法。

### Q: 步骤状态如何更新？
A: 更新 `StepOption.IsCompleted = true`，组件自动重新渲染。

### Q: 如何自定义步骤内容？
A: 使用 `StepItem` 的 `HeaderTemplate`、`ContentTemplate` 自定义显示。
