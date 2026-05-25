# PopConfirm 气泡确认框

## 概述

PopConfirm 气泡确认框组件用于点击元素后，弹出气泡确认框。PopConfirm 的属性与 Popover 很类似，因此对于重复属性，请参考 Popover 的文档。

> PopConfirm component is used to click an element and pop up a bubble confirmation box.

**分类**: 通知组件  
**在线演示**: [https://www.blazor.zone/popconfirm](https://www.blazor.zone/popconfirm)

---

## 使用场景

### 1. 基础用法

PopConfirm 支持四种弹出位置：下面弹框、右侧弹窗、左侧弹窗、上面弹窗。通过 `Placement` 参数控制弹出位置。

```razor
<PopConfirmButton Content="确定要删除吗？" Placement="Placement.Bottom">
    <Button Text="下面弹框" />
</PopConfirmButton>

<PopConfirmButton Content="确定要删除吗？" Placement="Placement.Right">
    <Button Text="右侧弹窗" />
</PopConfirmButton>

<PopConfirmButton Content="确定要删除吗？" Placement="Placement.Left">
    <Button Text="左侧弹窗" />
</PopConfirmButton>

<PopConfirmButton Content="确定要删除吗？" Placement="Placement.Top">
    <Button Text="上面弹窗" />
</PopConfirmButton>
```

### 2. 更改确认弹窗显示文字

通过设置 `Content` 属性更改确认弹窗显示文字。

```razor
<PopConfirmButton Content="确定要执行此操作吗？" 
                ConfirmButtonText="确定" 
                CloseButtonText="取消">
    <Button Text="删除确认按钮" Color="Color.Danger" />
</PopConfirmButton>
```

### 3. 异步确认

通过设置 `IsAsync` 属性，点击确认按钮时异步进行数据提交。有些特定场景异步后需要按钮继续保持禁用状态，请通过 `IsKeepDisabled` 参数控制。

```razor
<PopConfirmButton Content="确定要删除吗？" 
                IsAsync="true"
                OnConfirm="OnDeleteAsync">
    <Button Text="异步确认" Color="Color.Danger" />
</PopConfirmButton>

@code {
    private async Task OnDeleteAsync()
    {
        // 模拟异步删除操作
        await Task.Delay(1000);
        await ToastService.Success("删除成功");
    }
}
```

### 4. 表单提交

通过设置 `ButtonType` 属性值为 `ButtonType.Submit` 使确认按钮点击后进行异步表单数据提交。

```razor
<ValidateForm Model="Model">
    <EditorForm TItem="BindItem" ItemsPerRow="2">
        <Buttons>
            <PopConfirmButton ButtonType="ButtonType.Submit" 
                            Content="确定要提交表单吗？"
                            ConfirmButtonText="确定"
                            CloseButtonText="取消">
                <Button Text="提交表单" ButtonType="ButtonType.Submit" />
            </PopConfirmButton>
        </Buttons>
    </EditorForm>
</ValidateForm>
```

### 5. 超链接按钮

通过设置 `IsLink` 属性，组件使用 A 标签进行渲染。

```razor
<PopConfirmButton Content="确定要访问此链接吗？" 
                IsLink="true"
                OnConfirm="OnLinkClick">
    <a href="javascript:void(0)">我是超链接</a>
</PopConfirmButton>

@code {
    private async Task OnLinkClick()
    {
        // 处理链接点击逻辑
        await Task.CompletedTask;
    }
}
```

### 6. 自定义样式

设置 `CustomClass` 自定义组件样式。

```razor
<PopConfirmButton Content="确定要删除吗？" 
                CustomClass="custom-popover">
    <Button Text="自定义样式按钮" Color="Color.Warning" />
</PopConfirmButton>

<style>
    .custom-popover {
        --bs-popover-border-color: var(--bs-primary);
        --bs-popover-body-padding-x: 1rem;
        --bs-popover-body-padding-y: 1rem;
    }
</style>
```

### 7. 自定义 PopConfirmButton 内容

通过设置 `BodyTemplate` 属性，自定义确认框内容。

```razor
<PopConfirmButton Content="自定义内容">
    <BodyTemplate>
        <div class="p-3">
            <h5>确认操作</h5>
            <p>您确定要执行此操作吗？此操作不可撤销。</p>
        </div>
    </BodyTemplate>
    <Button Text="自定义内容" Color="Color.Info" />
</PopConfirmButton>
```

### 8. 自定义组件

通过设置 `ShowCloseButton="false"` `ShowConfirmButton="false"` 不显示内置功能按钮，在自定义组件中自定义一个审批按钮。自定义组件内可通过级联参数调用组件内部的 Close 或者 Confirm 方法。

```razor
<PopConfirmButton ShowCloseButton="false" 
                ShowConfirmButton="false">
    <BodyTemplate>
        <div class="p-3">
            <h5>审批操作</h5>
            <p>请选择审批结果：</p>
            <div class="d-flex gap-2">
                <Button Text="批准" Color="Color.Success" OnClick="OnApprove" />
                <Button Text="拒绝" Color="Color.Danger" OnClick="OnReject" />
            </div>
        </div>
    </BodyTemplate>
    <Button Text="自定义组件" Color="Color.Secondary" />
</PopConfirmButton>

@code {
    [CascadingParameter(Name = "PopoverConfirmButtonCloseAsync")]
    [NotNull]
    private Func<Task>? OnCloseAsync { get; set; }

    [CascadingParameter(Name = "PopoverConfirmButtonConfirmAsync")]
    [NotNull]
    private Func<Task>? OnConfirmAsync { get; set; }

    private async Task OnApprove()
    {
        // 处理批准逻辑
        if (OnConfirmAsync != null)
        {
            await OnConfirmAsync.Invoke();
        }
    }

    private async Task OnReject()
    {
        // 处理拒绝逻辑
        if (OnCloseAsync != null)
        {
            await OnCloseAsync.Invoke();
        }
    }
}
```

### 9. 触发方式

通过设置 `Trigger` 参数来设置组件弹出确认框的方式，默认值为 `click`，还可以设置 `hover`、`focus`，可组合使用。

```razor
<PopConfirmButton Content="点击触发" Trigger="click">
    <Button Text="点击触发" />
</PopConfirmButton>

<PopConfirmButton Content="悬停触发" Trigger="hover">
    <Button Text="悬停触发" />
</PopConfirmButton>

<PopConfirmButton Content="焦点触发" Trigger="focus">
    <Button Text="焦点触发" />
</PopConfirmButton>

<PopConfirmButton Content="点击或悬停触发" Trigger="click hover">
    <Button Text="组合触发" />
</PopConfirmButton>
```

---

## 参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| AdditionalAttributes | 获得/设置 用户自定义属性 | IDictionary<string, Object> | — |
| BodyTemplate | 获得/设置 自定义内容 | RenderFragment | — |
| ButtonStyle | 获得/设置 按钮风格枚举 | ButtonStyle | — |
| ButtonType | 获得/设置 按钮类型 Submit 为表单提交按钮 Reset 为表单重置按钮 默认为 Button | ButtonType | Button |
| ChildContent | 获得/设置 RenderFragment 实例 | RenderFragment | — |
| CloseButtonColor | 获得/设置 关闭按钮颜色 | Color | — |
| CloseButtonIcon | 获得/设置 关闭按钮显示图标 | string | — |
| CloseButtonText | 获得/设置 关闭按钮显示文字 默认为 关闭 | string | 关闭 |
| Color | 获得/设置 按钮颜色 | Color | — |
| ConfirmButtonColor | 获得/设置 确认按钮颜色 | Color | — |
| ConfirmButtonIcon | 获得/设置 确认按钮显示图标 | string | — |
| ConfirmButtonText | 获得/设置 确认按钮显示文字 默认为 确定 | string | 确定 |
| ConfirmIcon | 获得/设置 确认框图标 | string | — |
| Content | 获得/设置 显示文字 | string | — |
| CustomClass | 获得/设置 自定义样式 默认 null | string | null |
| Icon | 获得/设置 显示图标 | string | — |
| Id | 获得/设置 组件 id 属性 | string | — |
| IsAsync | 获得/设置 是否为异步按钮，默认为 false 如果为 true 表示是异步按钮，点击按钮后禁用自身并且等待异步完成，过程中显示 loading 动画 | bool | false |
| IsBlock | 获得/设置 Block 模式 | bool | false |
| IsDisabled | 获得/设置 是否禁用 默认为 false | bool | false |
| IsKeepDisabled | 获得/设置 是否异步结束后是否保持禁用状态，默认为 false | bool | false |
| IsLink | 获得/设置 是否为 A 标签 默认 false 使用 button 渲染 | bool | false |
| IsOutline | 获得/设置 Outline 样式 默认 false | bool | false |
| LoadingIcon | 获得/设置 正在加载动画图标 默认为 fa-solid fa-spin fa-spinner | string | fa-solid fa-spin fa-spinner |
| OnBeforeClick | 获得/设置 点击确认弹窗前回调方法 返回真时弹出弹窗 返回假时不弹出 默认 null | Func<Task<bool>> | null |
| OnClick | 获得/设置 OnClick 事件 | EventCallback<MouseEventArgs> | — |
| OnClickWithoutRender | 获得/设置 OnClick 事件不刷新父组件 | Func<Task> | — |
| OnClose | 获得/设置 点击关闭时回调方法 | Func<Task> | — |
| OnConfirm | 获得/设置 点击确认时回调方法 | Func<Task> | — |
| Placement | 获得/设置 弹窗显示位置 默认 | Placement | — |
| ShowCloseButton | 获得/设置 是否显示关闭按钮 | bool | true |
| ShowConfirmButton | 获得/设置 是否显示确认按钮 | bool | true |
| ShowShadow | 获得/设置 是否显示阴影 默认 true | bool | true |
| Size | 获得/设置 Size 大小 | Size | — |
| StopPropagation | 获得/设置 点击事件是否向上传播 默认 false | bool | false |
| Text | 获得/设置 显示文字 | string | — |
| Title | 获得/设置 显示标题 | string | — |
| TooltipPlacement | 获得/设置 Tooltip 显示位置，默认为 Top | Placement | Top |
| TooltipText | 获得/设置 Tooltip 显示文字，默认为 null | string | null |
| TooltipTrigger | 获得/设置 Tooltip 触发方式，默认为 hover focus | string | hover focus |
| Trigger | 获得/设置 弹窗触发方式 默认 click 可设置 hover focus | string | click |

---

## 事件回调

| 事件名称 | 说明 | 回调类型 |
|---------|------|---------|
| OnBeforeClick | 点击确认弹窗前回调方法，返回真时弹出弹窗，返回假时不弹出 | Func<Task<bool>> |
| OnClick | OnClick 事件 | EventCallback<MouseEventArgs> |
| OnClickWithoutRender | OnClick 事件不刷新父组件 | Func<Task> |
| OnClose | 点击关闭时回调方法 | Func<Task> |
| OnConfirm | 点击确认时回调方法 | Func<Task> |

---

## 最佳实践

### 删除操作确认

在执行删除操作时，使用 PopConfirm 进行二次确认，防止误操作：

```razor
<Table TItem="BindItem" Items="Items">
    <TableColumns>
        <TableColumn @bind-Field="context.Name" />
        <TableColumn @bind-Field="context.Education" />
        <TableColumn>
            <Template>
                <PopConfirmButton Content="确定要删除该记录吗？" 
                                Placement="Placement.Left"
                                ConfirmButtonColor="Color.Danger"
                                OnConfirm="() => OnDelete(context.Id)">
                    <Button Icon="fa-solid fa-trash" Color="Color.Danger" Size="Size.Small" />
                </PopConfirmButton>
            </Template>
        </TableColumn>
    </TableColumns>
</Table>

@code {
    private List<BindItem> Items { get; set; } = new();
    
    private async Task OnDelete(int id)
    {
        // 执行删除操作
        Items.RemoveAll(i => i.Id == id);
        await ToastService.Success("删除成功");
    }
}
```

### 自定义确认按钮样式

通过 `ConfirmButtonColor` 和 `ConfirmButtonIcon` 自定义确认按钮的外观：

```razor
<PopConfirmButton Content="确定要保存更改吗？"
                ConfirmButtonText="保存"
                ConfirmButtonIcon="fa-solid fa-check"
                ConfirmButtonColor="Color.Success"
                CloseButtonText="取消"
                CloseButtonIcon="fa-solid fa-times"
                CloseButtonColor="Color.Secondary">
    <Button Text="保存更改" Color="Color.Success" />
</PopConfirmButton>
```

---

## 常见问题

### 1. 如何在确认前执行自定义逻辑？

使用 `OnBeforeClick` 回调方法，在弹出确认框前执行自定义逻辑，返回 `true` 时弹出弹窗，返回 `false` 时不弹出。

### 2. 如何实现异步确认？

设置 `IsAsync="true"`，并在 `OnConfirm` 回调中执行异步操作。按钮会在异步操作期间禁用自身并显示 loading 动画。

### 3. 如何自定义确认框内容？

使用 `BodyTemplate` 模板自定义确认框的内容区域，可以实现复杂的布局和交互。

### 4. 如何在自定义组件中关闭确认框？

通过级联参数获取 `OnCloseAsync` 或 `OnConfirmAsync` 方法，在自定义组件中调用这些方法：

```csharp
[CascadingParameter(Name = "PopoverConfirmButtonCloseAsync")]
private Func<Task>? OnCloseAsync { get; set; }

[CascadingParameter(Name = "PopoverConfirmButtonConfirmAsync")]
private Func<Task>? OnConfirmAsync { get; set; }
```

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | PopConfirm 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/popconfirm)
- [Popover 组件文档](https://www.blazor.zone/popover)
- [Button 组件文档](https://www.blazor.zone/button)
