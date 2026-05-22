# Tree

## 概述

Tree 组件

> Tree Component

**分类**: 数据展示

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ActiveItem` | `TreeItem?` | `}` | 获得/设置 选中节点 默认 null |
| `IsAccordion` | `bool` | `}` | 获得/设置 是否为手风琴效果 默认为 false |
| `ClickToggleNode` | `bool` | `}` | 获得/设置 是否点击节点时展开或者收缩子项 默认 false |
| `ShowSkeleton` | `bool` | `}` | 获得/设置 是否显示加载骨架屏 默认 false 不显示 |
| `NodeIcon` | `string?` | `}` | 获得/设置 Tree Node 节点图标 |
| `ExpandNodeIcon` | `string?` | `}` | 获得/设置 Tree Node 展开节点图标 |
| `Items` | `List<TreeItem>?` | `}` | 获得/设置 菜单数据集合 |
| `ShowCheckbox` | `bool` | `}` | 获得/设置 是否显示 CheckBox 默认 false 不显示 |
| `ShowRadio` | `bool` | `}` | 获得/设置 是否显示 Radio 默认 false 不显示 |
| `ShowIcon` | `bool` | `}` | 获得/设置 是否显示 Icon 图标 默认 false 不显示 |
| `Task` | `Func<TreeItem,` | `}` | 获得/设置 树形控件节点点击时回调委托 |
