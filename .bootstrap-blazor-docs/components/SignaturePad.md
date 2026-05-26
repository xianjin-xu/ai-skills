# SignaturePad 手写签名

## 组件概述

SignaturePad 是一个手写签名组件，用于移动终端签名并保存为 Base64 编码字符串。本组件依赖于 `BootstrapBlazor.SignaturePad`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.SignaturePad
```

或

```xml
<PackageReference Include="BootstrapBlazor.SignaturePad" Version="10.0.0" />
```

**重要提示：**

复杂签名会导致传输数据量大，SSR 会出现断流显示 reload 错误。配置更改单个传入集线器消息的最大大小（默认 32KB）解决这个问题：

```csharp
builder.Services.AddServerSideBlazor().AddHubOptions(o => o.MaximumReceiveMessageSize = null);
```

## 使用场景

### 1. 基础用法

鼠标滑动进行签名。

```razor
<SignaturePad OnResult="OnResult" />
```

```csharp
@code {
    private Task OnResult(string base64Data)
    {
        Console.WriteLine($"签名数据: {base64Data}");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `OnResult` 参数设置签名结果回调方法
- 用户在签名框内签名后，点击"确定"按钮，触发 `OnResult` 回调
- 回调参数为 Base64 编码的签名图像数据

### 2. 设置按钮样式

设置按钮 CSS 样式。

```razor
<SignaturePad OnResult="OnResult" BtnCssClass="btn btn-outline-success" />
```

**说明：**
- `BtnCssClass` 参数设置按钮 CSS 样式
- 可以自定义"清除"、"换颜色"、"撤消"、"确定"等按钮的样式
- 使用 Bootstrap 按钮样式类，如 `btn btn-primary`、`btn btn-outline-success` 等

### 3. 自定义按钮文本

自定义按钮文本。

```razor
<SignaturePad OnResult="OnResult" 
           SignAboveLabel="Sign above" 
           UndoBtnTitle="Undo" 
           SaveBase64BtnTitle="OK" 
           ChangeColorBtnTitle="Change color" 
           ClearBtnTitle="Clear" />
```

**说明：**
- `SignAboveLabel` 参数设置"在框内签名"标签文本
- `UndoBtnTitle` 参数设置"撤消"按钮文本
- `SaveBase64BtnTitle` 参数设置"确定"按钮文本
- `ChangeColorBtnTitle` 参数设置"换颜色"按钮文本
- `ClearBtnTitle` 参数设置"清除"按钮文本

### 4. 响应式签名界面

设备宽度小于 640px（例如手机）自动置顶无边框，宽度小于 500px 按钮自动旋转。可选透明背景。

```razor
<SignaturePad OnResult="OnResult" Responsive="true" BackgroundColor="transparent" />
```

**说明：**
- `Responsive` 参数启用响应式 CSS 界面，为所有用户设计最佳体验
- `BackgroundColor` 参数设置组件背景颜色，可以使用 `transparent` 实现透明背景
- 响应式设计自动适配不同屏幕尺寸

### 5. 启用/禁用功能按钮

通过参数控制显示哪些功能按钮。

```razor
<SignaturePad OnResult="OnResult" 
           EnableChangeColorBtn="true" 
           EnableSaveBase64Btn="true" 
           EnableSaveJPGBtn="false" 
           EnableSavePNGBtn="false" 
           EnableSaveSVGBtn="false" 
           EnableUndoBtn="true" />
```

**说明：**
- `EnableChangeColorBtn` - 启用换颜色按钮
- `EnableSaveBase64Btn` - 启用保存为 Base64 按钮
- `EnableSaveJPGBtn` - 启用保存为 JPG 按钮
- `EnableSavePNGBtn` - 启用保存为 PNG 按钮
- `EnableSaveSVGBtn` - 启用保存为 SVG 按钮
- `EnableUndoBtn` - 启用撤消按钮

### 6. 自定义保存按钮文本

自定义保存按钮的文本。

```razor
<SignaturePad OnResult="OnResult" 
           SaveBase64BtnTitle="保存" 
           SaveJPGBtnTitle="保存JPG" 
           SavePNGBtnTitle="保存PNG" 
           SaveSVGBtnTitle="保存SVG" 
           CloseBtnTitle="关闭" />
```

**说明：**
- `SaveBase64BtnTitle` - 保存为 Base64 按钮文本
- `SaveJPGBtnTitle` - 保存为 JPG 按钮文本
- `SavePNGBtnTitle` - 保存为 PNG 按钮文本
- `SaveSVGBtnTitle` - 保存为 SVG 按钮文本
- `CloseBtnTitle` - 关闭按钮文本

### 7. 错误处理和警告回调

通过 `OnError` 和 `OnAlert` 参数处理错误和警告。

```razor
<SignaturePad OnResult="OnResult" 
           OnError="OnError" 
           OnAlert="OnAlert" 
           SignatureAlertText="请先签名" />
```

```csharp
@code {
    private Task OnResult(string base64Data)
    {
        Console.WriteLine($"签名数据: {base64Data}");
        return Task.CompletedTask;
    }
    
    private Task OnError(string error)
    {
        Console.WriteLine($"错误: {error}");
        return Task.CompletedTask;
    }
    
    private Task OnAlert(string alert)
    {
        Console.WriteLine($"警告: {alert}");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `OnError` 参数设置错误回调方法
- `OnAlert` 参数设置手写签名警告信息回调
- `SignatureAlertText` 参数设置"请先签名"提示文本

### 8. 完整示例

包含签名、按钮样式、自定义文本、响应式设计等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>手写签名</CardTitle>
    </CardHeader>
    <CardBody>
        <SignaturePad @ref="signaturePadRef"
                   OnResult="OnResult" 
                   BtnCssClass="btn btn-primary" 
                   BtnSaveCssClass="btn btn-success" 
                   SignAboveLabel="请在下方框内签名" 
                   UndoBtnTitle="撤消" 
                   SaveBase64BtnTitle="保存为Base64" 
                   ChangeColorBtnTitle="换颜色" 
                   ClearBtnTitle="清除" 
                   CloseBtnTitle="关闭"
                   EnableChangeColorBtn="true" 
                   EnableSaveBase64Btn="true" 
                   EnableUndoBtn="true" 
                   Responsive="true" 
                   BackgroundColor="#FFFFFF" 
                   OnError="OnError" 
                   OnAlert="OnAlert" 
                   SignatureAlertText="请先完成签名" />
    </CardBody>
</Card>

@code {
    private SignaturePad signaturePadRef;
    
    private Task OnResult(string base64Data)
    {
        // 保存签名数据
        Console.WriteLine($"签名数据长度: {base64Data?.Length ?? 0}");
        // 可以将 base64Data 保存到数据库或转换为图像文件
        return Task.CompletedTask;
    }
    
    private Task OnError(string error)
    {
        Console.WriteLine($"签名错误: {error}");
        return Task.CompletedTask;
    }
    
    private Task OnAlert(string alert)
    {
        Console.WriteLine($"签名警告: {alert}");
        return Task.CompletedTask;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `OnResult` | 手写签名结果回调 | `Func<string, Task>` | - |
| `BackgroundColor` | 组件背景颜色 | `string` | - |
| `BtnCssClass` | 按钮 CSS 样式 | `string` | - |
| `BtnSaveCssClass` | 按钮"保存"的 CSS 样式 | `string` | - |
| `ChangeColorBtnTitle` | 换颜色按钮文本 | `string` | - |
| `ClearBtnTitle` | 清除按钮文本 | `string` | - |
| `CloseBtnTitle` | 关闭按钮文本 | `string` | - |
| `EnableAlertJS` | 启用 JS 错误弹窗 | `bool` | - |
| `EnableChangeColorBtn` | 启用换颜色按钮 | `bool` | - |
| `EnableSaveBase64Btn` | 启用保存为 Base64 按钮 | `bool` | - |
| `EnableSaveJPGBtn` | 启用保存为 JPG 按钮 | `bool` | - |
| `EnableSavePNGBtn` | 启用保存为 PNG 按钮 | `bool` | - |
| `EnableSaveSVGBtn` | 启用保存为 SVG 按钮 | `bool` | - |
| `EnableUndoBtn` | 启用撤消按钮 | `bool` | - |
| `OnAlert` | 手写签名警告信息回调 | `Func<string, Task>` | - |
| `OnClose` | 手写签名关闭信息回调 | `Func<Task>` | - |
| `OnError` | 获得/设置 错误回调方法 | `Func<string, Task>` | - |
| `Responsive` | 启用响应式 CSS 界面 | `bool` | - |
| `SaveBase64BtnTitle` | 保存为 Base64 按钮文本 | `string` | - |
| `SaveJPGBtnTitle` | 保存为 JPG 按钮文本 | `string` | - |
| `SavePNGBtnTitle` | 保存为 PNG 按钮文本 | `string` | - |
| `SaveSVGBtnTitle` | 保存为 SVG 按钮文本 | `string` | - |
| `SignAboveLabel` | 在框内签名标签文本 | `string` | - |
| `SignatureAlertText` | 请先签名提示文本 | `string` | - |
| `UndoBtnTitle` | 撤消按钮文本 | `string` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 最佳实践

1. **数据大小**：复杂签名会导致传输数据量大，建议配置 `MaximumReceiveMessageSize` 为 `null` 解决 SSR 断流问题
2. **响应式设计**：启用 `Responsive="true"` 提供更好的移动端体验
3. **按钮控制**：根据需求启用/禁用功能按钮，简化用户界面
4. **错误处理**：使用 `OnError` 和 `OnAlert` 回调处理错误和警告情况
5. **背景颜色**：根据界面设计设置 `BackgroundColor`，可以使用透明背景

## 常见问题

**Q: 如何解决 SSR 断流错误？**
A: 配置更改单个传入集线器消息的最大大小：`builder.Services.AddServerSideBlazor().AddHubOptions(o => o.MaximumReceiveMessageSize = null);`

**Q: 如何获取签名数据？**
A: 通过 `OnResult` 回调方法的参数获取 Base64 编码的签名图像数据。

**Q: 如何保存签名为图像文件？**
A: 将 `OnResult` 回调中的 Base64 数据转换为字节数组，然后保存为图像文件（JPG、PNG 等）。

**Q: 如何自定义按钮样式？**
A: 使用 `BtnCssClass` 和 `BtnSaveCssClass` 参数设置按钮的 CSS 样式类。

**Q: 响应式设计如何工作？**
A: 当设备宽度小于 640px 时自动置顶无边框，宽度小于 500px 时按钮自动旋转。

**Q: 如何禁用某些功能按钮？**
A: 使用 `EnableChangeColorBtn`、`EnableSaveBase64Btn`、`EnableUndoBtn` 等参数控制按钮显示。

## 版本历史

- **10.0.0**: 初始版本，支持手写签名、按钮样式、自定义文本、响应式设计、多种保存格式等功能
