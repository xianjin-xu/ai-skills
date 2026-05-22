# Collapse

## 概述

Collapse 组件

> Collapse component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/collapse](https://www.blazor.zone/collapse)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsAccordion` | `bool` | `}` | 获得/设置 是否为手风琴效果 默认为 false |
| `CollapseItems` | `RenderFragment?` | `}` | 获得/设置 CollapseItems 模板 |
| `Task` | `Func<CollapseItem,` | `}` | 获得/设置 CollapseItem 展开收缩时回调方法 |

## 代码示例

### 基本用法

```razor
<Collapse OnCollapseChanged="@OnChanged">
        <CollapseItems>
            <CollapseItem Text="@Localizer["Consistency"]">
                <div>@Localizer["ConsistencyItem1"]</div>
                <div>@Localizer["ConsistencyItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Feedback"]" IsCollapsed="false">
                <div>@Localizer["FeedbackItem1"]</div>
                <div>@Localizer["FeedbackItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Efficiency"]">
                <div>@Localizer["EfficiencyItem1"]</div>
                <div>@Localizer["EfficiencyItem2"]</div>
                <div>@Localizer["EfficiencyItem3"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Controllability"]">
                <div>@Localizer["ControllabilityItem1"]</div>
                <div>@Localizer["ControllabilityItem2"]</div>
            </CollapseItem>
        </CollapseItems>
    </Collapse>
```

### 基本用法

```razor
<Collapse IsAccordion="true">
        <CollapseItems>
            <CollapseItem Text="@Localizer["Consistency"]">
                <div>@Localizer["ConsistencyItem1"]</div>
                <div>@Localizer["ConsistencyItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Feedback"]">
                <div>@Localizer["FeedbackItem1"]</div>
                <div>@Localizer["FeedbackItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Efficiency"]">
                <div>@Localizer["EfficiencyItem1"]</div>
                <div>@Localizer["EfficiencyItem2"]</div>
                <div>@Localizer["EfficiencyItem3"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Controllability"]">
                <div>@Localizer["ControllabilityItem1"]</div>
                <div>@Localizer["ControllabilityItem2"]</div>
            </CollapseItem>
        </CollapseItems>
    </Collapse>
```

### 基本用法

```razor
<Collapse IsAccordion="true">
        <CollapseItems>
            <CollapseItem Text="@Localizer["Consistency"]" TitleColor="Color.Primary">
                <div>@Localizer["ConsistencyItem1"]</div>
                <div>@Localizer["ConsistencyItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Feedback"]" TitleColor="Color.Info">
                <div>@Localizer["FeedbackItem1"]</div>
                <div>@Localizer["FeedbackItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Efficiency"]" TitleColor="Color.Success">
                <div>@Localizer["EfficiencyItem1"]</div>
                <div>@Localizer["EfficiencyItem2"]</div>
                <div>@Localizer["EfficiencyItem3"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Controllability"]" TitleColor="Color.Warning">
                <div>@Localizer["ControllabilityItem1"]</div>
                <div>@Localizer["ControllabilityItem2"]</div>
            </CollapseItem>
        </CollapseItems>
    </Collapse>
```

### 基本用法

```razor
<Collapse>
        <CollapseItems>
            @if (State)
            {
                <CollapseItem Text="@Localizer["Consistency"]">
                    <div>@Localizer["ConsistencyItem1"]</div>
                    <div>@Localizer["ConsistencyItem2"]</div>
                </CollapseItem>
                <CollapseItem Text="@Localizer["Feedback"]" IsCollapsed="false">
                    <div>@Localizer["FeedbackItem1"]</div>
                    <div>@Localizer["FeedbackItem2"]</div>
                </CollapseItem>
            }
            else
            {
                <Collapse>
                    <CollapseItems>
                        <CollapseItem Text="@Localizer["Consistency"]">
                            <div>@Localizer["ConsistencyItem1"]</div>
                            <div>@Localizer["ConsistencyItem2"]</div>
                        </CollapseItem>
                        <CollapseItem Text="@Localizer["Feedback"]">
                            <div>@Localizer["FeedbackItem1"]</div>
                            <div>@Localizer["FeedbackItem2"]</div>
                        </CollapseItem>
                        <CollapseItem Text="@Localizer["Efficiency"]">
                            <div>@Localizer["EfficiencyItem1"]</div>
                            <div>@Localizer["EfficiencyItem2"]</div>
                            <div>@Localizer["EfficiencyItem3"]</div>
                        </CollapseItem>
                        <CollapseItem Text="@Localizer["Controllability"]">
                            <div>@Localizer["ControllabilityItem1"]</div>
                            <div>@Localizer["ControllabilityItem2"]</div>
                        </CollapseItem>
                    </CollapseItems>
                </Collapse>
```

### 基本用法

```razor
<Collapse IsAccordion="true">
        <CollapseItems>
            <CollapseItem Text="@Localizer["Consistency"]" Icon="fa-solid fa-people-roof">
                <div>@Localizer["ConsistencyItem1"]</div>
                <div>@Localizer["ConsistencyItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Feedback"]" Icon="fa-solid fa-users">
                <div>@Localizer["FeedbackItem1"]</div>
                <div>@Localizer["FeedbackItem2"]</div>
            </CollapseItem>
            <CollapseItem Text="@Localizer["Controllability"]" Icon="fa-solid fa-users-gear">
                <div>@Localizer["ControllabilityItem1"]</div>
                <div>@Localizer["ControllabilityItem2"]</div>
            </CollapseItem>
        </CollapseItems>
    </Collapse>
```
