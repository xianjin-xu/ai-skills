# Label (组件标签)

## 概述

本套组件中有 ValidateForm、EditorForm 以及多种继承 `ValidateBase<TValue>` 的表单组件，这些组件中有一套特殊的**显示前置标签逻辑**。

- `ValidateForm` 组件是可验证的表单组件，此组件内的表单组件会自动进行数据合规性检查，如果数据不合规将会阻止提交(Submit)动作，是数据提交中使用最最最频繁的组件
- `EditorForm` 组件是普通的表单组件，此组件绑定 Model 后即可自动生成整个表单，大大减少重复性编码，外面套上 ValidateForm 即可开启数据合规性检查，非常方便、简洁、高效

**相关组件**：
- `ValidateForm`：可验证表单组件
- `EditorForm`：普通表单组件
- `BootstrapLabel`：标签组件
- `BootstrapLabelSetting`：标签设置组件

**在线演示**: https://www.blazor.zone/label

---

## ShowLabel 显示逻辑（就近原则）

标签是否显示遵循**就近原则**：离自身越近的设置生效。

**优先级（从高到低）**：
1. 表单组件自身 `ShowLabel` 属性
2. `EditorForm` / `ValidateForm` 的 `ShowLabel` 属性
3. 全局默认设置

**示例**：
```razor
<!-- ValidateForm 设置 ShowLabel=true，但文本框自身设置 ShowLabel=false -->
<!-- 最终结果：不显示标签 -->
<ValidateForm ShowLabel="true">
    <BootstrapInput @bind-Value="Name" ShowLabel="false" />
</ValidateForm>
```

---

## 使用场景

### 1. 单独使用（适用于数据录入）

#### 未使用双向绑定时

- **默认不会显示 Label**
- 通过 `ShowLabel` 属性控制是否显示
- 设置 `DisplayText` 时显示指定内容
- 未设置时渲染一个无内容的 `label` 组件进行占位

```razor
<!-- 第一个：未进行任何设置，不显示标签 -->
<BootstrapInput @bind-Value="Dummy.Name" />

<!-- 第二个：ShowLabel='true' DisplayText='' 显示无内容的占位标签 -->
<BootstrapInput @bind-Value="Dummy.Name" ShowLabel="true" DisplayText="" />

<!-- 第三个：ShowLabel='true' DisplayText='Name' 显示设置的内容标签 -->
<BootstrapInput @bind-Value="Dummy.Name" ShowLabel="true" DisplayText="Name" />

<!-- 第四个：ShowLabel='true' DisplayText='@null' 显示无内容的占位标签 -->
<BootstrapInput @bind-Value="Dummy.Name" ShowLabel="true" DisplayText="@null" />
```

#### 使用双向绑定时

- 双向绑定后，可通过 `DisplayText` 利用 **Display 特性**自动获取标签文本
- `DisplayText="@null"` 时，使用资源文件中的 Label 定义

```razor
<!-- 第一个：@bind-Value='Dummy.Name'，不显示标签 -->
<BootstrapInput @bind-Value="Dummy.Name" />

<!-- 第二个：显示资源文件中的标签内容 -->
<BootstrapInput @bind-Value="Dummy.Name" ShowLabel="true" DisplayText="@Localizer[nameof(Foo.Address)]" />

<!-- 第三个：显示无内容占位标签 -->
<BootstrapInput @bind-Value="Dummy.Name" ShowLabel="true" DisplayText="" />

<!-- 第四个：显示资源文件机制下的标签内容 Label -->
<BootstrapInput @bind-Value="Dummy.Name" ShowLabel="true" DisplayText="@null" />
```

---

### 2. EditorForm 中使用

#### 未套 ValidateForm（普通表单）

- **默认不显示标签**（未设置 `ShowLabel` 时等同于 `false`）
- 设置 `ShowLabel="true"` 后，所有组件显示标签

```razor
<!-- 不显示标签 -->
<EditorForm TModel="Foo" ShowLabel="false">
    ...
</EditorForm>

<!-- 显示标签（默认行为，ShowLabel 未设置时等同于 true） -->
<EditorForm TModel="Foo">
    ...
</EditorForm>
```

#### 标签对齐方式

```razor
<!-- 右对齐 -->
<EditorForm TModel="Foo" ShowLabel="true" LabelAlign="Alignment.Right">
    ...
</EditorForm>

<!-- 居中对齐 -->
<EditorForm TModel="Foo" ShowLabel="true" LabelAlign="Alignment.Center">
    ...
</EditorForm>
```

