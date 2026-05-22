# ContextMenu

## 概述

ContextMenu 组件

> A component that represents a context menu

**分类**: 其他
**在线演示**: [https://www.blazor.zone/context-menu](https://www.blazor.zone/context-menu)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ShowShadow` | `bool` | `true` | 获得/设置 是否显示阴影 默认 <see langword="true" /> |
| `Task` | `Func<object?,` | `}` | 获得/设置 弹出前回调方法 默认 null |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |

## 代码示例

### 基本用法

```razor
<ContextMenu>
            <ContextMenuItem Icon="fa-solid fa-copy" Text="@Localizer["ContextMenuItemCopy"]" OnClick="OnCopy"></ContextMenuItem>
            <ContextMenuItem Icon="fa-solid fa-paste" Text="@Localizer["ContextMenuItemPast"]" OnClick="OnPaste"></ContextMenuItem>
        </ContextMenu>
```

### 基本用法

```razor
<ContextMenu>
            <ContextMenuItem Icon="fa-solid fa-copy" Text="@Localizer["ContextMenuItemCopy"]" OnClick="OnCopy"></ContextMenuItem>
            <ContextMenuItem Icon="fa-solid fa-paste" Text="@Localizer["ContextMenuItemPast"]" OnClick="OnPaste"></ContextMenuItem>
        </ContextMenu>
```

### 基本用法

```razor
<ContextMenu>
            <ContextMenuItem Icon="fa-solid fa-copy" Text="@Localizer["ContextMenuItemCopy"]" OnClick="OnCopy"></ContextMenuItem>
            <ContextMenuItem Icon="fa-solid fa-paste" Text="@Localizer["ContextMenuItemPast"]" OnClick="OnPaste"></ContextMenuItem>
        </ContextMenu>
```

### 基本用法

```razor
<ContextMenu>
            <ContextMenuItem Icon="fa-solid fa-copy" Text="@Localizer["ContextMenuItemCopy"]" OnClick="OnCopy"></ContextMenuItem>
            <ContextMenuItem Icon="fa-solid fa-paste" Text="@Localizer["ContextMenuItemPast"]" OnClick="OnPaste"></ContextMenuItem>
        </ContextMenu>
```

### 基本用法

```razor
<ContextMenu OnBeforeShowCallback="OnBeforeShowCallback">
            @if (SelectModel?.Id == "1020")
            {
                <ContextMenuItem Icon="fa-solid fa-copy" Text="@Localizer["ContextMenuItemCopy"]" OnClick="OnCopy"></ContextMenuItem>
                <ContextMenuItem Icon="fa-solid fa-paste" Text="@Localizer["ContextMenuItemPast"]" OnClick="OnPaste"></ContextMenuItem>
            }
            else
            {
                <ContextMenuItem Icon="fa-solid fa-copy" Text="CopySub" OnClick="OnCopySub"></ContextMenuItem>
            }
        </ContextMenu>
```
