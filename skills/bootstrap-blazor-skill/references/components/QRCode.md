# QRCode 二维码

## 组件概述

QRCode 组件用于二维码生成。本组件依赖于 `BootstrapBlazor.BarCode`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.BarCode
```

或

```xml
<PackageReference Include="BootstrapBlazor.BarCode" Version="10.0.0" />
```

## 使用场景

### 1. 基础用法

点击生成按钮，生成特定的 QRCode。

```razor
<QRCode Content="https://www.example.com" />
```

**说明：**
- `Content` 参数指定二维码内容信息
- 用户需要在输入框中输入内容，然后点击"生成"按钮生成二维码
- 默认显示"清除"和"生成"两个按钮

### 2. 直接生成

通过 `Content` 参数指定二维码内容，页面加载时直接生成二维码。

```razor
<QRCode Content="https://www.example.com" ShowButtons="false" />
```

**说明：**
- `Content` 参数设置为二维码内容（如 URL、文本等）
- `ShowButtons="false"` 隐藏生成和清除按钮
- 页面加载时自动生成二维码，无需用户点击

### 3. 设置二维码大小

通过 `Width` 参数指定二维码宽度，高度与宽度一致。

```razor
<QRCode Content="https://www.example.com" Width="256" />
```

**说明：**
- `Width` 参数设置二维码宽度（像素），高度与宽度一致
- 最小值为 40，默认值为 128
- 建议根据显示需求设置合适的大小

### 4. 设置二维码颜色

通过 `DarkColor` 参数指定二维码黑色部分颜色，`LightColor` 参数指定二维码白色部分颜色。

```razor
<QRCode Content="https://www.example.com" 
           DarkColor="#000000" 
           LightColor="#FFFFFF" />
```

**说明：**
- `DarkColor` 参数设置二维码黑色区域颜色，默认值为 `#000000`
- `LightColor` 参数设置二维码白色区域颜色，默认值为 `#FFFFFF`
- 可以使用颜色名称、十六进制颜色码或 RGB 值

### 5. 自定义按钮文本和图标

通过 `GenerateButtonText`、`ClearButtonText`、`GenerateButtonIcon`、`ClearButtonIcon` 参数自定义按钮。

```razor
<QRCode Content="https://www.example.com" 
           GenerateButtonText="生成二维码" 
           ClearButtonText="清空" 
           GenerateButtonIcon="fa fa-qrcode" 
           ClearButtonIcon="fa fa-eraser" />
```

**说明：**
- `GenerateButtonText` 参数设置生成按钮文字
- `ClearButtonText` 参数设置清除按钮文字
- `GenerateButtonIcon` 参数设置生成按钮图标（FontAwesome 图标类名）
- `ClearButtonIcon` 参数设置清除按钮图标（FontAwesome 图标类名）

### 6. 显示/隐藏按钮

通过 `ShowButtons` 参数控制是否显示工具按钮。

```razor
<QRCode Content="https://www.example.com" ShowButtons="false" />
```

**说明：**
- `ShowButtons` 参数类型为 `bool`，默认值为 `false`
- 设置为 `false` 时隐藏生成和清除按钮
- 适用于只需要显示二维码、不需要用户交互的场景

### 7. 二维码生成/清除回调

通过 `OnGenerated` 和 `OnCleared` 参数处理二维码生成和清除事件。

```razor
<QRCode Content="https://www.example.com" 
           OnGenerated="OnQrCodeGenerated" 
           OnCleared="OnQrCodeCleared" />
```

