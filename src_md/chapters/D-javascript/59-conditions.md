# 条件语句

JavaScript 中的条件语句允许您根据满足的特定条件来控制代码的流程。它们对于创建动态和交互式应用程序至关重要。在本章中，我们将深入探讨不同类型的条件语句以及如何有效使用它们。

#### If 语句

if 语句是 JavaScript 中最基本的条件类型。它使您能够仅在指定条件评估为 true 时执行代码块。语法很简单：

```javascript
if (condition) {
    // code to be executed if the condition is true
}
```

#### 示例：

考虑一个您想检查某人是否成年的场景：

```javascript
let age = 18;
if (age >= 18) {
    console.log("You are an adult.");
}
```

### If-Else 语句

if-else 语句在 if 语句的基础上，提供了在条件为 false 时执行的替代代码块。它看起来是这样的：

```javascript
if (condition) {
    // code to be executed if the condition is true
} else {
    // code to be executed if the condition is false
}
```

#### 示例：

让我们修改之前的示例来处理成年人和未成年人：

```javascript
let age = 16;
if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}
```

#### Else-If 语句

else-if 语句允许您检查多个条件并根据结果执行不同的代码块。它可以与 if 和 if-else 语句结合使用。语法如下：

```javascript
if (condition1) {
    // code to be executed if condition1 is true
} else if (condition2) {
    // code to be executed if condition2 is true
} else {
    // code to be executed if all conditions are false
}
```

#### 示例：

想象您正在给考试评分，想根据分数分配字母等级：

```javascript
let score = 85;
if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}
```

### Switch 语句

switch 语句提供了处理多个条件的替代方法。它允许您指定不同的情况并根据表达式的值执行代码。语法如下：

```javascript
switch (expression) {
    case value1:
        // code to be executed if expression matches value1
        break;
    case value2:
        // code to be executed if expression matches value2
        break;
    default:
        // code to be executed if expression doesn't match any case
}
```

#### 示例：

让我们使用 switch 语句根据数值打印星期几的名称：

```javascript
let day = 3;
switch (day) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    default:
        console.log("Another day");
}
```

### 三元运算符

三元运算符是在 JavaScript 中编写简单条件的简洁方法。它允许您根据条件为变量赋值。语法是：

```javascript
variable = (condition) ? value1 : value2;
```

#### 示例：

以下是如何使用三元运算符来确定某人是成年人还是未成年人：

```javascript
let age = 20;
let status = (age >= 18) ? "adult" : "minor";
console.log(status); // Output: adult
```

#### 逻辑运算符

逻辑运算符通常用于组合多个条件。最常见的逻辑运算符是 &&（AND）、||（OR）和 !（NOT）。

#### 示例：

考虑一个您想根据某人的年龄和是否有身份证来检查是否允许进入的场景：

```javascript
let age = 25;
let hasID = true;
if (age >= 18 && hasID) {
    console.log("Entry allowed.");
} else {
    console.log("Entry denied.");
}
```

通过掌握这些条件语句，您将能够创建更强大和灵活的 JavaScript 代码。明智地使用它们来控制应用程序的流程并有效处理不同的场景。

