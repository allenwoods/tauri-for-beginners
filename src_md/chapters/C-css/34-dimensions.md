# 尺寸

在 CSS 中，可以使用 width 和 height 属性来指定对象的尺寸。

#### 示例

```css
p {
    width: 500px;
    height: 700px;
}
```

此外，这些属性可以使用 vw、vh 和 % 单位。vw 单位将元素的宽度更改为占据屏幕宽度给定百分比数字的像素数。例如，如果宽度为 50vw，对象将占据屏幕宽度的 50%。

#### 示例

这显示了一个高度和宽度等于屏幕总宽度的段落。

```css
p {
    width: 50vw;
    height: 50vw;
}
```

也可以将 height 和 width 属性指定为百分比。

#### 示例

```css
p {
    width: 50%;
    height: 50%;
}
```

