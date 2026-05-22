# Segmented

## 概述

Segmented 组件

> Segmented Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/segmented](https://www.blazor.zone/segmented)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<SegmentedOption<TValue>>?` | `}` | 获得/设置 选项集合 默认 null |
| `Value` | `TValue?` | `}` | 获得/设置 选中值 默认 null |
| `Task` | `Func<TValue,` | `}` | 获得/设置 选中值改变后回调委托方法 默认 null |
| `IsDisabled` | `bool` | `}` | 获得/设置 是否禁用 默认 false |
| `IsBlock` | `bool` | `}` | 获得/设置 是否充满父元素 默认 false |
| `ShowTooltip` | `bool` | `}` | 获得/设置 是否自动显示 Tooltip 默认 false |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 组件内容 |
| `Size` | `Size` | `}` | 获得/设置 组件大小 默认值 <see cref="Size.None"/> |
| `ItemTemplate` | `RenderFragment<SegmentedOption<TValue>>?` | `}` | 获得/设置 候选项模板 默认 null |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<TValue>` | 获得/设置 选中值回调委托 默认 null |

## 代码示例

### 基本用法

```razor
<Segmented Items="@Items" Value="@Value" OnValueChanged="OnValueChanged">
    </Segmented>
```

### 基本用法

```razor
<Segmented Items="@DisabledItems"></Segmented>
```

### 基本用法

```razor
<Segmented TValue="int" IsBlock="true" ShowTooltip="true">
        <SegmentedItem Text="Daily" Value="12" />
        <SegmentedItem Text="Weekly" Value="34" IsDisabled="true" />
        <SegmentedItem Text="Monthly" Value="56" IsActive="true" />
        <SegmentedItem Text="Quarterly" Value="78" IsDisabled="true" />
        <SegmentedItem Text="Yearly" Value="90" />
        <SegmentedItem Text="long-text1-long-text-long-text-long-text" Value="11" />
        <SegmentedItem Text="long-text2-long-text-long-text-long-text" Value="22" />
    </Segmented>
```

### 基本用法

```razor
<Segmented Items="@ItemTemplateItems">
        <ItemTemplate>
            <div class="d-flex flex-column">
                <span class="segmented-item-icon">
                    <i class="@context.Icon"></i>
                </span>
                <span>
                    @context.Text
                </span>
            </div>
        </ItemTemplate>
    </Segmented>
```

### 基本用法

```razor
<Segmented Items="@IconItems"></Segmented>
```
