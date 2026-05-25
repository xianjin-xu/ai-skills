# Split 面板分割

## 概述

Split 面板分割组件用于创建可调整大小的面板布局。支持左右分割、垂直分割、嵌套使用、折叠/展开等功能。

> Split component is used to create resizable panel layouts. Supports left-right split, vertical split, nested usage, collapse/expand and other features.

**分类**: 布局组件
**在线演示**: [https://www.blazor.zone/split](https://www.blazor.zone/split)

---

## 使用场景

### 1. 基础用法 - 左右分割

默认情况下，Split 组件创建左右分割的面板。显示拖动栏，显示调整按钮。

```razor
<Split ShowBarHandle="true">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是左侧面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是右侧面板</div>
    </SecondPaneTemplate>
</Split>
```

### 2. 设置初始化百分比

通过设置 `Basis` 属性来设置初始化位置占比，默认为 `50%`。

```razor
<Split Basis="40%">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是左侧面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是右侧面板</div>
    </SecondPaneTemplate>
</Split>
```

### 3. 垂直分割

通过设置 `IsVertical` 属性控制垂直分割面板。

```razor
<Split IsVertical="true">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center w-100">我是上部面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center w-100">我是底部面板</div>
    </SecondPaneTemplate>
</Split>
```

### 4. 嵌套使用

通过嵌套 `Split` 组件进行组合布局。

```razor
<Split>
    <FirstPaneTemplate>
        <Split IsVertical="true">
            <FirstPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">上边面板</div>
            </FirstPaneTemplate>
            <SecondPaneTemplate>
                <div class="d-flex justify-content-center align-items-center h-100">下边面板</div>
            </SecondPaneTemplate>
        </Split>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">右边面板</div>
    </SecondPaneTemplate>
</Split>
```

### 5. 折叠/展开

通过设置 `IsCollapsible` 属性来设置是否可以折叠面板。开启后，可以通过 `IsKeepOriginalSize` 控制恢复时是否保持原始大小。

```razor
<Split IsCollapsible="true" IsKeepOriginalSize="true">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">上边面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">下边面板</div>
    </SecondPaneTemplate>
</Split>
```

### 6. 最小值

通过设置 `FirstPaneMinimumSize` 和 `SecondPaneMinimumSize` 值限制面板最小尺寸，支持所有单位。本例中设置左右面板最小值均为 `10%`。

```razor
<Split FirstPaneMinimumSize="10%" SecondPaneMinimumSize="10%">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是左侧面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是右侧面板</div>
    </SecondPaneTemplate>
</Split>
```

### 7. 代码设置面板宽度

通过组件实例方法 `SetLeftWidth` 设置左侧/上侧面板宽度，右侧/下侧面板宽度自适应。

```razor
<Split @ref="_split">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是左侧面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是右侧面板</div>
    </SecondPaneTemplate>
</Split>
<Button Text="25%" OnClick="() => SetWidth("25%")"></Button>
<Button Text="50%" OnClick="() => SetWidth("50%")"></Button>
<Button Text="100%" OnClick="() => SetWidth("100%")"></Button>

@code {
    private Split? _split { get; set; }

    private async Task SetWidth(string width)
    {
        if (_split != null)
        {
            await _split.SetLeftWidth(width);
        }
    }
}
```

### 8. 自定义拖动条

通过 CSS 自定义拖动条的样式。

```razor
<Split class="custom-split">
    <FirstPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是左侧面板</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div class="d-flex justify-content-center align-items-center h-100">我是右侧面板</div>
    </SecondPaneTemplate>
</Split>

<style>
    .custom-split .split-bar {
        background-color: #007bff;
    }
</style>
```

---

## 参数 (Parameters)

### Split 参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `Basis` | `string` | `"50%"` | 获得/设置 第一个窗格初始化位置占比 |
| `FirstPaneMinimumSize` | `string?` | `null` | 获得/设置 第一个窗格最小宽度 |
| `FirstPaneTemplate` | `RenderFragment?` | `null` | 获得/设置 第一个窗格模板 |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsCollapsible` | `bool` | `false` | 获得/设置 是否开启折叠功能 |
| `IsKeepOriginalSize` | `bool` | `true` | 获得/设置 开启 `IsCollapsible` 后恢复时是否保持原始大小 |
| `IsVertical` | `bool` | `false` | 获得/设置 是否垂直分割 |
| `OnCollapsedAsync` | `Func<bool, Task>?` | `null` | 获得/设置 窗格折叠时回调方法（已弃用） |
| `OnResizedAsync` | `Func<SplitterResizedEventArgs, Task>?` | `null` | 获得/设置 窗格尺寸改变时回调方法 |
| `SecondPaneMinimumSize` | `string?` | `null` | 获得/设置 第二个窗格最小宽度 |
| `SecondPaneTemplate` | `RenderFragment?` | `null` | 获得/设置 第二个窗格模板 |
| `ShowBarHandle` | `bool` | `true` | 获得/设置 是否显示拖动条 |

---

## 方法 (Methods)

### Split 方法

| 方法名 | 说明 |
|--------|------|
| `SetLeftWidth(string width)` | 设置左侧/上侧面板宽度 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnResizedAsync` | 窗格尺寸改变时的回调方法 |

---

## 最佳实践

### 1. 嵌套布局

通过嵌套 `Split` 组件可以创建复杂的布局结构。

```razor
<Split>
    <FirstPaneTemplate>
        <Split IsVertical="true">
            <FirstPaneTemplate>
                <div>左上</div>
            </FirstPaneTemplate>
            <SecondPaneTemplate>
                <div>左下</div>
            </SecondPaneTemplate>
        </Split>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div>右侧</div>
    </SecondPaneTemplate>
</Split>
```

### 2. 折叠功能

当需要节省空间时，可以启用折叠功能。

```razor
<Split IsCollapsible="true" IsKeepOriginalSize="true">
    <FirstPaneTemplate>
        <div>左侧内容</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div>右侧内容</div>
    </SecondPaneTemplate>
</Split>
```

### 3. 最小尺寸限制

通过设置最小尺寸防止面板被拖拽到过小。

```razor
<Split FirstPaneMinimumSize="200px" SecondPaneMinimumSize="300px">
    <FirstPaneTemplate>
        <div>左侧</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div>右侧</div>
    </SecondPaneTemplate>
</Split>
```

---

## 常见问题 (FAQ)

### Q1: 如何动态改变面板大小？

**A**: 通过 `@ref` 获取组件实例，调用 `SetLeftWidth()` 方法。

```razor
<Split @ref="_split">
    <FirstPaneTemplate>
        <div>左侧</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div>右侧</div>
    </SecondPaneTemplate>
</Split>

@code {
    private Split? _split { get; set; }

    private async Task ChangeSize()
    {
        await _split!.SetLeftWidth("30%");
    }
}
```

### Q2: 如何监听面板尺寸变化？

**A**: 使用 `OnResizedAsync` 回调方法监听尺寸变化。

```razor
<Split OnResizedAsync="OnResized">
    <FirstPaneTemplate>
        <div>左侧</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div>右侧</div>
    </SecondPaneTemplate>
</Split>

@code {
    private Task OnResized(SplitterResizedEventArgs args)
    {
        Console.WriteLine($"面板尺寸变化: {args}");
        return Task.CompletedTask;
    }
}
```

### Q3: 如何创建垂直分割？

**A**: 设置 `IsVertical="true"` 创建垂直分割面板。

```razor
<Split IsVertical="true">
    <FirstPaneTemplate>
        <div>上方</div>
    </FirstPaneTemplate>
    <SecondPaneTemplate>
        <div>下方</div>
    </SecondPaneTemplate>
</Split>
```

---

## 版本历史

| 版本 | 变更内容 |
|------|----------|
| 7.0 | 新增 Split 组件 |
| 8.0 | 新增 `IsCollapsible` 折叠功能 |
