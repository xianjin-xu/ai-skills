# Footer

## 概述

Footer 组件

> Footer Component

**分类**: 布局
**在线演示**: [https://www.blazor.zone/footer](https://www.blazor.zone/footer)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `}` | 获得/设置 Footer 显示文字 |
| `Target` | `string?` | `}` | 获得/设置 Footer 组件中返回顶端按钮控制的滚动条所在组件 设置 <see cref="ShowGoto"/> 为 true 时生效 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 内容 |
| `ShowGoto` | `bool` | `true` | 获得/设置 是否显示 Goto 小组件 默认 true 显示 |

## 代码示例

### 基本用法

```razor
<Footer>
            <div class="row g-3 text-center">
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
                <div class="col-6 col-md-4 col-lg-3">友情链接</div>
            </div>
        </Footer>
```
