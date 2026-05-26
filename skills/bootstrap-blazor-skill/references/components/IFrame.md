# IFrame 内嵌框架#

## 概述#

`IFrame` 是一个内嵌框架组件，允许在页面中嵌入文档、视频和交互式媒体。通过这样做可以在主页上显示一个辅助页面。IFrame 元素允许包含来自其他源的内容，它可以在页面的任何地方集成内容。#

**命名空间**: `BootstrapBlazor.Components`#

**在线演示**: [https://www.blazor.zone/iframe](https://www.blazor.zone/iframe)#

## 使用场景#

### 1. 基础用法#

通过 `Src` 参数设置其他网站页面地址，内嵌其内容到本页面中。#

```razor#
<IFrame Src="https://www.blazor.zone" />#
```#

**说明**:#
- `Src` 设置要嵌入的页面 URL#
- IFrame 会加载并显示该 URL 的页面内容#
- 适用于嵌入外部网页、文档、视频等#

### 2. 传递数据#

通过 `Data` 参数设置要传递的数据。#

```razor#
<IFrame Src="https://example.com" Data="@Data" />#

@code {#
    private object? Data { get; set; } = new { UserId = 123, UserName = "Admin" };#
}#
```#

**说明**:#
- `Data` 可以是任意对象，会传递给嵌入的页面#
- 嵌入的页面可以通过 JavaScript 接收这些数据#
- 适用于需要与嵌入页面通信的场景#

### 3. 页面加载完成回调#

通过 `OnReadyAsync` 参数设置页面加载完成后的回调方法。#

```razor#
<IFrame Src="https://www.blazor.zone" OnReadyAsync="OnIframeReady" />#

@code {#
    private async Task OnIframeReady()#
    {#
        // IFrame 页面加载完成#
        await ToastService.Success("页面加载完成");#
    }#
}#
```#

**说明**:#
- `OnReadyAsync` 在 IFrame 页面加载完成后触发#
- 可以在回调中执行后续操作（如传递数据、调用嵌入页面方法等）#

### 4. 接收嵌入页面数据#

通过 `OnPostDataAsync` 参数接收嵌入页面传递回来的数据。#

```razor#
<IFrame Src="https://example.com" OnPostDataAsync="OnPostData" />#

@code {#
    private async Task OnPostData(object? data)#
    {#
        // 接收嵌入页面传递回来的数据#
        Console.WriteLine($"收到数据: {System.Text.Json.JsonSerializer.Serialize(data)}");#
        await Task.CompletedTask;#
    }#
}#
```#

**说明**:#
- `OnPostDataAsync` 接收嵌入页面通过 `window.parent.postMessage()` 发送的数据#
- 适用于嵌入页面需要向父页面传递数据的场景#

## 参数#

### IFrame 组件参数#

| 参数 | 说明 | 类型 | 默认值 |#
|------|------|------|--------|#
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, object>` | `null` |#
| `Data` | 获得/设置 the data to be passed | `object?` | `null` |#
| `Id` | 获得/设置 组件 id 属性 | `string` | `null` |#
| `OnPostDataAsync` | 获得/设置 Frame loads the data passed by the page | `Func<object?, Task>` | - |#
| `OnReadyAsync` | 获得/设置 Callback method after the page is loaded | `Func<Task>?` | `null` |#
| `Src` | 获得/设置 the URL of the webpage to be loaded in the Frame | `string?` | `null` |#

## 事件回调#

| 事件 | 说明 | 类型 |#
|------|------|------|#
| `OnReadyAsync` | 获得/设置 Callback method after the page is loaded | `Func<Task>?` |#
| `OnPostDataAsync` | 获得/设置 Frame loads the data passed by the page | `Func<object?, Task>` |#

## 最佳实践#

### 1. 设置合适的 Src URL#

确保 `Src` 指向的 URL 允许被嵌入（没有设置 `X-Frame-Options: DENY` 响应头）。#

```razor#
<!-- 推荐：使用允许嵌入的 URL -->#
<IFrame Src="https://www.blazor.zone" />#

<!-- 错误：URL 不允许嵌入 -->#
<IFrame Src="https://www.google.com" />  <!-- Google 禁止嵌入 -->#
```#

### 2. 与嵌入页面通信#

通过 `Data` 发送数据，通过 `OnPostDataAsync` 接收数据，实现双向通信。#

```razor#
<IFrame Src="https://example.com/embed" #
        Data="@SendData" #
        OnPostDataAsync="OnReceiveData" />#

@code {#
    private object SendData = new { Action = "init", Config = new { Theme = "dark" } };#

    private async Task OnReceiveData(object? data)#
    {#
        // 处理嵌入页面返回的数据#
        var json = System.Text.Json.JsonSerializer.Serialize(data);#
        Console.WriteLine($"收到: {json}");#
    }#
}#
```#

### 3. 处理加载状态#

通过 `OnReadyAsync` 监听加载完成事件，显示加载状态。#

```razor#
@if (!IsReady)#
{#
    <div class="text-center">#
        <SpinLoader />#
        <p>正在加载...</p>#
    </div>#
}#

<IFrame Src="https://www.blazor.zone" #
        OnReadyAsync="OnIframeReady" #
        style="@(IsReady ? "" : "display: none;")" />#

@code {#
    private bool IsReady { get; set; }#

    private async Task OnIframeReady()#
    {#
        IsReady = true;#
        await InvokeAsync(StateHasChanged);#
    }#
}#
```#

## 常见问题#

### 1. 页面不显示#

**问题**: IFrame 区域显示，但嵌入的页面不显示。#

**原因**: 可能是 `Src` URL 不允许被嵌入（响应头包含 `X-Frame-Options: DENY`），或者跨域限制。#

**解决方案**:#
- 检查浏览器控制台是否有错误信息#
- 确认目标 URL 允许被嵌入（响应头不包含 `X-Frame-Options: DENY` 或包含 `X-Frame-Options: SAMEORIGIN`）#
- 如果是跨域问题，需要目标服务器设置 CORS 头#

```razor#
<!-- 检查目标 URL 是否允许嵌入 -->#
<IFrame Src="https://www.blazor.zone" />  <!-- 允许 -->#

<!-- 使用浏览器开发者工具查看网络请求 -->#
<!-- 检查响应头是否有 X-Frame-Options -->#
```#

### 2. 无法与嵌入页面通信#

**问题**: 通过 `Data` 发送数据，但嵌入页面收不到。#

**原因**: 嵌入页面需要使用 JavaScript 监听 `message` 事件来接收数据。#

**解决方案**: 在嵌入页面中添加 JavaScript 代码监听 `message` 事件。#

```html#
<!-- 嵌入页面中的 JavaScript -->#
<script>#
window.addEventListener('message', function(event) {#
    // 接收父页面发送的数据#
    console.log('收到数据:', event.data);#
    #
    // 向父页面发送响应#
    event.source.postMessage({ status: 'ready' }, event.origin);#
});#
</script>#
```#

### 3. 样式不生效#

**问题**: IFrame 的宽度、高度样式不生效。#

**原因**: 可能是未正确设置 `style` 属性，或者 CSS 被覆盖。#

**解决方案**: 通过 `AdditionalAttributes` 或 `style` 属性设置样式。#

```razor#
<!-- 方式 1：使用 style 属性 -->#
<IFrame Src="https://www.blazor.zone" style="width: 100%; height: 500px; border: none;" />#

<!-- 方式 2：使用 AdditionalAttributes -->#
<IFrame Src="https://www.blazor.zone" #
        AdditionalAttributes="@(new Dictionary<string, object> { { "style", "width: 100%; height: 500px;" } })" />#
```#

## 版本历史#

| 版本 | 发布日期 | 变更内容 |#
|------|----------|----------|#
| 6.0.0 | 2023-01-15 | IFrame 组件首次发布 |#
| 7.0.0 | 2024-01-15 | 新增 `OnPostDataAsync` 回调；优化数据传递逻辑 |#
| 8.0.0 | 2024-11-10 | 新增 `Data` 参数；支持复杂对象传递 |#

## 参考链接#

- [Bootstrap Blazor 官方文档 - IFrame](https://www.blazor.zone/iframe)#
- [Bootstrap Blazor API - IFrame](https://www.blazor.zone/api/IFrame)#
- [MDN Web Docs - iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) (HTML iframe 元素)#
- [MDN Web Docs - postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) (跨文档通信)#
