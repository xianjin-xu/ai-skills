# Rate

## 概述

Rate 组件

> Rate Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/rate](https://www.blazor.zone/rate)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `StarIcon` | `string?` | `}` | 获得/设置 选中图标 |
| `UnStarIcon` | `string?` | `}` | 获得/设置 未选中图标 |
| `Value` | `double` | `}` | 获得/设置 组件值 |
| `IsDisable` | `bool` | `}` | - |
| `IsReadonly` | `bool` | `}` | - |
| `IsWrap` | `bool` | `}` | 获得/设置 是否禁止换行，默认为 true |
| `ShowValue` | `bool` | `}` | 获得/设置 是否显示 Value，默认为 false |
| `ItemTemplate` | `RenderFragment<double>?` | `}` | 获得/设置 子项模板 |
| `Task` | `Func<double,` | `}` | 获得/设置 组件值变化时回调方法 |
| `Max` | `int` | `5` | 获得/设置 最大值，默认为 5 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<double>` | 获得/设置 组件值变化时回调委托 |

## 代码示例

### 基本用法

```razor
<Rate @bind-Value="IconListValue" class="custom-rate">
                <ItemTemplate>
                    <i class="@GetIconList(int.Parse(Math.Round(context, 0, MidpointRounding.AwayFromZero).ToString()))"></i>
                </ItemTemplate>
            </Rate>
```

### 基本用法

```razor
<Rate Value="@BindValue1" ShowValue="true"></Rate>
```

### 基本用法

```razor
<Rate Value="@BindValue3" ShowValue="true" IsWrap="true"></Rate>
```
