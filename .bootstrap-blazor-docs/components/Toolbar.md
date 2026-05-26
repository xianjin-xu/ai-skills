# Toolbar 工具栏

## 概述

Toolbar 组件是按钮或其他应用程序特定工具的容器，用于组织和布局工具栏内容。

> Toolbar component is a container for buttons or other application-specific tools, used to organize and layout toolbar content.

**分类**: 布局组件  
**在线演示**: [https://www.blazor.zone/toolbar](https://www.blazor.zone/toolbar)

---

## 使用场景

### 1. 基本用法

最简单的工具栏包含多个工具按钮，使用 `ToolbarItem` 包裹各个工具项。

```razor
<Toolbar>
    <ToolbarItem>
        <Button Icon="fa-solid fa-plus" Text="新增" Color="Color.Primary"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Icon="fa-solid fa-pencil" Text="编辑" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Icon="fa-solid fa-trash" Text="删除" Color="Color.Danger" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Icon="fa-solid fa-download" Text="导出" IsOutline="true"></Button>
    </ToolbarItem>
</Toolbar>
```

### 2. 按钮组

使用 `ToolbarButtonGroup` 将相关按钮分组显示，按钮之间无间距。

```razor
<Toolbar>
    <ToolbarButtonGroup>
        <Button Icon="fa-solid fa-align-left" IsOutline="true"></Button>
        <Button Icon="fa-solid fa-align-center" IsOutline="true"></Button>
        <Button Icon="fa-solid fa-align-right" IsOutline="true"></Button>
        <Button Icon="fa-solid fa-align-justify" IsOutline="true"></Button>
    </ToolbarButtonGroup>
    <ToolbarSeparator />
    <ToolbarButtonGroup>
        <Button Icon="fa-solid fa-bold" IsOutline="true"></Button>
        <Button Icon="fa-solid fa-italic" IsOutline="true"></Button>
        <Button Icon="fa-solid fa-underline" IsOutline="true"></Button>
    </ToolbarButtonGroup>
</Toolbar>
```

### 3. 分隔符

使用 `ToolbarSeparator` 在工具栏项之间添加视觉分隔符。

```razor
<Toolbar>
    <ToolbarItem>
        <Button Icon="fa-solid fa-file" Text="新建" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarSeparator />
    <ToolbarItem>
        <Button Icon="fa-solid fa-folder-open" Text="打开" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarSeparator />
    <ToolbarItem>
        <Button Icon="fa-solid fa-save" Text="保存" Color="Primary"></Button>
    </ToolbarItem>
</Toolbar>
```

### 4. 间距对齐

使用 `ToolbarSpace` 在工具栏项之间创建弹性间距，将后续项推到右侧。

```razor
<Toolbar>
    <ToolbarItem>
        <Button Icon="fa-solid fa-bars" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarSpace />
    <ToolbarItem>
        <Input @bind-Value="_searchKeyword" Placeholder="搜索..." style="width: 200px;"></Input>
    </ToolbarItem>
    <ToolbarItem>
        <Button Icon="fa-solid fa-search" Color="Color.Primary"></Button>
    </ToolbarItem>
</Toolbar>

@code {
    private string? _searchKeyword { get; set; }
}
```

### 5. 换行显示

设置 `IsWrap="true"` 允许工具栏内容在空间不足时换行显示。

```razor
<Toolbar IsWrap="true">
    <ToolbarItem>
        <Button Text="按钮 1" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Text="按钮 2" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Text="按钮 3" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Text="按钮 4" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Text="按钮 5" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Text="按钮 6" IsOutline="true"></Button>
    </ToolbarItem>
    <ToolbarSeparator />
    <ToolbarItem>
        <Button Text="操作 A" Color="Color.Primary"></Button>
    </ToolbarItem>
    <ToolbarItem>
        <Button Text="操作 B" IsOutline="true"></Button>
    </ToolbarItem>
</Toolbar>
```

### 6. 复杂工具栏

组合使用各种工具栏子组件创建功能丰富的工具栏。

```razor
<Toolbar IsWrap="true">
    <ToolbarItem>
        <Button Icon="fa-solid fa-wand-magic-sparkles" IsOutline="true" Title="格式刷"></Button>
    </ToolbarItem>
    <ToolbarSeparator />
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
    <ToolbarSeparator />
    <ToolbarItem>
        <Select TValue="int" Color="Color.Primary" IsPopover="true" style="min-width: 120px;">
            <Options>
                <SelectOption Value="1" Text="选项 1"></SelectOption>
                <SelectOption Value="2" Text="选项 2"></SelectOption>
                <SelectOption Value="3" Text="选项 3"></SelectOption>
            </Options>
        </Select>
    </ToolbarItem>
    <ToolbarItem>
        <Dropdown TValue="string" Value="@_item3" Items="_items3" IsPopover="true"></Dropdown>
    </ToolbarItem>
    <ToolbarSpace></ToolbarSpace>
    <ToolbarButtonGroup>
        <Button Icon="fa-solid fa-save" IsOutline="true" Title="保存"></Button>
        <Button Icon="fa-solid fa-undo" IsOutline="true" Title="撤销"></Button>
        <Button Icon="fa-solid fa-redo" IsOutline="true" Title="重做"></Button>
    </ToolbarButtonGroup>
</Toolbar>

@code {
    private string? _item1 { get; set; }
    private List<string> _item2 { get; set; } = new();
    private string? _item3 { get; set; }
    private List<SelectedItem> _items1 { get; set; } = new();
    private List<SelectedItem> _items2 { get; set; } = new();
    private List<SelectedItem> _items3 { get; set; } = new();
}
```

---

## 参数 (Parameters)

### Toolbar 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件模板 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsWrap` | `bool` | `false` | 获得/设置 是否允许换行显示工具栏内容 |

---

## 子组件 (Child Components)

### ToolbarItem

工具栏项容器，用于包裹单个工具项。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件模板 |

### ToolbarButtonGroup

按钮组容器，用于将多个按钮分组显示。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件模板 |

### ToolbarSeparator

工具栏分隔符，用于在工具栏项之间添加视觉分隔。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件模板 |

### ToolbarSpace

工具栏间距，用于在工具栏项之间创建弹性间距。

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件模板 |

---

## 最佳实践

### 1. 工具栏布局建议

- **左侧放置常用操作**：将最常用的操作按钮放在工具栏左侧
- **右侧放置搜索和设置**：将搜索框、设置按钮等放在工具栏右侧，使用 `ToolbarSpace` 分隔
- **相关功能分组**：使用 `ToolbarButtonGroup` 将相关功能按钮分组，使用 `ToolbarSeparator` 分隔不同组别

### 2. 按钮样式建议

- **主要操作使用实心按钮**：如"保存"、"提交"等主要操作使用 `Color="Color.Primary"` 实心按钮
- **次要操作使用轮廓按钮**：如"编辑"、"删除"等次要操作使用 `IsOutline="true"` 轮廓按钮
- **图标按钮添加 Title**：纯图标按钮应添加 `Title` 属性以提供tooltip提示

### 3. 响应式设计

- **启用换行**：在窄屏场景下，设置 `IsWrap="true"` 允许工具栏内容换行
- **使用 IsPopover**：下拉组件设置 `IsPopover="true"` 可在工具栏中更紧凑地显示

---

## 常见问题 (FAQ)

### Q1: 如何让工具栏项右对齐？

**A**: 在需要右对齐的工具栏项之前添加 `ToolbarSpace` 组件，`ToolbarSpace` 会占据剩余空间，将后续项推到右侧。

```razor
<Toolbar>
    <ToolbarItem>
        <Button Text="左侧按钮"></Button>
    </ToolbarItem>
    <ToolbarSpace />
    <ToolbarItem>
        <Button Text="右侧按钮"></Button>
    </ToolbarItem>
</Toolbar>
```

### Q2: 如何在工具栏中使用下拉菜单？

**A**: 在 `ToolbarItem` 中使用 `Dropdown` 组件。

```razor
<Toolbar>
    <ToolbarItem>
        <Dropdown TValue="string" Value="@_value" Items="_items">
            <DropdownItem Icon="fa-solid fa-gear" Text="设置"></DropdownItem>
            <DropdownItem Icon="fa-solid fa-question-circle" Text="帮助"></DropdownItem>
        </Dropdown>
    </ToolbarItem>
</Toolbar>
```

### Q3: 工具栏可以嵌套在其他组件中吗？

**A**: 可以。Toolbar 组件可以嵌套在 `Card`、`Modal`、`Drawer` 等组件中，作为这些组件的工具栏使用。

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 Toolbar 组件 |
