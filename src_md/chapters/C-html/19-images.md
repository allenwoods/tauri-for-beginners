# 图片

HTML 中的图片使用 `<img>` 标签嵌入。与大多数其他元素不同，`<img>` 标签是自闭合的，这意味着它没有闭合标签。这是因为它内部不包含任何内容，只有定义图片源和其他属性的属性。

## `<img>` 标签的属性

`<img>` 标签带有几个属性，您可以使用它们来指定图片源和其他属性：

- src：此属性指定您要显示的图片的路径。它可以是绝对 URL（链接到在线图片）或相对 URL（链接到项目目录中的图片）。
- alt：此属性为图片提供替代文本（如果无法显示）。这对可访问性和 SEO 很重要。
- width 和 height：这些属性定义图片的尺寸。

## 示例

#### 相对链接

相对链接指向位于 HTML 文件同一目录或子目录中的图片。这对于作为项目一部分的图片很有用。

```html
<h1>This is a relative link to an image located within the same directory as the
HTML file.</h1>
<img src="America.jpg" alt="Image of America" width="500" height="300" />
```

#### 绝对链接

绝对链接指向托管在外部服务器上的图片。这对于不属于您项目的图片很有用。

```html
<h1>This is an absolute link to an online image</h1>
<img src="https://cdn.britannica.com/68/7068-004-7848FEB4/Flag-Canada.jpg"
alt="Flag of Canada" width="500" height="300" />
```

## 最佳实践

在 HTML 文档中使用图片时，请考虑以下最佳实践：

- **始终包含 alt 属性**：这提高了依赖屏幕阅读器的用户的可访问性，也有利于您网站的 SEO。
- **对项目图片使用相对链接**：这确保在移动或共享项目时包含图片。
- **对外部图片使用绝对链接**：这可以通过不包含大型图片文件来帮助减少项目大小。
- **指定 width 和 height 属性**：这控制图片的显示大小，并可以通过允许浏览器在图片加载之前为其分配空间来改善页面加载时间。

通过遵循这些准则，您可以有效地在 HTML 文档中使用图片来增强网页的视觉吸引力和用户体验。

