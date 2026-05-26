# SelectTree 树状选择器

## 组件概述

SelectTree 是一个树状选择器组件，在下拉框内呈现树状数据结构，供用户选择。支持单选和多选模式，提供搜索、验证、可编辑等丰富功能。

## 使用场景

### 1. 基础用法

基本的使用方式。

```razor
<SelectTree TValue="string" Items="@TreeItems" Value="@SelectedValue" OnValueChanged="OnValueChanged" />
```

```csharp
@code {
    private string SelectedValue { get; set; }
    private List<TreeViewItem<string>> TreeItems { get; set; }
    
    private Task OnValueChanged(string value)
    {
        SelectedValue = value;
        return Task.CompletedTask;
    }
}
```

**说明：**
- `TValue` - 值类型参数
- `Items` - 树状数据集合
- `Value` - 当前选中值
- `OnValueChanged` - 值改变回调

### 2. 禁用状态

通过设置 `IsDisabled` 使组件禁用。

```razor
<SelectTree TValue="string" Items="@TreeItems" IsDisabled="true" />
```

**说明：**
- `IsDisabled="true"` 禁用组件
- 禁用后无法展开、选择

### 3. 双向绑定

绑定组件内变量，数据自动同步。

```razor
<SelectTree TValue="string" Items="@TreeItems" @bind-Value="SelectedValue" />
```

**说明：**
- 使用 `@bind-Value` 实现双向绑定
- 值改变时自动同步

### 4. 客户端验证

组件内置 ValidateForm 可设置验证规则。

```razor
<ValidateForm>
    <SelectTree TValue="string" Items="@TreeItems" @bind-Value="SelectedValue" 
               RequiredErrorMessage="请选择项目" />
    <Button ButtonType="ButtonType.Submit">提交</Button>
</ValidateForm>
```

**说明：**
- 配合 `ValidateForm` 组件使用
- 设置 `RequiredErrorMessage` 必填错误消息

### 5. 可输入

通过设置 `IsEditable="true"` 可设置下拉框选择后文本框可输入。

```razor
<SelectTree TValue="string" Items="@TreeItems" IsEditable="true" />
```

**说明：**
- `IsEditable="true"` 后，文本框显示的内容为 TreeView 选中节点的 Value 值
- 输入值可以不在 Items 集合中

### 6. 悬浮弹窗

通过设置 `IsPopover` 参数，组件使用 popover 渲染 UI 防止由于父容器设置 `overflow: hidden` 使弹窗无法显示问题。

```razor
<SelectTree TValue="string" Items="@TreeItems" IsPopover="true" />
```

**说明：**
- `IsPopover="true"` 使用 Popover 模式渲染下拉框
- 适用于父容器有 `overflow: hidden` 样式的场景

### 7. 显示搜索栏

通过设置 `ShowSearch="true"` 显示搜索栏。

```razor
<SelectTree TValue="string" Items="@TreeItems" ShowSearch="true" 
           OnSearchAsync="OnSearch" />
```

```csharp
@code {
    private async Task<List<TreeViewItem<string>>> OnSearch(string searchText)
    {
        // 根据 searchText 搜索并返回匹配的节点
        var results = TreeItems.Where(item => item.Text.Contains(searchText)).ToList();
        return await Task.FromResult(results);
    }
}
```

**说明：**
- `ShowSearch="true"` 显示搜索栏
- `OnSearchAsync` 搜索回调方法

### 8. 完整示例

包含选择、禁用、验证、搜索等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>树状选择器示例</CardTitle>
    </CardHeader>
    <CardBody>
        <ValidateForm>
            <div class="row g-3">
                <div class="col-12 col-md-6">
                    <SelectTree TValue="string" 
                               Items="@TreeItems" 
                               @bind-Value="SelectedValue" 
                               ShowSearch="true" 
                               IsEditable="true"
                               IsPopover="true"
                               PlaceHolder="请选择项目"
                               RequiredErrorMessage="请选择项目"
                               OnSearchAsync="OnSearch" 
                               OnValueChanged="OnValueChanged" />
                </div>
                <div class="col-12 col-md-6">
                    <Button ButtonType="ButtonType.Submit" Color="Color.Primary">提交</Button>
                    <Button Color="Color.Secondary" @onclick="Reset">重置</Button>
                </div>
            </div>
        </ValidateForm>
    </CardBody>
</Card>

