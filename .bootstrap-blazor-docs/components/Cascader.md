# Cascader (级联选择器)

## 概述

`Cascader` 是一个级联选择器组件，用于选择多级关联数据，支持父子节点选择、全路径显示等配置。

> Cascader component implementation class

**分类**: 表单输入  
**在线演示**: [https://www.blazor.zone/cascader](https://www.blazor.zone/cascader)

## 使用场景

### 1. 基本用法

```razor
<Cascader @bind-Value="SelectedValue" Items="CascadeItems" />
```

```csharp
@code {
    string? SelectedValue { get; set; }
    List<CascaderItem> CascadeItems = new List<CascaderItem>
    {
        new CascaderItem("1", "北京") { Items = new List<CascaderItem> 
        {
            new CascaderItem("1-1", "朝阳区")
        }},
        new CascaderItem("2", "上海")
    };
}
```

### 2. 父节点可选择

```razor
<Cascader @bind-Value="SelectedValue" Items="CascadeItems" ParentSelectable="true" />
```

### 3. 显示全路径

```razor
<Cascader @bind-Value="SelectedValue" Items="CascadeItems" ShowFullLevels="true" />
```

### 4. 可清除

```razor
<Cascader @bind-Value="SelectedValue" Items="CascadeItems" IsClearable="true" />
```

### 5. 自定义图标

```razor
<Cascader @bind-Value="SelectedValue" Items="CascadeItems" 
           Icon="fa-solid fa-location-dot" 
           SubMenuIcon="fa-solid fa-chevron-right" />
```

### 6. 选中项改变回调

```razor
<Cascader Items="CascadeItems" OnSelectedItemChanged="OnCascaderValueChanged" />
```

```csharp
@code {
    async Task OnCascaderValueChanged(CascaderItem[] items)
    {
        // 处理选中项改变逻辑
    }
}
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TValue` | `default` | 获得/设置组件值 |
| `Color` | `Color` | `Color.None` | 获得/设置按钮颜色 |
| `PlaceHolder` | `string?` | `null` | 获得/设置组件 PlaceHolder 文字 |
| `Items` | `IEnumerable<CascaderItem>?` | `null` | 获得/设置绑定数据集 |
| `OnSelectedItemChanged` | `Func<CascaderItem[], Task>?` | `null` | 获得/设置选中项改变回调方法 |
| `ParentSelectable` | `bool` | `true` | 获得/设置父节点是否可选择 |
| `ShowFullLevels` | `bool` | `true` | 获得/设置是否显示全路径 |
| `Icon` | `string?` | `null` | 获得/设置菜单指示图标 |
| `SubMenuIcon` | `string?` | `null` | 获得/设置子菜单指示图标 |
| `IsClearable` | `bool` | `false` | 获得/设置是否可清除 |
| `ClearIcon` | `string?` | `null` | 获得/设置清除图标 |
| `OnClearAsync` | `Func<Task>?` | `null` | 获得/设置清除回调方法 |
| `OnBlurAsync` | `Func<TValue, Task>?` | `null` | 获得/设置失去焦点回调方法 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `ValueChanged` | 值改变时触发 |
| `OnSelectedItemChanged` | 选中项改变时触发 |
| `OnClearAsync` | 清除时触发 |
| `OnBlurAsync` | 失去焦点时触发 |

## 最佳实践

1. **数据绑定**: 使用 `Items` 参数提供级联数据（`CascaderItem` 集合）
2. **值绑定**: 使用 `Value` 参数绑定选中值（通常是字符串类型）
3. **父节点选择**: 设置 `ParentSelectable="true"` 允许选择父节点
4. **全路径显示**: 设置 `ShowFullLevels="true"` 显示完整路径（如"北京/朝阳区"）
5. **可清除**: 设置 `IsClearable="true"` 显示清除按钮
6. **回调处理**: 使用 `OnSelectedItemChanged` 处理选中项改变事件

## 常见问题

### Q: 如何绑定级联数据？
A: 使用 `Items` 参数提供 `CascaderItem` 集合，每个 `CascaderItem` 可以包含子节点（`Items` 属性）。

### Q: 如何绑定选中值？
A: 使用 `Value` 参数绑定到字符串变量，值为选中项的 `Value` 属性。

### Q: 如何允许选择父节点？
A: 设置 `ParentSelectable="true"` 允许选择父节点（而不仅仅是叶子节点）。

### Q: 如何显示完整路径？
A: 设置 `ShowFullLevels="true"` 显示完整路径（如"北京/朝阳区"）。

### Q: 如何处理选中项改变？
A: 使用 `OnSelectedItemChanged` 回调处理选中项改变事件，参数为 `CascaderItem[]` 数组。
