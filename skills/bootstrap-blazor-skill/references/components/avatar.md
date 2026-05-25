# Avatar (头像)

## 概述

`Avatar` 组件用于**用图标、图片或者字符的形式展示用户或事物信息**。

**主要特性**：
- 支持三种展示类型（图标、图片、字符）
- 支持圆形/方形形状（IsCircle）
- 支持不同尺寸（Size）
- 支持边框显示（IsBorder）
- 支持异步加载图片（GetUrlAsync）

**在线演示**: https://www.blazor.zone/avatar

---

## 使用场景

### 1. 基础用法（设置形状和大小）

通过 `IsCircle` 和 `Size` 设置头像的形状和大小。

```razor
<!-- 圆形头像 -->
<Avatar IsCircle="true" Size="Size.Medium">
    <Icon Name="fa fa-user" />
</Avatar>

<!-- 方形头像 -->
<Avatar IsCircle="false" Size="Size.Medium">
    <Icon Name="fa fa-user" />
</Avatar>

<!-- 不同尺寸 -->
<Avatar IsCircle="true" Size="Size.Small">
    <Icon Name="fa fa-user" />
</Avatar>

<Avatar IsCircle="true" Size="Size.Medium">
    <Icon Name="fa fa-user" />
</Avatar>

<Avatar IsCircle="true" Size="Size.Large">
    <Icon Name="fa fa-user" />
</Avatar>
```

---

### 2. 展示类型（图标、图片、字符）

支持三种类型：图标、图片和字符。

```razor
<!-- 图标类型 -->
<Avatar IsCircle="true">
    <Icon Name="fa fa-user" />
</Avatar>

<!-- 图片类型 -->
<Avatar Url="https://via.placeholder.com/100" IsCircle="true" />

<!-- 字符类型 -->
<Avatar IsCircle="true" IsText="true" Text="张" />
```

**说明**：
- **图标类型**：在 `Avatar` 标签内放置 `Icon` 组件
- **图片类型**：通过 `Url` 参数设置图片地址
- **字符类型**：设置 `IsText="true"` 并通过 `Text` 参数设置显示文字

---

### 3. 边框功能（IsBorder）

通过设置 `IsBorder="true"` 显示头像框边框。此模式下图片加载失败时边框为 `border-danger` 样式，加载成功时边框为 `border-success`；其余模式下边框为 `border-info`。

```razor
<!-- 带边框的头像 -->
<Avatar IsCircle="true" IsBorder="true" Url="https://via.placeholder.com/100" />

<!-- 图片加载失败的头像（边框变红） -->
<Avatar IsCircle="true" IsBorder="true" Url="wrong-url.jpg" />
```

---

### 4. 异步加载（GetUrlAsync）

适用于图片地址由 WebAPI 等接口异步获取的场景。

```razor
<!-- 异步加载图片 -->
<Avatar IsCircle="true" GetUrlAsync="@GetAvatarUrl" />

@code {
    private async Task<string> GetAvatarUrl()
    {
        // 模拟从 API 获取图片地址
        await Task.Delay(1000);
        return "https://via.placeholder.com/100";
    }
}
```

---

## 参数 (Parameters)

### Avatar 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Url` | `string?` | `null` | 获得/设置 Image 头像路径地址 |
| `IsCircle` | `bool` | `false` | 获得/设置 是否为圆形 |
| `IsIcon` | `bool` | `false` | 获得/设置 是否为图标 |
| `Icon` | `string?` | `null` | 获得/设置 头像框显示图标 |
| `IsText` | `bool` | `false` | 获得/设置 是否显示为文字 |
| `Text` | `string?` | `null` | 获得/设置 头像框显示文字 |
| `Size` | `Size` | `Size.Medium` | 获得/设置 头像框大小 |
| `IsBorder` | `bool` | `false` | 获得/设置 是否显示 Border 默认为 false |
| `GetUrlAsync` | `Func<Task<string>>?` | `null` | 获得/设置 获取图片地址异步回调方法 |
| `AdditionalAttributes` | `IDictionary<string, object>?` | `null` | 获得/设置 用户自定义属性 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 最佳实践

1. **选择合适的展示类型**：用户有头像用图片（`Url`），用户无头像用图标（`Icon`）或字符（`Text`）
2. **合理使用形状**：圆形（`IsCircle="true"`）更常见，方形（`IsCircle="false"`）适合特殊场景
3. **使用 Size 控制大小**：`Small`（24px）、`Medium`（32px，默认）、`Large`（40px）
4. **图片加载失败处理**：使用 `IsBorder="true"` 可在图片加载失败时显示红色边框提示
5. **异步加载场景**：图片地址需要 API 获取时，使用 `GetUrlAsync` 回调
6. **与 Image 组件的区别**：`Avatar` 是头像组件（带形状、边框等），`Image` 是普通图片组件
