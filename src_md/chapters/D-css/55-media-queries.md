# 媒体查询

CSS 中的媒体查询是一个强大的工具，允许您基于各种条件应用不同的样式。它们是响应式 Web 设计的基石，使您能够在不同设备和屏幕尺寸上创建无缝的用户体验。在本章中，我们将探索媒体查询的一些详细示例和附加功能。

## 基本示例

#### 首选颜色方案

prefers-color-scheme 媒体功能允许您针对具有特定颜色方案偏好的设备。例如，您可以为偏好浅色或深色颜色方案的设备应用不同的样式。以下是一个示例：

```css
@media (prefers-color-scheme: dark) {
    body {
        background-color: #000; /* 为深色模式设置黑色背景 */
        color: #fff; /* 为深色模式设置白色文本 */
    }
}
```

#### 方向

您还可以使用媒体查询基于设备方向应用样式。例如，您可以根据设备是横向还是纵向模式来更改布局：

```css
@media (orientation: landscape) {
    body {
        display: flex;
        flex-direction: row;
    }
}
@media (orientation: portrait) {
    body {
        display: flex;
        flex-direction: column;
    }
}
```

#### 屏幕宽度

媒体查询的另一个常见用途是基于屏幕宽度应用样式。这对于创建适应不同屏幕尺寸的响应式设计特别有用：

```css
@media (max-width: 600px) {
    body {
        font-size: 14px;
    }
}
```

#### 分辨率

您可以使用 min-resolution 媒体功能针对高分辨率屏幕的设备。这对于为能够显示高分辨率图像的设备提供高分辨率图像很有用：

```css
@media (min-resolution: 2dppx) {
    img {
        content: url(high-res-image.png);
    }
}
```

### 宽高比

媒体查询还可以用于基于设备的宽高比应用样式。这可以帮助您创建在宽屏和窄屏上都看起来很好的布局：

```css
@media (min-aspect-ratio: 16/9) {
    .container {
        width: 80%;
    }
}
@media (max-aspect-ratio: 4/3) {
    .container {
        width: 100%;
    }
}
```

#### 悬停和指针

您可以使用媒体查询基于用户的输入方法应用样式。例如，当用户用鼠标悬停在链接上时，您可以更改链接的外观：

```css
@media (hover: hover) {
    a:hover {
        text-decoration: underline;
    }
}
@media (pointer: fine) {
    button {
        padding: 10px 20px;
    }
}
```

#### 显示模式

display-mode 媒体功能允许您基于应用程序的显示模式应用样式。例如，您可以为在全屏模式下运行的应用程序创建全屏布局：

```css
@media (display-mode: fullscreen) {
    .fullscreen {
        width: 100vw;
        height: 100vh;
    }
}
```

#### 组合媒体功能

您可以组合多个媒体功能来创建更具体的样式。例如，您可以为最小宽度为 600px 且偏好深色颜色方案的设备应用样式：

```css
@media (min-width: 600px) and (prefers-color-scheme: dark) {
    body {
        background-color: #333;
        color: #ccc;
    }
}
```

通过使用媒体查询，您可以创建适应不同设备和用户偏好的响应式设计，提供更好的用户体验。

