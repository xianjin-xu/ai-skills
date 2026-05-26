# Logout

## 概述

ListView 组件基类

> ListView component基类

**分类**: 其他
**在线演示**: [https://www.blazor.zone/logout](https://www.blazor.zone/logout)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `ImageUrl` | `string?` | `}` | 获得/设置 组件当前用户头像 |
| `DisplayName` | `string?` | `}` | 获得/设置 组件当前用户显示名称 |
| `PrefixDisplayNameText` | `string?` | `}` | 获得/设置 组件当前用户显示名称前置文本 默认 欢迎 |
| `UserName` | `string?` | `}` | 获得/设置 组件当前用户登录账号 |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |
| `ShowUserName` | `bool` | `true` | 获得/设置 是否显示用户名 默认 true 显示 |
| `PrefixUserNameText` | `string?` | `}` | 获得/设置 组件当前用户登录账号前置文本 默认 当前账号 |
| `HeaderTemplate` | `RenderFragment?` | `}` | 获得/设置 组件 HeaderTemplate |
| `LinkTemplate` | `RenderFragment?` | `}` | 获得/设置 组件 LinkTemplate |
| `AvatarRadius` | `string?` | `}` | 获得/设置 组件头像边框圆角 默认 null 未设置 |

## 代码示例

### 基本用法

```razor
<Logout ImageUrl="@WebsiteOption.Value.GetAssetUrl("images/Argo.png")" DisplayName="Administrators" UserName="Admin">
        <i class="fa-fw fa-solid fa-user"></i>
        <span>@Localizer["LogoutsChildContentCustomDisplay"]</span>
    </Logout>
```

### 基本用法

```razor
<Logout ImageUrl="@WebsiteOption.Value.GetAssetUrl("images/Argo.png")" DisplayName="Administrators" UserName="Admin" class="bg-warning">
        <HeaderTemplate>
            <div class="d-flex flex-fill align-items-center">
                <img alt="avatar" src="@WebsiteOption.Value.GetAssetUrl("images/Argo-C.png")" style="border-radius: 50%;">
                <div class="flex-fill">
                    <div class="logout-dn">@Localizer["LogoutsHeaderTemplateUser1"]</div>
                    <div class="logout-un">@Localizer["LogoutsHeaderTemplateUser2"]</div>
                </div>
            </div>
        </HeaderTemplate>
    </Logout>
```

### 基本用法

```razor
<Logout ImageUrl="@WebsiteOption.Value.GetAssetUrl("images/Argo.png")" DisplayName="Administrators" UserName="Admin" class="bg-primary">
        <LinkTemplate>
            <a href="#">
                <i class="fa-solid fa-user"></i><span>@Localizer["LogoutsLinkTemplatePersonalCenter"]</span>
            </a>
            <a href="#">
                <i class="fa-solid fa-gear"></i><span>@Localizer["LogoutsLinkTemplateSetup"]</span>
            </a>
            <LogoutLink Url="/logouts" />
        </LinkTemplate>
    </Logout>
```
