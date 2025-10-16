# 伪类

CSS 中的伪类允许您基于元素的状态或其在文档树中的位置来选择和设置元素样式。它们由冒号后跟伪类名称表示。

以下是一些常用的伪类：

1. :hover - 当鼠标指针悬停在元素上时选择元素。示例：

```css
a:hover {
    color: red;
}
```

2. :active - 当元素被激活（点击或触摸）时选择元素。示例：

```css
button:active {
    background-color: blue;
}
```

3. :focus - 当元素具有焦点时（例如，通过键盘导航选择时）选择元素。示例：

```css
input:focus {
    border-color: green;
}
```

4. :first-child - 选择其父元素的第一个子元素。示例：

```css
ul li:first-child {
    font-weight: bold;
}
```

5. :nth-child() - 基于元素在其父元素中的位置选择元素。示例：

```css
ul li:nth-child(odd) {
    background-color: lightgray;
}
```

这些只是 CSS 中可用的许多伪类中的几个示例。它们提供了基于各种条件和状态设置元素样式的强大方法。

