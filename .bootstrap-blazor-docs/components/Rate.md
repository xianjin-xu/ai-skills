# Rate 评分#

## 概述#

Rate 评分组件通过 1-5 颗星表示数值等级，后台可以通过 `@bind-Value` 对数值进行双向绑定。通过 Rate 组件更改其值，鼠标滑动更改值，点击星星时确认其值。

> Rate component uses 1-5 stars to represent numerical levels, supporting two-way binding via `@bind-Value`.

**分类**: 表单组件  
**在线演示**: [https://www.blazor.zone/rate](https://www.blazor.zone/rate)

---

## 使用场景#

### 1. 基础用法#

Rate 组件通过 1-5 颗星表示数值等级。

```razor
<Rate @bind-Value="RateValue" />

@code {
    private double RateValue { get; set; } = 3;
}
```

### 2. 模板#

通过设置 `ItemTemplate` 模板，配合自定义样式 `custom-rate` 实现复杂功能。

```razor
<Rate @bind-Value="RateValue">
    <ItemTemplate>
        <i class="@(context <= RateValue ? "fa-solid fa-star" : "fa-regular fa-star")"></i>
    </ItemTemplate>
</Rate>

<style>
    .custom-rate {
        --bb-rate-font-size: 1.7rem;
        --bb-rate-height: 30px;
        --bb-rate-width: 30px;
        --bb-rate-active-color: var(--bs-primary);
    }
</style>
```

### 3. 禁用#

通过设置 `IsDisable` 属性值禁用组件。

```razor
<Rate @bind-Value="RateValue" IsDisable="true" />
```

### 4. 只读#

通过设置 `IsReadonly` 属性值使组件只读，有颜色不响应点击事件。

```razor
<Rate @bind-Value="RateValue" IsReadonly="true" />
```

### 5. 显示评分#

通过设置 `ShowValue="true"` 使组件显示当前值。

```razor
<Rate @bind-Value="RateValue" ShowValue="true" />
```

### 6. 自动折行#

通过设置 `IsWrap="true"` 使组件自动折行，默认不折行。

```razor
<Rate @bind-Value="RateValue" IsWrap="true" />
```

### 7. 自定义图标#

通过设置 `StarIcon` 和 `UnStarIcon` 自定义选中和未选中图标。

```razor
<Rate @bind-Value="RateValue" 
       StarIcon="fa-solid fa-heart" 
       UnStarIcon="fa-regular fa-heart" />
```

---

## 参数#

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|---------|
| AdditionalAttributes | 获得/设置 用户自定义属性 | IDictionary<string, Object> | — |
| IsDisable | 获得/设置 是否禁用，默认为 false | bool | false |
| IsReadonly | 获得/设置 是否只读，默认为 false | bool | false |
| IsWrap | 获得/设置 是否禁止换行，默认为 true | bool | true |
| ItemTemplate | 获得/设置 子项模板 | RenderFragment<double> | — |
| Max | 获得/设置 最大值，默认为 5 | int | 5 |
| OnValueChanged | 获得/设置 组件值变化时回调方法 | Func<double, Task> | — |
| ShowValue | 获得/设置 是否显示 Value，默认为 false | bool | false |
| StarIcon | 获得/设置 选中图标 | string | — |
| UnStarIcon | 获得/设置 未选中图标 | string | — |
| Value | 获得/设置 组件值 | double | — |
| ValueChanged | 获得/设置 组件值变化时回调委托 | EventCallback<double> | — |

---

## 事件回调#

| 事件名称 | 说明 | 回调类型 |
|---------|------|---------|
| OnValueChanged | 组件值变化时回调方法 | Func<double, Task> |

---

## 最佳实践#

### 显示半星评分#

通过自定义 `ItemTemplate` 实现半星显示：

```razor
<Rate @bind-Value="RateValue" Max="5">
    <ItemTemplate>
        @{
            var index = context;
            var floorValue = Math.Floor(index);
            var decimalValue = index - floorValue;
        }
        <span class="rate-star">
            @if (decimalValue >= 0.75)
            {
                <i class="fa-solid fa-star"></i>
            }
            else if (decimalValue >= 0.25)
            {
                <i class="fa-solid fa-star-half-alt"></i>
            }
            else
            {
                <i class="fa-regular fa-star"></i>
            }
        </span>
    </ItemTemplate>
</Rate>

@code {
    private double RateValue { get; set; } = 3.5;
}
```

### 配合表单使用#

Rate 组件可以在表单中使用：

```razor
<ValidateForm Model="Model">
    <EditorForm TItem="RatingModel">
        <FieldItems>
            <EditorItem @bind-Field="context.Rating" />
        </FieldItems>
    </EditorForm>
</ValidateForm>

@code {
    private RatingModel Model { get; set; } = new();
    
    public class RatingModel
    {
        [Display(Name = "评分")]
        [Range(1, 5, ErrorMessage = "请选择1-5星")]
        public double Rating { get; set; }
    }
}
```

---

## 常见问题#

### 1. 如何获取评分值？#

通过 `Value` 属性或 `@bind-Value` 双向绑定获取评分值。

### 2. 如何自定义星星数量？#

设置 `Max` 参数可以改变最大星星数量，默认为 5。

### 3. 如何禁用组件？#

设置 `IsDisable="true"` 可以禁用组件，用户无法交互。

### 4. 如何显示当前评分值？#

设置 `ShowValue="true"` 可以在组件旁边显示当前评分值。

---

## 版本历史#

| 版本 | 发布时间 | 更新内容 |
|------|---------|---------|
| 7.0.0 | 2023-xx-xx | Rate 组件发布 |

---

**参考链接**:
- [官方文档](https://www.blazor.zone/rate)
- [Slider 组件文档](https://www.blazor.zone/slider)
