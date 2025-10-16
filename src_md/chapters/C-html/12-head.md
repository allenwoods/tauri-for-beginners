# Head

`<head>` 元素是 HTML 文档的重要组成部分。它包含有关文档的元数据和其他不可见信息。在本章中，我们将探索一些可以嵌套在 `<head>` 元素中的常用元素。

## Title 元素

`<title>` 元素指定文档的标题，显示在浏览器的标题栏或标签页中。

#### 示例

```html
<title>My Website</title>
```

#### 解释

这将网页的标题设置为"My Website"。

## Meta 元素

`<meta>` 元素用于提供有关 HTML 文档的元数据，如字符编码、视口设置和关键词。

### 示例

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="A brief description of the webpage">
<meta name="keywords" content="HTML, CSS, JavaScript">
<meta name="author" content="John Doe">
```

#### 解释

- 第一个 `<meta>` 元素将字符编码设置为 UTF-8，确保特殊字符的正确渲染。
- 第二个 `<meta>` 元素将视口设置为设备宽度和初始缩放，使网页在不同设备上响应式。
- 第三个 `<meta>` 元素提供网页的简要描述，可供搜索引擎使用。
- 第四个 `<meta>` 元素指定与网页内容相关的关键词，有助于搜索引擎优化（SEO）。
- 第五个 `<meta>` 元素指定文档的作者。

## Link 元素

`<link>` 元素用于将外部样式表、图标文件或其他外部资源链接到 HTML 文档。

#### 示例

```html
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?
family=Roboto:wght@400;700&display=swap">
```

### 解释

- 第一个 `<link>` 元素将名为"styles.css"的外部 CSS 文件链接到 HTML 文档，允许您为网页设置样式。
- 第二个 `<link>` 元素将名为"favicon.ico"的网站图标文件（显示在浏览器标签页中的图标）链接到 HTML 文档。
- 第三个 `<link>` 元素预连接到 Google Fonts API，这可以提高加载性能。
- 第四个 `<link>` 元素将特定的 Google 字体（Roboto）链接到 HTML 文档，允许您在样式中使用此字体。

## Base 元素

`<base>` 元素指定文档中所有相对 URL 的基础 URL。

#### 示例

```html
<base href="https://example.com/">
```

### 解释

这将文档中所有相对 URL 的基础 URL 设置为"https://example.com/"。因此，如果您有一个带有相对 URL 的锚标签，如 `<a href="/about">About</a>`，它将解析为"https://example.com/about"。

## Style 元素

`<style>` 元素允许您直接在 HTML 文档中包含内部 CSS 样式。

#### 示例

```html
<style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f0f0f0;
    }
</style>
```

#### 解释

此 `<style>` 元素包含内部 CSS，将字体族设置为 Roboto，并将 body 的背景颜色设置为浅灰色。

## Script 元素

`<script>` 元素允许您在 HTML 文档中包含或引用 JavaScript 代码。

#### 示例

```html
<script src="scripts.js" defer></script>
```

#### 解释

此 `<script>` 元素引用名为"scripts.js"的外部 JavaScript 文件，并使用 defer 属性确保脚本在 HTML 文档完全解析后执行。

这些只是可以嵌套在 `<head>` 元素中的元素的一些示例。记住在包含所有必要元素后使用 `</head>` 关闭 `<head>` 元素。

