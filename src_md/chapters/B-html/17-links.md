# 链接

HTML 中的链接使用 <a> 标签创建，它代表"锚点"。此标签对于创建连接不同网页或资源的超链接至关重要。要指定链接的目标，使用 href 属性。例如，如果您想创建指向 Google 主页的链接，您会这样写：

```html
<a href="https://google.com">Google's Homepage</a>
```

target 属性是链接的另一个重要方面。它控制链接文档将在哪里打开。大多数浏览器支持 \_blank 和 \_self 目标。\_blank 目标在新标签页中打开链接，为用户提供在探索新页面时保持当前页面打开的方式。另一方面，\_self 目标在同一标签页中打开链接，替换当前页面。

HTML 中有两种主要类型的链接：绝对链接和相对链接。理解这两种之间的区别对于有效的 Web 开发至关重要。

### 绝对链接

绝对链接包含完整的 URL，包括协议（例如 http、https）。这种类型的链接用于链接到外部网站。绝对链接简单明了，无论在哪里使用都始终指向同一位置。

示例：

```html
<a href="https://google.com">This is an absolute link</a>
```

### 相对链接

相比之下，相对链接不包含完整的 URL。相反，它提供相对于当前页面位置的路径。这种类型的链接对于链接到同一网站内的其他页面特别有用。相对链接使管理内部链接更容易，特别是在站点结构内移动文件时。

示例：

```html
<a href="otherpages/otherpage.html">This is a relative link</a>
```

#### Target 属性

target 属性指定在哪里打开链接文档。最常见的值是 \_blank 和 \_self。

- \_blank：在新标签页中打开链接。
- \_self：在同一标签页中打开链接。

#### 示例：

```html
<a href="https://google.com" target="_blank">This page opens in another tab</a>
<a href="https://google.com" target="_self">This page opens in the current tab</a>
```

通过掌握这些概念，您可以有效地在 HTML 文档中创建和管理链接。无论您是链接到外部资源还是在您自己的站点内导航，理解如何使用绝对和相对链接以及 target 属性都将增强您的 Web 开发技能。

