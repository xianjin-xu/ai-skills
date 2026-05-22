# Modal

## 概述

Modal 组件

> Modal component

**分类**: 反馈
**在线演示**: [https://www.blazor.zone/modal](https://www.blazor.zone/modal)

## 参数 (Parameters)

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsBackdrop` | `bool` | `}` | 获得/设置 是否在后台关闭弹出窗口，默认为 false |
| `IsKeyboard` | `bool` | `true` | 获得/设置 是否启用键盘支持，默认为 true 响应 ESC 键 |
| `IsFade` | `bool?` | `}` | 获得/设置 是否启用淡入淡出动画，默认为 null |
| `ChildContent` | `RenderFragment?` | `}` | 获得/设置 子组件 |
| `Task` | `Func<Modal,` | `}` | 获得/设置 组件完成渲染时的回调方法 |
| `OnShownAsync` | `Func<Task>?` | `}` | 获得/设置 弹出窗口显示时的回调方法 |
| `OnCloseAsync` | `Func<Task>?` | `}` | - |
| `OnClosingAsync` | `Func<Task<bool>>?` | `}` | - |

## 代码示例

### 基本用法

```razor
<Modal @ref="Modal" IsKeyboard="true">
        <ModalDialog Title="@Localizer["ModalsNormalDefaultPopup"]" ShowSaveButton="true" OnSaveAsync="OnSaveAsync">
            <BodyTemplate>
                <div>@Localizer["ModalsNormalDefaultPopupText"]</div>
            </BodyTemplate>
        </ModalDialog>
    </Modal>
```

### 基本用法

```razor
<Modal @ref="BackdropModal" IsBackdrop="true">
        <ModalDialog Title="@Localizer["ModalsIsBackdropToClose"]">
            <BodyTemplate>
                <div>@Localizer["ModalsTitlePopupWindowText"]</div>
            </BodyTemplate>
        </ModalDialog>
    </Modal>
```

### 基本用法

```razor
<Modal @ref="SmallModal">
        <ModalDialog Size="Size.Small" ShowResize="true" Title="@Localizer["ModalsResize"]">
            <BodyTemplate>
                <div>@Localizer["ModalsTitlePopupWindowText"]</div>
            </BodyTemplate>
        </ModalDialog>
    </Modal>
```

### 基本用法

```razor
<Modal @ref="CenterModal">
        <ModalDialog IsCentered="true" Title="@Localizer["ModalsVerticallyCenteredPopup"]">
            <BodyTemplate>
                <div>@Localizer["ModalsTitlePopupWindowText"]</div>
            </BodyTemplate>
        </ModalDialog>
    </Modal>
```

### 基本用法

```razor
<Modal @ref="LongContentModal">
                <ModalDialog IsCentered="true" Title="@Localizer["ModalsVeryLongContent"]">
                    <BodyTemplate>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                    </BodyTemplate>
                </ModalDialog>
            </Modal>
<Modal @ref="ScrollModal">
                <ModalDialog IsCentered="true" IsScrolling="true" Title="@Localizer["ModalsScrollBarPopup"]" ShowExportPdfButtonInHeader="true">
                    <BodyTemplate>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                        <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                        <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
                    </BodyTemplate>
                </ModalDialog>
            </Modal>
```
