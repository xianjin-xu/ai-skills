# Reconnector 重连组件

## 组件概述

Reconnector 是一个重连组件，用于自定义连接失败时各种状态信息。当 Blazor Server 连接断开时，组件会显示不同的状态模板。

## 使用方法

### 1. 在 _Layout.cshtml 文件中增加代码

```html
@RenderBody()

<div id="blazor-error-ui">
</div>

@* add ReconnectorOutlet component *@
<component type="typeof(ReconnectorOutlet)" param-AutoReconnect="true" render-mode="ServerPrerendered" />
```

**说明：**
- `AutoReconnect` 参数用于控制是否开启网络重连，默认 `true` 已开启
- 可以通过 `param-AutoReconnect="false"` 关闭自动重连

### 2. 在 App.razor 文件中增加代码

```razor
<Reconnector>
    <ReconnectingTemplate>
        <p>连接出现了一点小问题，需要重新连接。</p>
        <p>重新连接中，请稍后... 也可以立即 <a href="javascript:location.reload()">重新加载</a></p>
    </ReconnectingTemplate>
    <ReconnectFailedTemplate>
        <p>连接失败了，请确认网络是否正常。</p>
        <p>
            如果网络正常，你可以<a href="javascript:window.Blazor.reconnect()">重新连接</a>
            或者立即 <a href="javascript:location.reload()">重新加载</a>
        </p>
    </ReconnectFailedTemplate>
    <ReconnectRejectedTemplate>
        <p>所有的连接尝试都被拒绝了，这很有可能是由于网络问题或者服务器问题引起的。</p>
        <p>您可以尝试<a href="javascript:location.reload()">重新加载</a>服务器。如果是由于服务器问题引起的失败，重新连接可能不成功</p>
    </ReconnectRejectedTemplate>
</Reconnector>
```

**说明：**
- 可单独设置不同状态模板
- `ReconnectingTemplate` - 正在连接模板
- `ReconnectFailedTemplate` - 连接失败模板
- `ReconnectRejectedTemplate` - 连接拒绝模板

## 使用场景

### 1. 基础用法

使用默认模板。

```razor
<Reconnector />
```

**说明：**
- 组件内置了默认样式
- 如果不满意可根据自己需求进行样式覆盖
- 组件应用于 `components-reconnect-modal` 元素的 CSS 类

### 2. 自定义正在连接模板

自定义 `ReconnectingTemplate` 模板。

```razor
<Reconnector>
    <ReconnectingTemplate>
        <div class="connection-mask"></div>
        <div class="connection-body">
            <div class="row g-3">
                <div class="col-12 col-sm-5">
                    <h5>Bootstrap Blazor UI 组件库</h5>
                    <div class="mb-2">正在尝试重新连接服务器</div>
                    <div class="mb-2">服务器正在更新新版本，稍等一会儿即可提供服务</div>
                </div>
                <div class="col-12 col-sm-2">
                    <div class="d-flex align-items-center justify-content-center h-100">
                        <a href="javascript:window.Blazor.reconnect()" class="btn btn-primary">重新连接</a>
                    </div>
                </div>
            </div>
        </div>
    </ReconnectingTemplate>
</Reconnector>
```

### 3. 自定义连接失败模板

自定义 `ReconnectFailedTemplate` 模板。

```razor
<Reconnector>
    <ReconnectFailedTemplate>
        <div class="connection-mask"></div>
        <div class="connection-body">
            <div class="row g-3">
                <div class="col-12 col-sm-5">
                    <h5>Reconnector 组件</h5>
                    <div class="mb-2"><b>与服务器连接失败</b></div>
                    <div class="mb-2">请确认网络是否正常，或者 F12 打开 Developer tools 查看控制台是否有错误输出</div>
                </div>
                <div class="col-12 col-sm-2">
                    <div class="d-flex flex-column align-items-center justify-content-center h-100">
                        <a href="javascript:window.Blazor.reconnect()" class="btn btn-primary mb-2">重新连接</a>
                        <a href="javascript:location.reload()" class="btn btn-info">重新加载</a>
                    </div>
                </div>
            </div>
        </div>
    </ReconnectFailedTemplate>
</Reconnector>
```

### 4. 自定义连接拒绝模板

自定义 `ReconnectRejectedTemplate` 模板。

```razor
<Reconnector>
    <ReconnectRejectedTemplate>
        <div class="connection-mask"></div>
        <div class="connection-body">
            <div class="row g-3">
                <div class="col-12 col-sm-5">
                    <h5>Reconnector 组件</h5>
                    <div class="mb-2"><b>服务器拒绝连接</b></div>
                    <div class="mb-2">所有的连接尝试都被拒绝了，这很有可能是由于网络问题或者服务器问题引起的。</div>
                </div>
                <div class="col-12 col-sm-2">
                    <div class="d-flex flex-column align-items-center justify-content-center h-100">
                        <a href="javascript:location.reload()" class="btn btn-info">重新加载</a>
                    </div>
                </div>
            </div>
        </div>
    </ReconnectRejectedTemplate>
</Reconnector>
```

### 5. 完整示例

包含三种状态模板的完整实现。

