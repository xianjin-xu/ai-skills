# Checkbox

## 概述

Checkbox 组件

> Checkbox component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/checkbox](https://www.blazor.zone/checkbox)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `}` | 获得/设置 按钮颜色，默认为 <see cref="Color.None"/> |
| `Size` | `Size` | `}` | 获得/设置 Size 大小，默认为 <see cref="Size.None"/> |
| `ShowAfterLabel` | `bool` | `}` | 获得/设置 是否显示 Checkbox 后置 label 文字，默认为 false |
| `State` | `CheckboxState` | `}` | 获得/设置 选择框状态 |
| `Task` | `Func<CheckboxState,` | `}` | 获得/设置 选中状态改变前的回调方法。返回 false 可以阻止状态改变 |
| `TValue` | `Func<CheckboxState,` | `}` | 获得/设置 选择框状态改变时回调此方法 |
| `StopPropagation` | `bool` | `}` | 获得/设置 是否事件冒泡 默认为 false |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 RenderFragment 实例 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `StateChanged` | `EventCallback<CheckboxState>` | - |

## 代码示例

### 基本用法

```razor
<Checkbox TValue="string" State="CheckboxState.Checked">
        <i class="fa-solid fa-flag"></i>
        <span>@Localizer["StatusText1"]</span>
    </Checkbox>
```
