# SwitchButton 状态切换按钮

## 组件概述

SwitchButton 是一个状态切换按钮组件，点击按钮后切换状态。适用于需要切换开/关状态的场景。

## 使用场景

### 1. 基础用法

点击组件自动切换状态。

```razor
<SwitchButton ToggleState="false" ToggleStateChanged="OnStateChanged" />
```

```csharp
@code {
    private Task OnStateChanged(bool state)
    {
        Console.WriteLine($"当前状态: {state}");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `ToggleState` 参数设置组件的初始状态（`true` 为开，`false` 为关）
- `ToggleStateChanged` 回调方法在状态切换时触发
- 组件会显示"开"或"关"文字，根据状态自动变化

### 2. 初始化状态

通过设置 `ToggleState` 初始化组件状态。

```razor
<SwitchButton ToggleState="true" ToggleStateChanged="OnStateChanged" />
```

**说明：**
- `ToggleState="true"` 表示初始状态为"开"
- `ToggleState="false"` 表示初始状态为"关"（默认值）

### 3. 自定义显示文字

通过 `OnText` 和 `OffText` 参数自定义开/关状态显示的文字。

```razor
<SwitchButton ToggleState="false" 
           OnText="启用" 
           OffText="禁用" 
           ToggleStateChanged="OnStateChanged" />
```

**说明：**
- `OnText` 参数设置"开"状态显示的文字，默认值为"开"
- `OffText` 参数设置"关"状态显示的文字，默认值为"关"
- 可以根据业务需求自定义显示文字，如"启用"/"禁用"、"是"/"否"等

### 4. 点击回调方法

通过设置 `OnClick` 回调方法处理点击事件。

```razor
<SwitchButton ToggleState="false" 
           OnClick="OnButtonClick" 
           ToggleStateChanged="OnStateChanged" />
```

```csharp
@code {
    private Task OnButtonClick(MouseEventArgs args)
    {
        Console.WriteLine("按钮被点击");
        return Task.CompletedTask;
    }
    
    private Task OnStateChanged(bool state)
    {
        Console.WriteLine($"状态切换为: {state}");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `OnClick` 回调是 `EventCallback<MouseEventArgs>` 类型，会自动刷新当前组件或者页面
- 若不需要刷新组件或者页面，可使用 `ToggleStateChanged` 回调
- `OnClick` 和 `ToggleStateChanged` 可以同时使用

### 5. 完整示例

包含状态切换、显示文字自定义、点击回调等完整功能。

```razor
<Card>
    <CardBody>
        <div class="row g-3">
            <div class="col-12">
                <div class="form-inline">
                    <Label>状态切换按钮:</Label>
                    <SwitchButton ToggleState="@currentState" 
                               OnText="启用" 
                               OffText="禁用" 
                               OnClick="OnClick" 
                               ToggleStateChanged="OnStateChanged" />
                </div>
            </div>
            <div class="col-12">
                <div class="form-inline">
                    <Label>当前状态:</Label>
                    <Badge Color="@(currentState ? Color.Success : Color.Danger)">
                        @(currentState ? "启用" : "禁用")
                    </Badge>
                </div>
            </div>
            <div class="col-12">
                <Button OnClick="ResetState">重置状态</Button>
            </div>
        </div>
    </CardBody>
</Card>

@code {
    private bool currentState = false;
    
    private Task OnClick(MouseEventArgs args)
    {
        Console.WriteLine("按钮被点击");
        return Task.CompletedTask;
    }
    
    private Task OnStateChanged(bool state)
    {
        currentState = state;
        Console.WriteLine($"状态切换为: {state}");
        return Task.CompletedTask;
    }
    
    private Task ResetState()
    {
        currentState = false;
        return Task.CompletedTask;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `ToggleState` | 获得/设置 当前状态 | `bool` | `false` |
| `OnText` | 获得/设置 On 状态显示文字 | `string` | `开` |
| `OffText` | 获得/设置 Off 状态显示文字 | `string` | `关` |
| `OnClick` | 点击回调方法 | `EventCallback<MouseEventArgs>` | - |
| `ToggleStateChanged` | 状态切换回调方法 | `EventCallback<bool>` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 最佳实践

1. **状态管理**：使用 `ToggleStateChanged` 回调来更新状态变量，避免使用 `OnClick` 导致页面刷新
2. **文字自定义**：根据业务场景自定义 `OnText` 和 `OffText`，使界面更友好
3. **初始状态**：根据业务需求合理设置 `ToggleState` 初始值
4. **回调选择**：如果不需要页面刷新，优先使用 `ToggleStateChanged` 而非 `OnClick`
5. **可访问性**：为组件添加 `Id` 属性，提高可访问性

## 常见问题

**Q: OnClick 和 ToggleStateChanged 有什么区别？**
A: `OnClick` 是标准的鼠标点击事件回调，会触发组件或页面刷新；`ToggleStateChanged` 是状态切换回调，不会触发刷新。如果不需要刷新，建议使用 `ToggleStateChanged`。

**Q: 如何自定义开/关状态的显示文字？**
A: 使用 `OnText` 和 `OffText` 参数设置，如 `OnText="启用"`、`OffText="禁用"`。

**Q: 如何获取当前状态？**
A: 通过 `ToggleStateChanged` 回调方法的参数获取，或绑定 `ToggleState` 参数到本地变量。

**Q: 如何禁用组件？**
A: 目前 SwitchButton 组件不支持直接禁用。可以通过外层容器或自定义 CSS 来实现禁用效果。

**Q: 组件支持哪些事件？**
A: 支持 `OnClick`（鼠标点击）和 `ToggleStateChanged`（状态切换）两个事件回调。

## 版本历史

- **初始版本**: 支持状态切换、自定义文字、点击回调、状态切换回调功能
