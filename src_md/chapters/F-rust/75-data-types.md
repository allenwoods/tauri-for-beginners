# 数据类型

在 Rust 中，有多种内置数据类型可以用来定义变量。以下是一些常用的数据类型：

#### 整数类型

Rust 提供了多种整数类型，它们在大小和有符号性方面有所不同。以下是一些示例：

- `i8`：8位有符号整数（-128 到 127）
- `u16`：16位无符号整数（0 到 65,535）
- `i32`：32位有符号整数（-2,147,483,648 到 2,147,483,647）

#### 示例：

```rust
let age: u8 = 25;
let count: i32 = -10;
```

#### 浮点类型

Rust 支持两种浮点类型：`f32` 和 `f64`。`f32` 类型是单精度浮点数，而 `f64` 是双精度浮点数。

示例：

```rust
let pi: f32 = 3.14;
let gravity: f64 = 9.8;
```

### 布尔类型

Rust 中的布尔类型是 `bool`，它可能有两个值：`true` 或 `false`。

示例：

```rust
let is_rust_fun: bool = true;
let is_python_fun: bool = false;
```

#### 字符类型

Rust 中的字符类型是 `char`，它表示一个 Unicode 标量值。

示例：

```rust
let heart_emoji: char = '❤';
let smiley_emoji: char = '';
```

#### 字符串类型

Rust 有一个内置的字符串类型叫做 `String`，它是一个可增长的、UTF-8 编码的字符串。

示例：

```rust
let greeting: String = String::from("Hello, world!");
let name: String = "Alice".to_string();
```

这些只是 Rust 中可用数据类型的一些示例。你可以在 Rust 文档中探索更多数据类型及其用法。
