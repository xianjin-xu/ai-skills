# PulseButton 心跳按钮

## 组件概述

PulseButton 是一个心跳按钮组件，适用于突出显示功能吸引使用者关注。按钮默认为圆形，继承于 Button 组件，在按钮原有功能基础上增加了一个心跳环。

## 使用场景

### 1. 基础用法

基础的按钮用法。

```razor
<PulseButton Text="点击我" OnClick="OnClick" />
```

```csharp
@code {
    private Task OnClick(MouseEventArgs args)
    {
        Console.WriteLine("按钮被点击");
        return Task.CompletedTask;
    }
}
```

**说明：**
- PulseButton 继承于 Button 组件，拥有 Button 的所有功能
- 默认显示为圆形按钮，带心跳环动画
- 心跳环动画用于吸引用户注意力

### 2. 设置按钮颜色

通过 `Color` 参数设置按钮颜色。

```razor
<PulseButton Text="主要" Color="Color.Primary" OnClick="OnClick" />
<PulseButton Text="成功" Color="Color.Success" OnClick="OnClick" />
<PulseButton Text="警告" Color="Color.Warning" OnClick="OnClick" />
<PulseButton Text="危险" Color="Color.Danger" OnClick="OnClick" />
```

**说明：**
- `Color` 参数设置按钮颜色
- 支持 Bootstrap 所有颜色类型：`Primary`、`Secondary`、`Success`、`Danger`、`Warning`、`Info`、`Light`、`Dark`

### 3. 设置心跳环颜色

通过 `PulseColor` 参数设置心跳环颜色。

```razor
<PulseButton Text="点击我" Color="Color.Primary" PulseColor="Color.Success" OnClick="OnClick" />
```

**说明：**
- `PulseColor` 参数设置心跳环颜色
- 心跳环颜色可以与按钮颜色不同，形成对比效果
- 支持所有 Bootstrap 颜色类型

### 4. 设置按钮大小

通过 `Size` 参数设置按钮大小。

```razor
<PulseButton Text="小按钮" Size="Size.Small" OnClick="OnClick" />
<PulseButton Text="中按钮" Size="Size.Medium" OnClick="OnClick" />
<PulseButton Text="大按钮" Size="Size.Large" OnClick="OnClick" />
```

**说明：**
- `Size` 参数设置按钮大小
- 支持 `Size.Small`、`Size.Medium`、`Size.Large` 等尺寸

### 5. 设置按钮图标

通过 `Icon` 参数设置按钮图标。

```razor
<PulseButton Text="设置" Icon="fa fa-cog" OnClick="OnClick" />
<PulseButton Text="保存" Icon="fa fa-save" OnClick="OnClick" />
<PulseButton Text="删除" Icon="fa fa-trash" OnClick="OnClick" />
```

**说明：**
- `Icon` 参数设置显示图标（FontAwesome 图标类名）
- 图标显示在按钮文本前面

### 6. 异步按钮

通过 `IsAsync` 参数设置是否为异步按钮。

```razor
<PulseButton Text="异步操作" IsAsync="true" OnClick="OnAsyncClick" />
```

```csharp
@code {
    private async Task OnAsyncClick(MouseEventArgs args)
    {
        // 模拟异步操作
        await Task.Delay(2000);
        Console.WriteLine("异步操作完成");
    }
}
```

**说明：**
- `IsAsync="true"` 表示是异步按钮
- 点击按钮后禁用自身并且等待异步完成，过程中显示 loading 动画
- `LoadingIcon` 参数可以自定义 loading 动画图标

### 7. 禁用按钮

通过 `IsDisabled` 参数禁用按钮。

```razor
<PulseButton Text="禁用按钮" IsDisabled="true" />
```

**说明：**
- `IsDisabled="true"` 禁用按钮
- 禁用后按钮无法点击，样式变为禁用状态

### 8. Outline 样式

通过 `IsOutline` 参数设置 Outline 样式按钮。

```razor
<PulseButton Text="Outline" Color="Color.Primary" IsOutline="true" OnClick="OnClick" />
```

**说明：**
- `IsOutline="true"` 设置 Outline 样式
- Outline 样式按钮只有边框有颜色，内部透明

### 9. Block 模式

通过 `IsBlock` 参数设置 Block 模式按钮。

```razor
<PulseButton Text="Block 按钮" IsBlock="true" OnClick="OnClick" />
```

**说明：**
- `IsBlock="true"` 设置 Block 模式
- Block 模式按钮宽度占满父容器

### 10. 完整示例

包含心跳按钮、颜色设置、大小设置、图标、异步操作等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>心跳按钮示例</CardTitle>
    </CardHeader>
    <CardBody>
        <div class="row g-3">
            <div class="col-12">
                <div class="form-inline">
                    <Label>按钮颜色:</Label>
                    <PulseButton Text="主要" Color="Color.Primary" PulseColor="Color.Primary" OnClick="OnClick" />
                    <PulseButton Text="成功" Color="Color.Success" PulseColor="Color.Success" OnClick="OnClick" />
                    <PulseButton Text="警告" Color="Color.Warning" PulseColor="Color.Warning" OnClick="OnClick" />
                </div>
            </div>
            <div class="col-12">
                <div class="form-inline">
                    <Label>按钮大小:</Label>
                    <PulseButton Text="小" Size="Size.Small" OnClick="OnClick" />
                    <PulseButton Text="中" Size="Size.Medium" OnClick="OnClick" />
                    <PulseButton Text="大" Size="Size.Large" OnClick="OnClick" />
                </div>
            </div>
            <div class="col-12">
                <div class="form-inline">
                    <Label>异步按钮:</Label>
                    <PulseButton Text="异步操作" IsAsync="true" OnClick="OnAsyncClick" Color="Color.Info" />
                </div>
            </div>
        </div>
    </CardBody>
