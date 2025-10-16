# 控制流

Rust 中的控制流允许你决定语句和表达式的执行顺序。它包括条件语句、循环和分支。

条件语句：Rust 提供 `if`、`else if` 和 `else` 关键字用于条件执行。以下是一个示例：

```rust
let number = 7;
if number < 5 {
    println!("Number is less than 5");
} else if number == 5 {
    println!("Number is equal to 5");
} else {
    println!("Number is greater than 5");
}
```

循环：Rust 提供不同类型的循环，如 `loop`、`while` 和 `for`。以下是一个 `for` 循环的示例：

```rust
let numbers = [1, 2, 3, 4, 5];
for number in numbers.iter() {
    println!("Number: {}", number);
}
```

分支：Rust 提供 `match` 关键字用于模式匹配和分支。以下是一个示例：

```rust
let fruit = "apple";
match fruit {
    "apple" => println!("It's an apple"),
    "banana" => println!("It's a banana"),
    _ => println!("It's something else"),
}
```

这些只是 Rust 中控制流的一些示例。你可以探索更高级的概念，如 `if let` 和 `while let`，用于更具体的场景。

