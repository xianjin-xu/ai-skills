# Footer 页脚组件

## 概述

`Footer` 是一个页脚组件，显示在网页的最下方，提供返回顶端按钮功能。适用于需要在页面底部显示版权信息、友情链接等内容，并提供快速返回页面顶部的场景。

**命名空间**: `BootstrapBlazor.Components`

**在线演示**: [https://www.blazor.zone/footer](https://www.blazor.zone/footer)

## 使用场景

### 1. 基础用法

通过 `Target` 参数传递滚动条组件的 ID 给页脚组件，点击返回顶端时页面自动滚动回顶端。

```razor
<Footer Target="root" />

<div id="root" style="height: 2000px;">
    <p>页面内容...</p>
</div>
```

**说明**:
- `Target` 参数指定滚动容器的 ID（通常是具有滚动条的元素的 ID）
- 点击 Footer 右侧的 "返回顶端" 按钮时，页面会自动滚动到顶部
- 本示例传递的是组件客户端 ID

### 2. 是否显示 Goto 导航

通过设置 `ShowGoto` 参数，可以关闭 Footer 右侧的导航小组件（返回顶端按钮）。

```razor
<Footer Target="root" ShowGoto="false" />

<div id="root" style="height: 2000px;">
    <p>页面内容...</p>
</div>
```

**说明**:
- `ShowGoto="true"`（默认值）- 显示返回顶端按钮
- `ShowGoto="false"` - 隐藏返回顶端按钮
- 当页面不需要返回顶端功能时，可以设置为 `false`

### 3. 自定义内容

通过设置 `ChildContent` 参数自定义组件内部显示内容，可以显示友情链接、版权信息等。

```razor
<Footer Target="root">
    <div class="row g-3 text-center">
        <div class="col-6 col-md-4 col-lg-3">友情链接 1</div>
        <div class="col-6 col-md-4 col-lg-3">友情链接 2</div>
        <div class="col-6 col-md-4 col-lg-3">友情链接 3</div>
        <!-- 更多链接... -->
    </div>
</Footer>

<div id="root" style="height: 2000px;">
    <p>页面内容...</p>
</div>
```

**说明**:
- 使用 `ChildContent` 可以自定义 Footer 的内部内容
- 常见用法：显示友情链接、版权信息、网站地图链接等
- 内容区域支持任意 Razor 模板

### 4. 设置显示文字

通过 `Text` 参数设置 Footer 的显示文字（通常用作版权信息）。

```razor
<Footer Target="root" Text="© 2024 My Company. All rights reserved." />

<div id="root" style="height: 2000px;">
    <p>页面内容...</p>
</div>
```

**说明**:
- `Text` 参数用于显示简单的文本信息（如版权声明）
- 如果需要更复杂的内容，应使用 `ChildContent` 参数

## 参数

### Footer 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |
| `ChildContent` | 获得/设置 内容 | `RenderFragment` | `null` |
| `ShowGoto` | 获得/设置 是否显示 Goto 小组件（返回顶端按钮），默认 true 显示 | `bool` | `true` |
| `Target` | 获得/设置 Footer 组件中返回顶端按钮控制的滚动条所在组件，设置 `ShowGoto` 为 true 时生效 | `string` | `null` |
| `Text` | 获得/设置 Footer 显示文字 | `string` | `null` |

## 事件回调

Footer 组件暂无事件回调参数。

## CSS 变量

Footer 组件支持通过 CSS 变量自定义样式：

```css
.footer {
    --bb-footer-bg: var(--bs-secondary);
    --bb-footer-color: inherit;
    --bb-footer-padding: .5rem 1rem;
}
```

**可用 CSS 变量**:

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `--bb-footer-bg` | 背景颜色 | `var(--bs-secondary)` |
| `--bb-footer-color` | 文字颜色 | `inherit` |
| `--bb-footer-padding` | 内边距 | `.5rem 1rem` |

**自定义样式示例**:

```css
/* 在您的 CSS 文件中覆盖变量 */
:root {
    --bb-footer-bg: #343a40;
    --bb-footer-color: #ffffff;
    --bb-footer-padding: 1rem 2rem;
}
```

## 最佳实践

### 1. 正确设置 Target 参数

`Target` 参数应指向页面中具有滚动条的容器元素的 ID。如果页面整体滚动，通常指向 `body` 或某个具有 `overflow: auto` 的容器。

```razor
<!-- 页面整体滚动 -->
<Footer Target="body" />

<!-- 或指定特定容器 -->
<div id="scrollContainer" style="height: 500px; overflow-y: auto;">
    <!-- 内容 -->
</div>
<Footer Target="scrollContainer" />
```

### 2. 结合布局组件使用

Footer 通常放在页面底部，可以与 `Layout` 组件配合使用。

```razor
<Layout>
    <Header>页头</Header>
    <Sidebar>侧边栏</Sidebar>
    <Main>主要内容</Main>
    <Footer>页脚</Footer>
</Layout>
```

### 3. 内容区域的设计建议

Footer 的内容区域应简洁明了，避免过多复杂内容。

```razor
<!-- 推荐：简洁的版权信息 -->
<Footer Target="root" Text="© 2024 我的公司" />

<!-- 推荐：结构化的友情链接 -->
<Footer Target="root">
    <div class="container">
        <div class="row">
            <div class="col-4">
                <h5>产品</h5>
                <ul>
                    <li><a href="#">功能</a></li>
                    <li><a href="#">价格</a></li>
                </ul>
            </div>
            <div class="col-4">
                <h5>支持</h5>
                <ul>
                    <li><a href="#">文档</a></li>
                </ul>
            </div>
            <!-- 更多列... -->
        </div>
    </div>
</Footer>
```

## 常见问题

### 1. 点击返回顶端按钮无反应

**问题**: 点击 Footer 的返回顶端按钮后，页面没有滚动到顶部。

**原因**: 可能是 `Target` 参数设置不正确，或者指定的 ID 元素不存在。

**解决方案**:
- 确保 `Target` 参数的值与页面中某个元素的 ID 匹配
- 确保该元素具有滚动条（overflow 属性设置为 auto 或 scroll）
- 如果是页面整体滚动，可以尝试设置为 `Target="body"` 或 `Target="document"`

```razor
<Footer Target="body" />  <!-- 尝试使用 body -->
<Footer Target="document" />  <!-- 或尝试使用 document -->
```

### 2. Footer 样式不符合预期

**问题**: Footer 的背景色、文字颜色或内边距不符合设计需求。

**原因**: 需要通过 CSS 变量自定义样式。

**解决方案**: 在您的 CSS 文件中覆盖 Footer 的 CSS 变量。

```css
/* 自定义 Footer 样式 */
.footer {
    --bb-footer-bg: #2c3e50;
    --bb-footer-color: #ecf0f1;
    --bb-footer-padding: 2rem 1rem;
}
```

### 3. Footer 位置不正确

**问题**: Footer 没有显示在页面底部。

**原因**: Footer 组件的定位依赖于父容器的样式设置。

**解决方案**: 确保 Footer 的父容器设置了正确的定位样式。

```razor
<!-- 方案 1：使用 fixed-bottom 类固定在底部 -->
<div class="fixed-bottom">
    <Footer Target="body" />
</div>

<!-- 方案 2：使用 CSS 固定位置 -->
<style>
    .my-footer {
        position: fixed;
        bottom: 0;
        width: 100%;
    }
</style>
<Footer class="my-footer" Target="body" />
```

**注意**: Footer 组件使用时注意样式表 position 属性的设置。

## 版本历史

| 版本 | 发布日期 | 变更内容 |
|------|----------|----------|
| 6.0.0 | 2023-01-15 | Footer 组件首次发布 |
| 7.0.0 | 2024-01-15 | 新增 CSS 变量支持；优化 Target 参数逻辑 |

## 参考链接

- [Bootstrap Blazor 官方文档 - Footer](https://www.blazor.zone/footer)
- [Bootstrap Blazor API - Footer](https://www.blazor.zone/api/Footer)
