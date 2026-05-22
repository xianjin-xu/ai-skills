# DragDrap

## 概述

拖拽容器

> Drag Drop Container

**分类**: 其他

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `List<TItem>?` | `}` | 获取/设置 拖拽列表 |
| `MaxItems` | `int?` | `}` | 获取/设置 最大数量 默认 null 不限制 |
| `ChildContent` | `RenderFragment<TItem>?` | `}` | 获得/设置 子组件 |
| `string` | `Func<TItem,` | `}` | 获得/设置 每个 Item 的特殊 class |
| `TItem` | `Func<TItem,` | `}` | 获得/设置 复制内容 |
| `bool` | `Func<TItem,` | `}` | 获得/设置 当前节点是否允许被拖拽 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnItemDropRejectedByMaxItemLimit` | `EventCallback<TItem>` | 获得/设置 当拖拽因为数量超限被禁止时调用 |
| `OnItemDropRejected` | `EventCallback<TItem>` | 获得/设置 当拖拽被禁止时调用 |
| `OnReplacedItemDrop` | `EventCallback<TItem>` | 获得/设置 返回被替换的 Item |
| `OnItemDrop` | `EventCallback<TItem>` | 获得/设置 返回放下的 Item |
