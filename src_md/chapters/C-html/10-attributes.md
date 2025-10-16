# 属性

HTML 中的属性提供有关元素的附加信息。它们用于修改 HTML 元素的行为或外观。

以下是 HTML 中常用属性的一些示例：

## 常见的 HTML 属性

HTML 属性提供有关元素的附加信息，对于修改其行为和外观至关重要。了解如何有效使用这些属性可以大大增强网页的功能和可访问性。让我们探索 HTML 中一些最常用的属性：

#### Class 属性

class 属性用于为元素指定一个或多个类名。此属性对于将相同样式应用于多个元素特别有用。例如：

```html
<div class="container main-content"></div>
```

在此示例中，div 元素有两个类：container 和 main-content。这些类可以用 CSS 定位以应用特定样式。

#### ID 属性

id 属性用于唯一标识元素。这对于用 CSS 或 JavaScript 定位特定元素很有用。例如：

```html
<h1 id="header-title">Welcome to My Website</h1>
```

这里，h1 元素的 id 为 header-title，可用于应用唯一样式或使用 JavaScript 操作元素。

#### Src 属性

src 属性指定外部资源的源 URL，如图片或脚本。例如：

```html
<img src="image.jpg" alt="A beautiful scenery">
```

在这种情况下，src 属性指向图片文件的路径。

#### Href 属性

href 属性定义超链接的目标 URL，通常在 `<a>` 标签中使用。例如：

```html
<a href="https://www.example.com">Visit Example</a>
```

这里，href 属性指定点击链接时将导航到的 URL。

#### Alt 属性

alt 属性为图片提供替代文本，如果图片加载失败或出于可访问性目的，将显示此文本。例如：

```html
<img src="image.jpg" alt="A beautiful scenery">
```

alt 属性提供图片的文本描述，这对屏幕阅读器和图片无法显示时很有用。

这些示例仅说明了 HTML 中可用的众多属性中的几个。每个元素都有自己的一组属性，可用于自定义其行为和外观。其他常用属性包括 title、style、data-*、disabled、readonly 和 placeholder。

有关属性的完整列表及其用法，请始终参考官方 HTML 文档。正确使用属性可以显著提高网页的功能和可访问性。

