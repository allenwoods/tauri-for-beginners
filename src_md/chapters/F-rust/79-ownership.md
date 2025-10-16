# 所有权

在 Rust 中，所有权是一个独特的功能，有助于确保内存安全并防止数据竞争。它是将 Rust 与其他编程语言区分开来的关键概念。

#### 所有权规则

- 1. Rust 中的每个值都有一个变量作为其所有者。
- 2. 一次只能有一个所有者。
- 3. 当所有者超出作用域时，该值被丢弃。

#### 借用

为了允许对值进行多个引用而不获取所有权，Rust 引入了借用的概念。借用可以通过引用完成，引用是指向值的指针。

```rust
fn main() {
    let s = String::from("Hello, world!");
    // 使用引用借用值
    let len = calculate_length(&s);
    println!("The length of '{}' is {}.", s, len);
}
fn calculate_length(s: &String) -> usize {
    s.len()
}
```

#### 所有权转移

所有权可以使用 `move` 关键字转移。当你想将值的所有权转移到不同作用域时，这很有用。

```rust
fn main() {
    let s1 = String::from("Hello");
    let s2 = take_ownership(s1);
    println!("{}", s2);
}
fn take_ownership(s: String) -> String {
    s
}
```

### 所有权和函数

当值传递给函数时，除非使用引用借用值，否则所有权会被转移。

### 结论

理解所有权在 Rust 编程中至关重要。它允许安全高效的内存管理，防止悬空指针和数据竞争等常见问题。

