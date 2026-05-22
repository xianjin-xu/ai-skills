# Circle

## 概述

Circle 组件

> Circle component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/circle](https://www.blazor.zone/circle)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `int` | `}` | 获得/设置 当前值 |

## 代码示例

### 基本用法

```razor
<Circle Width="250" Value="75" Color="Color.Success" StrokeWidth="10" ShowProgress="false">
        <div class="circle-demo">
            <h1>42,001,776</h1>
            <p>@Localizer["ChildContentP1"]</p>
            <span>
                @Localizer["ChildContentSpan"]
                <i>75%</i>
            </span>
        </div>
    </Circle>
```
