# SearchDialog 搜索弹窗

## 概述

SearchDialog 搜索弹窗组件是 Dialog 组件的扩展，适用于数据弹出窗设置搜索条件。通过调用注入服务 DialogService 的 ShowSearchDialog 方法直接弹出搜索条件弹窗，大大减少代码量。SearchDialogOption 配置类继承 DialogOption，更多参数设置请参考 Dialog 组件文档。

> SearchDialog component is an extension of Dialog component, suitable for data popup window to set search conditions.

**分类**: 通知组件  
**在线演示**: [https://www.blazor.zone/search-dialog](https://www.blazor.zone/search-dialog)

---

## 使用场景

### 1. 基础用法

通过绑定 TModel 数据模型，自动生成模型各个字段的搜索表单。使用 `DialogService.ShowSearchDialog` 方法弹出搜索弹窗。

```razor
@inject DialogService DialogService

<Button Text="点击弹出搜索弹窗" OnClick="OnSearchClick" />

@code {
    private async Task OnSearchClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private Task OnSearchAsync()
    {
        // 执行搜索逻辑
        return Task.CompletedTask;
    }
}
```

### 2. 自定义搜索弹窗内显示的条件字段

通过设定 `Columns` 参数显式设置显示的搜索字段，可以精确控制哪些字段显示在搜索弹窗中。

```razor
@inject DialogService DialogService

<Button Text="点击弹出搜索弹窗" OnClick="OnSearchClick" />

@code {
    private async Task OnSearchClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            Columns = new List<string>() { "Name", "Education", "City" },
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private Task OnSearchAsync()
    {
        return Task.CompletedTask;
    }
}
```

### 3. 设置搜索弹窗内布局方式

通过设定 `RowType` 参数显式设置弹窗内组件布局方式，默认为上下布局（Row），可设置值为 `inline` 水平布局。

```razor
@inject DialogService DialogService

<Button Text="搜索弹窗(左对齐)" OnClick="OnSearchLeftClick" />
<Button Text="搜索弹窗(右对齐)" OnClick="OnSearchRightClick" />

@code {
    private async Task OnSearchLeftClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            RowType = RowType.Inline,
            LabelAlign = Alignment.Left,
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private async Task OnSearchRightClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            RowType = RowType.Inline,
            LabelAlign = Alignment.Right,
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private Task OnSearchAsync()
    {
        return Task.CompletedTask;
    }
}
```

### 4. 自定义按钮文本

通过设定 `QueryButtonText`、`ResetButtonText`、`CloseButtonText` 等参数自定义按钮显示文本。

```razor
@inject DialogService DialogService

<Button Text="点击弹出搜索弹窗" OnClick="OnSearchClick" />

@code {
    private async Task OnSearchClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "高级搜索",
            Model = new BindItem(),
            QueryButtonText = "查询",
            ResetButtonText = "重置",
            CloseButtonText = "关闭",
            OnSearchClick = OnSearchAsync,
            OnResetSearchClick = OnResetAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private Task OnSearchAsync()
    {
        return Task.CompletedTask;
    }

    private Task OnResetAsync()
    {
        return Task.CompletedTask;
    }
}
```

### 5. 对话框尺寸与全屏

通过设定 `Size` 参数控制对话框尺寸，设定 `FullScreenSize` 参数控制全屏尺寸。

```razor
@inject DialogService DialogService

<Button Text="大尺寸弹窗" OnClick="OnLargeClick" />
<Button Text="全屏弹窗" OnClick="OnFullScreenClick" />

@code {
    private async Task OnLargeClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            Size = Size.Large,
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private async Task OnFullScreenClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            FullScreenSize = FullScreenSize.ExtraLarge,
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private Task OnSearchAsync()
    {
        return Task.CompletedTask;
    }
}
```

### 6. 显示标签与每行组件数量

通过设定 `ShowLabel` 参数控制是否显示标签，设定 `ItemsPerRow` 参数控制每行显示组件数量。

```razor
@inject DialogService DialogService

<Button Text="点击弹出搜索弹窗" OnClick="OnSearchClick" />

@code {
    private async Task OnSearchClick()
    {
        var option = new SearchDialogOption<BindItem>()
        {
            Title = "搜索",
            Model = new BindItem(),
            ShowLabel = true,
            ItemsPerRow = 2,
            OnSearchClick = OnSearchAsync
        };
        await DialogService.ShowSearchDialog<BindItem>(option);
    }

    private Task OnSearchAsync()
    {
        return Task.CompletedTask;
    }
}
```

---

## 参数

### SearchDialogOption 属性

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| BodyContext | 获得/设置 关联数据多用于传值 | Object | — |
| BodyTemplate | 获得/设置 ModalBody 组件 | RenderFragment | — |
| Class | 获得/设置 对话框自定义样式 | string | — |
| CloseButtonIcon | 获得/设置 关闭按钮图标 默认值为 null 且使用当前主题图标 | string | null |
| CloseButtonText | 获得/设置 关闭按钮文本 | string | — |
| Component | 获得/设置 自定义组件 | BootstrapDynamicComponent | — |
| DialogBodyTemplate | 获得/设置 SearchDialog Body 模板 | RenderFragment<TModel> | — |
| ExportPdfButtonOptions | 获得/设置 导出 PDF 按钮配置 | ExportPdfButtonOptions | — |
| FooterTemplate | 获得/设置 ModalFooter 组件 | RenderFragment | — |
| FullScreenSize | 获得/设置 对话框全屏尺寸 默认值为 None | FullScreenSize | None |
| HeaderTemplate | 获得/设置 ModalHeader 组件模板 | RenderFragment | — |
| HeaderToolbarTemplate | 获得/设置 ModalHeader 组件自定义按钮 | RenderFragment | — |
| IsAutoCloseAfterSave | 获得/设置 是否自动关闭对话框（保存成功后） 默认值为 true | bool | true |
| IsBackdrop | 获得/设置 是否支持点击背景关闭对话框 默认值为 false | bool | false |
| IsCentered | 获得/设置 是否垂直居中 默认值为 true | bool | true |
| IsDraggable | 获得/设置 是否允许拖拽对话框 默认值为 false | bool | false |
| IsFade | 获得/设置 是否启用渐显动画 默认值为 null | Nullable<bool> | null |
| IsHidePreviousDialog | 获得/设置 是否隐藏上一个对话框 默认值为 false | bool | false |
| IsKeyboard | 获得/设置 是否支持通过 ESC 关闭对话框 默认值为 true | bool | true |
| IsScrolling | 获得/设置 内容过长时是否滚动 默认值为 false | bool | false |
| Items | 获得 搜索条件集合 | IEnumerable<IEditorItem> | — |
| ItemsPerRow | 获得/设置 每行显示组件数量 默认为 null | Nullable<int> | null |
| LabelAlign | 获得/设置 设置 Inline 模式下标签对齐方式 默认 None 等效于 Left 左对齐 | Alignment | None |
| Model | 获得/设置 编辑框模型 | TModel | — |
| OnCloseAsync | 获得/设置 弹出窗口关闭时的回调委托 | Func<Task> | — |
| OnClosingAsync | 关闭之前回调方法 返回 true 时关闭弹窗 返回 false 时阻止关闭弹窗 | Func<Task<bool>> | — |
| OnFilterChanged | 获得/设置 过滤器改变回调事件 Func 版本 | Func<FilterKeyValueAction, Task> | — |
| OnResetSearchClick | 获得/设置 重置回调委托 | Func<Task> | — |
| OnSaveAsync | 获得/设置 保存按钮回调方法 | Func<Task<bool>> | — |
| OnSearchClick | 获得/设置 搜索回调委托 | Func<Task> | — |
| OnShownAsync | 获得/设置 对话框显示回调方法 | Func<Task> | — |
| PrintButtonText | 获得/设置 标题栏打印按钮文本 默认值为资源文件中的 "Print" | string | — |
| QueryButtonText | 获得/设置 查询按钮文本 | string | — |
| ResetButtonText | 获得/设置 重置按钮文本 | string | — |
| RowType | 获得/设置 设置行内组件布局格式 默认 Row 布局 | RowType | Row |
| SaveButtonIcon | 获得/设置 保存按钮图标 默认值为 null 且使用当前主题图标 | string | null |
| SaveButtonText | 获得/设置 保存按钮文本 | string | — |
| SearchFormLocalizerOptions | 获得/设置 搜索表单本地化配置项 | Nullable<SearchFormLocalizerOptions> | — |
| SearchItems | 获得/设置 搜索表单项集合 | List<ISearchItem> | — |
| ShowCloseButton | 获得/设置 是否显示关闭按钮 默认值为 true | bool | true |
| ShowExportPdfButton | 获得/设置 是否显示导出 PDF 按钮 默认值为 false | bool | false |
| ShowExportPdfButtonInHeader | 获得/设置 是否在标题栏显示导出 PDF 按钮 默认值为 false | bool | false |
| ShowFooter | 获得/设置 是否显示页脚 默认值为 true | bool | true |
| ShowHeaderCloseButton | 获得/设置 是否显示标题栏关闭按钮 默认值为 true | bool | true |
| ShowLabel | 获得/设置 是否显示标签 默认为 true 显示标签 | bool | true |
| ShowMaximizeButton | 获得/设置 是否显示最大化按钮 默认值为 false | bool | false |
| ShowPrintButton | 获得/设置 是否显示打印按钮 默认值为 false | bool | false |
| ShowPrintButtonInHeader | 获得/设置 是否在标题栏显示打印按钮 默认值为 false | bool | false |
| ShowResize | 获得/设置 是否显示调整大小按钮 默认值为 false | bool | false |
| ShowSaveButton | 获得/设置 是否显示保存按钮 默认值为 false | bool | false |
| ShowUnsetGroupItemsOnTop | 获得/设置 未分组编辑项布局位置 默认 false 在尾部 | bool | false |
| Size | 获得/设置 对话框尺寸 | Size | — |
| Title | 获得/设置 对话框标题 | string | — |
| UseSearchForm | 获得/设置 是否使用 SearchForm 组件进行搜索条件编辑 默认 false 不使用 | bool | false |

---

## 事件回调

| 事件名称 | 说明 | 回调类型 |
|---------|------|---------|
| OnCloseAsync | 弹出窗口关闭时的回调委托 | Func<Task> |
| OnClosingAsync | 关闭之前回调方法，返回 true 时关闭弹窗，返回 false 时阻止关闭弹窗 | Func<Task<bool>> |
| OnFilterChanged | 过滤器改变回调事件 | Func<FilterKeyValueAction, Task> |
| OnResetSearchClick | 重置回调委托 | Func<Task> |
| OnSaveAsync | 保存按钮回调方法 | Func<Task<bool>> |
| OnSearchClick | 搜索回调委托 | Func<Task> |
| OnShownAsync | 对话框显示回调方法 | Func<Task> |

---

## 最佳实践

### 数据模型定义

使用 SearchDialog 时，需要定义数据模型并标记搜索相关属性：

```csharp
public class BindItem
{
    [Display(Name = "主键")]
    [AutoGenerateColumn(Ignore = true)]
    public int Id { get; set; }

    [Display(Name = "姓名")]
    [AutoGenerateColumn(Searchable = true)]
    public string? Name { get; set; }

    [Display(Name = "学历")]
    [AutoGenerateColumn(Searchable = true)]
    public EnumEducation? Education { get; set; }

    [Display(Name = "城市")]
    [AutoGenerateColumn(Searchable = true)]
    public string? City { get; set; }
}
```

### 搜索回调处理

在搜索回调中获取搜索条件并进行数据处理：

```csharp
private async Task OnSearchAsync()
{
    // 获取搜索条件
    var items = Option.SearchItems;
    
    // 根据搜索条件进行数据过滤
    // ...
    
    await Task.CompletedTask;
}
```

### 重置回调处理

在重置回调中清空搜索条件：

```csharp
private async Task OnResetAsync()
{
    // 清空模型数据
    Option.Model = new BindItem();
    
    await Task.CompletedTask;
}
```

---

## 常见问题

### 1. 如何获取搜索条件？

通过 `SearchDialogOption.SearchItems` 属性获取搜索条件集合，每个 `ISearchItem` 包含字段名称和搜索值。

### 2. 如何自定义搜索字段？

通过 `Columns` 参数指定需要显示的搜索字段名称列表，只有列表中的字段才会显示在搜索弹窗中。

### 3. 如何实现水平布局？

设置 `RowType` 参数为 `RowType.Inline` 即可实现水平布局，同时可以通过 `LabelAlign` 参数设置标签对齐方式。

### 4. 如何在使用后自动关闭弹窗？

设置 `IsAutoCloseAfterSave` 参数为 `true`（默认值），在保存成功后会自动关闭对话框。

---

## 版本历史

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | SearchDialog 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/search-dialog)
- [Dialog 组件文档](https://www.blazor.zone/dialog)
