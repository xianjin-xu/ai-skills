# IFrame

## 概述

Frame component encapsulates the Html iframe element

> Frame component encapsulates the Html iframe element

**分类**: 其他
**在线演示**: [https://www.blazor.zone/iframe](https://www.blazor.zone/iframe)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Src` | `string?` | `}` | 获得/设置 the URL of the webpage to be loaded in the Frame |
| `Data` | `object?` | `}` | 获得/设置 the 数据 to be passed |
| `Task` | `Func<object?,` | `}` | 获得/设置 Frame loads the 数据 passed by the page |
| `OnReadyAsync` | `Func<Task>?` | `}` | 获得/设置 Callback method after the page is loaded |

## 代码示例

### 基本用法

```razor
<IFrame Src="https://pro.blazor.zone"></IFrame>
```
