# Timeline

## 概述

时间线组件基类

> Timeline Component Base Class

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/timeline](https://www.blazor.zone/timeline)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<TimelineItem>?` | `}` | 获得/设置 绑定数据集合 |
| `IsReverse` | `bool` | `}` | 获得/设置 是否反转 |
| `IsAlternate` | `bool` | `}` | 获得/设置 是否左右交替出现，默认 false |
| `IsLeft` | `bool` | `}` | 获得/设置 内容是否出现在时间线左侧，默认为 false |

## 代码示例

### 基本用法

```razor
<Timeline Items="TimelineItems" IsReverse="@IsReverse"></Timeline>
```
