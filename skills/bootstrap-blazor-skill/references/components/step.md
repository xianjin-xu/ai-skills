# Step

## 概述

Step 组件类

> Step Component Class

**分类**: 导航
**在线演示**: [https://www.blazor.zone/step](https://www.blazor.zone/step)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `List<StepOption>?` | `}` | 获得/设置 步骤集合 |
| `IsVertical` | `bool` | `}` | 获得/设置 是否垂直渲染 默认 false 水平渲染 |
| `StepIndex` | `int` | `}` | 获得/设置 当前步骤索引 默认 0 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 组件内容实例 |
| `FinishedTemplate` | `RenderFragment?` | `}` | 获得/设置 步骤全部完成时模板 默认 null |
| `OnFinishedCallback` | `Func<Task>?` | `}` | 获得/设置 步骤全部完成时回调方法 |

## 代码示例

### 基本用法

```razor
<Step @ref="@_step1" Items="@Items">
        <FinishedTemplate>
            <div style="height: 100px; margin-top: 1rem;">@((MarkupString)Localizer["StepsNormalFinishedTemplateDesc"].Value)</div>
        </FinishedTemplate>
    </Step>
```

### 基本用法

```razor
<Step @ref="@_step2">
        <StepItem Text="@Localizer["Step1Text"]" Title="@Localizer["Step1Title"]"></StepItem>
        <StepItem Text="@Localizer["Step2Text"]" Title="@Localizer["Step2Title"]"></StepItem>
        <StepItem Text="@Localizer["Step3Text"]" Title="@Localizer["Step3Title"]"></StepItem>
    </Step>
```

### 基本用法

```razor
<Step @ref="@_step3">
        <StepItem Text="@Localizer["Step1Text"]" Description="@Localizer["StepDesc"]" Title="@Localizer["Step1Title"]"></StepItem>
        <StepItem Text="@Localizer["Step2Text"]" Description="@Localizer["StepDesc"]" Title="@Localizer["Step2Title"]"></StepItem>
        <StepItem Text="@Localizer["Step3Text"]" Description="@Localizer["StepDesc"]" Title="@Localizer["Step3Title"]"></StepItem>
    </Step>
```

### 基本用法

```razor
<Step @ref="@_step4">
        <StepItem Text="@Localizer["Step1Text"]" Description="@Localizer["StepDesc"]" Title="@Localizer["Step1Title"]">
            <TitleTemplate>
                <div class="step-title">
                    <i class="fa fa-flag"></i>
                    <span>@context.Title</span>
                </div>
            </TitleTemplate>
        </StepItem>
        <StepItem Text="@Localizer["Step2Text"]" Description="@Localizer["StepDesc"]" Title="@Localizer["Step2Title"]">
            <TitleTemplate>
                <div class="step-title">
                    <i class="fa fa-flag"></i>
                    <span>@context.Title</span>
                </div>
                <div>@DateTime.Now</div>
            </TitleTemplate>
        </StepItem>
        <StepItem Text="@Localizer["Step3Text"]" Description="@Localizer["StepDesc"]" Title="@Localizer["Step3Title"]"></StepItem>
    </Step>
```

### 基本用法

```razor
<Step @ref="@_step5">
            <StepItem>
                <HeaderTemplate>
                    <i class="fa fa-edit"></i>
                    <span class="ms-2">@Localizer["Step1Text"]</span>
                    <div class="flex-fill text-center">
                        <i class="fa-solid fa-chevron-right"></i>
                    </div>
                </HeaderTemplate>
            </StepItem>
            <StepItem>
                <HeaderTemplate>
                    <i class="fa fa-user"></i>
                    <span class="ms-2">@Localizer["Step2Text"]</span>
                    <div class="flex-fill text-center">
                        <i class="fa-solid fa-chevron-right"></i>
                    </div>
                </HeaderTemplate>
            </StepItem>
            <StepItem>
                <HeaderTemplate>
                    <i class="fa fa-house"></i>
                    <span class="ms-2">@Localizer["Step3Text"]</span>
                </HeaderTemplate>
            </StepItem>
        </Step>
```
