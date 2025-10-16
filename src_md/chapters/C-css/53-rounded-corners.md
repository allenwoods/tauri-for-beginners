# 圆角

在 CSS 中，可以使用 border-radius 属性实现圆角。此属性允许您将元素的角变圆，使其看起来更视觉上吸引人。

要使用简写表示法应用圆角，您可以使用以下语法：

```css
selector {
    border-radius: 10px;
}
```

这将为元素的所有四个角应用半径为 10 像素的圆角。

如果您想为每个角指定不同的半径，可以使用完整表示法。以下是一个示例：

```css
selector {
    border-top-left-radius: 10px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 30px;
    border-bottom-left-radius: 40px;
}
```

在此示例中，每个角都有不同的半径，允许您创建更复杂的形状。

为了演示圆角的使用，以下是一个带有内部 CSS 的 HTML 文档示例：

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #f2f2f2;
        }
        .box {
            width: 200px;
            height: 200px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 10px;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
```

在此示例中，具有 box 类的 div 元素使用简写表示法设置了圆角样式。border-radius 属性设置为 10px，为元素提供圆角。

