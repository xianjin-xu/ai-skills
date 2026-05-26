# QueryBuilder 条件生成器

## 组件概述

QueryBuilder 是一个条件生成器组件，可用于表单、表格过滤条件生成。通过在 Razor 文件中直接通过 `QueryGroup` 和 `QueryColumn` 构建过滤条件。

## 使用场景

### 1. 基础用法

在 Razor 文件中直接通过 `QueryGroup` 和 `QueryColumn` 构建过滤条件。

```razor
<QueryBuilder TModel="Foo" @bind-Value="_filter">
    <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>
    <QueryGroup Logic="@FilterLogic.Or">
        <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains"></QueryColumn>
        <QueryColumn @bind-Field="@context.Education" Operator="@FilterAction.Equal"></QueryColumn>
    </QueryGroup>
    <QueryColumn @bind-Field="@context.Complete" Operator="@FilterAction.Equal"></QueryColumn>
    <QueryColumn @bind-Field="@context.DateTime" Operator="@FilterAction.GreaterThanOrEqual"></QueryColumn>
</QueryBuilder>
```

```csharp
@code {
    private FilterKeyValueAction _filter;
    
    public class Foo
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string Education { get; set; }
        public bool Complete { get; set; }
        public DateTime DateTime { get; set; }
    }
}
```

**说明：**
- `TModel` 参数指定数据模型类型
- `Value` 参数绑定过滤模型实例
- `QueryColumn` 定义单个过滤条件
- `QueryGroup` 定义条件组，可以嵌套
- `FilterAction` 枚举指定过滤操作（Equal、Contains、GreaterThanOrEqual 等）

### 2. 嵌套条件

通过嵌套 `QueryGroup` 构建复杂的过滤条件。

```razor
<QueryBuilder TModel="Foo" @bind-Value="_filter">
    <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>
    
    <QueryGroup Logic="@FilterLogic.Or">
        <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains"></QueryColumn>
        <QueryColumn @bind-Field="@context.Education" Operator="@FilterAction.Equal"></QueryColumn>
        
        <QueryGroup Logic="@FilterLogic.And">
            <QueryColumn @bind-Field="@context.DateTime" Operator="@FilterAction.GreaterThanOrEqual"></QueryColumn>
            <QueryColumn @bind-Field="@context.Complete" Operator="@FilterAction.Equal"></QueryColumn>
        </QueryGroup>
    </QueryGroup>
</QueryBuilder>
```

**说明：**
- 支持多层嵌套的 `QueryGroup`
- 每个 `QueryGroup` 可以指定逻辑运算符（`And` 或 `Or`）
- 嵌套条件可以构建复杂的过滤逻辑

### 3. 显示/隐藏控制按钮

通过设置 `ShowHeader="false"` 关闭控制按钮。

```razor
<QueryBuilder TModel="Foo" @bind-Value="_filter" ShowHeader="false">
    <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>
    <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains"></QueryColumn>
</QueryBuilder>
```

**说明：**
- `ShowHeader` 参数控制是否显示 Header 区域（包含控制按钮）
- 设置为 `false` 时隐藏控制按钮，用户无法动态添加/删除条件
- 适用于只需要静态过滤条件的场景

### 4. 自定义 Header 模板

通过 `HeaderTemplate` 参数自定义 Header 区域的内容。

```razor
<QueryBuilder TModel="Foo" @bind-Value="_filter">
    <HeaderTemplate>
        <div class="d-flex justify-content-between align-items-center">
            <span>过滤条件</span>
            <Button Size="Size.Small" OnClick="ApplyFilter">应用过滤</Button>
        </div>
    </HeaderTemplate>
    <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>
</QueryBuilder>
```

**说明：**
- `HeaderTemplate` 参数类型为 `RenderFragment<FilterKeyValueAction>`
- 可以自定义 Header 区域的内容和布局
- 适用于需要添加自定义按钮或信息的场景

### 5. 自定义按钮图标

通过 `PlusIcon`、`RemoveIcon`、`MinusIcon` 参数自定义按钮图标。

```razor
<QueryBuilder TModel="Foo" 
           @bind-Value="_filter" 
           PlusIcon="fa fa-plus-circle" 
           RemoveIcon="fa fa-trash" 
           MinusIcon="fa fa-minus-circle">
    <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>
</QueryBuilder>
```

**说明：**
- `PlusIcon` 参数设置增加过滤条件按钮的图标
- `RemoveIcon` 参数设置移除过滤条件按钮的图标
- `MinusIcon` 参数设置减少过滤条件按钮的图标
- 图标使用 FontAwesome 图标类名

### 6. 自定义文本

通过 `GroupText` 和 `ItemText` 参数自定义显示文本。

```razor
<QueryBuilder TModel="Foo" 
           @bind-Value="_filter" 
           GroupText="条件组" 
           ItemText="过滤项">
    <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal"></QueryColumn>
</QueryBuilder>
```

**说明：**
- `GroupText` 参数设置组合过滤条件文本（默认显示"并且"/"或者"）
- `ItemText` 参数设置过滤条件文本
- 可以根据业务需求自定义显示文本

### 7. 完整示例

包含条件生成、嵌套条件、自定义模板等完整功能。

