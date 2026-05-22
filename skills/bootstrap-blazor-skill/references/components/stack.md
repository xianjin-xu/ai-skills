# Stack

## 概述

Stack 组件

> Stack Component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/stack](https://www.blazor.zone/stack)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 内容 |
| `IsRow` | `bool` | `}` | 获得/设置 是否为行布局 默认 false |
| `IsReverse` | `bool` | `}` | 获得/设置 是否反向布局 默认 false |
| `IsWrap` | `bool` | `}` | 获得/设置 是否允许折行 默认 false |
| `AlignItems` | `StackAlignItems` | `}` | 获得/设置 垂直布局模式 默认 StackAlignItems.Stretch |
| `Justify` | `StackJustifyContent` | `}` | 获得/设置 水平布局调整 默认 StackJustifyContent.Start |

## 代码示例

### 基本用法

```razor
<Stack IsRow="@IsRow" Justify="@Justify" AlignItems="@AlignItems" IsWrap="@IsWrap" IsReverse="@IsReverse">
            <StackItem>
                <div class="stack-item-demo">Item 1</div>
            </StackItem>
            <StackItem AlignSelf="@AlignSelf">
                <div class="stack-item-demo">Item 2</div>
            </StackItem>
            <StackItem>
                <div class="stack-item-demo">Item 3</div>
            </StackItem>
        </Stack>
```
