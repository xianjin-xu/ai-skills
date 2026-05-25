# Modal 模态框

## 概述

`Modal` 是一个模态框容器组件，用于在保留当前页面状态的情况下，告知用户并承载相关操作。Modal 组件通常作为容器，内部放置 `ModalDialog` 组件来显示对话框内容。

**命名空间**: `BootstrapBlazor.Components`

## 使用场景

### 1. 基本用法

弹出一个对话框，适合需要定制性更大的场景。通过 `@ref` 获取组件引用，然后调用 `Show()` 方法显示弹窗。

```razor
<Modal @ref="MyModal">
    <ModalDialog Title="弹窗标题">
        <BodyTemplate>
            <div>弹窗正文</div>
        </BodyTemplate>
        <FooterTemplate>
            <Button Text="Close" OnClick="() => MyModal.Close()" />
            <Button Text="Save" OnClick="() => MyModal.Close()" />
        </FooterTemplate>
    </ModalDialog>
</Modal>

<Button Text="显示弹窗" OnClick="() => MyModal.Show()" />

@code {
    private Modal? MyModal { get; set; }
}
```

### 2. IsBackdrop 背景关闭模式

点击弹窗以外区域默认关闭弹窗效果。通过设置 `IsBackdrop="true"` 启用此功能。

```razor
<Modal @ref="BackdropModal" IsBackdrop="true">
    <ModalDialog Title="背景点击关闭">
        <BodyTemplate>
            <div>点击弹窗以外区域可以关闭弹窗</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="弹窗" OnClick="() => BackdropModal.Show()" />

@code {
    private Modal? BackdropModal { get; set; }
}
```

### 3. 调整大小弹窗

通过设置 `ShowResize="true"` 可以通过鼠标拉动弹窗右下角进行窗口大小调整。此参数设置在 `ModalDialog` 组件上。

```razor
<Modal @ref="ResizeModal">
    <ModalDialog Title="可调整大小" ShowResize="true">
        <BodyTemplate>
            <div>拖动右下角可以调整弹窗大小</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="弹窗" OnClick="() => ResizeModal.Show()" />

@code {
    private Modal? ResizeModal { get; set; }
}
```

### 4. 弹框大小

通过 `Size` 参数设置弹框组件的大小。此参数设置在 `ModalDialog` 组件上。

```razor
<Modal @ref="SizeModal">
    <ModalDialog Title="小弹窗" Size="Size.Small">
        <BodyTemplate>
            <div>小弹窗内容</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="小弹窗" OnClick="() => SizeModal.Show()" />
```

**可选大小**:
- `Size.Small` - 小弹窗
- `Size.Medium` - 中等弹窗（默认）
- `Size.Large` - 大弹窗
- `Size.ExtraLarge` - 超大弹窗
- `Size.ExtraExtraLarge` - 超超大弹窗

### 5. 全屏弹窗

设置 `FullScreenSize` 属性即可实现全屏弹窗。

```razor
<Modal @ref="FullScreenModal">
    <ModalDialog Title="全屏弹窗" FullScreenSize="true">
        <BodyTemplate>
            <div>全屏弹窗内容</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="全屏弹窗" OnClick="() => FullScreenModal.Show()" />

@code {
    private Modal? FullScreenModal { get; set; }
}
```

**响应式全屏**:
- `FullScreenSize="true"` - 始终全屏
- `FullScreenSize="Size.Medium"` - 中等屏幕尺寸以下全屏（<992px）
- `FullScreenSize="Size.Large"` - 大屏幕尺寸以下全屏（<1200px）
- `FullScreenSize="Size.ExtraLarge"` - 超大屏幕尺寸以下全屏（<1400px）

### 6. 垂直居中

通过 `IsCentered` 设置弹框组件的垂直居中。此参数设置在 `ModalDialog` 组件上。

```razor
<Modal @ref="CenteredModal">
    <ModalDialog Title="垂直居中" IsCentered="true">
        <BodyTemplate>
            <div>垂直居中的弹窗</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="垂直居中弹窗" OnClick="() => CenteredModal.Show()" />

@code {
    private Modal? CenteredModal { get; set; }
}
```

### 7. 超长内容

通过 `IsScrolling` 针对超出内容设置弹框组件滚轮滑动功能。此参数设置在 `ModalDialog` 组件上。

```razor
<Modal @ref="ScrollModal">
    <ModalDialog Title="超长内容" IsScrolling="true">
        <BodyTemplate>
            <div>
                <!-- 大量内容 -->
                <p>超长内容...</p>
                <!-- 重复多次 -->
            </div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="内容超长的弹窗" OnClick="() => ScrollModal.Show()" />

@code {
    private Modal? ScrollModal { get; set; }
}
```

### 8. 可拖拽弹窗

点击弹窗标题栏对弹窗进行拖拽。通过设置 `IsDraggable="true"` 启用拖拽功能。此参数设置在 `ModalDialog` 组件上。

```razor
<Modal @ref="DraggableModal">
    <ModalDialog Title="可拖拽弹窗" IsDraggable="true">
        <BodyTemplate>
            <div>点击标题栏可以拖拽弹窗</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="弹窗" OnClick="() => DraggableModal.Show()" />

@code {
    private Modal? DraggableModal { get; set; }
}
```

### 9. 最大化按钮

通过设置 `ShowMaximizeButton="true"` 弹窗显示最大化按钮。此参数设置在 `ModalDialog` 组件上。

