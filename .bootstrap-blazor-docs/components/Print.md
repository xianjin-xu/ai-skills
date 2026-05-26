# Print 打印按钮

## 概述

Print 打印按钮组件用于打印文档或者局部视图。设置 `PreviewUrl` 时，打开一个新网页进行打印预览，点击此页面的打印按钮进行网页打印。不设置 `PreviewUrl` 时，如果是 Dialog 组件中的打印按钮，则打印弹窗内容。

> Print button component is used to print documents or partial views.

**分类**: 其他组件  
**在线演示**: [https://www.blazor.zone/print](https://www.blazor.zone/print)

---

## 使用场景

### 1. 普通用法

通过点击打印按钮将页面进行打印。点击下方打印按钮后，弹出新页面进行打印预览，确认无误后点击打印预览页面中的打印按钮进行打印机选择进行打印操作。

```razor
<PrintButton Icon="fa-solid fa-print" Text="打印" PreviewUrl="/print-view" />
```

### 2. 打印弹窗

通过设置弹窗组件 `ShowPrint` 开启打印功能。

```razor
<Button Text="打开弹窗" OnClick="OnOpenDialog" />

@code {
    [Inject]
    private DialogService? DialogService { get; set; }

    private async Task OnOpenDialog()
    {
        if (DialogService != null)
        {
            await DialogService.ShowPrintDialog<PrintView>("打印预览");
        }
    }
}
```

### 3. 打印服务

通过设置要打印的内容组件，直接调用打印服务进行打印作业，打印服务 PrintService 服务文档参考官方文档。

```razor
<Button Text="打印" OnClick="OnPrint" />

@code {
    [Inject]
    private PrintService? PrintService { get; set; }

    private async Task OnPrint()
    {
        if (PrintService != null)
        {
            await PrintService.PrintAsync<PrintView>();
        }
    }
}
```

---

## 参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| PreviewUrl | 获得/设置 打印预览地址，设置后点击按钮打开新页面进行打印 | string | — |
| Text | 获得/设置 按钮显示文字 | string | — |
| Icon | 获得/设置 按钮图标 | string | fa-solid fa-print |
| Color | 获得/设置 按钮颜色 | Color | — |
| Size | 获得/设置 按钮尺寸 | Size | — |

---

## 方法

| 方法名称 | 说明 | 参数 |
|---------|------|------|
| PrintAsync | 打印指定组件 | TComponent |

---

## 最佳实践

### 打印当前页面

使用 `PrintService` 打印当前页面的局部内容：

```razor
<Button Text="打印当前页面" OnClick="OnPrintCurrentPage" />

@code {
    [Inject]
    private PrintService? PrintService { get; set; }

    private async Task OnPrintCurrentPage()
    {
        if (PrintService != null)
        {
            // 打印当前页面的指定元素
            await PrintService.PrintAsync<MyPrintComponent>();
        }
    }
}
```

### 打印弹窗内容

在 Dialog 弹窗中使用 PrintButton 打印弹窗内容：

```razor
<DialogParameters Parameters="GetDialogParameters()">
    <DialogContent>
        <div id="print-content">
            <h3>打印内容</h3>
            <p>这里是需要打印的内容</p>
        </div>
        <PrintButton Text="打印" PreviewUrl="" />
    </DialogContent>
</DialogParameters>

@code {
    private DialogParameters GetDialogParameters()
    {
        return new DialogParameters();
    }
}
```

---

## 常见问题

### 1. 如何打印指定内容？

使用 `PrintService.PrintAsync<TComponent>()` 方法可以打印指定的组件内容。

### 2. 如何实现打印预览？

设置 `PreviewUrl` 参数，点击打印按钮后会打开新页面进行打印预览。

### 3. 如何打印弹窗内容？

在 Dialog 弹窗中放置 PrintButton 组件，不设置 `PreviewUrl` 参数，点击打印按钮会打印弹窗内容。

### 4. 如何自定义打印样式？

在打印组件中使用 `@media print` CSS 媒体查询自定义打印样式：

```css
@media print {
    .no-print {
        display: none;
    }
    
    .print-only {
        display: block;
    }
}
```

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | Print 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/print)
- [Dialog 组件文档](https://www.blazor.zone/dialog)
- [PrintService 服务文档](https://www.blazor.zone/print-service)
