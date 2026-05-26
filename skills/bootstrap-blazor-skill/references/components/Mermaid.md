# Mermaid 构图工具

## 组件概述

Mermaid 组件可渲染 Markdown 启发的文本定义以动态创建和修改图表。本组件依赖于 `BootstrapBlazor.Mermaid`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.Mermaid
```

或

```xml
<PackageReference Include="BootstrapBlazor.Mermaid" Version="10.0.1" />
```

## 使用场景

### 1. 基本用法

Mermaid 基本样式，支持多种图表类型。

```razor
<Mermaid DiagramString="@diagramString" />
```

```csharp
@code {
    private string diagramString = @"
graph TD
    A[开始] --> B{判断条件}
    B -->|是| C[执行操作1]
    B -->|否| D[执行操作2]
    C --> E[结束]
    D --> E
";
}
```

### 2. 流程图（Flowchart）

创建流程图展示业务流程。

```razor
<Mermaid DiagramString="@flowchartString" Type="MermaidType.Flowchart" />
```

```csharp
@code {
    private string flowchartString = @"
graph LR
    A[Hard] -->|Text| B(Round)
    B --> C{Decision}
    C -->|One| D[Result 1]
    C -->|Two| E[Result 2]
";
}
```

**流程图方向：**
- `TB` - 从上到下
- `TD` - 从上到下（同 TB）
- `BT` - 从下到上
- `RL` - 从右到左
- `LR` - 从左到右

### 3. 时序图（Sequence Diagram）

展示系统之间的交互顺序。

```razor
<Mermaid DiagramString="@sequenceString" Type="MermaidType.Sequence" />
```

```csharp
@code {
    private string sequenceString = @"
sequenceDiagram
    Alice->>Bob: Hello Bob!
    Bob->>Alice: Hi Alice!
    Alice->>Bob: How are you?
    Bob->>Alice: I'm fine, thanks!
";
}
```

### 4. 甘特图（Gantt）

展示项目时间安排。

```razor
<Mermaid DiagramString="@ganttString" Type="MermaidType.Gantt" Title="项目计划" />
```

```csharp
@code {
    private string ganttString = @"
gantt
    title 项目开发计划
    dateFormat  YYYY-MM-DD
    section 设计阶段
    需求分析    :a1, 2024-01-01, 10d
    原型设计    :a2, after a1, 15d
    section 开发阶段
    前端开发    :b1, after a2, 30d
    后端开发    :b2, after a2, 30d
    section 测试阶段
    集成测试    :c1, after b1, 15d
    用户测试    :c2, after c1, 10d
";
}
```

### 5. 类图（Class Diagram）

展示类之间的关系。

```razor
<Mermaid DiagramString="@classString" Type="MermaidType.Class" />
```

```csharp
@code {
    private string classString = @"
classDiagram
    class Animal {
        +string name
        +int age
        +makeSound()
    }
    class Dog {
        +string breed
        +fetch()
    }
    class Cat {
        +string color
        +purr()
    }
    Animal <|-- Dog
    Animal <|-- Cat
";
}
```

### 6. 状态图（State Diagram）

展示对象状态变化。

```razor
<Mermaid DiagramString="@stateString" Type="MermaidType.State" />
```

```csharp
@code {
    private string stateString = @"
stateDiagram-v2
    [*] --> Still
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
";
}
```

### 7. 饼图（Pie Chart）

展示数据占比。

```razor
<Mermaid DiagramString="@pieString" Type="MermaidType.Pie" Title="销售占比" />
```

```csharp
@code {
    private string pieString = @"
pie title 产品销售占比
    ""产品A"" : 386
    ""产品B"" : 285
    ""产品C"" : 150
    ""产品D"" : 79
";
}
```

### 8. 增加自定义样式

通过 `MermaidStyleIntro` 为图表元素添加自定义样式。

```razor
<Mermaid DiagramString="@styledString" />
```

```csharp
@code {
    private string styledString = @"
graph TD
    A[开始] --> B{判断}
    B -->|是| C[操作1]
    B -->|否| D[操作2]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#dfd,stroke:#333,stroke-width:2px
    style D fill:#dfd,stroke:#333,stroke-width:2px
";
}
```

### 9. 下载 Pdf

Mermaid 图表支持导出为 Pdf 文档。

```razor
<Mermaid DiagramString="@diagramString" @ref="mermaidRef" />

<Button OnClick="DownloadPdf">下载 Pdf</Button>

@code {
    private Mermaid mermaidRef;
    private string diagramString = @"
graph TD
    A[开始] --> B[结束]
";
    
    private async Task DownloadPdf()
    {
        await mermaidRef.DownloadPdf();
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `DiagramString` | 设置 Mermaid 字串 | `string` | - |
| `Direction` | 获取/设置 图方向 | `Nullable<MermaidDirection>` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `Title` | 获取/设置 图标题 | `string` | `null` |
| `Type` | 获取/设置 图类型 | `MermaidType` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 图表类型枚举

**MermaidType 枚举值：**
- `Flowchart` - 流程图
- `Sequence` - 时序图
- `Gantt` - 甘特图
- `Class` - 类图
- `State` - 状态图
- `Pie` - 饼图
- `ER` - 实体关系图
- `Journey` - 用户旅程图
- `GitGraph` - Git 分支图

**MermaidDirection 枚举值：**
- `TB` - 从上到下
- `TD` - 从上到下
- `BT` - 从下到上
- `RL` - 从右到左
- `LR` - 从左到右

## 最佳实践

1. **语法正确**：确保 Mermaid 语法正确，避免拼写错误
2. **图表类型**：根据数据特点选择合适的图表类型
3. **标题设置**：为甘特图、饼图、时序图设置标题提高可读性
4. **样式优化**：使用自定义样式美化图表外观
5. **方向控制**：根据布局空间选择合适的图表方向

## 常见问题

**Q: Mermaid 支持哪些图表类型？**
A: 支持流程图、时序图、甘特图、类图、状态图、饼图、实体关系图、用户旅程图、Git 分支图等。

**Q: 如何为图表添加标题？**
A: 使用 `Title` 参数设置图表标题，适用于甘特图、饼图、时序图等。

**Q: 如何控制流程图的方向？**
A: 使用 `Direction` 参数设置图表方向，如 `MermaidDirection.LR` 表示从左到右。

**Q: 如何导出 Mermaid 图表？**
A: 使用组件实例的 `DownloadPdf()` 方法可以将图表导出为 Pdf 文档。

## 版本历史

- **10.0.1**: 初始版本，支持多种图表类型、标题设置、方向控制、Pdf 导出功能
