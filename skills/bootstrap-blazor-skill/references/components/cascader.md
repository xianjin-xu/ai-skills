# Cascader

## 概述

Cascader 组件实现类

> Cascader component implementation class

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/cascader](https://www.blazor.zone/cascader)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Color` | `Color` | `Color.None` | 获得/设置 按钮颜色 |
| `PlaceHolder` | `string?` | `}` | 获得/设置 组件 PlaceHolder 文字 默认为 请选择 .. |
| `Items` | `IEnumerable<CascaderItem>?` | `}` | 获得/设置 绑定数据集 |
| `Task` | `Func<CascaderItem[],` | `}` | 获得/设置 ValueChanged 方法 |
| `ParentSelectable` | `bool` | `true` | 获得/设置 父节点是否可选择 默认 true |
| `ShowFullLevels` | `bool` | `true` | 获得/设置 是否显示全路径 默认 true |
| `Icon` | `string?` | `}` | 获得/设置 菜单指示图标 |
| `SubMenuIcon` | `string?` | `}` | 获得/设置 子菜单指示图标 |
| `IsClearable` | `bool` | `}` | 获得/设置 是否可清除 默认 false |
| `ClearIcon` | `string?` | `}` | 获得/设置 右侧清除图标 默认 fa-solid fa-angle-up |
| `OnClearAsync` | `Func<Task>?` | `}` | 获得/设置 清除文本内容 OnClear 回调方法 默认 null |
