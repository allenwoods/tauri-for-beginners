# 从 Rust 调用前端

在 Tauri 应用程序中，Rust 可以通过 Tauri 事件系统、通道或直接执行 JavaScript 代码与前端通信。

## 事件系统

Tauri 提供了一个简单的事件系统，用于 Rust 和前端之间的双向通信。该系统非常适合涉及小数据流或多生产者、多消费者模式（如推送通知）的场景。

但是，事件系统不适合低延迟或高吞吐量要求。

Tauri 命令和事件之间的主要区别包括事件缺乏强类型支持、JSON 字符串负载不适合大消息，以及不支持用于细粒度控制的 capabilities 系统。

AppHandle 和 WebviewWindow 类型为事件系统实现了 Listener 和 Emitter 特征。

事件可以是全局的（发送给所有监听器）或特定于 webview（发送给特定 webview 中的监听器）。

#### 全局事件

要发出全局事件，使用 emit 函数：

```rust
use tauri::{AppHandle, Emitter};
#[tauri::command]
fn download(app: AppHandle, url: String) {
    app.emit("download-started", &url).unwrap();
    for progress in [1, 15, 50, 80, 100] {
        app.emit("download-progress", progress).unwrap();
    }
    app.emit("download-finished", &url).unwrap();
}
```

需要注意的是，全局事件会发送给**所有**监听器。

#### Webview 事件

要向特定的 webview 监听器发出事件，使用 emit_to 函数：

```rust
use tauri::{AppHandle, Emitter};
#[tauri::command]
fn login(app: AppHandle, user: String, password: String) {
    let authenticated = user == "tauri-apps" && password == "tauri";
    let result = if authenticated { "loggedIn" } else { "invalidCredentials" };
    app.emit_to("login", "login-result", result).unwrap();
}
```

要向多个 webview 发出事件，使用 emit_filter：

```rust
use tauri::{AppHandle, Emitter, EventTarget};
#[tauri::command]
fn open_file(app: AppHandle, path: std::path::PathBuf) {
    app.emit_filter("open-file", path, |target| match target {
        EventTarget::WebviewWindow { label } => label == "main" || label == "file-
viewer",
        _ => false,
    }).unwrap();
}
```

特定于 webview 的事件**不会**发送给全局事件监听器。使用 listen_any 来捕获所有事件。

### 事件负载

事件负载可以是任何实现 Clone 的 Serialize 类型。这是一个增强的下载事件示例：

```rust
use tauri::{AppHandle, Emitter};
use serde::Serialize;
#[derive(Clone, Serialize)]
#[serde(rename_all = "camelCase")]
struct DownloadStarted<'a> {
    url: &'a str,
    download_id: usize,
    content_length: usize,
}
#[derive(Clone, Serialize)]
#[serde(rename_all = "camelCase")]
struct DownloadProgress {
    download_id: usize,
    chunk_length: usize,
}
#[derive(Clone, Serialize)]
#[serde(rename_all = "camelCase")]
struct DownloadFinished {
    download_id: usize,
}
#[tauri::command]
fn download(app: AppHandle, url: String) {
    let content_length = 1000;
    let download_id = 1;
    app.emit("download-started", DownloadStarted {
        url: &url,
        download_id,
        content_length
    }).unwrap();
    for chunk_length in [15, 150, 35, 500, 300] {
        app.emit("download-progress", DownloadProgress {
            download_id,
            chunk_length,
        }).unwrap();
    }
    app.emit("download-finished", DownloadFinished { download_id }).unwrap();
}
```

#### 监听事件

Tauri 提供了在前端和 Rust 端监听事件的 API。

#### 在前端监听事件

## 通道

事件系统设计用于简单的全局双向通信。对于高性能数据流传输，使用通道。

通道确保快速、有序的数据传递，内部用于下载进度、子进程输出和 WebSocket 消息等任务。

这是使用通道的下载命令示例：

```rust
use tauri::{AppHandle, ipc::Channel};
use serde::Serialize;
#[derive(Clone, Serialize)]
#[serde(rename_all = "camelCase", tag = "event", content = "data")]
enum DownloadEvent<'a> {
    #[serde(rename_all = "camelCase")]
    Started {
        url: &'a str,
        download_id: usize,
        content_length: usize,
    },
    #[serde(rename_all = "camelCase")]
    Progress {
        download_id: usize,
        chunk_length: usize,
    },
    #[serde(rename_all = "camelCase")]
    Finished {
        download_id: usize,
    },
}
#[tauri::command]
fn download(app: AppHandle, url: String, on_event: Channel<DownloadEvent>) {
    let content_length = 1000;
    let download_id = 1;
    on_event.send(DownloadEvent::Started {
        url: &url,
        download_id,
        content_length,
    }).unwrap();
    for chunk_length in [15, 150, 35, 500, 300] {
        on_event.send(DownloadEvent::Progress {
            download_id,
            chunk_length,
        }).unwrap();
    }
    on_event.send(DownloadEvent::Finished { download_id }).unwrap();
}
```

要调用下载命令，创建通道并将其作为参数传递：

 

```javascript
import { invoke, Channel } from '@tauri-apps/api/core';
type DownloadEvent =
    | {
            event: 'started';
            data: {
                url: string;
                downloadId: number;
                contentLength: number;
            };
        }
    | {
            event: 'progress';
            data: {
                downloadId: number;
                chunkLength: number;
            };
        }
    | {
            event: 'finished';
            data: {
                downloadId: number;
            };
        };
const onEvent = new Channel<DownloadEvent>();
onEvent.onmessage = (message) => {
    console.log(`got download event ${message.event}`);
};
await invoke('download', {
    url: 'https://raw.githubusercontent.com/tauri-apps/tauri/dev/crates/tauri-
schema-generator/schemas/config.schema.json',
    onEvent,
});
```

## 执行 JavaScript

要在 webview 上下文中直接运行 JavaScript 代码，使用 WebviewWindow#eval 函数：

```rust
use tauri::Manager;
tauri::Builder::default()
    .setup(|app| {
        let webview = app.get_webview_window("main").unwrap();
        webview.eval("console.log('hello from Rust')")?;
        Ok(())
    })
```

对于需要 Rust 对象输入的复杂脚本，考虑使用 serialize-to-javascript crate。

