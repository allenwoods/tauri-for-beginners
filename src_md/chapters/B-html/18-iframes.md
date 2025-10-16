# 内联框架

HTML 中的 iframe 是一个强大的工具，允许您在当前页面中嵌入另一个网页。当您想要在网站上直接显示来自外部源的内容（如视频、地图或社交媒体源）时，此功能特别有用。

## 基本用法

要在网页中添加 iframe，您使用 <iframe> 标签并使用 src 属性指定源 URL。这是一个简单的示例：

```html
<iframe src="https://www.example.com"></iframe>
```

此代码将位于 https://www.example.com 的网页嵌入到您的当前页面中。

## 自定义外观和行为

您可以使用各种属性自定义 iframe 的外观和行为：

**宽度和高度**：您可以使用 width 和 height 属性设置 iframe 的尺寸。例如：

```html
<iframe src="https://www.example.com" width="500" height="300"></iframe>
```

**边框**：frameborder 属性控制 iframe 周围边框的存在。将其设置为 0 会移除边框，而 1 会添加边框：

```html
<iframe src="https://www.example.com" frameborder="0"></iframe>
```

**滚动**：scrolling 属性指定 iframe 是否应该有滚动条。您可以将其设置为 yes、no 或 auto：

```html
<iframe src="https://www.example.com" scrolling="no"></iframe>
```

**全屏**：allowfullscreen 属性允许 iframe 在全屏模式下查看：

```html
<iframe src="https://www.example.com" allowfullscreen></iframe>
```

## 安全考虑

当嵌入来自另一个源的内容时，确保源 URL 安全且可信至关重要。这有助于防止中间人攻击等安全风险。为此强烈建议使用 HTTPS。

## 高级功能

**沙盒**：sandbox 属性通过限制嵌入内容可以执行的操作来添加额外的安全层。例如，您可以通过指定适当的限制来禁止脚本或表单：

```html
<iframe src="https://www.example.com" sandbox="allow-scripts"></iframe>
```

- **跨源资源共享（CORS）**：如果嵌入内容需要与您的页面交互，请确保托管 iframe 内容的服务器设置了适当的 CORS 头。
- **响应式 Iframe**：要使 iframe 响应式，您可以使用 CSS 根据视口调整其大小。例如，以下 CSS 使 iframe 响应式：

```css
.responsive-iframe {
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
}
```

您可以像这样将此类应用到您的 iframe：

```html
<iframe src="https://www.example.com" class="responsive-iframe"></iframe>
```

通过理解和利用这些功能，您可以有效地在网页中嵌入和管理 iframe，通过无缝集成外部内容来增强用户体验。

