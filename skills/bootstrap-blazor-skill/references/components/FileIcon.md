# FileIcon

## 概述

Icon 图标组件

> File Icon Component

**分类**: 其他
**在线演示**: [https://www.blazor.zone/file-icon](https://www.blazor.zone/file-icon)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Extension` | `string?` | `}` | 获得/设置 文件类型扩展名 |
| `BackgroundTemplate` | `RenderFragment?` | `}` | 获得/设置 背景图模板 默认 null 使用内部内置的空文件 svg 图 |
| `IconColor` | `Color` | `Color.Primary` | 获得/设置 图标类型背景色 默认 <see cref="Color.Primary"/> |
| `Size` | `Size` | `}` | 获得/设置 图标大小 默认 <see cref="Size.None"/> |

## 代码示例

### 基本用法

```razor
<FileIcon Extension=".xlsx" IconColor="Color.Success">
                <BackgroundTemplate>
                    <i class="fa-regular fa-clipboard fa-4x" />
                </BackgroundTemplate>
            </FileIcon>
```
