# 类

类是 JavaScript 中面向对象编程的基本方面。它们提供了一种结构化的方式来定义创建具有共同属性和方法的对象的蓝图，增强了代码组织和可重用性。

#### 定义类

要在 JavaScript 中定义类，您使用 class 关键字后跟类名。考虑以下示例：

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    sayHello() {
        console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
    }
}
```

在此示例中，我们定义了一个 Person 类，其构造函数方法接受 name 和 age 作为参数。构造函数将这些值初始化为对象的属性。此外，sayHello 方法将问候消息记录到控制台。

### 创建实例

要创建类的实例，您使用 new 关键字后跟类名和任何必需的参数。以下是如何实例化 Person 对象：

```javascript
const john = new Person('John Doe', 25);
john.sayHello(); // Output: Hello, my name is John Doe and I'm 25 years old.
```

### 静态方法和属性

类还可以具有在所有实例之间共享的静态方法和属性。这些使用类名本身访问。例如：

```javascript
class Circle {
    static PI = 3.14159;
    static calculateArea(radius) {
        return Circle.PI * radius * radius;
    }
}
console.log(Circle.calculateArea(5)); // Output: 78.53975
```

在此示例中，Circle 类有一个静态属性 PI 和一个静态方法 calculateArea。静态方法可以直接在类上调用，无需实例。

### 继承

JavaScript 类支持继承，允许您创建从父类继承属性和方法的子类。这是使用 extends 关键字实现的。考虑以下示例：

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}
class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}
const dog = new Dog('Buddy');
dog.speak(); // Output: Buddy barks.
```

在此示例中，Animal 类有一个 speak 方法。Dog 类扩展 Animal 并重写 speak 方法以提供特定实现。

#### 私有字段和方法

JavaScript 支持私有字段和方法，这些在类外部无法访问。私有字段使用 # 前缀声明。例如：

```javascript
class Car {
    #engineStatus = 'off';
    startEngine() {
        this.#engineStatus = 'on';
        console.log('Engine started.');
    }
    getEngineStatus() {
        return this.#engineStatus;
    }
}
const car = new Car();
car.startEngine(); // Output: Engine started.
console.log(car.getEngineStatus()); // Output: on
```

在此示例中，#engineStatus 字段是私有的，只能在 Car 类内访问。

#### Getter 和 Setter

Getter 和 setter 允许您定义像属性一样访问的方法。它们对于控制对对象属性的访问很有用。例如：

```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
    set area(value) {
        throw new Error('Area is a read-only property.');
    }
}
const rect = new Rectangle(10, 5);
console.log(rect.area); // Output: 50
```

在此示例中，area getter 计算矩形的面积，如果有人尝试直接设置面积，setter 会抛出错误。

JavaScript 中的类提供了一种强大的方式来组织和构建您的代码，使管理对象及其行为变得更加容易。

