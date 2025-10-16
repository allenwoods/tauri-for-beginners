# 类型转换

JavaScript 中的类型转换是将一种数据类型转换为另一种数据类型的过程。JavaScript 提供了几个内置函数和运算符来促进这一点。了解类型转换的工作原理对于编写健壮和无错误的代码至关重要。

## 常见类型转换方法

#### 1. 字符串转换

要将值转换为字符串，您可以使用 String() 函数或将值与空字符串（''）连接。

```javascript
let num = 42;
let str = String(num);
console.log(typeof str); // Output: string
```

或者：

```javascript
let num = 42;
let str = num + '';
console.log(typeof str); // Output: string
```

#### 2. 数字转换

要将值转换为数字，请使用 Number() 函数或一元加号运算符（+）。

```javascript
let str = '42';
let num = Number(str);
console.log(typeof num); // Output: number
```

或者：

```javascript
let str = '42';
let num = +str;
console.log(typeof num); // Output: number
```

#### 3. 布尔转换

JavaScript 的 Boolean() 函数将值转换为布尔值。以下值被认为是假值并转换为 false：0、NaN、null、undefined、false 和空字符串（''）。所有其他值都是真值并转换为 true。

```javascript
let num = 0;
let bool = Boolean(num);
console.log(bool); // Output: false
```

或者：

```javascript
let num = 0;
let bool = !!num;
console.log(bool); // Output: false
```

#### 4. 隐式类型转换

JavaScript 在某些情况下也会执行隐式类型转换。例如，将 + 运算符与字符串和数字一起使用会将数字转换为字符串并连接它们。

```javascript
let num = 42;
let str = 'The answer is ' + num;
console.log(str); // Output: The answer is 42
```

隐式类型转换有时可能导致意外结果：

```javascript
console.log('5' - 3); // Output: 2
console.log('5' + 3); // Output: 53
```

在第一个示例中，- 运算符在执行减法之前将字符串 '5' 转换为数字。在第二个示例中，+ 运算符将字符串 '5' 与数字 3 连接。

## 附加类型转换方法

#### 5. 解析整数和浮点数

JavaScript 提供 parseInt() 和 parseFloat() 函数分别将字符串转换为整数和浮点数。

```javascript
let str = '42.5';
let intNum = parseInt(str);
let floatNum = parseFloat(str);
console.log(intNum); // Output: 42
console.log(floatNum); // Output: 42.5
```

#### 6. 日期转换

要将日期转换为数字（时间戳），请使用 getTime() 方法或一元加号运算符（+）。

```javascript
let date = new Date();
let timestamp = date.getTime();
console.log(timestamp); // Output: 1633024800000 (example)
let timestamp2 = +date;
console.log(timestamp2); // Output: 1633024800000 (example)
```

### 7. JSON 转换

JavaScript 提供 JSON.stringify() 将对象转换为 JSON 字符串，提供 JSON.parse() 将 JSON 字符串转换回对象。

```javascript
let obj = { name: 'John', age: 30 };
let jsonString = JSON.stringify(obj);
console.log(jsonString); // Output: '{"name":"John","age":30}'
let parsedObj = JSON.parse(jsonString);
console.log(parsedObj); // Output: { name: 'John', age: 30 }
```

了解这些类型转换方法将帮助您在 JavaScript 程序中更有效地处理数据。

