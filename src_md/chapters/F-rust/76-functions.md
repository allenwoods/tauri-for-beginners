# 函数

Rust 中的函数允许你封装一个代码块，该代码块可以被重用和多次调用。它们使用 `fn` 关键字定义，后跟函数名、可选参数和返回类型。

以下是一个简单的 Rust 函数示例：

```rust
fn greet(name: &str) {
    println!("Hello, {}!", name);
}
```

在这个示例中，`greet` 函数接受一个类型为 `&str`（字符串切片）的参数 `name`，并使用 `println!` 宏打印问候消息。

你可以这样调用 `greet` 函数：

```rust
greet("Alice");
```

这将输出：

```
Hello, Alice!
```

函数也可以有返回类型。以下是一个计算两个数字之和并返回结果的函数示例：

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

在这个示例中，`add` 函数接受两个类型为 `i32`（32位有符号整数）的参数 `a` 和 `b`，并返回 `a` 和 `b` 的和。

你可以这样调用 `add` 函数并将结果存储在变量中：

```rust
let result = add(3, 5);
println!("The sum is: {}", result);
```

这将输出：

```shell
The sum is: 8
```

Rust 中的函数还可以有默认参数值、可变长度参数和闭包。你可以在 Rust 文档中探索这些高级主题。

记住总是在代码中调用函数之前定义它们。

