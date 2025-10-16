# 项目结构

理解您的 Tauri 项目结构对于高效开发至关重要。让我们仔细看看构成典型 Tauri 应用程序的各种文件和目录。

```text
C:.
│ package.json
│
├───src
│ index.html
│ main.js
│ styles.css
│
└───src-tauri
   │ build.rs
   │ Cargo.toml
   │ tauri.conf.json
   │
   └───src
          lib.rs
          main.rs
```

## package.json 文件

package.json 文件位于项目根目录，包含有关应用程序的基本信息，如名称、版本和依赖项。它还包括可以使用 npm 执行的脚本。

```json
{
  "name": "example",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "tauri": "tauri"
  },
  "devDependencies": {
    "@tauri-apps/cli": ">=2.0.0-rc.0"
  }
}
```

 

## src 目录

此目录包含您的前端代码，负责用户界面。它包括三个主要文件：index.html、styles.css 和 main.js。

#### src/index.html

src 目录中的 index.html 文件包含应用程序的 HTML 结构。最初，它应该看起来像这样：

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="styles.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tauri App</title>
    <script type="module" src="/main.js" defer></script>
  </head>
  <body>
      <h1>Welcome to Tauri!</h1>
  </body>
</html>
```

### src/styles.css

styles.css 文件包含定义应用程序外观的 CSS 规则，包括文本对齐、图像大小、颜色和背景。

```css
:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
  color: #0f0f0f;
  background-color: #f6f6f6;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
