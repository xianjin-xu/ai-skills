# Navbar

## 概述

Navbar 组件

> Navbar component

**分类**: 导航
**在线演示**: [https://www.blazor.zone/navbar](https://www.blazor.zone/navbar)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Size` | `Size` | `Size.Medium` | 获得/设置 组件大小，默认为 <see cref="Size.Medium"/> |
| `BackgroundColorCssClass` | `string?` | `}` | 获得/设置 背景色样式名称，默认为 null 未设置 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件模板 |

## 代码示例

### 基本用法

```razor
<Navbar>
        <NavbarBrand>
            <a>Navbar</a>
        </NavbarBrand>
        <NavbarToggleButton Target="#test"></NavbarToggleButton>
        <NavbarCollapse Id="test">
            <NavbarGroup IsScrolling="true">
                <NavbarLink>Home</NavbarLink>
                <NavbarLink Text="Link"></NavbarLink>
                <NavbarDropdown Text="Dropdown">
                    <NavbarDropdownItem>
                        <i class="fa-solid fa-fw fa-home"></i><span>Action</span>
                    </NavbarDropdownItem>
                    <NavbarDropdownItem>
                        <i class="fa-solid fa-fw fa-flag"></i><span>Another action</span>
                    </NavbarDropdownItem>
                    <NavbarDropdownDivider></NavbarDropdownDivider>
                    <NavbarDropdownItem>
                        <i class="fa-solid fa-fw fa-home"></i><span>Something else here</span>
                    </NavbarDropdownItem>
                </NavbarDropdown>
                <NavbarLink IsDisabled="true">Disabled</NavbarLink>
                <NavbarItem>
                    <a class="nav-link">About</a>
                </NavbarItem>
            </NavbarGroup>
            <NavbarGroup>
                <ValidateForm class="d-flex" role="search" Model="_searchModel" OnValidSubmit="OnValidSubmit">
                    <BootstrapInput class="me-2" placeholder="Search" @bind-Value="_searchModel.SearchText"
                                    ShowLabel="false" SkipValidate="true"></BootstrapInput>
                    <Button Color="Color.Success" IsOutline="true" ButtonType="ButtonType.Submit">Search</Button>
                </ValidateForm>
            </NavbarGroup>
        </NavbarCollapse>
    </Navbar>
```