#### 内置 ValidateForm 中使用

```razor
<!-- 显示标签（ShowLabel 未设置时等同于 true） -->
<EditorForm TModel="Foo">
    <ValidateForm>
        ...
    </ValidateForm>
</EditorForm>

<!-- 不显示标签 -->
<EditorForm TModel="Foo" ShowLabel="false">
    <ValidateForm>
        ...
    </ValidateForm>
</EditorForm>
```

---

### 3. ValidateForm 中使用

#### 默认自动开启显示标签

```razor
<!-- 显示标签（ShowLabel 未设置时等同于 true） -->
<ValidateForm Model="@Dummy">
    ...
</ValidateForm>

<!-- 不显示标签 -->
<ValidateForm Model="@Dummy" ShowLabel="false">
    ...
</ValidateForm>
```

#### 行内表单（form-inline）

```razor
<!-- 标签前置（form-inline 样式） -->
<ValidateForm Model="@Dummy" class="form-inline">
    <BootstrapInput @bind-Value="Dummy.Name" />
</ValidateForm>

<!-- 标签右对齐（form-inline-end 样式） -->
<ValidateForm Model="@Dummy" class="form-inline-end">
    <BootstrapInput @bind-Value="Dummy.Name" />
</ValidateForm>

<!-- 标签居中对齐（form-inline-center 样式） -->
<ValidateForm Model="@Dummy" class="form-inline-center">
    <BootstrapInput @bind-Value="Dummy.Name" />
</ValidateForm>
```

---

## 标签宽度控制

### 方式一：CSS 变量（全局设置）

组件前置标签默认宽度为 **120px**（约六个汉字）。

在项目样式文件中覆盖 CSS 变量：

```css
:root {
    --bb-row-label-width: 120px;
}
```

> **提示**：本例中通过设置 `form-inline` 样式内的 `BootstrapInput` 组件 `ShowLabelTooltip` 为 `true`，使鼠标悬停在被裁剪的 label 时显示完整信息。

---

### 方式二：LabelWidth 参数（组件级设置）

`ValidateForm`、`EditorForm`、`BootstrapLabelSetting`、`BootstrapLabel` 均可设置 `LabelWidth` 值。**组件采用就近原则确定最终值**。

```razor
<ValidateForm Model="@Dummy4" LabelWidth="100">
    <EditorForm TModel="Foo" ItemsPerRow="2" RowType="RowType.Inline"
                LabelAlign="Alignment.Right" LabelWidth="120"
                AutoGenerateAllItem="false">
        <FieldItems>
            <EditorItem @bind-Field="@Dummy4.Name"></EditorItem>
        </FieldItems>
    </EditorForm>

    <BootstrapLabelSetting LabelWidth="220">
        <div class="row form-inline g-3 mt-0">
            <div class="col-12 col-sm-6">
                <BootstrapLabel LabelWidth="180" Value="@LocalizerForm["LongDisplayText"]"></BootstrapLabel>
                <BootstrapInput @bind-Value="Dummy4.Name" ShowLabel="false" />
            </div>
        </div>
    </BootstrapLabelSetting>
</ValidateForm>
```

**就近原则取值结果**：
- `ValidateForm`：100
- `EditorForm`：120
- `BootstrapLabelSetting`：220
- `BootstrapLabel`：**180**（最终生效值）

---

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Value` | `string?` | `null` | 获得/设置组件值（显示文本），默认 null |
| `ShowLabelTooltip` | `bool?` | `false` | 获得/设置是否显示 Tooltip，多用于标签文字过长导致裁减时使用，默认 false 不显示 |
| `LabelWidth` | `int?` | `null` | 获得/设置标签宽度，默认 null 未设置使用全局设置 `--bb-row-label-width` 值 |

---

## 最佳实践

1. **优先使用双向绑定 + Display 特性**：通过 `DisplayText="@null"` 自动从资源文件获取标签文本，保持代码简洁
2. **全局设置标签宽度**：在项目 CSS 中设置 `--bb-row-label-width`，避免每个组件单独设置
3. **长文本标签使用 ShowLabelTooltip**：当标签文字可能溢出时，设置 `ShowLabelTooltip="true"` 提升用户体验
4. **ValidateForm 中慎用 ShowLabel="false"`：会隐藏所有标签，如需局部隐藏应在具体组件上设置
5. **EditorForm 默认不显示标签**：记得设置 `ShowLabel="true"` 或在外层套 `ValidateForm`
