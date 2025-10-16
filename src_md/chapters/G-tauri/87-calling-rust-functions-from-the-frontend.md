# 从前端调用 Rust 函数

Tauri 提供了一个强大的系统，可以使用命令从前端安全地调用 Rust 函数，以及一个事件系统用于更动态的交互。

## 命令

Tauri 中的命令系统允许您的 Web 应用调用 Rust 函数。命令可以处理参数、返回值、错误，并且可以是异步的。

#### 基本示例

要定义命令，请在您的 src-tauri/src/lib.rs 文件中使用 #[tauri::command] 注解函数：

```rust
#[tauri::command]
fn my_custom_command() {
    println!("I was invoked from JavaScript!");
}
```

需要注意的是，命令名称必须是唯一的。

由于胶水代码限制，lib.rs 中的命令不能是公共的。在 lib.rs 中创建公共命令会导致错误。

使用构建器函数注册您的命令：

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![my_custom_command])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

从 JavaScript 调用命令：

```javascript
import { invoke } from '@tauri-apps/api/core';
const invoke = window.__TAURI__.core.invoke;
invoke('my_custom_command');
```

#### 在单独模块中的命令

为了更好地组织，在单独的模块中定义命令：

```rust
#[tauri::command]
pub fn my_custom_command() {
    println!("I was invoked from JavaScript!");
}
```

单独模块中的命令应该是公共的，以允许在 lib.rs 中使用它们。

在 lib.rs 中，包含模块并注册命令：

```rust
mod commands;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![commands::my_custom_command])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

#### WASM

对于调用不带参数的 invoke() 的 Rust 前端，调整您的代码：

```rust
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = ["window", "__TAURI__", "core"], js_name =
invoke)]
    async fn invoke_without_args(cmd: &str) -> JsValue;
    #[wasm_bindgen(js_namespace = ["window", "__TAURI__", "core"])]
    async fn invoke(cmd: &str, args: JsValue) -> JsValue;
}
```

#### 传递参数

命令可以接受参数：

```rust
#[tauri::command]
fn my_custom_command(invoke_message: String) {
    println!("I was invoked from JavaScript, with this message: {}",
invoke_message);
}
```

将参数作为带有 camelCase 键的 JSON 对象传递：

```javascript
invoke('my_custom_command', { invokeMessage: 'Hello!' });
```

为了传递带有 Snake Case 键的参数，您可以使用带有 rename_all 属性的 snake_case：

```rust
#[tauri::command(rename_all = "snake_case")]
fn my_custom_command(invoke_message: String) {}
invoke('my_custom_command', { invoke_message: 'Hello!' });
```

### 返回数据

命令可以返回数据：

```rust
#[tauri::command]
fn my_custom_command() -> String {
    "Hello from Rust!".into()
}
```

invoke 函数返回一个 promise：

```javascript
invoke('my_custom_command').then((message) => console.log(message));
```

#### 返回数组缓冲区

对于大数据，使用 tauri::ipc::Response：

```rust
use tauri::ipc::Response;
#[tauri::command]
fn read_file() -> Response {
    let data = std::fs::read("/path/to/file").unwrap();
    tauri::ipc::Response::new(data)
}
```

#### 错误处理

命令可以使用 Result 返回错误：

```rust
#[tauri::command]
fn login(user: String, password: String) -> Result<String, String> {
    if user == "tauri" && password == "tauri" {
        Ok("logged_in".to_string())
    } else {
        Err("invalid credentials".to_string())
    }
}
```

在 JavaScript 中处理错误：

```javascript
invoke('login', { user: 'tauri', password: '0j4rijw8=' })
  .then((message) => console.log(message))
  .catch((error) => console.error(error));
