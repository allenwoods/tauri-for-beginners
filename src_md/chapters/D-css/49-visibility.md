# 可见性

CSS 中的可见性决定元素在网页上是可见还是隐藏。它使用 visibility 属性控制。CSS 中的 visibility 属性是控制网页上元素可见性的基本工具。它允许开发人员隐藏或显示元素而不影响页面的布局。此属性接受几个值，但最常用的是 visible 和 hidden。

- visible：元素正常显示。它占用页面上的空间并且对用户可见。
- hidden：元素不显示，但它仍然占用页面上的空间。它实际上是不可见的，但其空间被保留。

#### 语法

使用 visibility 属性的基本语法很简单：

```css
element {
    visibility: value;
}
```

### 值

visibility 属性可以采用几个值，每个值都有其特定的行为：

- visible：这是默认值。元素可见。
- hidden：元素被隐藏但仍占用布局中的空间。
- collapse：此值特定于表格元素。对于表格行、列、列组和行组，collapse 从显示中移除元素并移除它占用的空间。对于其他元素，collapse 被视为 hidden。
- initial：将属性设置为其默认值。
- inherit：从其父元素继承属性。

### 示例

以下是如何在 CSS 中使用 visibility 属性的简单示例：

```css
.my-element {
    visibility: hidden;
}
```

在此示例中，具有 my-element 类的元素将在页面上隐藏，但它仍将占用布局中的空间。

#### visibility 和 display 之间的区别

理解 visibility 和 display 属性之间的区别至关重要：

- visibility: hidden：元素不可见，但它仍占用布局中的空间。它周围的其他元素将表现得好像隐藏的元素仍然存在。
- display: none：元素完全从文档流中移除。它不占用任何空间，其他元素将布局得好像该元素不存在。

#### 用例

#### 何时使用 visibility: hidden

- **保留布局**：当您想要隐藏元素但保持页面布局时使用 visibility: hidden。例如，您可能有一个占位符，您想要隐藏但保留它占用的空间。
- **可访问性**：当您想要在视觉上隐藏元素但仍使其对屏幕阅读器或 JavaScript 可访问时使用 visibility: hidden。

#### 何时使用 display: none

- **移除元素**：当您想要完全从文档流中移除元素时使用 display: none。这对于根本不应该影响页面布局的元素很有用。
- **条件渲染**：当您想要基于某些条件（如用户交互或媒体查询）条件性地渲染元素时使用 display: none。

#### 与 JavaScript 的交互

使用 visibility: hidden 隐藏的元素仍然可以使用 JavaScript 进行交互。例如，您可以更改它们的属性、添加事件监听器或以其他方式操作它们。但是，它们对用户不可见。

### 可访问性考虑

使用 visibility: hidden 时，元素仍然对屏幕阅读器可访问。这对于为依赖辅助技术的用户提供附加上下文或信息很有用。但是，如果您也想完全对屏幕阅读器隐藏元素，您应该使用 display: none。

#### 结论

CSS 中的 visibility 属性是控制网页上元素可见性的强大工具。通过理解 visibility 和 display 之间的区别，并知道何时使用每一个，您可以创建更灵活和可访问的 Web 设计。

请记住，当您想要隐藏元素但保留其空间时使用 visibility，当您想要完全从文档流中移除它时使用 display: none。

