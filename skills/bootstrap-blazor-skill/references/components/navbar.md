# Navbar (导航栏)

## 概述

`Navbar` 是一个响应式导航栏组件，提供品牌、导航链接、下拉菜单等功能，支持不同尺寸和背景色。

> Navbar component!

**分类**: 导航  
**在线演示**: [https://www.blazor.zone/navbar](https://www.blazor.zone/navbar)

## 使用场景

### 1. 基本用法

```razor
<Navbar>
    <NavbarBrand>
        <a class="navbar-brand">Brand</a>
    </NavbarBrand>
    <NavbarToggleButton Target="#navbarContent"></NavbarToggleButton>
    <NavbarCollapse Id="navbarContent">
        <NavbarGroup>
            <NavbarLink>Home</NavbarLink>
            <NavbarLink>About</NavbarLink>
        </NavbarGroup>
    </NavbarCollapse>
</Navbar>
```

### 2. 不同尺寸

```razor
<Navbar Size="Size.Small">
    <!-- 内容 -->
</Navbar>

<Navbar Size="Size.Large">
    <!-- 内容 -->
</Navbar>
```

### 3. 自定义背景色

```razor
<Navbar BackgroundColorCssClass="bg-primary">
    <!-- 内容 -->
</Navbar>
```

### 4. 下拉菜单

```razor
<Navbar>
    <NavbarCollapse>
        <NavbarGroup>
            <NavbarDropdown Text="Dropdown">
                <NavbarDropdownItem>Action</NavbarDropdownItem>
                <NavbarDropdownItem>Another action</NavbarDropdownItem>
                <NavbarDropdownDivider />
                <NavbarDropdownItem>Something else</NavbarDropdownItem>
            </NavbarDropdown>
        </NavbarGroup>
    </NavbarCollapse>
</Navbar>
```

### 5. 滚动模式

```razor
<Navbar>
    <NavbarCollapse>
        <NavbarGroup IsScrolling="true">
            <NavbarLink>Link 1</NavbarLink>
            <NavbarLink>Link 2</NavbarLink>
            <NavbarLink>Link 3</NavbarLink>
        </NavbarGroup>
    </NavbarCollapse>
</Navbar>
```

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Size` | `Size` | `Size.Medium` | 获得/设置组件大小 |
| `BackgroundColorCssClass` | `string?` | `null` | 获得/设置背景色样式名称 |
| `ChildContent` | `RenderFragment?` | `null` | 获得/设置子组件模板 |

## 事件回调 (EventCallbacks)

| 事件名 | 说明 |
|--------|------|
| `OnClick` | 点击时触发 |

## 最佳实践

1. **基本结构**: 使用 `NavbarBrand`、`NavbarToggleButton`、`NavbarCollapse`、`NavbarGroup` 构建导航栏
2. **响应式**: `NavbarToggleButton` 和 `NavbarCollapse` 配合实现移动端折叠
3. **尺寸控制**: 使用 `Size` 参数设置导航栏高度（`Small`、`Medium`、`Large`）
4. **背景色**: 使用 `BackgroundColorCssClass` 参数设置背景色（如 `bg-primary`）
5. **滚动模式**: 设置 `NavbarGroup` 的 `IsScrolling="true"` 启用滚动模式
6. **下拉菜单**: 使用 `NavbarDropdown` 创建下拉菜单

## 常见问题

### Q: 如何创建响应式导航栏？
A: 使用 `NavbarToggleButton` 和 `NavbarCollapse` 配合，`NavbarToggleButton` 控制 `NavbarCollapse` 的显示/隐藏。

### Q: 如何设置导航栏高度？
A: 使用 `Size` 参数设置尺寸，可选 `Size.Small`、`Size.Medium`、`Size.Large`。

### Q: 如何设置背景色？
A: 使用 `BackgroundColorCssClass` 参数设置背景色 CSS 类，如 `bg-primary`、`bg-dark` 等。

### Q: 如何创建下拉菜单？
A: 使用 `NavbarDropdown` 组件创建下拉菜单，内部使用 `NavbarDropdownItem` 定义菜单项。

### Q: 如何启用滚动模式？
A: 设置 `NavbarGroup` 的 `IsScrolling="true"` 启用水平滚动模式。

## 子组件

`Navbar` 组件包含以下子组件：
- `NavbarBrand` - 品牌区域
- `NavbarToggleButton` - 切换按钮（移动端）
- `NavbarCollapse` - 折叠区域
- `NavbarGroup` - 导航项组
- `NavbarLink` - 导航链接
- `NavbarDropdown` - 下拉菜单
- `NavbarDropdownItem` - 下拉菜单项
- `NavbarDropdownDivider` - 下拉菜单分隔符
- `NavbarItem` - 导航项容器
