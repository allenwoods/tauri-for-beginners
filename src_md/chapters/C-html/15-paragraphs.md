# 段落

在 HTML 中，`<p>` 标签是定义段落的基础。作为块级元素，它自然在新行开始并跨越其容器的全宽。这种行为确保段落视觉上不同，大多数浏览器在文本前后添加默认边距以增强可读性。

#### 代码示例

考虑以下示例，它演示了在 HTML 文档中使用 `<p>` 标签：

```html
<!DOCTYPE html>
<html>
<head>
    <title>Paragraph Example</title>
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
    ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
    occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum.</p>
</body>
</html>
```

### 详细解释

- `<!DOCTYPE html>` 声明指定 HTML 版本并确保正确渲染。
- `<html>` 标签作为文档的根元素。
- 在 `<head>` 部分中，定义了文档标题等元信息。
- `<body>` 部分包含可见内容，包括标题和段落。
- `<h1>` 标签表示主标题。
- 每个 `<p>` 标签封装一个段落，确保文本整齐组织和分离。

#### 在浏览器中的渲染

在浏览器中查看时，`<p>` 标签内的内容显示为不同的段落，每个段落之间用空格分隔。这种间距由浏览器的默认样式表控制，但可以使用 CSS 进行定制。

