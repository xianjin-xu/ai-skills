# Timer (计时器)

## 概述

`Timer` 组件用于**倒计时或正计时**功能。支持开始、暂停、重置等操作。

**主要特性**：
- 支持倒计时（Countdown）和正计时（Stopwatch）两种模式
- 可设置初始时间（InitialValue）
- 可设置时间间隔（Interval）
- 支持开始、暂停、重置操作
- 可显示时、分、秒、毫秒
- 支持通过 `TimerState` 获取计时器状态

**在线演示**: https://www.blazor.zone/timer

---

## 使用场景

### 1. 基础用法（正计时）

`Timer` 组件可以用于正计时（从 0 开始计时）。

```razor
<!-- 正计时器 -->
<Timer @ref="TimerRef" />

<Button OnClick="StartTimer">开始</Button>
<Button OnClick="PauseTimer">暂停</Button>
<Button OnClick="ResetTimer">重置</Button>

@code {
    private Timer? TimerRef { get; set; }

    private void StartTimer()
    {
        TimerRef?.Start();
    }

    private void PauseTimer()
    {
        TimerRef?.Pause();
    }

    private void ResetTimer()
    {
        TimerRef?.Reset();
    }
}
```

---

### 2. 倒计时模式（Countdown）

通过设置 `IsCountdown="true"` 启用倒计时模式。

```razor
<!-- 倒计时器 -->
<Timer @ref="CountdownTimer" IsCountdown="true" InitialValue="300" />

<Button OnClick="StartCountdown">开始倒计时</Button>
<Button OnClick="PauseCountdown">暂停</Button>
<Button OnClick="ResetCountdown">重置</Button>

@code {
    private Timer? CountdownTimer { get; set; }

    private void StartCountdown()
    {
        CountdownTimer?.Start();
    }

    private void PauseCountdown()
    {
        CountdownTimer?.Pause();
    }

    private void ResetCountdown()
    {
        CountdownTimer?.Reset();
    }
}
```

**说明**：`InitialValue="300"` 表示倒计时 300 秒（5 分钟）。

---

### 3. 自定义显示格式（Format）

通过 `Format` 参数设置显示格式。

```razor
<!-- 自定义格式：仅显示分:秒 -->
<Timer @ref="TimerRef" Format="mm:ss" />

@code {
    private Timer? TimerRef { get; set; }
}
```

**常用格式**：
- `hh:mm:ss` - 时:分:秒（默认）
- `mm:ss` - 分:秒
- `ss` - 秒
- `hh:mm:ss.fff` - 时:分:秒.毫秒

---

### 4. 设置时间间隔（Interval）

通过 `Interval` 参数设置计时器更新的时间间隔（毫秒）。

```razor
<!-- 每 100 毫秒更新一次 -->
<Timer @ref="TimerRef" Interval="100" />

@code {
    private Timer? TimerRef { get; set; }
}
```

---

### 5. 获取计时器状态（TimerState）

通过 `TimerState` 属性获取计时器的当前状态。

```razor
<!-- 显示计时器状态 -->
<Timer @ref="TimerRef" OnTick="OnTimerTick" />

<p>当前时间: @CurrentTime</p>

@code {
    private Timer? TimerRef { get; set; }
    private string CurrentTime { get; set; } = "00:00:00";

    private void OnTimerTick(TimerState state)
    {
        CurrentTime = state.Elapsed.ToString(@"hh\:mm\:ss");
    }
}
```

---

## 参数 (Parameters)

### Timer 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `IsCountdown` | `bool` | `false` | 获得/设置是否倒计时模式 |
| `InitialValue` | `double` | `0` | 获得/设置初始值（秒） |
| `Format` | `string?` | `null` | 获得/设置显示格式 |
| `Interval` | `int` | `1000` | 获得/设置时间间隔（毫秒） |
| `AutoStart` | `bool` | `false` | 获得/设置是否自动开始 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnTick` | `Func<TimerState, Task>?` | 计时器 tick 回调 |
| `OnTimeout` | `Func<Task>?` | 倒计时结束回调 |

---

## 方法 (Methods)

### Timer 组件方法

| 方法名 | 返回类型 | 说明 |
|--------|----------|------|
| `Start()` | `void` | 开始计时 |
| `Pause()` | `void` | 暂停计时 |
| `Reset()` | `void` | 重置计时器 |
| `Stop()` | `void` | 停止计时 |

---

## 状态类 (TimerState)

`TimerState` 类包含计时器的当前状态信息。

| 属性名 | 类型 | 说明 |
|--------|------|------|
| `Elapsed` | `TimeSpan` | 获得已过时间 |
| `IsRunning` | `bool` | 获得是否正在运行 |
| `IsCountdown` | `bool` | 获得是否倒计时模式 |
| `Remaining` | `TimeSpan` | 获得剩余时间（倒计时模式） |

---

## 最佳实践

1. **使用 @ref 获取组件引用**：通过 `@ref` 获取 `Timer` 组件引用，然后调用 `Start()`、`Pause()`、`Reset()` 方法
2. **合理设置 Interval**：正计时通常设置 1000（1 秒），倒计时可以设置更小的值（如 100）以获得更精确的显示
3. **处理 OnTimeout 事件**：倒计时结束时，处理 `OnTimeout` 事件执行相应操作（如提示用户）
4. **格式化显示**：使用 `Format` 参数控制显示格式，避免显示过多不必要的信息
5. **避免内存泄漏**：在组件销毁时，确保计时器已停止（通常在 `Dispose` 方法中调用 `Stop()`）
