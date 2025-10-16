# 列表

#### 有序列表

有序列表是呈现特定序列中项目的绝佳方式。它们使用 <ol> 元素，列表中的每个项目都包装在 <li> 元素中。默认情况下，项目从 1 开始编号，使其非常适合说明、排名或顺序很重要的任何场景。

以下是 HTML 中有序列表的示例：

```html
<h2>This is an ordered list</h2>
<ol>
  <li>This is number 1</li>
  <li>This is number 2</li>
  <li>This is number 3</li>
</ol>
```

如果您需要从不同的值开始编号，可以使用 start 属性：

```html
<h2>This is an ordered list starting from 5</h2>
<ol start="5">
  <li>This is number 5</li>
  <li>This is number 6</li>
  <li>This is number 7</li>
</ol>
```

### 无序列表

当项目的顺序不重要时，使用无序列表。它们使用 <ul> 元素，每个项目也包装在 <li> 元素中。与数字不同，每个项目通常以项目符号为前缀。

以下是 HTML 中无序列表的示例：

```html
<h2>This is an unordered list</h2>
<ul>
  <li>This is item 1</li>
  <li>This is item 2</li>
  <li>This is item 3</li>
</ul>
```

您可以使用 CSS 自定义项目符号以更改其外观：

```html
<h2>This is a customized unordered list</h2>
<ul style="list-style-type: square;">
  <li>This is item 1</li>
  <li>This is item 2</li>
  <li>This is item 3</li>
</ul>
```

#### 描述列表

描述列表非常适合定义术语及其描述。它们使用 <dl> 元素，每个术语包装在 <dt> 元素中，每个描述包装在 <dd> 元素中。这种格式对于词汇表、定义或元数据特别有用。

以下是 HTML 中描述列表的示例：

```html
<h2>This is a description list</h2>
<dl>
  <dt>Espresso</dt>
  <dd>- black hot drink</dd>
  <dt>Milk</dt>
  <dd>- white cold drink</dd>
</dl>
```

您还可以在单个术语下分组多个描述：

```html
<h2>This is a grouped description list</h2>
<dl>
  <dt>Coffee</dt>
  <dd>- black hot drink</dd>
  <dd>- can be served with milk</dd>
  <dt>Tea</dt>
  <dd>- hot drink</dd>
  <dd>- can be served with lemon</dd>
</dl>
```

 

