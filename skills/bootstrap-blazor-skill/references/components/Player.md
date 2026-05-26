# Player 音视频播放器

## 组件概述

Player 组件是一个简单、可访问和可定制的媒体播放器，支持视频、音频、YouTube 和 Vimeo。本组件依赖于 `BootstrapBlazor.Player`，使用本组件时需要引用其组件包。

**依赖安装：**

```bash
dotnet add package BootstrapBlazor.Player
```

或

```xml
<PackageReference Include="BootstrapBlazor.Player" Version="10.0.1" />
```

## 使用场景

### 1. 基础用法

通过回调方法 `OnInitAsync` 设置组件所需要的配置实例 `PlayerOption`。通过 `PlayerOption` 属性值对播放器进行设置。

```razor
<Player OnInitAsync="OnPlayerInit" />
```

```csharp
@code {
    private Task OnPlayerInit(PlayerOption option)
    {
        option.AutoPlay = true;
        option.Url = "https://example.com/video.mp4";
        return Task.CompletedTask;
    }
}
```

**说明：**
- 通过 `OnInitAsync` 回调方法配置播放器选项
- `PlayerOption` 包含播放器的各种配置属性
- 支持自动播放、循环播放、静音等多种配置

### 2. 播放视频文件

播放本地或远程的视频文件。

```razor
<Player OnInitAsync="OnVideoInit" />
```

```csharp
@code {
    private Task OnVideoInit(PlayerOption option)
    {
        option.Url = "https://example.com/movie.mp4";
        option.AutoPlay = false;
        option.Controls = true;
        option.Preload = "auto";
        return Task.CompletedTask;
    }
}
```

**支持的视频格式：**
- MP4 (.mp4)
- WebM (.webm)
- OGG (.ogv)
- AVI (.avi)
- MOV (.mov)

### 3. HLS 支持

通过设置 `IsHls="true"` 开启 HLS (HTTP Live Streaming) 支持，适用于直播流媒体。

```razor
<Player IsHls="true" OnInitAsync="OnHlsInit" />
```

```csharp
@code {
    private Task OnHlsInit(PlayerOption option)
    {
        option.Url = "https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8";
        option.AutoPlay = true;
        return Task.CompletedTask;
    }
}
```

**说明：**
- HLS 是一种用于流媒体的协议，特别适合直播场景
- 需要设置 `IsHls="true"` 来启用 HLS 支持
- URL 应该指向 `.m3u8` 播放列表文件

### 4. YouTube 支持

通过设置 `Mode="PlayerSources"` 参数 `Provider="youtube"` 播放 YouTube 视频。

```razor
<Player Mode="PlayerMode.PlayerSources" Provider="PlayerProvider.YouTube" VideoId="dQw4w9WgXcQ" />
```

**说明：**
- `VideoId` 参数是 YouTube 视频的 ID（URL 中 `v=` 后面的值）
- 支持 YouTube 的所有功能，包括字幕、播放列表等
- 需要网络连接访问 YouTube 服务器

### 5. Vimeo 支持

通过设置 `Mode="PlayerSources"` 参数 `Provider="vimeo"` 播放 Vimeo 视频。

```razor
<Player Mode="PlayerMode.PlayerSources" Provider="PlayerProvider.Vimeo" VideoId="148751763" />
```

**说明：**
- `VideoId` 参数是 Vimeo 视频的 ID（URL 中的数字部分）
- 支持 Vimeo 的所有功能，包括高清播放、字幕等
- 需要网络连接访问 Vimeo 服务器

### 6. 音频播放器

通过设置 `Mode="PlayerMode.Audio"` 播放音频文件。

```razor
<Player Mode="PlayerMode.Audio" OnInitAsync="OnAudioInit" />
```

```csharp
@code {
    private Task OnAudioInit(PlayerOption option)
    {
        option.Url = "https://example.com/audio.mp3";
        option.AutoPlay = false;
        option.Controls = true;
        option.Loop = true;
        return Task.CompletedTask;
    }
}
```