```csharp
@code {
    private Task OnQrCodeGenerated()
    {
        Console.WriteLine("二维码已生成");
        return Task.CompletedTask;
    }
    
    private Task OnQrCodeCleared()
    {
        Console.WriteLine("二维码已清除");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `OnGenerated` 参数类型为 `Func<Task>`，二维码生成后回调
- `OnCleared` 参数类型为 `Func<Task>`，二维码清除后回调
- 可以在回调中执行后续操作，如记录日志、更新状态等

### 8. 完整示例

包含二维码生成、大小设置、颜色自定义、按钮控制等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>二维码生成器</CardTitle>
    </CardHeader>
    <CardBody>
        <div class="row g-3">
            <div class="col-12">
                <div class="form-inline">
                    <Label>二维码内容:</Label>
                    <Input @bind-Value="qrContent" PlaceHolder="输入网址或文本" />
                </div>
            </div>
            <div class="col-12">
                <div class="form-inline">
                    <Label>二维码大小:</Label>
                    <InputNumber @bind-Value="qrWidth" Min="40" Max="512" />
                </div>
            </div>
            <div class="col-12">
                <div class="form-inline">
                    <Label>前景色:</Label>
                    <Input Type="InputType.Color" @bind-Value="darkColor" />
                    <Label>背景色:</Label>
                    <Input Type="InputType.Color" @bind-Value="lightColor" />
                </div>
            </div>
            <div class="col-12">
                <QRCode Content="@qrContent" 
                       Width="@qrWidth" 
                       DarkColor="@darkColor" 
                       LightColor="@lightColor" 
                       ShowButtons="true" 
                       GenerateButtonText="生成二维码" 
                       ClearButtonText="清空" 
                       OnGenerated="OnGenerated" 
                       OnCleared="OnCleared" />
            </div>
        </div>
    </CardBody>
</Card>

@code {
    private string qrContent = "https://www.example.com";
    private int qrWidth = 128;
    private string darkColor = "#000000";
    private string lightColor = "#FFFFFF";
    
    private Task OnGenerated()
    {
        Console.WriteLine("二维码已生成");
        return Task.CompletedTask;
    }
    
    private Task OnCleared()
    {
        Console.WriteLine("二维码已清除");
        return Task.CompletedTask;
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Content` | 获得/设置 二维码内容信息 | `string` | - |
| `Width` | 获得/设置 二维码内容宽度（高度与宽度一致，最小值为 40） | `int` | `128` |
| `DarkColor` | 获得/设置 二维码黑色区域颜色 | `string` | `#000000` |
| `LightColor` | 获得/设置 二维码白色区域颜色 | `string` | `#ffffff` |
| `ShowButtons` | 获得/设置 是否显示工具按钮 | `bool` | `false` |
| `GenerateButtonText` | 获得/设置 生成按钮文字 | `string` | - |
| `ClearButtonText` | 获得/设置 清除按钮文字 | `string` | - |
| `GenerateButtonIcon` | 获得/设置 生成按钮图标 | `string` | - |
| `ClearButtonIcon` | 获得/设置 清除按钮图标 | `string` | - |
| `PlaceHolder` | 获得/设置 PlaceHolder 文字 | `string` | - |
| `OnGenerated` | 获得/设置 二维码生成后回调委托 | `Func<Task>` | - |
| `OnCleared` | 获得/设置 二维码清除后回调委托 | `Func<Task>` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 最佳实践

1. **内容选择**：二维码内容可以是 URL、文本、联系方式等，根据使用场景选择合适的内容
2. **大小设置**：根据显示需求设置 `Width` 参数，过小可能难以扫描，过大可能影响页面布局
3. **颜色搭配**：确保前景色和背景色对比度足够，避免扫描困难
4. **按钮控制**：对于只需要显示二维码的场景，设置 `ShowButtons="false"` 隐藏按钮
5. **回调函数**：使用 `OnGenerated` 和 `OnCleared` 回调处理生成和清除事件

## 常见问题

**Q: 如何生成包含 URL 的二维码？**
A: 设置 `Content` 参数为完整的 URL 地址，如 `Content="https://www.example.com"`。

**Q: 如何自定义二维码大小？**
A: 使用 `Width` 参数设置，如 `Width="256"` 表示 256x256 像素。

**Q: 如何修改二维码颜色？**
A: 使用 `DarkColor` 和 `LightColor` 参数设置，如 `DarkColor="#FF0000"` 表示红色前景。

**Q: 如何隐藏生成和清除按钮？**
A: 设置 `ShowButtons="false"` 可以隐藏按钮。

**Q: 如何获取二维码生成状态？**
A: 使用 `OnGenerated` 回调方法，二维码生成成功后会自动调用此方法。

**Q: 二维码生成失败怎么办？**
A: 检查 `Content` 参数是否为空，内容是否过长（某些二维码标准有长度限制）。

## 版本历史

- **10.0.0**: 初始版本，支持二维码生成、大小设置、颜色自定义、按钮控制、生成/清除回调等功能
