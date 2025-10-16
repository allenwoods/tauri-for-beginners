# 在 Tauri 中管理状态

管理 Tauri 应用程序的状态对于维护其生命周期和行为至关重要。Tauri 提供了一种直接的方式来使用 Manager API 处理状态，允许您在执行命令时访问它。

## 基本示例

让我们从一个基本示例开始，说明如何在 Tauri 应用程序中管理状态：

```rust
use tauri::{Builder, Manager};
struct AppData {
    welcome_message: &'static str,
}
fn main() {
    Builder::default()
        .setup(|app| {
            app.manage(AppData {
                welcome_message: "Welcome to Tauri!",
            });
            Ok(())
        })
        .run(tauri::generate_context!())
        .unwrap();
}
```

在这个示例中，我们定义了一个简单的 AppData 结构体来保存我们的状态。然后我们使用 setup 方法在 Tauri 应用程序中管理这个状态。

要检索您的状态，您可以使用任何实现 Manager 特征的类型，例如 App 实例：

```rust
let data = app.state::<AppData>();
```

有关更多详细信息，请参阅访问状态部分。

## 处理可变性

Rust 的所有权模型防止跨线程或通过共享指针（如 Arc 或 Tauri 的 State）直接修改共享值。这是为了避免数据竞争。

要修改共享状态，您可以使用内部可变性。标准库的 Mutex 可以用于安全地锁定和解锁状态以进行修改：

```rust
use std::sync::Mutex;
use tauri::{Builder, Manager};
#[derive(Default)]
struct AppState {
    counter: u32,
}
fn main() {
    Builder::default()
        .setup(|app| {
            app.manage(Mutex::new(AppState::default()));
            Ok(())
        })
        .run(tauri::generate_context!())
        .unwrap();
}
```

要修改状态，锁定互斥锁：

```rust
let state = app.state::<Mutex<AppState>>();
let mut state = state.lock().unwrap();
state.counter += 1;
```

当 MutexGuard 被丢弃时，互斥锁会自动解锁。

#### 使用异步 Mutex

根据 Tokio 文档，标准库的 Mutex 通常足以用于异步代码。但是，如果您需要在 await 点之间持有 MutexGuard，则需要异步互斥锁。

#### 您需要 Arc 吗？

在 Rust 中，Arc 通常用于跨线程共享值的所有权，通常与 Mutex 配对使用（Arc<Mutex<T>>）。Tauri 为您处理了这一点，因此您不需要对存储在 State 中的值使用 Arc。

## 访问状态

#### 在命令中

您可以在命令中访问和修改状态：

```rust
#[tauri::command]
fn increase_counter(state: State<'_, Mutex<AppState>>) -> u32 {
    let mut state = state.lock().unwrap();
    state.counter += 1;
    state.counter
}
```

有关命令的更多信息，请参阅从前端调用 Rust。

#### 异步命令

对于使用 Tokio 异步 Mutex 的异步命令：

```rust
#[tauri::command]
async fn increase_counter(state: State<'_, Mutex<AppState>>) -> Result<u32, ()> {
    let mut state = state.lock().await;
    state.counter += 1;
    Ok(state.counter)
}
```

异步命令的返回类型必须是 Result。

### 使用 Manager 特征

要在命令外部（如事件处理程序或不同线程中）访问状态，使用实现 Manager 特征的类型的 state() 方法：

 

```rust
use tauri::{Builder, GlobalWindowEvent, Manager};
#[derive(Default)]
struct AppState {
    counter: u32,
}
fn on_window_event(event: GlobalWindowEvent) {
    let app_handle = event.window().app_handle();
    let state = app_handle.state::<Mutex<AppState>>();
    let mut state = state.lock().unwrap();
    state.counter += 1;
}
fn main() {
    Builder::default()
        .setup(|app| {
            app.manage(Mutex::new(AppState::default()));
            Ok(())
        })
        .on_window_event(on_window_event)
        .run(tauri::generate_context!())
        .unwrap();
}
```

当命令注入不可行时，这种方法很有用。

## 类型不匹配

需要注意的是，为 State 参数使用错误的类型会导致运行时 panic。

例如，使用 State<'_, AppState> 而不是 State<'_, Mutex<AppState>> 会导致问题。

为了避免这种情况，考虑使用类型别名：

```rust
use std::sync::Mutex;
#[derive(Default)]
struct AppStateInner {
    counter: u32,
}
type AppState = Mutex<AppStateInner>;
```

确保您正确使用类型别名，以防止再次将其包装在 Mutex 中。

