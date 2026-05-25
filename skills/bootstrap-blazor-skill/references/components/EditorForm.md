# EditorForm

## 概述

编辑表单基类

> Editor Form Base Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/editor-form](https://www.blazor.zone/editor-form)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ItemsPerRow` | `int?` | `}` | 获得/设置 每行显示组件数量 默认为 null |
| `ItemChangedType` | `ItemChangedType` | `}` | 获得/设置 实体类编辑模式 Add 还是 Update |
| `RowType` | `RowType` | `}` | 获得/设置 设置行格式 默认 Row 布局 |
| `LabelAlign` | `Alignment` | `}` | 获得/设置 设置 <see cref="RowType" /> Inline 模式下标签对齐方式 默认 None 等效于 Left 左对齐 |
| `LabelWidth` | `int?` | `}` | 获得/设置 标签宽度 默认 null 未设置使用全局设置 <code>--bb-row-label-width</code> 值 |
| `FieldItems` | `RenderFragment<TModel>?` | `}` | 获得/设置 绑定属性集合模板 设置 <see cref="Items"/> 时本参数优先级高 |
| `Buttons` | `RenderFragment?` | `}` | 获得/设置 按钮模板 |
| `Model` | `TModel?` | `}` | 获得/设置 绑定模型 |
| `ShowLabel` | `bool?` | `}` | 获得/设置 是否显示前置标签 默认为 null 未设置时默认显示标签 |
| `ShowLabelTooltip` | `bool?` | `}` | 获得/设置 是否显示标签 Tooltip 多用于标签文字过长导致裁减时使用 默认 null |
| `IsDisplay` | `bool` | `}` | 获得/设置 是否显示为 Display 组件 默认为 false |
| `IsShowDisplayTooltip` | `bool` | `}` | 获得/设置 是否显示 Display 组件的 Tooltip 默认为 false |
| `AutoGenerateAllItem` | `bool` | `true` | 获得/设置 是否自动生成模型的所有属性 默认为 true 生成所有属性 |
| `IgnoreItems` | `List<string>?` | `}` | 获得/设置 忽略项目集合 默认 null 未设置 |
| `Items` | `IEnumerable<IEditorItem>?` | `}` | 获得/设置 绑定字段信息集合 设置此参数后 <see cref="FieldItems"/> 模板优先级更高 |
| `IEnumerable` | `Func<IEnumerable<ITableColumn>,` | `}` | 获得/设置 自定义列排序规则 默认 null 未设置 使用内部排序机制 1 2 3 0 -3 -2 -1 顺序 |
| `ShowUnsetGroupItemsOnTop` | `bool` | `}` | 获得/设置 未设置 GroupName 编辑项是否放置在顶部 默认 false |
| `PlaceHolderText` | `string?` | `}` | 获得/设置 默认占位符文本 默认 null |
| `IsRenderWhenValueChanged` | `bool` | `}` | 获得/设置 当值变化时是否重新渲染组件 默认 false |
| `GroupType` | `EditorFormGroupType` | `}` | 获得/设置 分组类型 默认 <see cref="EditorFormGroupType.GroupBox"/> |

## 代码示例

### 基本用法

```razor
<EditorForm Model="@Model">
            <FieldItems>
                <EditorItem @bind-Field="@context.Education" Readonly="true"></EditorItem>
                <EditorItem @bind-Field="@context.Complete" Readonly="true"></EditorItem>
                <EditorItem @bind-Field="@context.Hobby" Items="@Hobbies" Readonly="true"></EditorItem>
            </FieldItems>
            <Buttons>
                <Button Icon="fa-solid fa-floppy-disk" Text="@Localizer["SubButtonText"]"></Button>
            </Buttons>
        </EditorForm>
```

### 基本用法

```razor
<EditorForm TModel="Foo">
                <FieldItems>
                    <EditorItem @bind-Field="@context.DateTime" Readonly="true"></EditorItem>
                    <EditorItem @bind-Field="@context.Hobby" Items="@Hobbies"></EditorItem>
                </FieldItems>
                <Buttons>
                    <Button ButtonType="ButtonType.Submit" Icon="fa-solid fa-floppy-disk" Text="@Localizer["SubButtonText"]"></Button>
                </Buttons>
            </EditorForm>
```

### 基本用法

```razor
<EditorForm Model="@Model" AutoGenerateAllItem="false">
            <FieldItems>
                <EditorItem @bind-Field="@context.Name"></EditorItem>
                <EditorItem @bind-Field="@context.Count"></EditorItem>
            </FieldItems>
        </EditorForm>
```

### 基本用法

```razor
<EditorForm Model="Model" AutoGenerateAllItem="false">
                <FieldItems>
                    <EditorItem @bind-Field="@context.Name"></EditorItem>
                    <EditorItem @bind-Field="@context.Address"></EditorItem>
                    <EditorItem @bind-Field="@context.Count">
                        <EditTemplate Context="value">
                            <div class="col-12 col-sm-6">
                                <Select SkipValidate="true" @bind-Value="@value.Count" Items="@DummyItems" ShowSearch="true"></Select>
                            </div>
                            <div class="col-12 col-sm-6">
                                <BootstrapInput Value="@value.Count" Readonly="true"></BootstrapInput>
                            </div>
                        </EditTemplate>
                    </EditorItem>
                    <EditorItem @bind-Field="@context.Hobby" Items="@Hobbies"></EditorItem>
                </FieldItems>
                <Buttons>
                    <Button ButtonType="ButtonType.Submit" Icon="fa-solid fa-floppy-disk" Text="@Localizer["SubButtonText"]"></Button>
                </Buttons>
            </EditorForm>
```

### 基本用法

```razor
<EditorForm TModel="Foo" ItemsPerRow="3">
                <FieldItems>
                    <EditorItem @bind-Field="@context.Hobby" Items="@Hobbies"></EditorItem>
                </FieldItems>
                <Buttons>
                    <Button ButtonType="ButtonType.Submit" Icon="fa-solid fa-floppy-disk" Text="@Localizer["SubButtonText"]"></Button>
                </Buttons>
            </EditorForm>
```
