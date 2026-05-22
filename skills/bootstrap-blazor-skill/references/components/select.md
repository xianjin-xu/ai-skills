# Select

## 概述

Select 组件

> Select component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/select](https://www.blazor.zone/select)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsUseActiveWhenValueIsNull` | `bool` | `-` | 获得/设置 值为 null 时是否使用第一个选项或者标记为 active 的候选项作为默认值 |
| `IsUseDefaultItemWhenValueIsNull` | `bool` | `}` | 获得/设置 值为 null 时是否使用第一个选项或者标记为 active 的候选项作为默认值 |
| `DisplayTemplate` | `RenderFragment<SelectedItem?>?` | `}` | 获得/设置 显示模板，默认为 null |
| `Task` | `Func<string,` | `}` | - |
| `Options` | `RenderFragment?` | `}` | 获得/设置 静态数据的选项模板 |
| `DisableItemChangedWhenFirstRender` | `bool` | `}` | 获得/设置 是否在首次渲染时禁用 OnSelectedItemChanged 回调方法，默认为 false |
| `ShowSwal` | `bool` | `}` | 获得/设置 是否显示 Swal 确认弹窗，默认为 false |
| `SwalCategory` | `SwalCategory` | `SwalCategory.Question` | 获得/设置 Swal 类别，默认为 Question |
| `SwalTitle` | `string?` | `}` | 获得/设置 Swal 标题，默认为 null |
| `SwalContent` | `string?` | `}` | 获得/设置 Swal 内容，默认为 null |
| `SwalFooter` | `string?` | `}` | 获得/设置 Swal 底部内容，默认为 null |
| `LookupService` | `ILookupService?` | `}` | - |
| `LookupServiceKey` | `string?` | `}` | - |
| `LookupServiceData` | `object?` | `}` | - |
| `DefaultVirtualizeItemText` | `string?` | `}` | 获得/设置 虚拟化项目的默认文本，默认为 null |
| `IsAutoClearSearchTextWhenCollapsed` | `bool` | `}` | 获得/设置 下拉框关闭时是否自动清空搜索文本 |
| `OnCollapsed` | `Func<Task>?` | `}` | 获得/设置 下拉框关闭时的回调方法 |

## 代码示例

### 基本用法

```razor
<Select Color="Color.Primary" Items="Items" @bind-Value="BindingModel.Name"></Select>
```

### 基本用法

```razor
<Select Color="Color.Primary" Items="Items" @bind-Value="Item"></Select>
```

### 基本用法

```razor
<Select @bind-Value="ValidateModel.Name">
                    <Options>
                        <SelectOption Text="@Localizer["SelectsOption1"]" Value="" />
                        <SelectOption Text="@Localizer["SelectsOption2"]" Value="1" />
                        <SelectOption Text="@Localizer["SelectsOption3"]" Value="2" />
                        <SelectOption Text="@Localizer["SelectsOption4"]" Value="3" />
                    </Options>
                </Select>
```

### 基本用法

```razor
<Select TValue="string" Color="Color.Primary" Items="GroupItems">
            </Select>
```

### 基本用法

```razor
<Select TValue="string">
                <Options>
                    <SelectOption Text="@Localizer["SelectsOption1"]" Value="1" />
                    <SelectOption Text="@Localizer["SelectsOption2"]" Value="2" Active="true" />
                    <SelectOption Text="@Localizer["SelectsOption3"]" Value="3" />
                </Options>
            </Select>
```
