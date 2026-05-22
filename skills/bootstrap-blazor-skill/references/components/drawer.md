# Drawer

## 概述

Drawer 抽屉组件

> Drawer component

**分类**: 反馈
**在线演示**: [https://www.blazor.zone/drawer](https://www.blazor.zone/drawer)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Width` | `string` | `"360px"` | 获得/设置 抽屉宽度 左右布局时生效 |
| `Height` | `string` | `"290px"` | 获得/设置 抽屉高度 上下布局时生效 |
| `IsOpen` | `bool` | `}` | 获得/设置 抽屉是否打开 默认 false 未打开 |
| `OnClickBackdrop` | `Func<Task>?` | `}` | 获得/设置 点击背景遮罩时回调委托方法 默认为 null |
| `IsBackdrop` | `bool` | `}` | 获得/设置 点击遮罩是否关闭抽屉 默认为 false |
| `ShowBackdrop` | `bool` | `true` | 获得/设置 是否显示遮罩 默认为 true 显示遮罩 |
| `Placement` | `Placement` | `Placement.Left` | 获得/设置 组件出现位置 默认显示在 Left 位置 |
| `Position` | `string?` | `}` | 获得/设置 组件定位位置 默认 null 未设置 使用样式内置定位 fixed 可更改为 absolute |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |
| `AllowResize` | `bool` | `}` | 获得/设置 是否允许调整大小 默认 false |
| `ZIndex` | `int?` | `}` | 获得/设置 z-index 参数值 默认 null 未设置 |
| `OnCloseAsync` | `Func<Task>?` | `}` | 获得/设置 关闭抽屉回调委托 默认 null |
| `BodyContext` | `object?` | `}` | 获得/设置 抽屉内容相关数据 多用于传值 |
| `IsKeyboard` | `bool` | `}` | 获得/设置 是否支持键盘 ESC 关闭当前弹窗 默认 false |
| `BodyScroll` | `bool` | `}` | 获得/设置 抽屉显示时是否允许滚动 body 默认为 false 不滚动 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `IsOpenChanged` | `EventCallback<bool>` | 获得/设置 IsOpen 属性改变时回调委托方法 |

## 代码示例

### 基本用法

```razor
<Drawer Placement="@DrawerAlign" @bind-IsOpen="@IsOpen" AllowResize="true">
        <div class="d-flex justify-content-center align-items-center flex-column" style="height: 290px;">
            <p>@Localizer["Content"]</p>
            <button type="button" class="btn btn-primary" @onclick="@(e => IsOpen = false)">@Localizer["Close"]</button>
        </div>
    </Drawer>
```

### 基本用法

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="@IsBackdropOpen" IsBackdrop="true">
        <p class="mt-3 text-center">
            @Localizer["PlacementContent"]
        </p>
    </Drawer>
```

### 基本用法

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="@IsShowBackdropOpen" ShowBackdrop="false">
        <div class="d-flex justify-content-center align-items-center flex-column" style="height: 290px;">
            <p>@Localizer["Content"]</p>
            <button type="button" class="btn btn-primary" @onclick="@(e => IsShowBackdropOpen = false)">@Localizer["Close"]</button>
        </div>
    </Drawer>
```

### 基本用法

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="@IsKeyboardOpen" IsKeyboard="true">
        <div class="d-flex justify-content-center align-items-center flex-column" style="height: 290px;">
            <p>@Localizer["Content"]</p>
            <button type="button" class="btn btn-primary" @onclick="@(e => IsKeyboardOpen = false)">@Localizer["Close"]</button>
        </div>
    </Drawer>
```

### 基本用法

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="@IsBodyScrollOpen" BodyScroll="true">
        <div class="d-flex justify-content-center align-items-center flex-column" style="height: 290px;">
            <p>@Localizer["Content"]</p>
            <button type="button" class="btn btn-primary" @onclick="@(e => IsBodyScrollOpen = false)">@Localizer["Close"]</button>
        </div>
    </Drawer>
```