```razor
<Modal @ref="MaximizeModal">
    <ModalDialog Title="最大化按钮" ShowMaximizeButton="true">
        <BodyTemplate>
            <div>点击最大化按钮可以全屏显示</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="弹窗" OnClick="() => MaximizeModal.Show()" />

@code {
    private Modal? MaximizeModal { get; set; }
}
```

### 10. 弹窗已显示回调方法

通过设置 `OnShownAsync` 回调委托，弹窗显示后回调此方法。

```razor
<Modal @ref="CallbackModal" OnShownAsync="OnModalShown">
    <ModalDialog Title="回调示例">
        <BodyTemplate>
            <div>弹窗已显示</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="弹窗" OnClick="() => CallbackModal.Show()" />

@code {
    private Modal? CallbackModal { get; set; }

    private Task OnModalShown()
    {
        // 弹窗显示后的处理逻辑
        Console.WriteLine("Modal shown");
        return Task.CompletedTask;
    }
}
```

## 参数

### Modal 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `ChildContent` | 获得/设置 子组件（通常是 ModalDialog） | `RenderFragment` | `null` |
| `FirstAfterRenderCallbackAsync` | 获得/设置 组件完成渲染时的回调方法 | `Func<Modal, Task>` | `null` |
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |
| `IsBackdrop` | 获得/设置 是否在后台关闭弹出窗口 | `bool` | `false` |
| `IsFade` | 获得/设置 是否启用淡入淡出动画 | `bool?` | `null` |
| `IsKeyboard` | 获得/设置 是否启用键盘支持（ESC 键） | `bool` | `true` |
| `OnCloseAsync` | 获得/设置 弹出窗口关闭时的回调委托 | `Func<Task>` | `null` |
| `OnClosingAsync` | 关闭之前回调方法，返回 true 时关闭弹窗 | `Func<Task<bool>>` | `null` |
| `OnShownAsync` | 获得/设置 弹出窗口显示时的回调方法 | `Func<Task>` | `null` |

## 方法

| 方法 | 说明 |
|------|------|
| `Show()` | 显示弹窗 |
| `Close()` | 关闭弹窗 |
| `Toggle()` | 切换弹窗显示状态 |

## 最佳实践

### 1. 使用 @ref 获取组件引用

Modal 组件通常通过 `@ref` 获取引用，然后在代码中调用 `Show()` 或 `Close()` 方法。

```razor
<Modal @ref="MyModal">
    <ModalDialog Title="示例">
        <BodyTemplate>
            <div>内容</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="打开" OnClick="() => MyModal.Show()" />
<Button Text="关闭" OnClick="() => MyModal.Close()" />

@code {
    private Modal? MyModal { get; set; }
}
```

### 2. Modal 与 ModalDialog 的关系

- `Modal` 是容器组件，负责控制弹窗的显示/隐藏
- `ModalDialog` 是内容组件，负责显示弹窗的标题、正文、页脚等内容
- 一个 `Modal` 内部可以包含一个 `ModalDialog`

```razor
<Modal @ref="Modal">
    <ModalDialog Title="标题">
        <BodyTemplate>正文</BodyTemplate>
        <FooterTemplate>页脚</FooterTemplate>
    </ModalDialog>
</Modal>
```

### 3. 键盘支持

默认情况下，Modal 支持 ESC 键关闭弹窗。如果不希望用户按 ESC 关闭，可以设置 `IsKeyboard="false"`。

```razor
<Modal @ref="Modal" IsKeyboard="false">
    <ModalDialog Title="不可ESC关闭">
        <BodyTemplate>
            <div>必须点击按钮才能关闭</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>
```

## 常见问题

### 1. 弹窗不显示

**问题**: 调用 `Show()` 方法后，弹窗不显示。

**原因**: 可能是未正确设置 `@ref`，或者 Modal 组件未正确渲染。

**解决方案**:
- 确保已设置 `@ref="MyModal"` 并在代码中声明了对应的变量
- 确保在调用 `Show()` 之前，组件已经完成渲染（可以在 `OnAfterRenderAsync` 中调用）

```razor
@code {
    private Modal? MyModal { get; set; }

    protected override async Task OnAfterRenderAsync(bool firstRender)
    {
        if (firstRender)
        {
            // 确保组件已渲染
            await base.OnAfterRenderAsync(firstRender);
        }
    }

    private void OpenModal()
    {
        MyModal?.Show();  // 使用 ?. 避免空引用
    }
}
```

### 2. 弹窗关闭后无法再次打开

**问题**: 弹窗关闭后，再次调用 `Show()` 无法打开。

**原因**: 可能是关闭逻辑有问题，或者组件状态未正确重置。

**解决方案**:
- 检查 `OnClosingAsync` 回调是否返回了 `true`（返回 `false` 会阻止关闭）
- 确保在正确的时机调用 `Close()`

```razor
<Modal @ref="Modal" OnClosingAsync="OnClosing">
    <ModalDialog Title="示例">
        <BodyTemplate>
            <div>内容</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

@code {
    private Modal? Modal { get; set; }

    private Task<bool> OnClosing()
    {
        // 返回 true 允许关闭，返回 false 阻止关闭
        return Task.FromResult(true);
    }
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | Modal 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 IsDraggable 参数；优化键盘支持 |
| 8.0.0 | 2024-11-10 | 新增 FullScreenSize 响应式全屏支持 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Modal](https://www.blazor.zone/modal)
- [Bootstrap Blazor API - Modal](https://www.blazor.zone/api/Modal)
