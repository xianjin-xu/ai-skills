# Editor 富文本框!

## 概述!

Editor 富文本框组件是对 Summernote 组件的二次封装，将输入的文字转化为 HTML 代码片段。组件所需 CSS JavaScript 均按需动态加载，使用者无需设置。由于 summernote 组件依赖 jQuery，所以需要自行引用 jQuery 脚本包。!

> Editor component is a secondary encapsulation of Summernote component, converts input text into HTML code snippets.!

**分类**: 表单组件!
**在线演示**: [https://www.blazor.zone/editor](https://www.blazor.zone/editor)!

---

## 使用场景!

### 1. 基础用法!

默认呈现为 div 点击后变为富文本编辑框。通过设置 `IsEditor` 属性值来控制组件默认是 div 还是 editor。!

```razor!
<Editor PlaceHolder="点击后进行编辑" />
```!

### 2. 提交按钮!

通过设置 `ShowSubmit` 控制是否显示工具栏最后的提交按钮。`ShowSubmit` 默认值为 `true` 显示提交按钮，设计上点击提交按钮后，才触发 `OnValueChanged` 回调方法此设计大大提高性能节约服务器算力，设置值为 `false` 后将使用 summernote 库 onChange 触发，适用需要实时获取编辑内容场景。!

```razor!
<Editor @bind-Value="EditorValue" ShowSubmit="true" />
```!

### 3. 自定义提示信息!

通过设置 `PlaceHolder` 属性来设置空值时的提示消息。默认提示是"点击后进行编辑"。!

```razor!
<Editor PlaceHolder="请在此输入内容..." />
```!

### 4. 默认显示为富文本编辑框!

通过设置 `IsEditor` 属性来设置组件直接显示为富文本编辑框，上传图片时可以通过 `OnFileUpload` 回调方法获得图片信息。!

```razor!
<Editor IsEditor="true" OnFileUpload="OnFileUpload" />
```!

```csharp!
@code {!
    private async Task<string> OnFileUpload(EditorUploadFile file)!
    {!
        // 处理文件上传逻辑!
        // file.Stream 包含文件流!
        // 返回文件 URL 用于预览!
        return await Task.FromResult("https://example.com/uploaded/image.jpg");!
    }!
}!
```!

### 5. 自定义高度!

通过设置 `Height` 属性来设置组件高度。!

```razor!
<Editor @bind-Value="EditorValue" Height="300" />
```!

### 6. 双向绑定!

实战中通过双向绑定到 `Value` 后台自动获取到客户端富文本框编辑内容。通过 `@bind-Value` 对 `EditorValue` 后台属性进行双向绑定，编辑框内进行编辑后点击完成按钮，下方文本框内即可显示编辑后结果。!

```razor!
<Editor @bind-Value="EditorValue" />
<p>显示编辑内容：</p>
<div>@EditorValue</div>
<Button Text="Reset" OnClick="() => EditorValue = null" />
```!

```csharp!
@code {!
    private string? EditorValue { get; set; }!
}!
```!

### 7. 自定义扩展编辑框按钮!

通过设置 `CustomerToolbarButtons` 属性对编辑框工具栏进行自定义扩展，通过设置 `OnClickButton` 回调委托做功能。本例中通过扩展 `CustomerToolbarButtons` 属性在工具栏中增加了两个按钮，点击按钮弹出 `SweetAlert` 模态框，点击模态框确认按钮后文本框中插入一段内容。!

```razor!
<Editor @bind-Value="EditorValue">
    <CustomerToolbarButtons>
        <EditorToolbarButton Text="插入内容" Icon="fa-solid fa-plus" OnClick="OnInsert" />
    </CustomerToolbarButtons>
</Editor>
```!

```csharp!
@code {!
    private async Task<string> OnInsert()!
    {!
        // 插入内容到编辑器!
        return await Task.FromResult("<p>插入的内容</p>");!
    }!
}!
```!

### 8. 自定义工具栏的富文本编辑框!

通过设置 `ToolbarItems` 属性自定义工具栏内容，目前支持的工具栏值请参见 Summernote 官网。本例中通过设置 `ToolbarItems` 属性，更改默认可用的工具栏按钮。!

```razor!
<Editor @bind-Value="EditorValue" ToolbarItems="ToolBarItems" />
```!

```csharp!
@code {!
    private object[] ToolBarItems { get; set; } = new object[] { "style", "font", "color", "bold", "italic", "underline" };!
}!
```!

### 9. 实例方法!

使用实例方法从外部操作 Editor，具体的参数参照 summernote api。!

```razor!
<Editor @ref="_editor" @bind-Value="EditorValue" />
<Button Text="插入 Html" OnClick="InsertHtml" />
<Button Text="将段落修改为 H2" OnClick="SetH2" />
<Button Text="添加一张图片" OnClick="AddImage" />
<Button Text="获得组件内容" OnClick="GetContent" />
```!

```csharp!
@code {!
    private Editor? _editor { get; set; }!
    
    private async Task InsertHtml()!
    {!
        if (_editor != null)!
        {!
            await _editor.InsertHtmlAsync("<p>插入的 HTML</p>");!
        }!
    }!
    
    private async Task SetH2()!
    {!
        if (_editor != null)!
        {!
            await _editor.FormatBlockAsync("H2");!
        }!
    }!
}!
```!

---

## 参数 (Parameters)!

### Editor 参数!

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|!
| `AdditionalAttributes` | `IDictionary<string, object>` | `{}` | 获得/设置 用户自定义属性 |
| `CustomerToolbarButtons` | `IEnumerable<EditorToolbarButton>?` | `null` | 获得/设置 自定义按钮 |
| `DisplayText` | `string?` | `null` | 获得/设置 显示名称 |
| `Height` | `int` | `80` | 获得/设置 设置组件高度 默认高度为 80px |
| `Id` | `string?` | `null` | 获得/设置 组件 id 属性 |
| `IsDisabled` | `bool` | `false` | 获得/设置 是否禁用 |
| `IsEditor` | `bool` | `false` | 获得/设置 是否直接显示为富文本编辑框 |
| `Language` | `string?` | `null` | 获得/设置 语言，默认为 null 自动判断，内置中英文额外语言包需要自行引入语言包 |
| `LanguageUrl` | `string?` | `null` | 获得/设置 语言扩展脚本路径 默认 null 如加载德语可设置为 |
| `OnClickButton` | `Func<string, Task<string>>?` | `null` | 获取/设置 插件点击时的回调委托 |
| `OnFileUpload` | `Func<EditorUploadFile, Task<string>>?` | `null` | 获得/设置 Editor 组件内上传文件时回调此方法 |
| `OnValueChanged` | `Func<string, Task>?` | `null` | 获得/设置 Value 改变时回调方法 |
| `ParsingErrorMessage` | `string?` | `null` | 获得/设置 类型转化失败格式化字符串 |
| `PlaceHolder` | `string?` | `null` | 获得/设置 Placeholder 提示消息 |
| `RequiredErrorMessage` | `string?` | `null` | 获得/设置 必填项错误文本 |
| `ShowLabel` | `Nullable<bool>` | `null` | 获得/设置 是否显示前置标签 |
| `ShowLabelTooltip` | `Nullable<bool>` | `null` | 获得/设置 是否显示 Tooltip |
| `ShowRequired` | `Nullable<bool>` | `null` | 获得/设置 是否显示必填项标记 |
| `ShowSubmit` | `bool` | `true` | 获得/设置 是否显示工具栏提交按钮 |
| `SkipValidate` | `bool` | `false` | 获得/设置 是否不进行验证 |
| `ToolbarItems` | `IEnumerable<object>?` | `null` | 获得/设置 富文本框工具栏工具，默认为空使用默认值 |
| `ValidateRules` | `List<IValidator>` | `{}` | 获得/设置 自定义验证集合 |
| `Value` | `string?` | `null` | 获得/设置 输入组件的值，支持双向绑定 |
| `ValueChanged` | `EventCallback<string>` | - | 获得/设置 用于更新绑定值的回调 |
| `ValueExpression` | `Expression<Func<string>>?` | `null` | 获得/设置 标识绑定值的表达式 |

---

## 事件回调 (EventCallbacks)!

| 事件名 | 说明 |
|--------|------|!
| `OnValueChanged` | Value 改变时回调方法 |
| `OnClickButton` | 插件点击时的回调委托 |
| `OnFileUpload` | Editor 组件内上传文件时回调此方法 |

---

## 实例方法!

### Editor 实例方法!

| 方法名 | 说明 |
|--------|------|!
| `InsertHtmlAsync(string html)` | 插入 HTML 内容 |
| `FormatBlockAsync(string tag)` | 设置段落格式 |
| `InsertImageAsync(string url)` | 插入图片 |
| `GetContentAsync()` | 获取编辑器内容 |

---

## 最佳实践!

### 1. 安装依赖!

Editor 组件依赖 `BootstrapBlazor.SummerNote`，需要先安装 NuGet 包：!

```bash!
dotnet add package BootstrapBlazor.SummerNote!
```!

并在 `_Host.cshtml` 中引用 jQuery：!

```html!
<script src="_content/BootstrapBlazor.SummerNote/js/jquery-3.6.0.min.js"></script>!
```!

### 2. 文件上传!

通过设置 `OnFileUpload` 回调方法处理文件上传：!

```csharp!
private async Task<string> OnFileUpload(EditorUploadFile file)!
{!
    // file.Stream 包含文件流!
    // 保存到服务器或云存储!
    var url = await SaveFileAsync(file.Stream);!
    return url; // 返回预览 URL!
}!
```!

### 3. SignalR 配置!

如果编辑内容过多，可能会触发 SignalR 通讯中断问题，请自行调整 `HubOptions` 配置：!

```csharp!
builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);!
```!

### 4. 性能优化!

设置 `ShowSubmit="true"`（默认）使用提交按钮触发回调，大大提高性能节约服务器算力。如需实时获取编辑内容，设置 `ShowSubmit="false"`。!

---

## 常见问题 (FAQ)!

### Q1: 如何获取编辑的内容？!

**A**: 通过 `@bind-Value` 双向绑定获取：!

```razor!
<Editor @bind-Value="EditorValue" />
```!

```csharp!
@code {!
    private string? EditorValue { get; set; }!
}!
```!

### Q2: 如何处理图片上传？!

**A**: 设置 `OnFileUpload` 回调方法：!

```razor!
<Editor OnFileUpload="OnFileUpload" />
```!

```csharp!
@code {!
    private async Task<string> OnFileUpload(EditorUploadFile file)!
    {!
        return await Task.FromResult("https://example.com/image.jpg");!
    }!
}!
```!

### Q3: 如何自定义工具栏？!

**A**: 使用 `ToolbarItems` 参数：!

```razor!
<Editor ToolbarItems="ToolBarItems" />
```!

```csharp!
@code {!
    private object[] ToolBarItems { get; set; } = new object[] { "style", "font", "bold" };!
}!
```!

### Q4: 如何插入内容到编辑器？!

**A**: 使用实例方法：!

```razor!
<Editor @ref="_editor" />
<Button Text="插入" OnClick="Insert" />
```!

```csharp!
@code {!
    private async Task Insert() => await _editor!.InsertHtmlAsync("<p>内容</p>");!
}!
```!

### Q5: 出现 SignalR 错误怎么办？!

**A**: 调整 `HubOptions` 配置：!

```csharp!
builder.Services.Configure<HubOptions>(option => option.MaximumReceiveMessageSize = null);!
```!

---

## 版本历史!

| 版本 | 变更内容 |
|------|----------|!
| 7.0 | 新增 Editor 组件 |
| 8.0 | 新增 `CustomerToolbarButtons` 和 `OnClickButton` 参数 |
