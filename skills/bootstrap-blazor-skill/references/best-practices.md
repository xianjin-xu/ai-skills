# Bootstrap Blazor 最佳实践

## 响应式断点

Bootstrap Blazor 组件已默认适配 `xxl`（≥1400px）。

| 断点 | xs | sm | md | lg | xl | xxl |
|------|-----|------|------|------|------|------|
| 阈值 | <576 | ≥576 | ≥768 | ≥992 | ≥1200 | ≥1400 |

- 很多组件默认值为 `xxl`（如 Dialog 默认大小 `dialog-xxl`）
- 使用 `Row`/`Column` 时通过 `xxl="6"` `lg="4"` 等控制断点列宽

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

### 表单标签 (Label) 最佳实践

#### ShowLabel 优先级（就近原则）

标签是否显示遵循**就近原则**，离组件越近的设置越优先：

1. 表单组件自身 `ShowLabel` 属性（最高）
2. `EditorForm` / `ValidateForm` 的 `ShowLabel` 属性
3. 全局默认设置（最低）

```razor
<!-- ValidateForm 设置 ShowLabel=true，但组件自身设 false → 最终不显示 -->
<ValidateForm ShowLabel="true">
    <BootstrapInput @bind-Value="Name" ShowLabel="false" />
</ValidateForm>
```

#### 本地化标签文本

Label 文字应放入资源文件（`zh.json` / `en.json`），配合 `Display` 特性自动获取：

```csharp
public class Foo
{
    [Display(Name = "Name")]  // 资源文件中查找 "Name" 键
    public string Name { get; set; }
}
```

```razor
<!-- DisplayText="@null" 自动从 Display 特性 + 资源文件获取 -->
<BootstrapInput @bind-Value="Model.Name" ShowLabel="true" DisplayText="@null" />
```

#### 标签宽度控制

- **全局设置**：CSS 变量 `--bb-row-label-width`（默认 120px）
- **组件级设置**：`LabelWidth` 参数（就近原则）
- **长文本**：`ShowLabelTooltip="true"` 显示 Tooltip

#### 各场景 ShowLabel 默认值

| 场景 | 默认值 | 说明 |
|------|--------|------|
| 单独使用组件 | `false` | 需显式设为 true |
| EditorForm/ValidateForm 内 | `true` | 自动生成标签 |

## 表格 (Table)

### 常用参数速查

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

### 常用参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `Title` | `string` | 标题 |
| `IsDraggable` | `bool` | 是否可拖拽 |
| `IsResizable` | `bool` | 是否可调整大小 |
| `ShowFooter` | `bool` | 是否显示底部 |
| `Size` | `Size` | 对话框大小 |
| `FullScreenSize` | `FullScreenSize` | 全屏模式 |

### 编程式调用

```csharp
await DialogService.Show(new DialogOption()
{
    Title = "编辑",
    BodyTemplate = builder => { /* 构建内容 */ },
});
```

## 组件分层 (z-index)

| 组件 | z-index | 组件 | z-index |
|------|---------|------|---------|
| Dropdown | 1000 | Modal | 1055 |
| Sticky | 1020 | Drawer | 1050 |
| Fixed | 1030 | Dialog | 1050 |
| Offcanvas | 1045 | Popover | 1070 |
| Modal Backdrop | 1050 | Swal | 1075 |
| | | Message/Toast | 1090 |

**多弹窗组合**：Drawer/Dialog 同层（1050）后者覆盖前者；Swal(1075) > Dialog；Message/Toast(1090) 始终置顶。

## 全局配置

> **完整指南**：详见 `references/global-option.md`

```csharp
builder.Services.AddBootstrapBlazor(opts =>
{
    opts.DefaultCultureInfo = "zh-CN";
    opts.IsPopover = true;                    // 解决 Dialog 内 Select 遮挡
    opts.TableSettings.CheckboxColumnWidth = 36;
    opts.EditDialogSettings.ShowCloseConfirm = true;
    opts.ToastDelay = 5000;
});
```

## 本地化

> **完整指南**：详见 `references/localization.md`

1. **WASM 模式**必须设置 `DefaultCultureInfo`，否则默认 `en`
2. **组件内置文本**用 `BootstrapBlazor.Components.{ComponentName}` 资源键覆盖
3. **回退机制**：`zh-CN` → `zh` → `en`（确保至少提供 `en`）

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