</Card>

@code {
    private Task OnClick(MouseEventArgs args)
    {
        Console.WriteLine("按钮被点击");
        return Task.CompletedTask;
    }
    
    private async Task OnAsyncClick(MouseEventArgs args)
    {
        await Task.Delay(2000);
        Console.WriteLine("异步操作完成");
        return Task.CompletedTask;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `PulseColor` | 获得/设置 心跳环颜色 | `Color` | - |
| `Color` | 获得/设置 按钮颜色 | `Color` | - |
| `Text` | 获得/设置 显示文字 | `string` | - |
| `Icon` | 获得/设置 显示图标 | `string` | - |
| `Size` | 获得/设置 Size 大小 | `Size` | - |
| `ButtonStyle` | 获得/设置 按钮风格枚举 | `ButtonStyle` | - |
| `ButtonType` | 获得/设置 按钮类型 | `ButtonType` | `Button` |
| `IsAsync` | 获得/设置 是否为异步按钮 | `bool` | `false` |
| `IsAutoFocus` | 获得/设置 是否自动获取焦点 | `bool` | `false` |
| `IsBlock` | 获得/设置 Block 模式 | `bool` | - |
| `IsDisabled` | 获得/设置 是否禁用 | `bool` | `false` |
| `IsKeepDisabled` | 获得/设置 是否异步结束后保持禁用 | `bool` | `false` |
| `IsOutline` | 获得/设置 Outline 样式 | `bool` | `false` |
| `LoadingIcon` | 获得/设置 正在加载动画图标 | `string` | `fa-solid fa-spin fa-spinner` |
| `ImageUrl` | 获得/设置 显示图片地址 | `string` | `null` |
| `OnClick` | 获得/设置 OnClick 事件 | `EventCallback<MouseEventArgs>` | - |
| `OnClickWithoutRender` | 获得/设置 OnClick 事件不刷新父组件 | `Func<Task>` | - |
| `StopPropagation` | 获得/设置 点击事件是否向上传播 | `bool` | `false` |
| `TooltipText` | 获得/设置 Tooltip 显示文字 | `string` | `null` |
| `TooltipPlacement` | 获得/设置 Tooltip 显示位置 | `Placement` | `Top` |
| `TooltipTrigger` | 获得/设置 Tooltip 触发方式 | `string` | `hover focus` |
| `ChildContent` | 获得/设置 RenderFragment 实例 | `RenderFragment` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## ButtonType 枚举

| 值 | 说明 |
|-----|------|
| `Button` | 普通按钮（默认） |
| `Submit` | 表单提交按钮 |
| `Reset` | 表单重置按钮 |

## ButtonStyle 枚举

| 值 | 说明 |
|-----|------|
| `None` | 无样式 |
| `Primary` | 主要样式 |
| `Secondary` | 次要样式 |
| `Success` | 成功样式 |
| `Danger` | 危险样式 |
| `Warning` | 警告样式 |
| `Info` | 信息样式 |
| `Light` | 浅色样式 |
| `Dark` | 深色样式 |
| `Link` | 链接样式 |

## 最佳实践

1. **吸引注意力**：使用心跳环动画吸引用户关注重要功能
2. **颜色搭配**：心跳环颜色与按钮颜色可以形成对比，增强视觉效果
3. **异步操作**：对于耗时操作，使用 `IsAsync="true"` 提供 loading 反馈
4. **按钮类型**：在表单中使用 `ButtonType.Submit` 作为提交按钮
5. **图标选择**：选择合适的 FontAwesome 图标增强按钮语义

## 常见问题

**Q: 如何去除心跳环动画？**
A: 目前 PulseButton 组件不支持直接去除心跳环动画。如果需要普通按钮，请使用 Button 组件。

**Q: 如何自定义心跳环颜色？**
A: 使用 `PulseColor` 参数设置，如 `PulseColor="Color.Success"`。

**Q: 如何禁用按钮？**
A: 设置 `IsDisabled="true"` 禁用按钮。

**Q: 如何处理异步操作？**
A: 设置 `IsAsync="true"`，并在 `OnClick` 回调中执行异步操作。

**Q: 如何设置按钮为表单提交按钮？**
A: 设置 `ButtonType="ButtonType.Submit"`。

**Q: 如何添加工具提示？**
A: 使用 `TooltipText` 参数设置提示文字，`TooltipPlacement` 设置显示位置。

## 版本历史

- **初始版本**: 支持心跳按钮、颜色设置、大小设置、图标、异步操作、禁用、Outline 样式、Block 模式等功能
