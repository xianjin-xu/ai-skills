# Display

## 概述

Display 组件

> Display Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/display](https://www.blazor.zone/display)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Task` | `Func<TValue,` | `}` | 获得/设置 异步格式化字符串 |
| `FormatString` | `string?` | `}` | 获得/设置 格式化字符串 如时间类型设置 yyyy-MM-dd |
| `Lookup` | `IEnumerable<SelectedItem>?` | `}` | - |
| `LookupService` | `ILookupService?` | `}` | - |
| `LookupServiceKey` | `string?` | `}` | - |
| `LookupServiceData` | `object?` | `}` | - |
| `LookupStringComparison` | `StringComparison` | `StringComparison.OrdinalIgnoreCase` | - |
| `string` | `Func<Assembly?,` | `}` | 获得/设置 类型解析回调方法 组件泛型为 Array 时内部调用 |
| `ShowTooltip` | `bool` | `}` | 获得/设置 是否显示 Tooltip 多用于标签文字过长导致裁减时使用 默认 false 不显示 |
