# ModalDialog 模态对话框

## 概述

`ModalDialog` 是一个模态对话框组件，通常作为 `Modal` 组件的子组件使用，用于显示对话框的标题、正文和页脚内容。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/modal](https://www.blazor.zone/modal)

> **注意**: 本文档需要进一步完善。当前的参数列表和示例基于有限的信息推断，建议参考官方文档获取最准确的信息。

## 使用场景

### 1. 基本用法

`ModalDialog` 必须放在 `Modal` 组件内部使用。通过 `Title` 参数设置对话框标题。

```razor
<Modal @ref="MyModal">
    <ModalDialog Title="基本对话框">
        <BodyTemplate>
            <div>这是一个基本的对话框内容</div>
        </BodyTemplate>
        <FooterTemplate>
            <Button Text="关闭" OnClick="() => MyModal.Close()" />
        </FooterTemplate>
    </ModalDialog>
</Modal>

<Button Text="打开对话框" OnClick="() => MyModal.Show()" />

@code {
    private Modal? MyModal { get; set; }
}
```

### 2. 保存按钮

通过 `ShowSaveButton="true"` 显示保存按钮，通过 `OnSaveAsync` 处理保存逻辑。

```razor
<Modal @ref="SaveModal">
    <ModalDialog Title="保存对话框" ShowSaveButton="true" OnSaveAsync="OnSaveAsync">
        <BodyTemplate>
            <div>点击保存按钮会触发 OnSaveAsync 回调</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>

<Button Text="打开" OnClick="() => SaveModal.Show()" />

@code {
    private Modal? SaveModal { get; set; }

    private Task OnSaveAsync()
    {
        // 保存逻辑
        Console.WriteLine("保存成功");
        return Task.CompletedTask;
    }
}
```

### 3. 对话框大小

通过 `Size` 参数设置对话框大小。

```razor
<Modal @ref="SizeModal">
    <ModalDialog Title="小对话框" Size="Size.Small">
        <BodyTemplate>
            <div>小尺寸的对话框</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>
```

**可选大小**: `Size.Small`, `Size.Medium`, `Size.Large`, `Size.ExtraLarge`, `Size.ExtraExtraLarge`

### 4. 垂直居中

通过 `IsCentered="true"` 使对话框垂直居中显示。

```razor
<Modal @ref="CenterModal">
    <ModalDialog Title="居中对话框" IsCentered="true">
        <BodyTemplate>
            <div>垂直居中的对话框</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>
```

### 5. 可调整大小

通过 `ShowResize="true"` 允许拖动对话框右下角调整大小。

```razor
<Modal @ref="ResizeModal">
    <ModalDialog Title="可调整大小" ShowResize="true">
        <BodyTemplate>
            <div>拖动右下角可以调整对话框大小</div>
        </BodyTemplate>
    </ModalDialog>
</Modal>
```

### 6. 滚动内容

通过 `IsScrolling="true"` 启用内容滚动。

```razor
<Modal @ref="ScrollModal">
    <ModalDialog Title="长内容对话框" IsScrolling="true">
        <BodyTemplate>
            <div style="height: 500px;">
                <p>这是很长的内容...</p>
            </div>
        </BodyTemplate>
    </ModalDialog>
</Modal>
```

## 参数

### ModalDialog 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Title` | 获得/设置 对话框标题 | `string` | `null` |
| `Size` | 获得/设置 对话框大小 | `Size` | `Size.Medium` |
| `IsCentered` | 获得/设置 是否垂直居中 | `bool` | `false` |
| `IsScrolling` | 获得/设置 是否启用滚动 | `bool` | `false` |
| `ShowSaveButton` | 获得/设置 是否显示保存按钮 | `bool` | `false` |
| `ShowCloseButton` | 获得/设置 是否显示关闭按钮 | `bool` | `true` |
| `ShowResize` | 获得/设置 是否显示调整大小手柄 | `bool` | `false` |
| `IsDraggable` | 获得/设置 是否可拖拽 | `bool` | `false` |
| `FullScreenSize` | 获得/设置 全屏显示的尺寸断点 | `Size` | `None` |
| `BodyTemplate` | 获得/设置 正文模板 | `RenderFragment` | `null` |
| `FooterTemplate` | 获得/设置 页脚模板 | `RenderFragment` | `null` |
| `HeaderTemplate` | 获得/设置 头部模板 | `RenderFragment` | `null` |

## 事件回调

| 事件 | 说明 | 类型 |
|------|------|------|
| `OnSaveAsync` | 获得/设置 点击保存按钮时的回调 | `Func<Task>` |
| `OnCloseAsync` | 获得/设置 对话框关闭时的回调 | `Func<Task>` |

## 最佳实践

### 1. Modal 与 ModalDialog 的配合使用

`ModalDialog` 必须放在 `Modal` 组件内部，不能单独使用。

```razor
<!-- 正确用法 -->
<Modal @ref="Modal">
    <ModalDialog Title="标题">
        <BodyTemplate>内容</BodyTemplate>
    </ModalDialog>
</Modal>

<!-- 错误用法：ModalDialog 不能单独使用 -->
<ModalDialog Title="标题">...</ModalDialog>
```

### 2. 使用 @ref 控制显示

通常通过 `Modal` 组件的 `@ref` 引用来控制对话框的显示和关闭。

```razor
<Modal @ref="MyModal">
    <ModalDialog Title="示例">
        <BodyTemplate>
            <div>内容</div>
        </BodyTemplate>
        <FooterTemplate>
            <Button Text="关闭" OnClick="() => MyModal.Close()" />
        </FooterTemplate>
    </ModalDialog>
</Modal>

<Button Text="打开" OnClick="() => MyModal.Show()" />
```

## 常见问题

### 1. 对话框不显示

**问题**: 调用 `Modal.Show()` 后对话框不显示。

**原因**: 可能是 `Modal` 组件的引用未正确设置。

**解决方案**: 确保已设置 `@ref="MyModal"` 并在代码中声明了对应的变量。

```razor
@code {
    private Modal? MyModal { get; set; }  // 必须为 Modal 类型，不是 ModalDialog
}
```

### 2. 保存按钮不触发回调

**问题**: 点击保存按钮后 `OnSaveAsync` 回调不触发。

**原因**: 可能是未设置 `ShowSaveButton="true"` 或未正确绑定 `OnSaveAsync`。

**解决方案**:

```razor
<ModalDialog Title="示例" 
            ShowSaveButton="true" 
            OnSaveAsync="HandleSave">

@code {
    private Task HandleSave()
    {
        // 保存逻辑
        return Task.CompletedTask;
    }
}
```

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | ModalDialog 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 IsDraggable 参数 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Modal](https://www.blazor.zone/modal)
- [Bootstrap Blazor API - ModalDialog](https://www.blazor.zone/api/ModalDialog)
