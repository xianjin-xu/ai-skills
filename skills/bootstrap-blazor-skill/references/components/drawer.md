# Drawer (抽屉组件)

## 概述

`Drawer` 组件用于**创建可从边缘滑出的抽屉面板**，常用于导航菜单、设置面板等场景。

**主要特性**：
- 支持 4 个位置（Left、Right、Top、Bottom）
- 支持点击遮罩关闭（IsBackdrop）
- 支持键盘 ESC 关闭（IsKeyboard）
- 支持调整大小（AllowResize）
- 支持自定义宽度/高度

**在线演示**: https://www.blazor.zone/drawer

---

## 使用场景

### 1. 基础用法（左侧抽屉）

`Drawer` 组件默认从左侧滑出。

```razor
<Drawer @bind-IsOpen="IsOpen">
    <div class="p-3">
        <h4>抽屉标题</h4>
        <p>抽屉内容...</p>
        <button class="btn btn-primary" @onclick="() => IsOpen = false">关闭</button>
    </div>
</Drawer>

<button class="btn btn-secondary" @onclick="() => IsOpen = true">打开抽屉</button>

@code {
    private bool IsOpen { get; set; }
}
```

---

### 2. 不同位置（Placement）

通过 `Placement` 参数设置抽屉出现位置。

```razor
<!-- 左侧（默认） -->
<Drawer Placement="Placement.Left" @bind-IsOpen="IsOpen">
    <div class="p-3">左侧抽屉</div>
</Drawer>

<!-- 右侧 -->
<Drawer Placement="Placement.Right" @bind-IsOpen="IsOpen">
    <div class="p-3">右侧抽屉</div>
</Drawer>

<!-- 顶部 -->
<Drawer Placement="Placement.Top" @bind-IsOpen="IsOpen">
    <div class="p-3">顶部抽屉</div>
</Drawer>

<!-- 底部 -->
<Drawer Placement="Placement.Bottom" @bind-IsOpen="IsOpen">
    <div class="p-3">底部抽屉</div>
</Drawer>
```

---

### 3. 点击遮罩关闭（IsBackdrop）

通过设置 `IsBackdrop="true"` 启用点击遮罩关闭抽屉。

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="IsBackdropOpen" IsBackdrop="true">
    <div class="p-3">
        <p>点击遮罩可关闭抽屉</p>
    </div>
</Drawer>
```

---

### 4. 键盘 ESC 关闭（IsKeyboard）

通过设置 `IsKeyboard="true"` 启用键盘 ESC 键关闭抽屉。

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="IsKeyboardOpen" IsKeyboard="true">
    <div class="p-3">
        <p>按 ESC 键可关闭抽屉</p>
    </div>
</Drawer>
```

---

### 5. 调整大小（AllowResize）

通过设置 `AllowResize="true"` 允许拖拽调整抽屉大小。

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="IsResizeOpen" AllowResize="true" Width="300px">
    <div class="p-3">
        <p>可拖拽右侧边缘调整宽度</p>
    </div>
</Drawer>
```

---

### 6. 不显示遮罩（ShowBackdrop）

通过设置 `ShowBackdrop="false"` 隐藏遮罩层（背景不遮暗）。

```razor
<Drawer Placement="Placement.Left" @bind-IsOpen="IsShowBackdropOpen" ShowBackdrop="false">
    <div class="p-3">
        <p>无遮罩抽屉</p>
    </div>
</Drawer>
```

---

## 参数 (Parameters)

### Drawer 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsOpen` | `bool` | `false` | 获得/设置 抽屉是否打开 默认 false 未打开 |
| `Placement` | `Placement` | `Placement.Left` | 获得/设置 组件出现位置 默认显示在 Left 位置 |
| `Width` | `string` | `"360px"` | 获得/设置 抽屉宽度 左右布局时生效 |
| `Height` | `string` | `"290px"` | 获得/设置 抽屉高度 上下布局时生效 |
| `IsBackdrop` | `bool` | `false` | 获得/设置 点击遮罩是否关闭抽屉 默认为 false |
| `ShowBackdrop` | `bool` | `true` | 获得/设置 是否显示遮罩 默认为 true 显示遮罩 |
| `AllowResize` | `bool` | `false` | 获得/设置 是否允许调整大小 默认 false |
| `IsKeyboard` | `bool` | `false` | 获得/设置 是否支持键盘 ESC 关闭当前弹窗 默认 false |
| `BodyScroll` | `bool` | `false` | 获得/设置 抽屉显示时是否允许滚动 body 默认为 false 不滚动 |
| `ZIndex` | `int?` | `null` | 获得/设置 z-index 参数值 默认 null 未设置 |
| `Position` | `string?` | `null` | 获得/设置 组件定位位置 默认 null 未设置 使用样式内置定位 fixed 可更改为 absolute |
| `OnClickBackdrop` | `Func<Task>?` | `null` | 获得/设置 点击背景遮罩时回调委托方法 默认为 null |
| `OnCloseAsync` | `Func<Task>?` | `null` | 获得/设置 关闭抽屉回调委托 默认 null |
| `BodyContext` | `object?` | `null` | 获得/设置 抽屉内容相关数据 多用于传值 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `IsOpenChanged` | `EventCallback<bool>` | 获得/设置 IsOpen 属性改变时回调委托方法 |

---

## 最佳实践

1. **使用 @bind-IsOpen 双向绑定**：通过 `@bind-IsOpen` 控制抽屉开关状态
2. **合理设置 Placement**：导航菜单用 `Left`，设置面板用 `Right`，通知栏用 `Top/Bottom`
3. **启用 IsBackdrop**：大多数场景启用 `IsBackdrop="true"`，点击遮罩关闭更符合用户习惯
4. **键盘无障碍**：启用 `IsKeyboard="true"` 支持 ESC 关闭，提升无障碍体验
5. **与 Modal 的区别**：`Drawer` 从边缘滑出（不占满屏），`Modal` 是居中对话框（占满屏宽）
6. **性能优化**：抽屉内容复杂时用 `LazyLoad` 延迟加载，避免影响主页面性能
