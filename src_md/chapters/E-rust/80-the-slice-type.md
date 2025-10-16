# 切片类型

Rust 中的切片类型允许你引用集合中连续的元素序列。它由 `&[T]` 类型表示，其中 `T` 是切片中元素的类型。

切片通常用于处理数组、向量和其他集合。它们提供了一种灵活高效的方式来访问和操作数据的子集，而无需复制整个集合。

以下是在 Rust 中使用切片的一些示例：

1. 从数组创建切片：

```rust
let numbers = [1, 2, 3, 4, 5];
let slice = &numbers[1..4]; // 创建一个包含元素 2、3 和 4 的切片
```

2. 将切片作为函数参数传递：

```rust
fn sum(numbers: &[i32]) -> i32 {
    let mut total = 0;
    for &num in numbers {
        total += num;
    }
    total
}
let numbers = [1, 2, 3, 4, 5];
let result = sum(&numbers); // 将数组的切片传递给函数
```

3. 修改切片：

```rust
let mut numbers = [1, 2, 3, 4, 5];
let slice = &mut numbers[1..4]; // 创建一个可变切片
slice[0] = 10; // 修改切片的第二个元素
assert_eq!(numbers, [1, 10, 3, 4, 5]); // 原始数组被修改
```

切片在 Rust 中提供了一种便捷的方式来处理数据的子集，允许你避免不必要的复制并提高性能。

