# CountUp

## 概述

CountUp 组件

> CountUp component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/count-up](https://www.blazor.zone/count-up)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `TValue?` | `}` | 获得/设置 Value 值 |
| `Option` | `CountUpOption?` | `}` | 获得/设置 计数配置项 默认 null |
| `OnCompleted` | `Func<Task>?` | `}` | 获得/设置 计数结束回调方法 默认 null |

## 代码示例

### 基本用法

```razor
<CountUp TValue="double" Value="@Value" Option="_option" OnCompleted="OnCompleted" class="fw-bold fs-1 mb-2 d-block"></CountUp>
```
