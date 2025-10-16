# 为您的 Flathub 应用创建 MetaInfo

## 制作您的元数据文件

要为您的 Flathub 应用程序创建元数据文件，您需要遵循特定的 XML 结构。以下是您的元数据文件应该看起来的示例：

 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>org.your.id</id>
    <launchable type="desktop-id">org.your.id.desktop</launchable>
    <name>Your App's Name</name>
    <developer id="io.github.roseblume.rosemusic">
        <name>Your Name</name>
    </developer>
    <content_rating type="oars-1.1">
    </content_rating>
    <keywords>
        <keyword>Keyword1</keyword>
        <keyword>Keyword2</keyword>
    </keywords>
    <branding>
        <color type="primary" scheme_preference="light">#00ffff</color>
        <color type="primary" scheme_preference="dark">#0c9aff</color>
    </branding>
    <recommends>
        <display_length compare="ge">360</display_length>
    </recommends>
    <summary>Your Summary</summary>
    <metadata_license>MIT</metadata_license>
    <project_license>MIT</project_license>
    <url type="homepage">https://github.com/Your-Username/Your-Repo</url>
    <supports>
        <control>pointing</control>
        <control>keyboard</control>
        <control>touch</control>
    </supports>
    <description>
        <p>
            Your Description
        </p>
    </description>
    <screenshots>
        <screenshot type="default">
            <image>https://site.com/your-image.png</image>
            <caption>Your Caption</caption>
        </screenshot>
    </screenshots>
    <releases>
        <release version="1.0.0" date="2024-11-02" >
            <description>
            <ul>
                <li>Updated UI</li>
                <li>Added Electronic Genre</li>
            </ul>
            </description>
        </release>
```

 

```xml
</releases>
    <update_contact>your-email@place.com</update_contact>
</component>
```

#### 必需部分

您的元数据文件必须包含以下部分：

- <id>：您应用程序的唯一标识符，应与清单文件中的 ID 匹配。
- <project_license>：指定您的项目分发的许可证。
- <name>：您应用程序的名称，它将显示给用户。
- <summary>：您的应用程序功能的简要摘要。
- <developer>：有关应用程序开发者的信息，包括 ID 和名称。示例：

```xml
<developer id="org.example">
    <name>Developer Name</name>
</developer>
```

<description>：您应用程序的详细描述，可以包括段落、强调文本、代码片段、列表等。示例：

```xml
<description>
    <p>Some <em>description</em></p>
    <p>Some <code>description</code></p>
    <p>A list of features</p>
    <ul>
        <li>First Feature</li>
        <li>Second Feature</li>
        <li>Third Feature</li>
    </ul>
    <p>The app can do:</p>
    <ol>
        <li>First Feature</li>
        <li>Second Feature</li>
        <li>Third Feature</li>
    </ol>
</description>
```

<launchable>：指定应用程序如何启动，通常引用桌面入口文件。示例：

```xml
<launchable type="desktop-id">org.example.app.desktop</launchable>
```

## 将您的 MetaInfo 文件添加到您的 Linux 包中

要在您的 Linux 包中包含您的元信息文件，您需要在配置中指定文件路径。以下是 Debian 和 RPM 包的示例配置：

```json
"linux": {
    "deb": {
        "files": {
            "/usr/share/metainfo/org.your.id.metainfo.xml":
"relative/path/from/your/tauri.conf.json/to/your/org.your.id.metainfo.xml"
        }
    },
    "rpm": {
        "files": {
            "/usr/share/metainfo/org.your.id.metainfo.xml":
"relative/path/from/your/tauri.conf.json/to/your/org.your.id.metainfo.xml"
        }
    }
}
```