@code {
    private string SelectedValue { get; set; }
    private List<TreeViewItem<string>> TreeItems { get; set; }
    
    private Task OnValueChanged(string value)
    {
        SelectedValue = value;
        Console.WriteLine($"选中值: {value}");
        return Task.CompletedTask;
    }
    
    private async Task<List<TreeViewItem<string>>> OnSearch(string searchText)
    {
        var results = TreeItems.Where(item => item.Text.Contains(searchText)).ToList();
        return await Task.FromResult(results);
    }
    
    private void Reset()
    {
        SelectedValue = null;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Value` | 获得/设置 输入组件的值，支持双向绑定 | `TValue` | - |
| `Items` | 获得/设置 分层数据集合 | `List<TreeViewItem<TValue>>` | - |
| `IsDisabled` | 获得/设置 是否禁用 | `bool` | `false` |
| `IsEditable` | 获得/设置 是否可编辑 | `bool` | `false` |
| `IsPopover` | 获得/设置 是否使用 Popover 渲染 | `bool` | `false` |
| `ShowSearch` | 获得/设置 是否显示搜索栏 | `bool` | `false` |
| `ShowResetSearchButton` | 获得/设置 是否显示重置搜索按钮 | `bool` | `true` |
| `ShowIcon` | 获得/设置 是否显示 Icon 图标 | `bool` | `false` |
| `ShowShadow` | 获得/设置 是否显示阴影 | `bool` | `true` |
| `PlaceHolder` | 获得 PlaceHolder 属性 | `string` | - |
| `DropdownIcon` | 获得/设置 下拉箭头 Icon 图标 | `string` | - |
| `Color` | 获得/设置 颜色 | `Color` | `Color.None` |
| `OnValueChanged` | 获得/设置 Value 改变时回调方法 | `Func<TValue, Task>` | - |
| `OnSearchAsync` | 获得/设置 搜索回调方法 | `Func<string, Task<List<TreeViewItem<TValue>>>>` | `null` |
| `OnExpandNodeAsync` | 获得/设置 点击节点获取子数据集合回调方法 | `Func<TreeViewItem<TValue>, Task<IEnumerable<TreeViewItem<TValue>>>>` | - |
| `CanExpandWhenDisabled` | 获得/设置 禁用时是否可以展开或折叠节点 | `bool` | `false` |
| `ModelEqualityComparer` | 获得/设置 比较数据是否相同回调方法 | `Func<TValue, TValue, bool>` | - |
| `StringComparison` | 获得/设置 字符串比较规则 | `StringComparison` | - |
| `SkipValidate` | 获得/设置 是否不进行验证 | `bool` | `false` |
| `RequiredErrorMessage` | 获得/设置 必填项错误文本 | `string` | `null` |
| `ParsingErrorMessage` | 获得/设置 类型转化失败格式化字符串 | `string` | `null` |
| `ShowLabel` | 获得/设置 是否显示前置标签 | `Nullable<bool>` | `null` |
| `ShowLabelTooltip` | 获得/设置 是否显示 Tooltip | `Nullable<bool>` | `null` |
| `ShowRequired` | 获得/设置 是否显示必填项标记 | `Nullable<bool>` | `null` |
| `ValidateRules` | 获得/设置 自定义验证集合 | `List<IValidator>` | - |

## 最佳实践

1. **数据绑定**: 使用 `@bind-Value` 实现双向绑定，简化代码
2. **搜索功能**: 设置 `ShowSearch="true"` 并实现 `OnSearchAsync` 回调
3. **验证规则**: 配合 `ValidateForm` 使用，设置 `RequiredErrorMessage`
4. **Popover 模式**: 当父容器有 `overflow: hidden` 时使用 `IsPopover="true"`
5. **可编辑**: 设置 `IsEditable="true"` 允许用户手动输入不在树中的值

## 常见问题

**Q: 如何实现异步加载子节点？**
A: 实现 `OnExpandNodeAsync` 回调方法，点击节点时动态加载子数据。

**Q: 如何自定义搜索逻辑？**
A: 实现 `OnSearchAsync` 回调方法，返回匹配的节点集合。

**Q: 如何禁用组件？**
A: 设置 `IsDisabled="true"`。

**Q: 如何验证必填？**
A: 配合 `ValidateForm` 组件，设置 `RequiredErrorMessage` 属性。

**Q: 为什么下拉框被遮挡？**
A: 父容器可能有 `overflow: hidden` 样式，设置 `IsPopover="true"` 使用 Popover 模式。

## 版本历史

- **初始版本**: 支持树状选择、搜索、验证、可编辑、Popover 模式等功能
