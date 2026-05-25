# Dropdown (下拉菜单组件)

## 概述

`Dropdown` 组件用于**创建下拉菜单**，点击按钮后显示菜单选项。

**主要特性**：
- 支持不同颜色（Color）
- 支持 Outline 样式（IsOutline）
- 支持不同尺寸（Size）
- 支持分裂式按钮（ShowSplit）
- 支持菜单对齐方式（MenuAlignment）
- 支持下拉方向（Direction）

**在线演示**: https://www.blazor.zone/dropdown

---

## 使用场景

### 1. 基础用法（简单下拉菜单）

`Dropdown` 组件通过 `Items` 参数绑定菜单项。

```razor
<Dropdown TValue="string?" Items="DropdownItems" OnSelectedItemChanged="OnDropdownChanged">
    <ButtonTemplate>
        <Button Color="Color.Primary">操作 <span class="caret"></span></Button>
    </ButtonTemplate>
</Dropdown>

@code {
    private List<SelectedItem> DropdownItems { get; set; } = new List<SelectedItem>
    {
        new SelectedItem("复制", "copy") { Icon = "fa fa-copy" },
        new SelectedItem("粘贴", "paste") { Icon = "fa fa-paste" },
        new SelectedItem("分隔符", "divider") { IsDisabled = true },
        new SelectedItem("删除", "delete") { Icon = "fa fa-trash" }
    };

    private void OnDropdownChanged(SelectedItem item)
    {
        Console.WriteLine($"选择了：{item?.Text}");
    }
}
```

---

### 2. 不同颜色（ Color）

通过设置 `Color` 参数设置下拉按钮颜色。

```razor
<!-- 主要颜色 -->
<Dropdown TValue="string?" Items="Items" Color="Color.Primary">
    <ButtonTemplate><Button Color="Color.Primary">主要</Button></ButtonTemplate>
</Dropdown>

<!-- 成功颜色 -->
<Dropdown TValue="string?" Items="Items" Color="Color.Success">
    <ButtonTemplate><Button Color="Color.Success">成功</Button></ButtonTemplate>
</Dropdown>

<!-- 危险颜色 -->
<Dropdown TValue="string?" Items="Items" Color="Color.Danger">
    <ButtonTemplate><Button Color="Color.Danger">危险</Button></ButtonTemplate>
</Dropdown>
```

---

### 3. Outline 样式（IsOutline）

通过设置 `IsOutline="true"` 使用 Outline 样式按钮。

```razor
<Dropdown TValue="string?" Items="Items" IsOutline="true" Color="Color.Primary">
    <ButtonTemplate><Button IsOutline="true" Color="Color.Primary">Outline 样式</Button></ButtonTemplate>
</Dropdown>
```

---

### 4. 分裂式按钮（ShowSplit）

通过设置 `ShowSplit="true"` 启用分裂式按钮（左按钮触发动作，右箭头展开菜单）。

```razor
<Dropdown TValue="string?" Items="Items" ShowSplit="true" OnClick="OnSplitClick">
    <ButtonTemplate>
        <Button Color="Color.Primary">
            <span>默认动作</span>
            <span class="caret"></span>
        </Button>
    </ButtonTemplate>
</Dropdown>

@code {
    private void OnSplitClick()
    {
        Console.WriteLine("点击了左按钮");
    }
}
```

---

### 5. 菜单对齐方式（MenuAlignment）

通过设置 `MenuAlignment` 参数设置下拉菜单对齐方式。

```razor
<!-- 左对齐（默认） -->
<Dropdown TValue="string?" Items="Items" MenuAlignment="Alignment.Left">
    <ButtonTemplate><Button>左对齐</Button></ButtonTemplate>
</Dropdown>

<!-- 右对齐 -->
<Dropdown TValue="string?" Items="Items" MenuAlignment="Alignment.Right">
    <ButtonTemplate><Button>右对齐</Button></ButtonTemplate>
</Dropdown>
```

---

### 6. 下拉方向（Direction）

通过设置 `Direction` 参数设置下拉菜单展开方向。

```razor
<!-- 向下（默认） -->
<Dropdown TValue="string?" Items="Items" Direction="Direction.Down">
    <ButtonTemplate><Button>向下</Button></ButtonTemplate>
</Dropdown>

<!-- 向上 -->
<Dropdown TValue="string?" Items="Items" Direction="Direction.Up">
    <ButtonTemplate><Button>向上</Button></ButtonTemplate>
</Dropdown>
```

---

## 参数 (Parameters)

### Dropdown 组件参数#

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<SelectedItem>?` | `null` | 获得/设置 绑定数据集 |
| `TValue` | `Type?` | `null` | 获得/设置 泛型类型 |
| `Color` | `Color` | `Color.Primary` | 获得/设置 颜色 默认 Color.Primary 无设置 |
| `IsOutline` | `bool` | `false` | 获得/设置 Outline 样式 默认 false |
| `Size` | `Size` | `Size.None` | 获得/设置 组件尺寸 默认 none 未设置 |
| `ShowSplit` | `bool` | `false` | 获得/设置 是否开启分裂式 默认 false |
| `MenuAlignment` | `Alignment` | `Alignment.Left` | 获得/设置 菜单对齐方式 默认 Left |
| `Direction` | `Direction` | `Direction.Down` | 获得/设置 下拉选项方向 默认 Down 向下 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `Icon` | `string?` | `null` | 获得/设置 显示图标 |
| `ShowIcon` | `bool` | `false` | 获得/设置 是否显示图标 |
| `ButtonTemplate` | `RenderFragment?` | `null` | 获得/设置 按钮内容模板 |
| `ItemTemplate` | `RenderFragment<SelectedItem>?` | `null` | 获得/设置 菜单项模板 |
| `HeaderTemplate` | `RenderFragment?` | `null` | 获得/设置 菜单头部模板 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnSelectedItemChanged` | `EventCallback<SelectedItem>` | 选择项改变时回调 |
| `OnClick` | `EventCallback<MouseEventArgs>` | ShowSplit 为 true 时，点击左按钮回调 |

---

## 最佳实践#

1. **使用 SelectedItem 绑定**：通过 `Items` 参数绑定 `List<SelectedItem>` 数据集
2. **合理使用 Color**：根据场景选择颜色（主要操作 `Primary`、危险操作 `Danger`、成功状态 `Success`）
3. **使用 ShowSplit**：对于常用操作，使用 `ShowSplit="true"` 让左按钮直接触发动作，右箭头展开更多选项
4. **菜单项分组**：使用 `SelectedItem` 的 `IsDisabled=true` 且 `Value="divider"` 创建分隔线
5. **与 Select 的区别**：`Dropdown` 是菜单按钮（点击触发），`Select` 是下拉选择框（表单控件）
6. **与 DropdownWidget 的区别**：`Dropdown` 是标准下拉菜单，`DropdownWidget` 是可自定义内容的高级下拉组件

---

## 常见问题#

### Q: 如何使用 FontAwesome 图标？
A: 在 `SelectedItem` 中设置 `Icon = "fa fa-icon-name"`。

### Q: 如何实现级联菜单？
A: 使用 `DropdownWidget` 组件支持更灵活的菜单内容（包括级联）。

### Q: 如何禁用某个菜单项？
A: 创建 `SelectedItem` 时设置 `IsDisabled = true`。

### Q: 如何动态更新菜单项？
A: 更新 `Items` 数据源后调用 `StateHasChanged()` 刷新 UI。