h1 {
  text-align: center;
}
```

#### src/main.js

main.js 文件为您的应用程序添加交互性。例如，它可以处理按钮点击等事件。最初，它应该包含以下代码：

```javascript
const { invoke } = window.__TAURI__.core;
```

## src-tauri 目录

此目录包含 Tauri 应用程序的后端代码和配置文件。它包括 build.rs、Cargo.toml 和 tauri.conf.json。

### src-tauri/build.rs

build.rs 文件用于构建应用程序。大多数项目将使用如下所示的文件：

```rust
fn main() {
    tauri_build::build()
}
```

#### src-tauri/Cargo.toml

Cargo.toml 文件包含控制代码编译方式和使用的优化信息。

```toml
[package]
name = "example"
version = "0.1.0"
description = "A Tauri App"
authors = ["you"]
edition = "2021"
[lib]
name = "example_lib"
crate-type = ["lib", "cdylib", "staticlib"]
[build-dependencies]
tauri-build = { version = "2", features = [] }
[dependencies]
tauri = { version = "2", features = [] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

### src-tauri/tauri.conf.json

tauri.conf.json 文件控制应用程序的各种设置，如其标题和构建命令将生成的安装程序/包。

```json
{
  "productName": "example",
  "version": "0.1.0",
  "identifier": "com.example.app",
  "build": {
    "frontendDist": "../src"
  },
  "app": {
    "withGlobalTauri": true,
    "windows": [
      {
        "title": "example",
        "label": "main",
        "maximized": true
      }
    ],
    "security": {
      "csp": null
    }
  },
  "bundle": {
    "active": true,
    "targets": ["deb", "rpm", "nsis", "msi"],
    "icon": [
      "icons/32x32.png",
      "icons/128x128.png",
      "icons/128x128@2x.png",
      "icons/icon.icns",
      "icons/icon.ico"
    ]
  }
}
```

## src-tauri/src 目录

在 src-tauri 目录中，有一个包含两个文件的 src 子目录：lib.rs 和 main.rs。

### src-tauri/src/lib.rs

lib.rs 文件用作 Android 和 iOS 设备的移动入口点。它应该看起来像这样：

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

### src-tauri/src/main.rs

main.rs 文件是非移动用户的入口点。它应该看起来像这样：

```rust
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
fn main() {
    example_lib::run()
}
```

## 运行您的项目

一旦所有文件都设置好了，在终端中打开项目的主目录并运行以下命令：

```shell
npm install # This installs the frontend dependencies
npm run tauri dev # This opens the developer window, which reloads every time one
of the project's files is modified and saved
```

```text
C:.
│ package.json
│
├───src
│ index.html
│ main.js
│ styles.css
│
└───src-tauri
   │ build.rs
   │ Cargo.toml
   │ tauri.conf.json
   │
   └───src
          lib.rs
          main.rs
```

 

#### package.json

项目根目录中的 package.json 文件包含诸如应用程序名称、版本和依赖项等信息。它还包含可以使用 npm 运行的脚本。

```json
{
  "name": "example",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "tauri": "tauri"
  },
  "devDependencies": {
    "@tauri-apps/cli": ">=2.0.0-rc.0"
  }
}
```

## src 目录

此目录包含您的前端代码。这是显示给用户的信息。它分别包含 3 个文件：index.html、styles.css 和 main.js。

### src/index.html

在 src 目录中，index.html 文件包含所有将显示的图像和文本。目前，它应该看起来像这样。

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="styles.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tauri App</title>
    <script type="module" src="/main.js" defer></script>
  </head>
  <body>
      <h1>Welcome to Tauri!</h1>
  </body>
</html>
```

#### src/styles.css

在 src 目录中，styles.css 包含有关文本对齐、图像大小、颜色和背景的所有信息，这些将在页面上显示。

```css
:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
  color: #0f0f0f;
  background-color: #f6f6f6;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
h1 {
  text-align: center;
}
```

### src/main.js

main.js 文件为应用程序添加交互性。例如，如果点击按钮，背景会改变颜色。目前只需要这个。

```javascript
const { invoke } = window.__TAURI__.core;
```

## src-tauri 目录

此目录包含所有后端代码以及一些应用程序配置文件。其中包含 build.rs、tauri.conf.json 和 Cargo.toml 文件。

#### src-tauri/build.rs

这是用于构建应用程序的代码。大多数项目将使用如下所示的文件。

```rust
fn main() {
    tauri_build::build()
}
```

#### src-tauri/Cargo.toml

此文件包含控制代码编译方式和使用的优化信息。

```toml
[package]
name = "example"
version = "0.1.0"
description = "A Tauri App"
authors = ["you"]
edition = "2021"
# See more keys and their definitions at https://doc.rust-
lang.org/cargo/reference/manifest.html
[lib]
name = "example_lib"
crate-type = ["lib", "cdylib", "staticlib"]
[profile.release]
panic = "abort" # Strip expensive panic clean-up logic
codegen-units = 1 # Compile crates one after another so the compiler can optimize
better
lto = true # Enables link to optimizations
opt-level = "s" # Optimize for binary size
[build-dependencies]
tauri-build = { version = "2.0.0-rc", features = [] }
[dependencies]
tauri = { version = "2.0.0-rc", features = [] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

### src-tauri/tauri.conf.json

此文件控制诸如应用程序标题以及构建命令将生成的安装程序/包等信息。目前文件应该看起来像这样。

```json
{
  "productName": "example",
  "version": "0.1.0",
  "identifier": "com.example.app",
  "build": {
    "frontendDist": "../src"
  },
  "app": {
    "withGlobalTauri": true,
    "windows": [
      {
        "title": "example",
        "label": "main",
        "maximized": true
      }
    ],
    "security": {
      "csp": null
    }
  },
  "bundle": {
    "active": true,
    "targets": ["deb", "rpm", "nsis", "msi"],
    "icon": [
      "icons/32x32.png",
      "icons/128x128.png",
      "icons/128x128@2x.png",
      "icons/icon.icns",
      "icons/icon.ico"
    ]
  }
}
```

## src-tauri/src 目录

在 src-tauri 目录中有一个 src 子目录。在此子目录中有两个文件，分别是 lib.rs 和 main.rs。

### src-tauri/src/lib.rs

此文件是用于 Android 和 IOS 设备的移动入口点。此文件应该看起来像这样。

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

#### src-tauri/src/main.rs

此文件是非移动用户的入口点。它应该看起来像这样。

```rust
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
fn main() {
    example_lib::run()
}
```

一旦所有文件都设置好了，在终端中打开项目主目录并运行以下命令。

```shell
npm install # This installs the frontend dependencies
npm run tauri dev # This opens the developer window which reloads everytime one of
the projects files are modified and saved
```

