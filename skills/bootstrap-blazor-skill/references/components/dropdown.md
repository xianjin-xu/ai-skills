# Dropdown

## 概述

Dropdown 下拉框组件

> Dropdown Component

**分类**: 反馈
**在线演示**: [https://www.blazor.zone/dropdown](https://www.blazor.zone/dropdown)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.Primary` | 获得/设置 颜色 默认 Color.Primary 无设置 |
| `IsOutline` | `bool` | `}` | 获得/设置 Outline 样式 默认 false |
| `Items` | `IEnumerable<SelectedItem>?` | `}` | 获得/设置 绑定数据集 |
| `ItemTemplate` | `RenderFragment<SelectedItem>?` | `}` | 获得/设置 选项模板 |
| `ButtonTemplate` | `RenderFragment<SelectedItem?>?` | `}` | 获得/设置 按钮内容模板 |
| `ShowSplit` | `bool` | `}` | 获得/设置 是否开启分裂式 默认 false |
| `OnClickWithoutRender` | `Func<Task>?` | `}` | <see cref="ShowSplit"/> 为 true 时生效 |
| `IsAsync` | `bool` | `}` | <see cref="ShowSplit"/> 为 true 时生效 |
| `IsKeepDisabled` | `bool` | `}` | - |
| `Icon` | `string?` | `}` | 获得/设置 显示图标 |
| `LoadingIcon` | `string?` | `}` | 获得/设置 正在加载动画图标 默认为 fa-solid fa-spin fa-spinner |
| `MenuAlignment` | `Alignment` | `}` | 获得/设置 获取菜单对齐方式 默认 none 未设置 |
| `Direction` | `Direction` | `}` | 获得/设置 下拉选项方向 默认 Dropdown 向下 |
| `Size` | `Size` | `}` | 获得/设置 组件尺寸 默认 none 未设置 |
| `IsFixedButtonText` | `bool` | `}` | 获得/设置 是否固定按钮文字 更改下拉框选项时按钮文字保持不变 默认 false 不固定 |
| `ShowFixedButtonTextInDropdown` | `bool` | `}` | 获得/设置 下拉菜单中是否显示固定文字 默认 false 不显示 |
| `FixedButtonText` | `string?` | `}` | 获得/设置 固定按钮显示文字 默认 null |
| `ItemsTemplate` | `RenderFragment?` | `}` | 获得/设置 Items 模板 默认 null |
| `Task` | `Func<SelectedItem,` | `}` | SelectedItemChanged 回调方法 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnClick` | `EventCallback<MouseEventArgs>` | <see cref="ShowSplit"/> 为 true 时生效 |

## 代码示例

### 基本用法

```razor
<Dropdown TValue="string" Items="Items" OnSelectedItemChanged="@ShowMessage" Color="Color.Secondary"></Dropdown>
```

### 基本用法

```razor
<Dropdown TValue="string" Items="EmptyList" Color="Color.Secondary"></Dropdown>
```

### 基本用法

```razor
<Dropdown TValue="string" Items="ItemTemplateList">
        <ItemTemplate>
            <Tooltip Title="just a tooltip text demo" Trigger="hover">
                <span class="fa-solid fa-flag"></span>
                <div class="ms-2 flex-fill">@context.Text</div>
            </Tooltip>
        </ItemTemplate>
    </Dropdown>
```

### 基本用法

```razor
<Dropdown TValue="string" IsFixedButtonText="true" FixedButtonText="More" Icon="fa solid fa-ellipsis">
        <ItemsTemplate>
            <DropdownItem Text="Copy" Icon="fa-solid fa-copy" OnClick="@(() => OnClickAction("Copy"))"></DropdownItem>
            <DropdownItem Text="Paste" Icon="fa-solid fa-paste" OnClick="@(() => OnClickAction("Paste"))"></DropdownItem>
            <Divider></Divider>
            <DropdownItem Text="Action1" Icon="fa-solid fa-flag" OnClick="@(() => OnClickAction("Action1"))"></DropdownItem>
            <DropdownItem>
                <Tooltip Title="just a tooltip text demo" Trigger="hover">
                    <span class="fa-solid fa-flag"></span>
                    <div class="ms-2 flex-fill" @onclick="@(() => OnClickAction("Action2"))">Action2</div>
                </Tooltip>
            </DropdownItem>
        </ItemsTemplate>
    </Dropdown>
```

### 基本用法

```razor
<Dropdown TValue="string" Items="Items" ShowSplit="true" IsAsync="true" OnClickWithoutRender="OnIsAsyncClick"></Dropdown>
```
