# 结构体

Rust 中的结构体是一种定义自定义数据类型的方法，可以保存不同类型的多个值。它们类似于 C 或 C++ 等其他编程语言中的结构体。

以下是如何在 Rust 中定义结构体的示例：

```rust
struct Person {
    name: String,
    age: u32,
    is_student: bool,
}
```

在上面的示例中，我们定义了一个名为 `Person` 的结构体，它有三个字段：类型为 `String` 的 `name`、类型为 `u32`（32位无符号整数）的 `age`，以及类型为 `bool` 的 `is_student`。

你可以创建 `Person` 结构体的实例并像这样访问其字段：

```rust
let person = Person {
    name: String::from("John Doe"),
    age: 25,
    is_student: true,
};
println!("Name: {}", person.name);
println!("Age: {}", person.age);
println!("Is Student: {}", person.is_student);
```

结构体也可以使用 `impl` 关键字关联方法。以下是一个示例：

```rust
impl Person {
    fn introduce(&self) {
        println!("Hi, my name is {} and I'm {} years old.", self.name, self.age);
    }
}
let person = Person {
    name: String::from("John Doe"),
    age: 25,
    is_student: true,
};
person.introduce();
```

在上面的示例中，我们为 `Person` 结构体定义了一个 `impl` 块，并定义了一个名为 `introduce` 的方法，该方法接受对 `self`（结构体的实例）的引用，并打印介绍该人的消息。

Rust 中的结构体是组织和操作数据的强大方式。它们提供了一种灵活高效的方式来定义具有自己字段和方法的自定义数据类型。

