# Dialog (对话框)

## 概述

Dialog 组件是 Bootstrap Blazor 中用于弹出窗口进行人机交互的核心组件。通过注入 `DialogService` 服务，调用 `Show` 方法弹出窗口。

**主要功能特性**：
- 支持多种弹出方式（普通弹窗、模态对话框、编辑对话框、搜索对话框、保存对话框）
- 支持弹窗传参（通过 `BodyContext` 参数）
- 支持自定义标题栏、工具栏按钮
- 支持调整大小、全屏、打印、导出 PDF
- 支持多级弹窗
- 支持 ESC 关闭、点击遮罩关闭

**分类**: 通知组件  
**在线演示**: [https://www.blazor.zone/dialog](https://www.blazor.zone/dialog)

## 组件使用介绍

### 注入 DialogService

使用 Dialog 组件前，需要先注入 `DialogService` 服务：

```csharp
@inject DialogService DialogService

// 或者使用 [Inject] 特性
[Inject]
[NotNull]
private DialogService? DialogService { get; set; }
```

### 关闭弹窗方法

在弹窗内的组件中，可以通过级联参数 `OnCloseAsync` 调用 `DialogOption` 实例的 `CloseDialogAsync` 方法关闭弹窗：

```csharp
var op = new DialogOption()
{
    Title = "数据查询窗口",
    ShowFooter = false,
    BodyContext = DataPrimaryId
};
op.Component = BootstrapDynamicComponent.CreateComponent<DataDialogComponent>(new Dictionary<string, object?>
{
    [nameof(DataDialogComponent.OnCloseAsync)] = new Action(() => op.CloseDialogAsync())
});
await DialogService.Show(op);
```

或者在弹窗组件内部使用级联参数：

```csharp
[CascadingParameter]
private Func<Task>? OnCloseAsync { get; set; }

private async Task OnClick()
{
    if (OnCloseAsync != null)
    {
        await OnCloseAsync();
    }
}
```

也可以使用关窗按钮组件：

```razor
<DialogCloseButton />
```

## 使用场景

### 1. 基本用法

通过设置 `DialogOption` 属性对模态框进行基本属性设置。

```csharp
var option = new DialogOption()
{
    Title = "基本弹窗",
    Size = Size.Medium,
    ShowFooter = true
};
option.Component = BootstrapDynamicComponent.CreateComponent<MyComponent>();
await DialogService.Show(option);
```

**功能说明**：
- 通过设置 `DialogOption.IsKeyboard` 参数，开启弹窗是否支持 ESC
- 点击弹窗外部遮罩可关闭弹窗（可通过 `IsBackdrop` 参数控制）

---

### 2. 调整大小

通过设置 `ShowResize="true"` 可以通过鼠标拉动弹窗右下角进行窗口大小调整。

```csharp
var option = new DialogOption()
{
    Title = "可调整大小的弹窗",
    ShowResize = true,
    Size = Size.Medium
};
```

---

### 3. 自定义标题栏

通过设置 `HeaderTemplate` 属性对模态框标题栏进行自定义设置。

```razor
<Dialog>
    <HeaderTemplate>
        <div class="custom-header">
            <span>自定义标题</span>
        </div>
    </HeaderTemplate>
</Dialog>
```

---

### 4. 标题栏自定义按钮

通过设置 `HeaderToolbarTemplate` 自定义 Header 中工具栏按钮。

```razor
<Dialog>
    <HeaderToolbarTemplate>
        <Button Icon="fa-solid fa-print" Text="打印" OnClick="OnPrint" />
    </HeaderToolbarTemplate>
</Dialog>
```

---

### 5. 弹出复杂组件

通过调用 `Show<Counter>()` 来弹出一个自定义组件。

```csharp
await DialogService.Show<Counter>(new DialogOption()
{
    Title = "弹出 Counter 组件",
    ShowFooter = false
});
```

**功能说明**：本例中弹出对话框中包含一个示例网站的自带 Counter 组件。

---

### 6. 弹窗传参

通过设置 `BodyContext` 属性值，可以把参数传递给弹窗中的组件内。

```csharp
var option = new DialogOption()
{
    Title = "弹窗传参示例",
    BodyContext = "我是传参"
};
option.Component = BootstrapDynamicComponent.CreateComponent<DemoComponent>();
await DialogService.Show(option);
```

在弹窗组件 `DemoComponent` 中通过级联参数获取传参值：

```csharp
[CascadingParameter]
private string? BodyContext { get; set; }
```

---

### 7. 模态对话框

通过 `ShowModal` 方法弹出线程阻塞模式的对话框。

```csharp
var ret = await DialogService.ShowModal<EditComponent>(new DialogOption()
{
    Title = "模态对话框",
    ShowFooter = true
});
```

**功能说明**：
- 点击按钮弹出模态弹窗
- 更改模态弹窗内数值点击**确认**按钮时数值更新
- 更改模态弹窗内数值点击**取消**或者**关闭**按钮时数值不更新
- 再次点击弹出模态弹窗时，数值保持一致

---

### 8. 编辑对话框

通过 `ShowEditDialog` 方法弹出保存对话框。

```csharp
var option = new EditDialogOption<Foo>()
{
    Title = "编辑数据",
    Model = foo,
    OnSaveAsync = OnSave
};
await DialogService.ShowEditDialog(option);
```

**功能说明**：
- 通过 `EditDialogOption` 参数对弹窗进行设置
- 设计出发点：通过给定 Model 或者 Items 自动生成带客户端验证的表单窗口

---

### 9. 搜索对话框

通过 `ShowSearchDialog` 方法弹出搜索对话框。

```csharp
var option = new SearchDialogOption<Foo>()
{
    Title = "搜索数据",
    OnSearchAsync = OnSearch
};
await DialogService.ShowSearchDialog(option);
```

**功能说明**：
- 通过 `SearchDialogOption` 参数对弹窗进行设置
- 设计出发点：通过给定 Model 或者 Items 自动生成搜索窗口

---

### 10. 保存对话框

通过 `ShowSaveDialog` 方法弹出保存对话框。

```csharp
var option = new DialogOption()
{
    Title = "保存数据",
    Component = BootstrapDynamicComponent.CreateComponent<SaveComponent>(),
    ShowFooter = true
};
await DialogService.ShowSaveDialog(option);
```

**功能说明**：
- 设计出发点：通过给定 TComponent 自动生成保存窗口
- 通过设置 `saveCallback` 在保存回调方法中进行数据处理
- TComponent 泛型组件所需要参数可以通过 `parameters` 进行传递

---

### 11. 多级弹窗

点击弹窗内部按钮继续弹出对话窗。

**功能介绍**：
- 点击按钮弹出对话窗
- 切换弹窗内 Tab 组件的第三个标签页（角色管理）
- 点击标签页中的弹窗继续弹出对话框
- 关闭当前对话框后之前打开的对话框保持状态

**技术要点**：
- 目前多级弹窗已经实现，每个 ModalDialog 均可以独立设置 `IsBackdrop` `IsKeyboard` 参数
- 修复了上一个版本按下 ESC 弹窗全部消失问题

---

### 12. 全屏弹窗

通过设置 `ShowMaximizeButton` 使 Header 上显示一个窗口最大化按钮。

```csharp
var option = new DialogOption()
{
    Title = "全屏弹窗",
    ShowMaximizeButton = true,
    FullScreenSize = FullScreenSize.Large
};
```

---

### 13. 打印按钮

通过设置 `ShowPrintButton` 使 Header 上显示一个打印预览按钮。

```csharp
var option = new DialogOption()
{
    Title = "带打印按钮的弹窗",
    ShowPrintButton = true,
    PrintButtonText = "打印预览"
};
```

---

### 14. 带导出 PDF 功能的弹窗

通过设置 `ShowExportPdfButtonInHeader` 使 Header 上显示一个导出 PDF 按钮。

```csharp
var option = new DialogOption()
{
    Title = "导出 PDF 弹窗",
    ShowExportPdfButtonInHeader = true,
    ExportPdfButtonOptions = new ExportPdfButtonOptions()
    {
        // 配置导出选项
    }
};
```

---

### 15. 异常捕获

通过 `BootstrapBlazorRoot` 内置 `ErrorLogger` 对弹窗内错误进行全局异常捕获。

```razor
<BootstrapBlazorRoot>
    <ErrorLogger>
        @Body
    </ErrorLogger>
</BootstrapBlazorRoot>
```

---

## DialogOption 重要参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Title` | `string?` | `null` | 获得/设置弹窗标题 |
| `Size` | `Size` | `Size.Medium` | 获得/设置弹窗大小 |
| `FullScreenSize` | `FullScreenSize` | `FullScreenSize.None` | 获得/设置全屏阈值 |
| `ShowFooter` | `bool` | `true` | 获得/设置是否显示 Footer |
| `ShowHeader` | `bool` | `true` | 获得/设置是否显示 Header |
| `ShowHeaderCloseButton` | `bool` | `true` | 获得/设置是否显示 Header 关闭按钮 |
| `ShowMaximizeButton` | `bool` | `false` | 获得/设置是否显示最大化按钮 |
| `ShowMinimizeButton` | `bool` | `false` | 获得/设置是否显示最小化按钮 |
| `ShowPrintButton` | `bool` | `false` | 获得/设置是否显示打印按钮 |
| `ShowResize` | `bool` | `false` | 获得/设置是否显示调整大小手柄 |
| `IsKeyboard` | `bool` | `true` | 获得/设置是否支持 ESC 关闭 |
| `IsBackdrop` | `bool` | `true` | 获得/设置是否显示遮罩 |
| `IsDraggable` | `bool` | `false` | 获得/设置是否可拖拽 |
| `BodyContext` | `object?` | `null` | 获得/设置弹窗传参 |
| `Component` | `BootstrapDynamicComponent` | `null` | 获得/设置弹窗内容组件 |
| `HeaderTemplate` | `RenderFragment?` | `null` | 获得/设置标题栏模板 |
| `HeaderToolbarTemplate` | `RenderFragment?` | `null` | 获得/设置标题栏工具栏模板 |
| `FooterTemplate` | `RenderFragment?` | `null` | 获得/设置 Footer 模板 |

## 最佳实践

### 1. 弹窗传参最佳实践

**推荐做法**：使用 `BodyContext` 传参，在弹窗组件中使用级联参数接收。

**示例**：

调用方：
```csharp
var option = new DialogOption()
{
    Title = "编辑用户",
    BodyContext = userId  // 传递用户ID
};
option.Component = BootstrapDynamicComponent.CreateComponent<EditUserComponent>();
await DialogService.Show(option);
```

弹窗组件：
```csharp
[CascadingParameter]
private int UserId { get; set; }  // 接收传参

protected override async Task OnInitializedAsync()
{
    // 根据 UserId 加载数据
    var user = await UserService.GetUserAsync(UserId);
}
```

---

### 2. 编辑对话框最佳实践

使用 `ShowEditDialog` 自动生成编辑表单：

```csharp
var option = new EditDialogOption<Foo>()
{
    Title = "编辑数据",
    Model = foo,  // 传入编辑模型
    OnSaveAsync = async (model, changedType) =>
    {
        // 保存逻辑
        await SaveModelAsync(model);
        return true;
    }
};
await DialogService.ShowEditDialog(option);
```

**优点**：
- 自动生成带验证的表单
- 自动处理取消/保存逻辑
- 支持复杂类型编辑

---

### 3. 多级弹窗管理

在多级弹窗场景中，每个弹窗应独立管理自己的状态：

```csharp
// 第一级弹窗
var option1 = new DialogOption()
{
    Title = "第一级",
    IsKeyboard = true,
    IsBackdrop = true
};

// 第二级弹窗（从第一级弹窗中打开）
var option2 = new DialogOption()
{
    Title = "第二级",
    IsKeyboard = false,  // 避免 ESC 关闭所有弹窗
    IsBackdrop = true
};
```

**注意事项**：
- 子弹窗的 `IsKeyboard` 应设为 `false`，避免 ESC 关闭所有弹窗
- 每个弹窗应有独立的关闭逻辑

---

### 4. 性能优化

对于复杂弹窗，建议：

1. **延迟加载**：弹窗内容在需要时再加载
2. **复用组件**：避免每次打开弹窗都创建新组件实例
3. **异步加载**：使用 `OnInitializedAsync` 异步加载数据

---

### 5. 常见错误

**错误 1**：未注入 `DialogService`

**解决方法**：在 `_Imports.razor` 中添加 `@inject DialogService DialogService` 或在组件中注入。

**错误 2**：弹窗传参类型不匹配

**解决方法**：确保 `BodyContext` 类型与弹窗组件中级联参数类型一致。

**错误 3**：多级弹窗 ESC 全部关闭

**解决方法**：子弹窗设置 `IsKeyboard="false"`。

---

## 相关组件

- `DialogService` - 弹窗服务
- `DialogOption` - 弹窗配置类
- `EditDialogOption<TModel>` - 编辑弹窗配置类
- `SearchDialogOption<TModel>` - 搜索弹窗配置类
- `ModalDialog` - 模态对话框组件

---

**生成说明**：本文档基于 Bootstrap Blazor 官方文档和源码自动生成，涵盖了 Dialog 组件的核心功能和使用方法。
