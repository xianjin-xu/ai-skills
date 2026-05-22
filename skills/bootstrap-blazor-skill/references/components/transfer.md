# Transfer

## 概述

Transfer 组件（穿梭框）

> Transfer Component

**分类**: 表单输入
**在线演示**: [https://www.blazor.zone/transfer](https://www.blazor.zone/transfer)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Items` | `IEnumerable<SelectedItem>?` | `}` | 获得/设置 组件绑定数据项集合 |
| `Task` | `Func<IEnumerable<SelectedItem>,` | `}` | 获得/设置 选中项集合发生改变时回调委托方法 |
| `LeftPanelText` | `string?` | `}` | 获得/设置 左侧面板 Header 显示文本 |
| `RightPanelText` | `string?` | `}` | 获得/设置 右侧面板 Header 显示文本 |
| `LeftIcon` | `string?` | `}` | 获得/设置 向左侧转移图标 |
| `RightIcon` | `string?` | `}` | 获得/设置 向右侧转移图标 |
| `LeftButtonText` | `string?` | `}` | 获得/设置 左侧按钮显示文本 |
| `RightButtonText` | `string?` | `}` | 获得/设置 右侧按钮显示文本 |
| `ShowSearch` | `bool` | `}` | 获得/设置 是否显示搜索框 |
| `LeftPannelSearchPlaceHolderString` | `string?` | `> LeftPanelSearchPlaceHolderString` | 获得/设置 左侧面板搜索框 placeholder 文字 |
| `LeftPanelSearchPlaceHolderString` | `string?` | `}` | 获得/设置 左侧面板搜索框 placeholder 文字 |
| `RightPannelSearchPlaceHolderString` | `string?` | `> RightPanelSearchPlaceHolderString` | 获得/设置 右侧面板搜索框 placeholder 文字 |
| `RightPanelSearchPlaceHolderString` | `string?` | `}` | 获得/设置 右侧面板搜索框 placeholder 文字 |
| `Max` | `int` | `}` | 获得/设置 右侧面板包含的最大数量，默认为 0 不限制 |
| `MaxErrorMessage` | `string?` | `}` | 获得/设置 设置最大值时的错误消息文字 |
| `Min` | `int` | `}` | 获得/设置 右侧面板包含的最小数量，默认为 0 不限制 |
| `MinErrorMessage` | `string?` | `}` | 获得/设置 设置最小值时的错误消息文字 |
| `string` | `Func<SelectedItem,` | `}` | 获得/设置 数据样式回调方法，默认为 null |
| `LeftHeaderTemplate` | `RenderFragment<List<SelectedItem>>?` | `}` | 获得/设置 左侧 Panel Header 模板 |
| `LeftItemTemplate` | `RenderFragment<SelectedItem>?` | `}` | 获得/设置 左侧 Panel Item 模板 |
| `RightHeaderTemplate` | `RenderFragment<List<SelectedItem>>?` | `}` | 获得/设置 右侧 Panel Header 模板 |
| `RightItemTemplate` | `RenderFragment<SelectedItem>?` | `}` | 获得/设置 右侧 Panel Item 模板 |
| `Height` | `string?` | `}` | 获得/设置 组件高度 默认值 null 未设置 |
| `IsWrapItem` | `bool` | `true` | 获得/设置 候选项是否为换行模式 默认 false 不换行 |
| `ItemWidth` | `string?` | `}` | 获得/设置 候选项宽度 默认 null 未设置 |
| `IsWrapItemText` | `bool` | `}` | 获得/设置 候选项文本是否为换行 默认 false 不换行 |
