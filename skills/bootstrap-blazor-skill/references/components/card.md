# Card

## 概述

Card 组件

> Card component

**分类**: 基础组件
**在线演示**: [https://www.blazor.zone/card](https://www.blazor.zone/card)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `HeaderPaddingY` | `string?` | `}` | 单位需自行给定 如 0.25rem |
| `CollapseIcon` | `string?` | `}` | 获得/设置 收缩展开箭头图标 默认 fa-solid fa-circle-chevron-right |
| `HeaderText` | `string?` | `}` | 获得/设置 HeaderTemplate 显示文本 |
| `HeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 CardHeard 模板 |
| `BodyTemplate` | `RenderFragment?` | `}` | 获得/设置 BodyTemplate 模板 |
| `FooterTemplate` | `RenderFragment?` | `}` | 获得/设置 FooterTemplate 模板 |
| `Color` | `Color` | `}` | 获得/设置 Card 颜色 |
| `IsCenter` | `bool` | `}` | 获得/设置 是否居中 默认 false |
| `IsCollapsible` | `bool` | `}` | 获得/设置 是否可收缩 默认 false |
| `Collapsed` | `bool` | `}` | 获得/设置 是否收缩 默认 false 展开 |
| `IsShadow` | `bool` | `}` | 获得/设置 是否显示阴影 默认 false |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `CollapsedChanged` | `EventCallback<bool>` | 获得/设置 是否收缩 默认 false 展开 |

## 代码示例

### 基本用法

```razor
<Card>
        <BodyTemplate>
            <h5>Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a class="btn btn-primary">Go somewhere</a>
        </BodyTemplate>
    </Card>
```

### 基本用法

```razor
<Card>
        <HeaderTemplate>
            Featured
        </HeaderTemplate>
        <BodyTemplate>
            <h5>Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a class="btn btn-primary">Go somewhere</a>
        </BodyTemplate>
        <FooterTemplate>
            2 days ago
        </FooterTemplate>
    </Card>
```

### 基本用法

```razor
<Card IsCenter="true">
        <HeaderTemplate>
            Featured
        </HeaderTemplate>
        <BodyTemplate>
            <h5>Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a class="btn btn-primary">Go somewhere</a>
        </BodyTemplate>
        <FooterTemplate>
            2 days ago
        </FooterTemplate>
    </Card>
```

### 基本用法

```razor
<Card IsCollapsible="true" HeaderText="@Localizer["CollapsibleTitle"]">
        <BodyTemplate>
            @Localizer["CollapsibleBody"]
        </BodyTemplate>
    </Card>
<Card IsCollapsible="true" HeaderText="@Localizer["CollapsibleTitle"]" class="mt-3">
        <HeaderTemplate>
            <div class="flex-fill">
            </div>
            <span>@Localizer["CollapsibleHeaderTemplate"]</span>
            <Select TValue="string" class="ms-1">
                <Options>
                    <SelectOption Text="Test1" Value="" />
                    <SelectOption Text="Test2" Value="1" />
                    <SelectOption Text="Test3" Value="2" />
                    <SelectOption Text="Test4" Value="3" />
                </Options>
            </Select>
        </HeaderTemplate>
        <BodyTemplate>
            @Localizer["CollapsibleBody"]
        </BodyTemplate>
    </Card>
<Card IsCollapsible="true" HeaderText="@Localizer["CollapsibleTitle"]" class="mt-3" Collapsed="true">
        <BodyTemplate>
            @Localizer["CollapsibleBody"]
        </BodyTemplate>
    </Card>
```

### 基本用法

```razor
<Card HeaderText="@Localizer["CollapsibleTitle"]" class="mt-3">
        <HeaderTemplate>
            <div class="flex-fill">
            </div>
            <span>@Localizer["CollapsibleHeaderTemplate"]</span>
            <Select TValue="string" class="ms-1">
                <Options>
                    <SelectOption Text="Test1" Value="" />
                    <SelectOption Text="Test2" Value="1" />
                    <SelectOption Text="Test3" Value="2" />
                    <SelectOption Text="Test4" Value="3" />
                </Options>
            </Select>
        </HeaderTemplate>
        <BodyTemplate>
            @Localizer["CollapsibleHeaderTemplateTitle"]
        </BodyTemplate>
    </Card>
```
