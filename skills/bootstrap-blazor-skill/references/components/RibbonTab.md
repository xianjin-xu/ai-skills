# RibbonTab 选项卡组件#

## 组件概述#

RibbonTab 是一个选项卡组件，提供类似 Office 菜单的选项卡界面。支持浮动按钮、右侧按钮模板、锚点等功能。

**分类**: 导航  
**在线演示**: [https://www.blazor.zone/ribbon-tab](https://www.blazor.zone/ribbon-tab)

## 使用场景#

### 1. 基础用法 - 浮动按钮#

通过设置 `ShowFloatButton="true"` 使选项卡右侧显示收缩按钮，不占用主窗体空间。

```razor
<RibbonTab Items="@FloatItems" ShowFloatButton="true" OnFloatChanged="OnFloatChanged">
    @Localizer["RibbonTabsFloatContent"]
</RibbonTab>
```

```csharp
@code {
    private IEnumerable<RibbonTabItem> FloatItems { get; set; }
    
    private Task OnFloatChanged(bool isFloat)
    {
        Console.WriteLine($"浮动状态: {isFloat}");
        return Task.CompletedTask;
    }
}
```

**说明：**
- `ShowFloatButton="true"` 显示右侧收缩按钮
- `OnFloatChanged` 浮动状态改变回调
- 收缩后选项卡向上移动，节省空间

### 2. 右侧按钮模板#

通过设置 `RightButtonsTemplate` 可以在选项卡右上角增加一些快捷按钮。

```razor
<RibbonTab Items="@RightItems" ShowFloatButton="true">
    <RightButtonsTemplate>
        <div class="ribbon-button">
            <i class="fa-regular fa-circle-question"></i>
            <span>@Localizer["RibbonTabsRightButtonsTemplateContent"]</span>
        </div>
    </RightButtonsTemplate>
</RibbonTab>
```

**说明：**
- `RightButtonsTemplate` 右侧按钮模板
- 可自定义快捷操作按钮

### 3. Header 点击回调#

通过设置 `OnMenuClickAsync` 回调方法处理点击 Header 部分逻辑。

```razor
<RibbonTab Items="@HeaderItems" OnMenuClickAsync="@OnMenuClickAsync">
    <div class="@FileClassString">@Localizer["RibbonTabsItemsText1"]</div>
    <div class="@EditClassString">@Localizer["RibbonTabsItemsText2"]</div>
</RibbonTab>
```

```csharp
@code {
    private async Task OnMenuClickAsync(RibbonTabItem item)
    {
        Console.WriteLine($"点击 Header: {item.Text}");
        await Task.CompletedTask;
    }
}
```

**说明：**
- `OnMenuClickAsync` Header 点击回调
- 可处理点击选项卡标签的逻辑

### 4. 锚点支持#

通过设置 `IsSupportAnchor="true"` 开启是否支持锚点功能。

```razor
<RibbonTab Items="@AnchorItems" IsSupportAnchor="true" 
           EncodeAnchorCallback="EncodeAnchorCallback" 
           DecodeAnchorCallback="DecodeAnchorCallback">
</RibbonTab>
```

```csharp
@code {
    private string EncodeAnchorCallback(string url, string text)
    {
        // 自定义编码规则
        return $"{url}#{text}";
    }
    
    private string DecodeAnchorCallback(string anchor)
    {
        // 自定义解码规则
        return anchor.Replace("#", "");
    }
}
```

**说明：**
- `IsSupportAnchor="true"` 开启 URL 锚点功能
- `EncodeAnchorCallback` 自定义哈希编码规则
- `DecodeAnchorCallback` 自定义哈希解码规则
- 支持自定义多级哈希，本例中特意使用组合 Hash

### 5. 完整示例#

包含浮动按钮、右侧按钮、Header 点击、锚点等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>RibbonTab 选项卡示例</CardTitle>
    </CardHeader>
    <CardBody>
        <RibbonTab Items="@AllItems" 
                   ShowFloatButton="true" 
                   IsSupportAnchor="true"
                   OnFloatChanged="OnFloatChanged"
                   OnMenuClickAsync="OnMenuClickAsync"
                   EncodeAnchorCallback="EncodeAnchor"
                   DecodeAnchorCallback="DecodeAnchor">
            <RightButtonsTemplate>
                <div class="ribbon-button">
                    <i class="fa fa-cog"></i>
                    <span>设置</span>
                </div>
            </RightButtonsTemplate>
            <ChildContent>
                <div class="ribbon-content">
                    <p>这是选项卡内容区域</p>
                </div>
            </ChildContent>
        </RibbonTab>
    </CardBody>
</Card>

@code {
    private IEnumerable<RibbonTabItem> AllItems { get; set; }
    
    private Task OnFloatChanged(bool isFloat)
    {
        Console.WriteLine($"浮动状态: {isFloat}");
        return Task.CompletedTask;
    }
    
    private async Task OnMenuClickAsync(RibbonTabItem item)
    {
        Console.WriteLine($"点击: {item.Text}");
        await Task.CompletedTask;
    }
    
    private string EncodeAnchor(string url, string text)
    {
        return $"{url}#{Uri.EscapeDataString(text)}";
    }
    
    private string DecodeAnchor(string anchor)
    {
        return Uri.UnescapeDataString(anchor.Replace("#", ""));
    }
}
```

## 组件参数#

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Items` | 获得/设置 数据源 | `IEnumerable<RibbonTabItem>?` | `null` |
| `IsBorder` | 获得/设置 是否为带边框卡片样式 | `bool` | `true` |
| `IsSupportAnchor` | 获得/设置 是否开启 Url 锚点 | `bool` | `false` |
| `ShowFloatButton` | 获得/设置 是否显示悬浮小箭头 | `bool` | `false` |
| `RightButtonsTemplate` | 获得/设置 右侧按钮模板 | `RenderFragment?` | `null` |
| `ChildContent` | 获得/设置 内容模板 | `RenderFragment?` | `null` |
| `RibbonArrowUpIcon` | 获得/设置 选项卡向上箭头图标 | `string?` | - |
| `RibbonArrowDownIcon` | 获得/设置 选项卡向下箭头图标 | `string?` | - |
| `RibbonArrowPinIcon` | 获得/设置 选项卡可固定图标 | `string?` | - |
| `OnFloatChanged` | 获得/设置 组件悬浮状态改变时的回调方法 | `Func<bool, Task>` | `null` |
| `OnMenuClickAsync` | 获得/设置 点击标签 Menu 回调方法 | `Func<RibbonTabItem, Task>` | - |
| `EncodeAnchorCallback` | 获得/设置 编码锚点回调方法 | `Func<string, string, string>` | - |
| `DecodeAnchorCallback` | 获得/设置 解码锚点回调方法 | `Func<string, string>` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## RibbonTabItem 属性#

| 属性 | 说明 | 类型 |
|------|------|------|
| `Text` | 选项卡显示文本 | `string` |
| `Icon` | 选项卡图标 | `string` |
| `Items` | 子项集合 | `List<RibbonTabItem>` |
| `IsDisabled` | 是否禁用 | `bool` |

## 最佳实践#

1. **浮动按钮**: 设置 `ShowFloatButton="true"` 节省主窗体空间
2. **右侧按钮**: 使用 `RightButtonsTemplate` 添加快捷操作
3. **锚点功能**: 设置 `IsSupportAnchor="true"` 支持 URL 锚点导航
4. **Header 回调**: 使用 `OnMenuClickAsync` 处理标签点击
5. **编码解码**: 自定义 `EncodeAnchorCallback` 和 `DecodeAnchorCallback` 实现自定义锚点规则

## 常见问题#

**Q: 如何收缩选项卡？**
A: 设置 `ShowFloatButton="true"`，点击收缩按钮即可。

**Q: 如何添加右侧按钮？**
A: 使用 `RightButtonsTemplate` 模板添加自定义按钮。

**Q: 如何支持锚点导航？**
A: 设置 `IsSupportAnchor="true"`，并实现 `EncodeAnchorCallback` 和 `DecodeAnchorCallback`。

**Q: 如何响应标签点击？**
A: 实现 `OnMenuClickAsync` 回调方法。

**Q: 如何自定义箭头图标？**
A: 设置 `RibbonArrowUpIcon`、`RibbonArrowDownIcon`、`RibbonArrowPinIcon` 属性。

## 版本历史#

- **初始版本**: 支持选项卡、浮动按钮、右侧模板、锚点导航、Header 回调等功能
