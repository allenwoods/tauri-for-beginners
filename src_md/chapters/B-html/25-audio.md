# 音频

<audio> 元素用于在文档中嵌入声音内容。它提供了一种标准方式来嵌入音频文件，具有各种控件和属性来增强用户体验。

#### 属性

- controls：此属性为音频播放器添加音频控件，如播放、暂停和音量。
- autoplay：当存在时，音频将在准备就绪时自动开始播放。
- loop：此属性使音频在每次完成时重新开始。
- muted：此属性默认静音音频。
- preload：此属性指定作者认为音频在页面加载时是否以及如何加载。它可以具有以下值：
  - none：页面加载时不应加载音频。
  - metadata：页面加载时只应加载元数据。
  - auto：页面加载时应完全加载音频。

#### <source> 元素

<source> 元素用于为 <audio> 元素指定多个媒体资源。它允许浏览器选择它支持的最佳格式。src 属性指定音频文件的路径，type 属性指定音频文件的 MIME 类型。

### 示例

```html
<audio controls autoplay>
  <source src="dog.ogg" type="audio/ogg">
  <source src="dog.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
```

在此示例中，<audio> 元素包含 controls 和 autoplay 属性。两个 <source> 元素嵌套在 <audio> 元素内，以 OGG 和 MP3 格式提供音频。如果浏览器不支持 <audio> 元素，则显示文本"Your browser does not support the audio element."。

#### 结果

![](_page_69_Picture_3.jpeg)

#### 浏览器支持

<audio> 元素受所有现代浏览器支持，但并非所有浏览器都支持相同的音频格式。提供多种格式以确保跨不同浏览器的兼容性是一个好习惯。

#### 可访问性

为了使音频内容可访问，请考虑为聋人或听力困难的用户提供文本转录或字幕。此外，确保音频控件对依赖键盘导航的用户是可键盘访问的。

### 结论

<audio> 元素是在网页中嵌入音频内容的强大工具。通过使用各种属性并提供多种音频格式，您可以为用户创建灵活且可访问的音频体验。

