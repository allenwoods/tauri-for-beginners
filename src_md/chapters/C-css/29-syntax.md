# 语法

CSS（层叠样式表）是一种强大的样式表语言，在 Web 开发中起着至关重要的作用。它用于描述用 HTML 或 XML 编写的文档的表示，规定元素应如何在各种媒体（如屏幕、纸张甚至语音）上渲染。

## 基本语法

CSS 的核心是其基本语法，它由选择器和声明块组成：

```css
selector {
    property: value;
}
```

- **选择器**：规则的这一部分针对您希望设置样式的 HTML 元素。
- **声明块**：用大括号括起来，此块包含一个或多个用分号分隔的声明。每个声明将 CSS 属性与值配对，用冒号分隔。

### 示例

考虑以下示例：

```css
h1 {
    color: blue;
    font-size: 20px;
}
```

在此代码片段中，h1 是选择器，color: blue; 和 font-size: 20px; 是设置 h1 元素样式的声明。

## 选择器

选择器在 CSS 中是基础，因为它们确定哪些 HTML 元素是样式目标。有几种类型的选择器：

**元素选择器**：通过标签名定位元素。

```css
p {
    color: red;
}
```

**类选择器**：通过 class 属性定位元素。

```css
.classname {
    color: green;
}
```

**ID 选择器**：通过 id 属性定位元素。

```css
#idname {
    color: blue;
}
```

**属性选择器**：基于属性或属性值定位元素。

```css
[type="text"] {
    border: 1px solid black;
}
```

**伪类选择器**：基于元素状态定位元素。

```css
a:hover {
    color: orange;
}
```

**伪元素选择器**：定位元素的部分。

```css
p::first-line {
    font-weight: bold;
}
```

## 属性和值

CSS 属性用于将样式应用于元素，每个属性可以采用一系列值。以下是一些常用属性：

**color**：设置文本的颜色。

```css
color: red;
```

**background-color**：设置元素的背景颜色。

```css
background-color: yellow;
```

**font-size**：设置字体大小。

```css
font-size: 16px;
```

**margin**：设置元素外部的空间。

```css
margin: 10px;
```

**padding**：设置元素内部的空间。

```css
padding: 10px;
```

**border**：设置元素周围的边框。

```css
border: 1px solid black;
```

## 层叠和特异性

CSS 中的"层叠"代表样式从多个源层叠下来的方式，规则的顺序和特异性决定应用哪些样式。

- **层叠**：当多个规则应用于同一元素时，CSS 文件中最后出现的规则优先。
- **特异性**：此概念通过为不同类型的选择器分配权重来确定应用哪个规则。ID 选择器比类选择器具有更高的特异性，而类选择器又比元素选择器具有更高的特异性。

### 特异性示例

```css
p {
    color: red;
}
#unique {
    color: blue;
}
```

```html
<p id="unique">This text will be blue.</p>
```

在此示例中，尽管 p 选择器将颜色设置为红色，但 #unique ID 选择器由于具有更高的特异性而覆盖它并将颜色设置为蓝色。

## 继承

CSS 属性可以从父元素继承到子元素。例如，如果您在父元素上设置 color 属性，其子元素将继承该颜色，除非它们有自己的 color 属性设置。

#### 继承示例

```css
div {
    color: green;
}
```

```html
<div>
    This text will be green.
    <p>This text will also be green.</p>
</div>
```

在此示例中，div 和 p 元素都将有绿色文本，因为 color 属性被继承了。

## 结论

掌握 CSS 语法对于创建视觉上吸引人的网页至关重要。通过理解选择器、属性、值、层叠、特异性和继承，您可以精确控制 HTML 文档的表示，确保精美和专业的外观。

