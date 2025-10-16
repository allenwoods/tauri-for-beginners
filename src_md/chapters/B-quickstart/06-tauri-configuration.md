# Tauri 配置

在本节中，我们将探索 tauri.conf.json 文件，这是 Tauri 应用程序的主配置文件。此文件允许您自定义应用程序的各个方面，如窗口标题、默认窗口大小以及构建过程中生成的包类型。

#### tauri.conf.json

以下是 tauri.conf.json 文件的示例：

```json
{
    "productName": "example",
    "version": "0.1.0",
    "identifier": "com.example.app",
    "build": {
        "frontendDist": "../src"
    },
    "app": {
        "withGlobalTauri": true,
        "windows": [
            {
                "title": "example",
                "label": "main",
                "maximized": true
            }
        ],
        "security": {
            "csp": null
        }
    },
    "bundle": {
        "active": true,
        "targets": ["deb", "rpm", "nsis", "msi"],
        "icon": [
            "icons/32x32.png",
            "icons/128x128.png",
            "icons/128x128@2x.png",
            "icons/icon.icns",
            "icons/icon.ico"
        ]
    }
}
```

让我们分解此配置文件的关键组件：

- **产品名称和版本**: productName 和 version 字段用于命名包和安装程序。例如，包可能命名为 example\_0.1.0\_arm64.deb。
- **Windows**: windows 数组包含应用程序可以显示的窗口列表。每个窗口都有一个 title 字段，指定显示给用户的标题。
- **Targets**: targets 字段列出了运行 npm run tauri build 时将生成的包和安装程序类型。在此示例中，目标包括 deb、rpm、nsis 和 msi。
- **Icons**: icon 字段包含将用作应用程序图标的图像文件列表。

通过配置这些字段，您可以定制 Tauri 应用程序以满足您的特定需求和偏好。

