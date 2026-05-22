# Row

## 概述

Row 组件

> Row Component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/row](https://www.blazor.zone/row)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ItemsPerRow` | `ItemsPerRow` | `}` | 获得/设置 设置一行显示多少个子组件 |
| `RowType` | `RowType` | `}` | 获得/设置 设置行格式 默认 Row 布局 |
| `ColSpan` | `int?` | `}` | 获得/设置 子 Row 跨父 Row 列数 默认为 null |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |

## 代码示例

### 基本用法

```razor
<Row ItemsPerRow="ItemsPerRow.Three">
        <Card>
            <BodyTemplate>
                <h5 class="card-title">Card 1</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </BodyTemplate>
        </Card>
        <Card>
            <BodyTemplate>
                <h5 class="card-title">Card 2</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </BodyTemplate>
        </Card>
        <Card>
            <BodyTemplate>
                <h5 class="card-title">Card 3</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </BodyTemplate>
        </Card>
        <Card>
            <BodyTemplate>
                <h5 class="card-title">Card 1</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </BodyTemplate>
        </Card>
        <Card>
            <BodyTemplate>
                <h5 class="card-title">Card 2</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </BodyTemplate>
        </Card>
        <Card>
            <BodyTemplate>
                <h5 class="card-title">Card 3</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </BodyTemplate>
        </Card>
    </Row>
```

### 基本用法

```razor
<Row ItemsPerRow="ItemsPerRow.Two" RowType="RowType.Inline">
            <CheckboxList @bind-Value="@Model.Hobby" Items="Hobbies1" />
            <BootstrapInput @bind-Value="@Model.Address" />
            <DateTimePicker @bind-Value="@Model.DateTime" />
            <BootstrapInputNumber @bind-Value="@Model.Count" />
            <Switch @bind-Value="@Model.Complete" />
            <Select @bind-Value="@Model.Education" />
        </Row>
```

### 基本用法

```razor
<Row ItemsPerRow="ItemsPerRow.Three">
            <CheckboxList @bind-Value="@RowFormModel.Hobby" Items="Hobbies2" />
            <BootstrapInput @bind-Value="@RowFormModel.Address" />
            <DateTimePicker @bind-Value="@RowFormModel.DateTime" />
            <BootstrapInputNumber @bind-Value="@RowFormModel.Count" />
            <Switch @bind-Value="@RowFormModel.Complete" />
            <Select @bind-Value="@RowFormModel.Education" />
        </Row>
```

### 基本用法

```razor
<Row ItemsPerRow="ItemsPerRow.Two">
            <BootstrapInput @bind-Value="@NestedModel.Name" />
            <Row ItemsPerRow="ItemsPerRow.Two">
                <Switch @bind-Value="@NestedModel.Complete" />
                <BootstrapInput @bind-Value="@NestedModel.Address" />
            </Row>
<Row>
            <Row ItemsPerRow="ItemsPerRow.Two">
                <BootstrapInput @bind-Value="@NestedModel.Name" />
                <BootstrapInput @bind-Value="@NestedModel.Address" />
            </Row>
<Row ItemsPerRow="ItemsPerRow.Three">
                <BootstrapInput @bind-Value="@NestedModel.Name" />
                <BootstrapInput @bind-Value="@NestedModel.Address" />
                <Row ItemsPerRow="ItemsPerRow.Two">
                    <BootstrapInput @bind-Value="@NestedModel.Name" />
                    <BootstrapInput @bind-Value="@NestedModel.Address" />
                </Row>
```
