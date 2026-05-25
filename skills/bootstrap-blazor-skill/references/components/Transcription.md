# Transcription (语音转文字)

## 概述

`Transcription` 组件用于**语音转文字**功能，支持实时语音识别和转写。

**主要特性**：
- 支持实时语音识别
- 支持多种语言识别
- 可显示识别结果
- 支持开始、停止、暂停操作
- 支持通过 `TranscriptionService` 服务控制

**在线演示**: https://www.blazor.zone/transcription

---

## 使用场景

### 1. 基础用法（语音转文字）

`Transcription` 组件可以通过 `@ref` 获取组件引用，然后调用相关方法。

```razor
<!-- 基础语音转文字 -->
<Transcription @ref="TranscriptionRef" />

<Button OnClick="StartTranscription">开始录音</Button>
<Button OnClick="StopTranscription">停止录音</Button>

@code {
    private Transcription? TranscriptionRef { get; set; }

    private void StartTranscription()
    {
        TranscriptionRef?.Start();
    }

    private void StopTranscription()
    {
        TranscriptionRef?.Stop();
    }
}
```

---

### 2. 显示识别结果（OnResult）

通过 `OnResult` 事件回调获取识别结果。

```razor
<!-- 显示识别结果 -->
<Transcription @ref="TranscriptionRef" OnResult="OnTranscriptionResult" />

<p>识别结果: @ResultText</p>

@code {
    private Transcription? TranscriptionRef { get; set; }
    private string ResultText { get; set; } = "";

    private void OnTranscriptionResult(string result)
    {
        ResultText = result;
    }

    private void StartTranscription()
    {
        TranscriptionRef?.Start();
    }
}
```

---

### 3. 设置语言（Language）

通过 `Language` 参数设置识别语言。

```razor
<!-- 中文识别 -->
<Transcription @ref="TranscriptionRef" Language="zh-CN" />

<!-- 英文识别 -->
<Transcription @ref="TranscriptionRef" Language="en-US" />

@code {
    private Transcription? TranscriptionRef { get; set; }
}
```

**常用语言代码**：
- `zh-CN` - 中文（简体）
- `en-US` - 英语（美国）
- `ja-JP` - 日语
- `ko-KR` - 韩语

---

### 4. 连续识别模式（Continuous）

通过设置 `Continuous="true"` 启用连续识别模式。

```razor
<!-- 连续识别 -->
<Transcription @ref="TranscriptionRef" Continuous="true" OnResult="OnResult" />

@code {
    private Transcription? TranscriptionRef { get; set; }

    private void OnResult(string result)
    {
        // 处理识别结果
        Console.WriteLine(result);
    }
}
```

---

### 5. 显示中间结果（InterimResults）

通过设置 `InterimResults="true"` 显示中间识别结果。

```razor
<!-- 显示中间结果 -->
<Transcription @ref="TranscriptionRef" InterimResults="true" OnResult="OnResult" />

@code {
    private Transcription? TranscriptionRef { get; set; }

    private void OnResult(string result)
    {
        // 处理中间结果
    }
}
```

---

## 参数 (Parameters)

### Transcription 组件参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Language` | `string?` | `null` | 获得/设置识别语言 |
| `Continuous` | `bool` | `false` | 获得/设置是否连续识别 |
| `InterimResults` | `bool` | `false` | 获得/设置是否显示中间结果 |
| `AutoStart` | `bool` | `false` | 获得/设置是否自动开始 |
| `ChildContent` | `RenderFragment?` | `null` | 子组件 |

---

## 事件回调 (EventCallbacks)

| 事件名 | 类型 | 说明 |
|--------|------|------|
| `OnResult` | `Func<string, Task>?` | 识别结果回调 |
| `OnError` | `Func<string, Task>?` | 错误回调 |
| `OnStart` | `Func<Task>?` | 开始录音回调 |
| `OnStop` | `Func<Task>?` | 停止录音回调 |

---

## 方法 (Methods)

### Transcription 组件方法

| 方法名 | 返回类型 | 说明 |
|--------|----------|------|
| `Start()` | `void` | 开始录音 |
| `Stop()` | `void` | 停止录音 |
| `Pause()` | `void` | 暂停录音 |
| `Resume()` | `void` | 恢复录音 |

---

## 最佳实践

1. **使用 @ref 获取组件引用**：通过 `@ref` 获取 `Transcription` 组件引用，然后调用 `Start()`、`Stop()` 等方法
2. **处理 OnResult 事件**：通过 `OnResult` 事件获取识别结果，更新 UI 或执行业务逻辑
3. **合理设置 Language**：根据用户语言设置正确的语言代码，提高识别准确率
4. **连续识别 vs 单次识别**：对于长语音，使用 `Continuous="true"` 连续识别；对于短语音，使用单次识别
5. **显示中间结果**：设置 `InterimResults="true"` 可以实时显示识别结果，提升用户体验
6. **错误处理**：处理 `OnError` 事件，对识别错误进行友好提示
7. **浏览器兼容性**：语音识别功能依赖浏览器支持，请确保在兼容的浏览器中使用（如 Chrome）
