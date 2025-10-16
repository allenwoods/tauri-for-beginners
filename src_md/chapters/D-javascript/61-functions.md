# 函数

JavaScript 中的函数是语言的重要组成部分，允许您封装可重用的代码块并在需要时执行它们。在本章中，我们将探索在 JavaScript 中定义和使用函数的各种方法，为您提供有效利用其功能的坚实基础。

## 函数声明

函数声明定义了一个命名函数。语法包括 function 关键字，后跟函数名、参数列表（用括号括起来）和函数体（用大括号括起来）。这种方法简单直接，被广泛使用。

```javascript
function functionName() {
    // code to be executed
}
```

例如，考虑一个向用户问候的简单函数：

```javascript
function greet() {
    console.log("Hello, world!");
}
```

## 函数调用

要执行函数，您只需要使用其名称后跟一对括号来调用它。这告诉 JavaScript 运行函数内的代码。

```javascript
functionName();
```

使用我们之前的示例，调用 greet 函数将如下所示：

```javascript
greet(); // Outputs: Hello, world!
```

## 函数参数

函数可以接受参数，这些参数充当调用函数时将传递的值的占位符。这些参数允许您将数据传递到函数中并在函数体内使用它们。

```javascript
function addNumbers(num1, num2) {
    return num1 + num2;
}
```

例如，您可以使用两个参数调用 addNumbers 函数：

```javascript
console.log(addNumbers(5, 10)); // Outputs: 15
```

## Return 语句

函数还可以使用 return 语句返回值。这允许您获取计算结果或对返回值执行进一步操作。

```javascript
function multiplyNumbers(num1, num2) {
    return num1 * num2;
}
```

例如，您可以捕获 multiplyNumbers 函数的结果：

```javascript
console.log(multiplyNumbers(5, 10)); // Outputs: 50
```

## 函数表达式

函数也可以分配给变量，称为函数表达式。这允许您创建匿名函数或将函数作为参数传递给其他函数。

```javascript
const multiply = function(num1, num2) {
    return num1 * num2;
};
```

然后您可以使用变量来调用函数：

```javascript
console.log(multiply(5, 10)); // Outputs: 50
```

## 箭头函数 (ES6)

箭头函数为编写函数提供了更简洁的语法。它们对于单行函数特别有用，并且没有自己的 this 上下文，这使得它们在特定情况下特别有用。

```javascript
const multiply = (num1, num2) => num1 * num2;
```

例如，使用箭头函数：

```javascript
console.log(multiply(5, 10)); // Outputs: 50
```

## 默认参数 (ES6)

您可以为函数中的参数设置默认值。如果没有为具有默认值的参数提供参数，将使用默认值。

```javascript
function greet(name = "Guest") {
    console.log(`Hello, ${name}!`);
}
```

例如，调用不带参数的 greet 函数：

```javascript
greet(); // Outputs: Hello, Guest!
greet("Alice"); // Outputs: Hello, Alice!
```

## 剩余参数 (ES6)

剩余参数允许您将不定数量的参数表示为数组。当您想要处理可变数量的参数时，这很有用。

```javascript
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}
```

例如，对多个数字求和：

```javascript
console.log(sum(1, 2, 3, 4)); // Outputs: 10
```

## 高阶函数

通过将其他函数作为参数或返回它们来操作其他函数的函数称为高阶函数。这些函数是 JavaScript 的强大功能，使您能够编写更抽象和灵活的代码。

```javascript
function applyOperation(num1, num2, operation) {
    return operation(num1, num2);
}
```

例如，使用高阶函数来添加数字：

```javascript
const add = (a, b) => a + b;
console.log(applyOperation(5, 10, add)); // Outputs: 15
```

总之，函数是 JavaScript 中强大的工具，能够实现代码重用和模块化。通过理解和利用不同类型的函数及其功能，您可以编写更高效和可维护的代码。