```razor
<Card>
    <CardHeader>
        <CardTitle>高级过滤</CardTitle>
    </CardHeader>
    <CardBody>
        <QueryBuilder TModel="Foo" 
                   @bind-Value="_filter" 
                   ShowHeader="true" 
                   GroupText="条件组" 
                   ItemText="过滤项">
            <HeaderTemplate>
                <div class="d-flex justify-content-between align-items-center">
                    <span>过滤条件</span>
                    <div>
                        <Button Size="Size.Small" Color="Color.Primary" OnClick="ApplyFilter">应用过滤</Button>
                        <Button Size="Size.Small" Color="Color.Secondary" OnClick="ResetFilter">重置</Button>
                    </div>
                </div>
            </HeaderTemplate>
            
            <QueryColumn @bind-Field="@context.Name" Operator="@FilterAction.Equal" PlaceHolder="输入姓名"></QueryColumn>
            
            <QueryGroup Logic="@FilterLogic.Or">
                <QueryColumn @bind-Field="@context.Address" Operator="@FilterAction.Contains" PlaceHolder="输入地址关键词"></QueryColumn>
                <QueryColumn @bind-Field="@context.Education" Operator="@FilterAction.Equal" PlaceHolder="选择学历"></QueryColumn>
                
                <QueryGroup Logic="@FilterLogic.And">
                    <QueryColumn @bind-Field="@context.DateTime" Operator="@FilterAction.GreaterThanOrEqual" PlaceHolder="起始日期"></QueryColumn>
                    <QueryColumn @bind-Field="@context.Complete" Operator="@FilterAction.Equal" PlaceHolder="完成状态"></QueryColumn>
                </QueryGroup>
            </QueryGroup>
        </QueryBuilder>
    </CardBody>
</Card>

@code {
    private FilterKeyValueAction _filter;
    
    private Task ApplyFilter()
    {
        // 应用过滤逻辑
        Console.WriteLine($"过滤条件: {JsonSerializer.Serialize(_filter)}");
        return Task.CompletedTask;
    }
    
    private Task ResetFilter()
    {
        _filter = new FilterKeyValueAction();
        return Task.CompletedTask;
    }
    
    public class Foo
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string Education { get; set; }
        public bool Complete { get; set; }
        public DateTime DateTime { get; set; }
    }
}
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Value` | 获得/设置 过滤模型 `FilterKeyValueAction` 实例值 | `FilterKeyValueAction` | - |
| `Logic` | 获得/设置 逻辑运算符 | `FilterLogic` | - |
| `ChildContent` | 获得/设置 模板 | `RenderFragment<TModel>` | - |
| `ShowHeader` | 获得/设置 是否显示 Header 区域 | `bool` | `true` |
| `HeaderTemplate` | 获得/设置 Header 模板 | `RenderFragment<FilterKeyValueAction>` | `null` |
| `PlusIcon` | 获得/设置 增加过滤条件图标 | `string` | - |
| `RemoveIcon` | 获得/设置 移除过滤条件图标 | `string` | - |
| `MinusIcon` | 获得/设置 减少过滤条件图标 | `string` | - |
| `GroupText` | 获得/设置 组合过滤条件文本 | `string` | - |
| `ItemText` | 获得/设置 过滤条件文本 | `string` | - |
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## 事件回调

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ValueChanged` | `EventCallback<FilterKeyValueAction>` | 获得/设置 Filter 回调方法，支持双向绑定 |

## FilterLogic 枚举

| 值 | 说明 |
|-----|------|
| `And` | 逻辑与（所有条件都必须满足） |
| `Or` | 逻辑或（满足任意一个条件即可） |

## FilterAction 枚举

| 值 | 说明 |
|-----|------|
| `Equal` | 等于 |
| `NotEqual` | 不等于 |
| `LessThan` | 小于 |
| `LessThanOrEqual` | 小于等于 |
| `GreaterThan` | 大于 |
| `GreaterThanOrEqual` | 大于等于 |
| `Contains` | 包含 |
| `NotContains` | 不包含 |
| `StartsWith` | 以...开始 |
| `EndsWith` | 以...结束 |
| `IsNull` | 为空 |
| `IsNotNull` | 不为空 |

## 子组件

### QueryColumn

`QueryColumn` 用于定义单个过滤条件。

**参数：**
- `Field` - 绑定的字段
- `Operator` - 过滤操作（`FilterAction` 枚举）
- `Value` - 过滤值
- `PlaceHolder` - 占位符文本

### QueryGroup

`QueryGroup` 用于定义条件组，可以嵌套。

**参数：**
- `Logic` - 逻辑运算符（`FilterLogic.And` 或 `FilterLogic.Or`）

## 最佳实践

1. **模型类型**：确保 `TModel` 指定的模型类型与数据源一致
2. **条件嵌套**：合理设计条件嵌套结构，避免过于复杂的逻辑
3. **用户体验**：对于简单场景，设置 `ShowHeader="false"` 隐藏控制按钮
4. **自定义模板**：使用 `HeaderTemplate` 添加应用、重置等按钮
5. **过滤操作**：根据字段类型选择合适的 `FilterAction`，如字符串使用 `Contains`，数值使用 `GreaterThanOrEqual`

## 常见问题

**Q: 如何获取过滤条件的值？**
A: 通过 `Value` 参数绑定的 `FilterKeyValueAction` 对象获取过滤条件。

**Q: 如何动态添加过滤条件？**
A: 当 `ShowHeader="true"` 时，用户可以通过界面上的按钮动态添加/删除条件。

**Q: 如何自定义过滤条件的界面？**
A: 通过 `QueryColumn` 的 `Field`、`Operator`、`Value` 等参数自定义每个过滤条件的界面。

**Q: 如何应用过滤条件到数据？**
A: 在 `ValueChanged` 回调或自定义按钮点击事件中，使用 `_filter` 对象构建查询条件并应用到数据源。

**Q: 支持哪些过滤操作？**
A: 支持等于、不等于、小于、大于、包含、不包含、以...开始、以...结束、为空、不为空等操作。

## 版本历史

- **初始版本**: 支持条件生成、嵌套条件、显示控制、自定义模板、自定义图标、自定义文本等功能