**支持的音频格式：**
- MP3 (.mp3)
- WAV (.wav)
- OGG (.ogg)
- AAC (.aac)
- FLAC (.flac)

### 7. 自定义播放器事件

通过 `OnEvent` 参数处理播放器的客户端事件。

```razor
<Player OnInitAsync="OnPlayerInit" OnEvent="OnPlayerEvent" />
```

```csharp
@code {
    private Task OnPlayerInit(PlayerOption option)
    {
        option.Url = "https://example.com/video.mp4";
        return Task.CompletedTask;
    }
    
    private Task OnPlayerEvent(string eventName)
    {
        Console.WriteLine($"Player event: {eventName}");
        return Task.CompletedTask;
    }
}
```

**常用事件：**
- `play` - 开始播放
- `pause` - 暂停播放
- `ended` - 播放结束
- `timeupdate` - 播放时间更新
- `volumechange` - 音量变化

## 组件参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Id` | 获得/设置 组件 id 属性 | `string` | - |
| `Mode` | 获得/设置 组件模式 | `PlayerMode` | - |
| `Options` | 获得/设置 PlayerOption 实例 | `PlayerOptions` | - |
| `OnEvent` | 获取或设置客户端事件回调 | `Func<string, Task>` | `null` |
| `AdditionalAttributes` | 获得/设置 用户自定义属性 | `IDictionary<string, Object>` | - |

## PlayerMode 枚举

| 值 | 说明 |
|-----|------|
| `Video` | 视频播放模式（默认） |
| `Audio` | 音频播放模式 |
| `PlayerSources` | 多源播放模式（用于 YouTube、Vimeo 等） |

## PlayerProvider 枚举

| 值 | 说明 |
|-----|------|
| `Html5` | HTML5 原生播放（默认） |
| `YouTube` | YouTube 视频 |
| `Vimeo` | Vimeo 视频 |

## PlayerOption 配置属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `Url` | 媒体文件 URL | `string` | - |
| `AutoPlay` | 是否自动播放 | `bool` | `false` |
| `Controls` | 是否显示控制栏 | `bool` | `true` |
| `Loop` | 是否循环播放 | `bool` | `false` |
| `Muted` | 是否静音 | `bool` | `false` |
| `Preload` | 预加载策略 | `string` | `auto` |
| `Poster` | 视频封面图片 URL | `string` | - |
| `Volume` | 音量 (0-1) | `double` | `1.0` |

## 最佳实践

1. **自动播放策略**：现代浏览器通常阻止自动播放，建议设置 `AutoPlay=false` 或用户交互后播放
2. **预加载策略**：对于大型视频文件，使用 `Preload="metadata"` 只加载元数据
3. **多格式支持**：提供多种格式的视频源以提高兼容性
4. **封面图片**：设置 `Poster` 属性提供视频封面，改善用户体验
5. **错误处理**：监听播放事件，处理加载失败等错误情况

## 常见问题

**Q: 为什么视频无法自动播放？**
A: 现代浏览器通常阻止自动播放，特别是带有声音的视频。可以设置 `Muted=true` 允许自动播放，或者让用户点击播放按钮。

**Q: 如何支持多种视频格式？**
A: 在 `OnInitAsync` 中配置多个数据源，或使用 `PlayerSources` 模式提供多个源。

**Q: 如何获取当前播放时间？**
A: 监听 `timeupdate` 事件，通过 JavaScript 互操作获取当前播放时间。

**Q: YouTube 视频无法播放怎么办？**
A: 检查 VideoId 是否正确，确保网络连接正常，某些地区可能无法访问 YouTube。

**Q: 如何自定义播放器样式？**
A: 通过 CSS 覆盖播放器的样式类，或使用 `AdditionalAttributes` 添加自定义属性。

## 版本历史

- **10.0.1**: 初始版本，支持视频、音频、YouTube、Vimeo 播放，HLS 流媒体支持