```

对于非 serde::Serialize 错误，将它们转换为 String：

```rust
#[tauri::command]
fn my_custom_command() -> Result<(), String> {
    std::fs::File::open("path/to/file").map_err(|err| err.to_string())?;
    Ok(())
}
```

使用 thiserror 创建自定义错误类型：

```rust
#[derive(Debug, thiserror::Error)]
enum Error {
    #[error(transparent)]
    Io(#[from] std::io::Error)
}
impl serde::Serialize for Error {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::ser::Serializer,
    {
        serializer.serialize_str(self.to_string().as_ref())
    }
}
#[tauri::command]
fn my_custom_command() -> Result<(), Error> {
    std::fs::File::open("path/that/does/not/exist")?;
    Ok(())
}
```

#### 异步命令

对于繁重的任务，使用异步命令：

```rust
#[tauri::command]
async fn my_custom_command(value: String) -> String {
    some_async_function().await;
    value
}
```

使用 Result 处理借用类型：

```rust
#[tauri::command]
async fn my_custom_command(value: &str) -> Result<String, ()> {
    some_async_function().await;
    Ok(format!(value))
}
```

从 JavaScript 调用异步命令：

```javascript
invoke('my_custom_command', { value: 'Hello, Async!' }).then(() =>
  console.log('Completed!')
);
```

 

#### 通道

使用 Tauri 通道进行数据流传输：

```rust
use tokio::io::AsyncReadExt;
#[tauri::command]
async fn load_image(path: std::path::PathBuf, reader: tauri::ipc::Channel<&[u8]>)
{
    let mut file = tokio::fs::File::open(path).await.unwrap();
    let mut chunk = vec![0; 4096];
    loop {
        let len = file.read(&mut chunk).await.unwrap();
        if len == 0 {
            break;
        }
        reader.send(&chunk).unwrap();
    }
}
```

### 访问 WebviewWindow 和 AppHandle

命令可以访问 WebviewWindow 和 AppHandle：

```rust
#[tauri::command]
async fn my_custom_command(webview_window: tauri::WebviewWindow) {
    println!("WebviewWindow: {}", webview_window.label());
}
#[tauri::command]
async fn my_custom_command(app_handle: tauri::AppHandle) {
    let app_dir = app_handle.path_resolver().app_dir();
    app_handle.global_shortcut_manager().register("CTRL + U", move || {});
}
```

#### 托管状态

使用 tauri::Builder 管理状态并在命令中访问它：

 

```rust
struct MyState(String);
#[tauri::command]
fn my_custom_command(state: tauri::State<MyState>) {
    assert_eq!(state.0 == "some state value", true);
}
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .manage(MyState("some state value".into()))
        .invoke_handler(tauri::generate_handler![my_custom_command])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

#### 原始请求访问

在命令中访问完整的 tauri::ipc::Request 对象：

```
#[derive(Debug, thiserror::Error)]
enum Error {
  #[error("unexpected request body")]
  RequestBodyMustBeRaw,
  #[error("missing `{0}` header")]
  MissingHeader(&'static str),
}
impl serde::Serialize for Error {
  fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
  where
    S: serde::ser::Serializer,
  {
    serializer.serialize_str(self.to_string().as_ref())
  }
}
#[tauri::command]
fn upload(request: tauri::ipc::Request) -> Result<(), Error> {
  let tauri::ipc::InvokeBody::Raw(upload_data) = request.body() else {
    return Err(Error::RequestBodyMustBeRaw);
  };
  let Some(authorization_header) = request.headers().get("Authorization") else {
    return Err(Error::MissingHeader("Authorization"));
  };
  Ok(())
}
```

 

Invoke with raw request body and headers:

```
const data = new Uint8Array([1, 2, 3]);
await __TAURI__.core.invoke('upload', data, {
  headers: {
    Authorization: 'apikey',
  },
});
```

#### 多个命令

使用 tauri::generate_handler! 注册多个命令：

```rust
#[tauri::command]
fn cmd_a() -> String {
    "Command a"
}
#[tauri::command]
fn cmd_b() -> String {
    "Command b"
}
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![cmd_a, cmd_b])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

