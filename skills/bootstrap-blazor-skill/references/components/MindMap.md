# MindMap 思维导图

## 组件概述

MindMap 组件用于将特定 Json 格式数据展示成 Web 思维导图。本组件依赖于 `BootstrapBlazor.MindMap`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.MindMap
```

或

```xml
<PackageReference Include="BootstrapBlazor.MindMap" Version="10.0.0" />
```

## 使用场景

### 1. 基本用法

用于将特定 Json 格式数据展示成 Web 思维导图。

```razor
<MindMap Data="@jsonData" />
```

```csharp
@code {
    private string jsonData = @"{
        ""data": {
            ""text": ""根节点""
        },
        ""children": [
            {
                ""data": { ""text": ""二级节点"" },
                ""children": [
                    { ""data": { ""text": ""三级节点1"" } },
                    { ""data": { ""text": ""三级节点2"" } }
                ]
            }
        ]
    }";
}
```

### 2. 设置布局类型

通过 `Layout` 参数设置思维导图的布局类型。

```razor
<MindMap Data="@jsonData" Layout="EnumMindMapLayout.LogicalStructure" />
```

**可用的布局类型：**
- `LogicalStructure` - 逻辑结构图（默认）
- `CatalogOrganization` - 目录组织图
- `OrganizationStructure` - 组织结构图
- `MindMap` - 思维导图
- `Timeline` - 时间线

### 3. 设置主题

通过 `Theme` 参数设置思维导图的显示主题。

```razor
<MindMap Data="@jsonData" Theme="EnumMindMapTheme.DefaultTheme" />
```

**可用的主题：**
- `DefaultTheme` - 默认主题
- `ClassicTheme` - 经典主题
- `FreshTheme` - 清新主题
- `SkyblueTheme` - 天蓝主题
- `WarmTheme` - 温暖主题

### 4. 导出 PNG 图片

MindMap 组件支持将思维导图导出为 PNG 图片。

```razor
<MindMap Data="@jsonData" @ref="mindMapRef" />

<Button OnClick="ExportPng">导出 PNG</Button>

@code {
    private MindMap mindMapRef;
    
    private async Task ExportPng()
    {
        await mindMapRef.Execute("exportPng");
    }
}
```

### 5. 导出 Json 数据

导出当前思维导图的 Json 数据。

```razor
<MindMap Data="@jsonData" @ref="mindMapRef" />

<Button OnClick="ExportJson">导出 Json</Button>

@code {
    private MindMap mindMapRef;
    
    private async Task ExportJson()
    {
        var json = await mindMapRef.Execute("exportJson");
        // 处理导出的 json 数据
    }
}
```

### 6. 自定义按钮和扩展方法

由于 MindMap 封装的 API 方法比较多，组件库无法完全封装，所以提供了扩展方法。可以通过自己的代码调用自己的 Javascript 来控制 MindMap。

**Razor 代码：**

```razor
<MindMap Data="@jsonData" @ref="mindMapRef" />

<Button OnClick="CallCustomMethod">调用自定义方法</Button>

@code {
    private MindMap mindMapRef;
    
    private async Task CallCustomMethod()
    {
        await mindMapRef.Execute("clickCustom", "args1");
    }
}
```

**Javascript 代码：**

```javascript
window.BootstrapBlazor.MindMap = {
    callbacks: {
        clickCustom: function (args) {
            console.log(this, args);
            // this 即为 MindMap 当前实例，可以调用其任意方法进行自己业务开发
        }
    }
}
```

### 7. 缩小和放大

通过组件实例方法控制思维导图的缩放。

```razor
<MindMap Data="@jsonData" @ref="mindMapRef" />

<Button OnClick="ZoomIn">放大</Button>
<Button OnClick="ZoomOut">缩小</Button>
<Button OnClick="Reset">复位</Button>
<Button OnClick="Fit">自适应</Button>

@code {
    private MindMap mindMapRef;
    
    private async Task ZoomIn() => await mindMapRef.Execute("zoomIn");
    private async Task ZoomOut() => await mindMapRef.Execute("zoomOut");
    private async Task Reset() => await mindMapRef.Execute("reset");
    private async Task Fit() => await mindMapRef.Execute("fit");
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Data` | 获得/设置 初始数据 | `string` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `Layout` | 获得/设置 组件布局类型 | `EnumMindMapLayout` | `LogicalStructure` |
| `Theme` | 获得/设置 组件主题 | `EnumMindMapTheme` | `DefaultTheme` |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 最佳实践

1. **数据格式**：确保 `Data` 参数的 Json 格式正确，包含 `data` 和 `children` 结构
2. **布局选择**：根据数据特点选择合适的布局类型，思维导图适合展示层级关系
3. **主题搭配**：根据页面风格选择合适的主题，保持视觉一致性
4. **扩展方法**：对于复杂的自定义操作，使用 `Execute` 方法调用 Javascript API
5. **性能优化**：对于大型思维导图，考虑分页加载或虚拟滚动

## 常见问题

**Q: 如何获取思维导图的完整数据？**
A: 使用 `Execute("exportJson")` 方法获取当前思维导图的完整 Json 数据。

**Q: 如何自定义思维导图的交互行为？**
A: 通过 `Execute` 方法调用 MindMap 的 Javascript API，并在 `window.BootstrapBlazor.MindMap.callbacks` 中定义回调函数。

**Q: 思维导图支持哪些布局类型？**
A: 支持逻辑结构图、目录组织图、组织结构图、思维导图、时间线等布局类型。

## 版本历史

- **10.0.0**: 初始版本，支持基本思维导图展示、布局切换、主题切换、导出功能
