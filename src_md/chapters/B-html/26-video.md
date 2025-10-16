# 视频

就像音频元素一样，源在 <source> 元素中定义。为了在大多数浏览器上播放视频，还需要定义 type 属性。此属性指定视频文件的 MIME 类型，这有助于浏览器确定是否可以播放该文件。

<video> 元素支持各种属性：

- width 和 height：定义视频播放器的尺寸。
- controls：添加视频控件，如播放、暂停和音量。
- autoplay：在准备就绪时立即开始播放视频。
- loop：使视频在每次完成时重新开始。
- muted：默认静音视频的音频。

以下是具有多个源的基本视频元素示例：

```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>
```

#### 在此示例中：

- width 和 height 属性设置视频播放器的大小。
- controls 属性添加播放控件。
- 提供了两个 <source> 元素，每个都有不同的视频格式（mp4 和 ogg）。这确保了跨不同浏览器的更好兼容性。
- 如果浏览器不支持 <video> 元素，则显示文本"Your browser does not support the video tag."。

通过使用多个 <source> 元素，您可以提供不同的视频格式，以确保您的视频在各种浏览器和设备上播放。

