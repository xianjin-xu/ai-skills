# Empty

## 概述

Empty 组件

> Empty Component

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/empty](https://www.blazor.zone/empty)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Image` | `string?` | `}` | 获得/设置 图片路径 默认为 null |
| `Text` | `string?` | `}` | 获得/设置 空状态描述 默认为 无数据 |
| `Template` | `RenderFragment?` | `}` | 获得/设置 自定义模板 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |

## 代码示例

### 基本用法

```razor
<Empty Image="https://gw.alipayobjects.com/zos/antfincdn/ZHrcdLPrvN/empty.svg" Width="133" Text="@Localizer["TemplateText"]">
            <Template>
                <Button OnClick="@(()=>NavigationManager.NavigateTo("components"))">@Localizer["TemplateIButtonText"]</Button>
            </Template>
        </Empty>
```
