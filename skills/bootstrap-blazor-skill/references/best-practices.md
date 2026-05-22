# Bootstrap Blazor 最佳实践

## 项目配置

### 必要的引用

```xml
<!-- _Imports.razor -->
@using BootstrapBlazor.Components
```

```csharp
// Program.cs - 注册 BootstrapBlazor 服务
builder.Services.AddBootstrapBlazor();
```

### 根组件设置

```razor
<!-- App.razor 或 MainLayout.razor -->
<BootstrapBlazorRoot>
    @Body
</BootstrapBlazorRoot>
```

## 表单验证 (ValidateForm)

### 基本模式

```razor
<ValidateForm Model="@Model" OnInvalidSubmit="@OnInvalidSubmit" OnValidSubmit="@OnValidSubmit">
    <ValidateFormItem>
        <EditorForm Model="@Model" />
    </ValidateFormItem>
</ValidateForm>
```

### 关键要点

1. **模型验证属性**: 使用 `[Required]`、`[Range]`、`[StringLength]` 等 DataAnnotations
2. **值类型验证**: 对于 `int`/`decimal` 等值类型，使用 `[Range]` 而非 `[Required]`，因为值类型总有默认值
3. **自定义验证**: 继承 `ValidatorBase` 或实现 `IValidator`
4. **异步验证**: 使用 `OnValidate` 回调进行服务端验证

### EditorForm vs 手动布局

- `EditorForm` 适合标准的增删改查表单，自动生成字段
- 手动 `<ValidateFormItem>` 适合需要自定义布局的复杂表单

## 表格 (Table)

### 基础配置

```razor
<Table TItem="Foo"
       Items="@Items"
       AutoGenerateColumns="true"
       IsPagination="true"
       IsStriped="true"
       ShowToolbar="true"
       ShowSearch="true"
       ShowColumnList="true"
       ShowExportButton="true">
</Table>
```

### 列定义

```razor
<Table TItem="Foo" Items="@Items" AutoGenerateColumns="false">
    <TableColumns>
        <TableColumn @bind-Field="@context.Name" />
        <TableColumn @bind-Field="@context.CreateTime" />
        <TableColumn @bind-Field="@context.Status" />
    </TableColumns>
</Table>
```

### 常用 Table 参数速查

| 功能 | 参数 | 说明 |
|------|------|------|
| 分页 | `IsPagination` | 启用分页 |
| 分页容量 | `PageItemsSource` | 每页条数选项 |
| 搜索 | `ShowSearch` | 显示搜索栏 |
| 工具栏 | `ShowToolbar` | 显示工具栏 |
| 列选择 | `ShowColumnList` | 显示列选择器 |
| 导出 | `ShowExportButton` | 显示导出按钮 |
| 编辑 | `IsExcel` | Excel 模式编辑 |
| 多选 | `ShowCheckbox` | 显示复选框列 |
| 树形 | `IsTree` | 树形表格模式 |
| 固定表头 | `IsFixedHeader` | 固定表头 |
| 斑马纹 | `IsStriped` | 斑马纹样式 |

### 编辑模式

- **行内编辑 (Inline)**: `IsExcel="true"`，适合简单表格快速编辑
- **弹窗编辑 (Dialog)**: 使用 `EditDialog` 模板，适合复杂表单
- **详情行 (Detail Row)**: 使用 `DetailRowTemplate` 展开明细

## 对话框 (Dialog)

### 基本用法

```razor
<Dialog @ref="Dialog" Title="标题" ShowFooter="true" Size="Size.ExtraLarge">
    <BodyTemplate>
        <!-- 对话框内容 -->
    </BodyTemplate>
    <FooterTemplate>
        <Button OnClick="OnSave" Text="保存" />
        <Button OnClick="OnClose" Text="取消" Color="Color.Secondary" />
    </FooterTemplate>
</Dialog>
```

### Dialog 常用参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `Title` | `string` | 标题 |
| `IsDraggable` | `bool` | 是否可拖拽 |
| `IsResizable` | `bool` | 是否可调整大小 |
| `ShowFooter` | `bool` | 是否显示底部 |
| `ShowPrintButton` | `bool` | 显示打印按钮 |
| `Size` | `Size` | 对话框大小 |
| `FullScreenSize` | `FullScreenSize` | 全屏模式 |

### 编程式调用

```csharp
// 通过服务弹窗
await DialogService.Show(new DialogOption()
{
    Title = "编辑",
    BodyTemplate = builder => { /* 构建内容 */ },
    // ...
});
```

## 全局配置

### BootstrapBlazorOptions

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    // Table 默认设置
    opts.TableSettings.CheckboxColumnWidth = 36;
    opts.TableSettings.ShowSearch = true;
    
    // 本地化
    opts.DefaultCultureInfo = "zh-CN";
    
    // 主题
    opts.Theme = "bootstrap";
});
```

### StepSettings / DialogSettings

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    // 步骤条全局配置
    opts.StepSettings.StepItemWidth = 200;
    
    // 对话框全局配置
    opts.DialogSettings.IsDraggable = true;
});
```

## 本地化

```csharp
// Program.cs
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.DefaultCultureInfo = "zh-CN";
});

// 组件内使用
@inject IStringLocalizer<MyPage> Localizer

<Button Text="@Localizer["Save"]" />
```

## 常见陷阱

### 1. 值类型验证

❌ 错误:
```csharp
[Required]
public int Age { get; set; }  // 总是 0，验证通过
```

✅ 正确:
```csharp
[Range(1, 150, ErrorMessage = "请输入有效年龄")]
public int Age { get; set; }
```

### 2. Table 空数据

确保 `Items` 不为 null:
```csharp
Items = new List<Foo>();  // 空列表 OK，null 会导致异常
```

### 3. 异步刷新

```csharp
// 使用 StateHasChanged 和 InvokeAsync
await InvokeAsync(StateHasChanged);
```

### 4. Modal vs Dialog

- `Dialog` 是功能完整的对话框，支持拖拽、调整大小、全屏
- `Modal` 是简单的模态框，用于确认/提示

### 5. ValidateForm 与 EditorForm 配合

`EditorForm` 必须放在 `ValidateForm` 内部才能触发验证：

```razor
<ValidateForm Model="@Model" OnValidSubmit="@OnSave">
    <EditorForm Model="@Model" />
</ValidateForm>
```
