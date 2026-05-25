# Typed (打字动画)

## 概述

`Typed` 组件用于**创建打字机效果的文字动画**，文字逐个显示，模拟打字效果。

**主要特性**：
- 支持打字速度控制
- 支持光标样式自定义
- 支持循环播放
- 支持暂停/继续
- 可自定义打字内容

**在线演示**: https://www.blazor.zone/typed

---

## 使用场景

### 1. 基础用法（简单打字效果）

`Typed` 组件可以通过 `Text` 参数设置打字内容。

```razor
<!-- 基础打字效果 -->
<Typed Text="欢迎使用 Bootstrap Blazor!" />

<p>上方会显示打字机效果的文字</p>
```

---

### 2. 控制打字速度（Speed）

通过 `Speed` 参数设置打字速度（毫秒/字符）。

```razor
<!-- 快速打字（50ms/字符） -->
<Typed Text="快速打字效果" Speed="50" />

<!-- 慢速打字（200ms/字符） -->
<Typed Text="慢速打字效果" Speed="200" />
```

---

### 3. 循环播放（Loop）

通过设置 `Loop="true"` 启用循环播放。

```razor
<!-- 循环打字效果 -->
<Typed Text="这段文字会循环显示" Loop="true" />
```

---

### 4. 自定义光标（CursorChar、CursorBlink）

通过 `CursorChar` 和 `CursorBlink` 参数自定义光标样式。

```razor
<!-- 自定义光标为下划线 -->
<Typed Text="自定义光标" CursorChar="_" />

<!-- 光标不闪烁 -->
<Typed Text="光标不闪烁" CursorBlink="false" />
```

**CursorChar 常用值**：
- `|` - 竖线（默认）
- `_` - 下划线
- `▋` - 方块

---

### 5. 多行打字（Lines）

通过 `Lines` 参数设置多行打字内容。

```razor
<!-- 多行打字效果 -->
<Typed Lines="@TypedLines" />

@code {
    private List<string> TypedLines { get; set; } = new List<string>
    {
        "第一行文字",
        "第二行文字",
        "第三行文字"
    };
}
```

---

### 6. 暂停/继续控制（@ref）

通过 `@ref` 获取组件引用，调用 `Start()`、`Stop()`、`Pause()`、`Resume()` 方法。

```razor
<!-- 可控的打字效果 -->
<Typed @ref="TypedRef" Text="可控的打字效果" AutoStart="false" />

<Button OnClick="StartTyped">开始</Button>
<Button OnClick="PauseTyped">暂停</Button>
<Button OnClick="ResumeTyped">继续</Button>
<Button OnClick="StopTyped">停止</Button>

@code {
    private Typed? TypedRef { get; set; }

    private void StartTyped() => TypedRef?.Start();
    private void PauseTyped() => TypedRef?.Pause();
    private void ResumeTyped() => TypedRef?.Resume();
    private void StopTyped() => TypedRef?.Stop();
}
```

---

## 参数 (Parameters)

### Typed 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Text` | `string?` | `null` | 获得/设置打字内容（单行） |
| `Lines` | `List<string>?` | `null` | 获得/设置打字内容（多行） |
| `Speed` | `int` | `100` | 获得/设置打字速度（毫秒/字符） |
| `Loop` | `bool` | `false` | 获得/设置是否循环播放 |
| `CursorChar` | `string` | `\|` | 获得/设置光标字符 |
| `CursorBlink` | `bool` | `true` | 获得/设置光标是否闪烁 |
| `AutoStart` | `bool` | `true` | 获得/设置是否自动开始 |
| `ShowCursor` | `bool` | `true` | 获得/设置是否显示光标 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnComplete` | `Func<Task>?` | 打字完成回调 |

---

## 方法 (Methods)

### Typed 组件方法

| 方法名 | 返回类型 | 说明 |
|--------|----------|------|
| `Start()` | `void` | 开始打字 |
| `Stop()` | `void` | 停止打字 |
| `Pause()` | `void` | 暂停打字 |
| `Resume()` | `void` | 继续打字 |

---

## 最佳实践

1. **合理使用 Speed**：快速展示用 50-100ms，慢速展示用 150-200ms
2. **多行内容用 Lines**：多行打字效果使用 `Lines` 参数，而不是多个 `Typed` 组件
3. **控制循环播放**：需要重复展示时使用 `Loop="true"`，否则打字完成后会停止
4. **自定义光标样式**：通过 `CursorChar` 和 `CursorBlink` 自定义光标，提升视觉效果
5. **处理 OnComplete 事件**：打字完成后需要执行逻辑时，处理 `OnComplete` 事件
6. **与 Typewriter 的区别**：`Typed` 是打字机效果组件，`Typewriter` 可能不存在或功能类似，以官方文档为准
