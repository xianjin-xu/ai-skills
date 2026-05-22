# Toolbar

## 概述

Toolbar 组件用于显示工具栏内容

> Toolbar Component for displaying toolbar content

**分类**: 其他
**在线演示**: [https://www.blazor.zone/toolbar](https://www.blazor.zone/toolbar)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsWrap` | `bool` | `}` | 获得/设置 是否允许换行显示工具栏内容，默认 false |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件模板 |

## 代码示例

### 基本用法

```razor
<Toolbar IsWrap="true">
        <ToolbarItem>
            <Button Icon="fa-solid fa-wand-magic-sparkles" IsOutline="true"></Button>
        </ToolbarItem>
        <ToolbarItem>
            <CheckboxList IsButton="true" Items="_items2" @bind-Value="_item2" ShowButtonBorderColor="true">
                <ItemTemplate>
                    <i class="@GetRadioIconByItem(context.Value)"></i>
                </ItemTemplate>
            </CheckboxList>
        </ToolbarItem>
        <ToolbarItem>
            <RadioList IsButton="true" Items="_items1" @bind-Value="_item1" ShowButtonBorderColor="true">
                <ItemTemplate>
                    <i class="@GetIconByItem(context.Value)"></i>
                </ItemTemplate>
            </RadioList>
        </ToolbarItem>
        <ToolbarItem>
            <Select TValue="int" Color="Color.Primary" IsPopover="true" style="min-width: 120px;">
                <Options>
                    <SelectOption Value="1" Text="Text 1"></SelectOption>
                    <SelectOption Value="2" Text="Text 2"></SelectOption>
                    <SelectOption Value="3" Text="Text 3"></SelectOption>
                </Options>
            </Select>
        </ToolbarItem>
        <ToolbarItem>
            <Dropdown TValue="string" Value="@_item3" Items="_items3" IsPopover="true"></Dropdown>
        </ToolbarItem>
        <ToolbarSpace></ToolbarSpace>
        <ToolbarButtonGroup>
            <Button Icon="fa-solid fa-save" IsOutline="true"></Button>
            <Button Icon="fa-solid fa-save" IsOutline="true"></Button>
            <Button Icon="fa-solid fa-save" IsOutline="true"></Button>
        </ToolbarButtonGroup>
        <ToolbarSeparator></ToolbarSeparator>
        <ToolbarButtonGroup>
            <Button Icon="fa-solid fa-save"></Button>
            <Button Icon="fa-solid fa-save"></Button>
            <Button Icon="fa-solid fa-save"></Button>
        </ToolbarButtonGroup>
    </Toolbar>
```
