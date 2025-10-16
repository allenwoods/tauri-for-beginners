# CSS 基础

内部 CSS 是在 HTML 文档中直接包含 CSS 样式的一种方式。它在 HTML 文件的 `<head>` 部分的 `<style>` 标签中定义。这允许您将样式专门应用于该 HTML 文档。

内部 CSS 示例：

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: lightblue;
        }
        h1 {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Welcome to my website!</h1>
    <p>This is an example of internal CSS.</p>
</body>
</html>
```

外部 CSS 是一个包含您网站所有 CSS 样式的单独文件。它使用 `<head>` 部分的 `<link>` 标签链接到 HTML 文档。这种方法允许您将 CSS 代码与 HTML 代码分开，使跨多个 HTML 文件维护和重用样式变得更加容易。

外部 CSS 示例：HTML 文件（index.html）：

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to my website!</h1>
    <p>This is an example of external CSS.</p>
</body>
</html>
```

CSS 文件（styles.css）：

```css
body {
    background-color: lightblue;
}
h1 {
    color: red;
}
```

内联 CSS 使用 style 属性直接应用于单个 HTML 元素。这允许您与 HTML 标签本身内联定义样式。虽然它对于快速样式更改很有用，但通常不建议用于大型项目，因为它会使 HTML 代码更难阅读和维护。

内联 CSS 示例：

```html
<!DOCTYPE html>
<html>
<body>
    <h1 style="color: red;">Welcome to my website!</h1>
    <p style="font-size: 18px;">This is an example of inline CSS.</p>
</body>
</html>
```

通过使用这些不同类型的 CSS，您可以灵活地选择最适合您特定需求的方法。