```razor
<Reconnector>
    <ReconnectingTemplate>
        <div class="connection-mask"></div>
        <div class="connection-body">
            <div class="row g-3">
                <div class="col-12 col-sm-5">
                    <h5>Bootstrap Blazor UI 组件库</h5>
                    <div class="mb-2">基于 <b>Bootstrap</b> 样式的 <b>Blazor UI</b> 组件库</div>
                    <div class="mb-2">适配移动端支持各种主流浏览器，适配 <b>ABP</b>，同时支持 <b>NET6.0/NET7.0/NET8.0/NET9.0/NET10.0</b></div>
                </div>
                <div class="col-12 col-sm-5">
                    <h5>Reconnector 组件</h5>
                    <div class="mb-2"><b>正在尝试重新连接服务器</b></div>
                    <div class="mb-2">服务器正在更新新版本，稍等一会儿即可提供服务</div>
                </div>
                <div class="col-12 col-sm-2">
                    <div class="d-flex align-items-center justify-content-center h-100">
                        <a href="javascript:window.Blazor.reconnect()" class="btn btn-primary">重新连接</a>
                    </div>
                </div>
            </div>
        </div>
    </ReconnectingTemplate>
    
    <ReconnectFailedTemplate>
        <div class="connection-mask"></div>
        <div class="connection-body">
            <div class="row g-3">
                <div class="col-12 col-sm-5">
                    <h5>Bootstrap Blazor UI 组件库</h5>
                    <div class="mb-2">基于 <b>Bootstrap</b> 样式的 <b>Blazor UI</b> 组件库</div>
                </div>
                <div class="col-12 col-sm-5">
                    <h5>Reconnector 组件</h5>
                    <div class="mb-2"><b>与服务器连接失败</b></div>
                    <div class="mb-2">请确认网络是否正常</div>
                </div>
                <div class="col-12 col-sm-2">
                    <div class="d-flex flex-column align-items-center justify-content-center h-100">
                        <a href="javascript:window.Blazor.reconnect()" class="btn btn-primary mb-2">重新连接</a>
                        <a href="javascript:location.reload()" class="btn btn-info">重新加载</a>
                    </div>
                </div>
            </div>
        </div>
    </ReconnectFailedTemplate>
    
    <ReconnectRejectedTemplate>
        <div class="connection-mask"></div>
        <div class="connection-body">
            <div class="row g-3">
                <div class="col-12 col-sm-5">
                    <h5>Bootstrap Blazor UI 组件库</h5>
                    <div class="mb-2">基于 <b>Bootstrap</b> 样式的 <b>Blazor UI</b> 组件库</div>
                </div>
                <div class="col-12 col-sm-5">
                    <h5>Reconnector 组件</h5>
                    <div class="mb-2"><b>服务器拒绝连接</b></div>
                    <div class="mb-2">所有的连接尝试都被拒绝了</div>
                </div>
                <div class="col-12 col-sm-2">
                    <div class="d-flex flex-column align-items-center justify-content-center h-100">
                        <a href="javascript:location.reload()" class="btn btn-info">重新加载</a>
                    </div>
                </div>
            </div>
        </div>
    </ReconnectRejectedTemplate>
</Reconnector>
```

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `AutoReconnect` | 获得/设置 是否自动尝试重连 | `bool` | `true` |
| `ReconnectInterval` | 获得/设置 自动重连间隔（毫秒） | `int` | `5000` |
| `ReconnectingTemplate` | 获得/设置 正在连接模板 | `RenderFragment` | - |
| `ReconnectFailedTemplate` | 获得/设置 连接失败模板 | `RenderFragment` | - |
| `ReconnectRejectedTemplate` | 获得/设置 连接拒绝模板 | `RenderFragment` | - |

## CSS 类

组件内置了默认样式，如果不满意可根据自己需求进行样式覆盖。组件应用于 `components-reconnect-modal` 元素的 CSS 类：

| CSS 类 | 说明 |
|-------|------|
| `components-reconnect-show` | 连接已丢失。客户端正在尝试重新连接。显示模式。 |
| `components-reconnect-hide` | 将为服务器重新建立活动连接。隐藏模式。 |
| `components-reconnect-failed` | 重新连接失败，可能是由于网络故障引起的。若要尝试重新连接，请在 JavaScript 中调用 `window.Blazor.reconnect()` |
| `components-reconnect-rejected` | 已拒绝重新连接。已达到服务器，但拒绝连接，服务器上的用户状态丢失。若要重新加载应用，请在 JavaScript 中调用 `location.reload()`。当出现以下情况时，可能会导致此连接状态：服务器端线路发生故障；客户端断开连接的时间足以使服务器删除用户的状态；服务器已重启，或者应用的工作进程被回收。 |

## 最佳实践

1. **三种状态**：确保实现所有三种状态模板（正在连接、连接失败、连接拒绝）
2. **用户友好**：在模板中提供清晰的信息和操作按钮（重新连接、重新加载）
3. **样式自定义**：通过 CSS 覆盖默认样式以匹配应用设计
4. **自动重连**：保持 `AutoReconnect="true"` 以自动尝试重连
5. **重连间隔**：根据需求调整 `ReconnectInterval` 参数（默认 5000 毫秒）

## 常见问题

**Q: 如何关闭自动重连？**
A: 在 _Layout.cshtml 中设置 `param-AutoReconnect="false"`。

**Q: 如何自定义模板样式？**
A: 通过 CSS 覆盖 `components-reconnect-modal` 元素的样式类。

**Q: 重新连接和重新加载有什么区别？**
A: 重新连接（`window.Blazor.reconnect()`）尝试恢复现有连接；重新加载（`location.reload()`）完全重新加载页面。

**Q: 什么时候会触发连接拒绝状态？**
A: 当服务器端线路发生故障、客户端断开连接时间太长、服务器重启或工作进程被回收时。

**Q: 如何在 JavaScript 中手动触发重连？**
A: 调用 `window.Blazor.reconnect()` 方法。

## 版本历史

- **初始版本**: 支持三种连接状态模板、自动重连、自定义间隔、CSS 样式覆盖等功能
