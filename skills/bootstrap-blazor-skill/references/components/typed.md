# Typed

## 概述

Typed 组件类

> Typed Component Class

**分类**: 数据展示
**在线演示**: [https://www.blazor.zone/typed](https://www.blazor.zone/typed)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `}` | 获得/设置 组件显示文字，默认 null |
| `Options` | `TypedOptions?` | `}` | 获得/设置 组件配置实例，默认 null |
| `OnCompleteAsync` | `Func<Task>?` | `}` | 获得/设置 打字结束回调方法，默认 null |

## 代码示例

### 基本用法

```razor
<Typed Text="<code>BootstrapBlazor</code> is an enterprise-level UI component library"></Typed>
```

### 基本用法

```razor
<Typed Options="_options"></Typed>
```
