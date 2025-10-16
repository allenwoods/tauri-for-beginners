# 字符串

JavaScript 中的字符串是用单引号（'）或双引号（"）括起来的字符序列。它们用于表示文本，是语言中的基本数据类型之一。

## 不可变性

在 JavaScript 中，字符串是不可变的，这意味着一旦创建了字符串，就无法更改。但是，您可以基于对现有字符串执行的操作创建新字符串。这种不可变性确保字符串保持一致并防止意外的副作用。

## 常见操作

### 连接

连接是将两个或多个字符串连接在一起的过程。在 JavaScript 中，这通常使用 + 运算符完成：

```javascript
let greeting = 'Hello, ' + 'world!';
```

### 字符串插值

字符串插值允许您使用模板字面量在字符串中嵌入表达式，模板字面量用反引号（`）括起来。此功能使动态构造字符串变得更容易：

```javascript
let name = 'Alice';
let greeting = `Hello, ${name}!`;
```

#### 访问字符

您可以使用括号表示法访问字符串中的单个字符，其中索引从 0 开始：

```javascript
let myString = 'Hello';
let firstChar = myString[0]; // 'H'
```

## 内置方法

JavaScript 提供了丰富的内置方法来处理字符串。一些最常用的方法包括：

**查找字符串的长度**：使用 length 属性获取字符串中的字符数。

```javascript
let myString = 'Hello';
let length = myString.length; // 5
```

**改变大小写**：使用 toUpperCase() 和 toLowerCase() 将字符串转换为大写或小写。

```javascript
let myString = 'Hello';
let upper = myString.toUpperCase(); // 'HELLO'
let lower = myString.toLowerCase(); // 'hello'
```

**搜索子字符串**：使用 indexOf() 查找字符串中子字符串的位置。

```javascript
let myString = 'Hello, world!';
let position = myString.indexOf('world'); // 7
```

**提取子字符串**：使用 substring()、substr() 或 slice() 提取字符串的部分。

```javascript
let myString = 'Hello, world!';
let sub = myString.substring(0, 5); // 'Hello'
```

## Unicode 支持

JavaScript 支持 Unicode 字符，允许您在字符串中使用来自不同语言和脚本的字符。这对于国际化和处理多样化数据集特别有用。

#### 转义序列

转义序列用于表示字符串中的特殊字符。常见的转义序列包括：

换行：\n 制表符：\t 反斜杠：\\ 单引号：\' 双引号：\"

```javascript
let multiline = 'This is line one.\nThis is line two.';
```

字符串是 JavaScript 编程的重要组成部分。了解如何有效地使用它们对于构建健壮和动态的应用程序至关重要。通过掌握字符串操作和方法，您可以高效地操作和从文本中提取信息，使您的代码更强大和多功能。

