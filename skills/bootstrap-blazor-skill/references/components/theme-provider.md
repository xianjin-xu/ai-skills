# ThemeProvider

## 概述

ThemeProvider 主题提供者组件

> ThemeProvider Component

**分类**: 其他

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `AutoModeIcon` | `string?` | `}` | 获得/设置 自动模式图标，默认 null |
| `AutoModeText` | `string?` | `}` | 获得/设置 自动模式文本，默认 null 未设置使用本地化资源 |
| `DarkModeIcon` | `string?` | `}` | 获得/设置 暗黑模式图标，默认 null |
| `DarkModeText` | `string?` | `}` | 获得/设置 暗黑模式文本，默认 null 未设置使用本地化资源 |
| `LightModeIcon` | `string?` | `}` | 获得/设置 明亮模式图标，默认 null |
| `LightModeText` | `string?` | `}` | 获得/设置 明亮模式文本，默认 null 未设置使用本地化资源 |
| `ActiveIcon` | `string?` | `}` | 获得/设置 当前选中模式图标，默认 null |
| `ShowShadow` | `bool` | `true` | 获得/设置 下拉框是否显示阴影效果，默认 true |
| `Alignment` | `Alignment` | `Alignment.Right` | 获得/设置 下拉框对齐方式，默认 Right |
| `Task` | `Func<ThemeValue,` | `}` | 获得/设置 主题切换回调方法 |
| `ThemeValue` | `ThemeValue` | `ThemeValue.UseLocalStorage` | 获得/设置 主题类型 |

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `ThemeValueChanged` | `EventCallback<ThemeValue>` | 获得/设置 主题类型改变回调方法 |
