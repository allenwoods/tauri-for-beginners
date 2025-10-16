# 分发到 Android 设备

## 将 apksigner、keytool 和 zipalign 添加到您的 PATH

要将您的应用程序分发到 Android 设备，您需要确保 apksigner、keytool 和 zipalign 在您系统的 PATH 中可用。以下是添加它们的步骤：

#### 1. 定位工具：

- apksigner 和 zipalign 是 Android SDK Build-Tools 的一部分。您可以在 Android SDK 安装的 build-tools 目录中找到它们。
- keytool 是随 Android Studio 分发的 JetBrains Runtime (JBR) 的一部分。您可以在 JBR 安装的 bin 目录中找到它。

#### 2. 更新您的 PATH：

#### 在 Windows 上：

- 1. 打开开始菜单并搜索"环境变量"。
- 2. 点击"编辑系统环境变量"。
- 3. 在系统属性窗口中，点击"环境变量"按钮。
- 4. 在环境变量窗口中，在"系统变量"部分找到 Path 变量并点击"编辑"。
- 5. 将包含 apksigner、keytool 和 zipalign 的目录路径添加到列表中。例如：

```shell
C:\path\to\android-sdk\build-tools\version
C:\path\to\android-studio\jbr\bin
```

6. 点击"确定"保存更改。

#### 在 macOS 和 Linux 上：

- 1. 打开终端。
- 2. 使用文本编辑器编辑您的 shell 配置文件（例如 ~/.bashrc、~/.zshrc 或 ~/.profile）。
- 3. 将以下行添加到文件中，将路径替换为您工具的实际位置：

```shell
export PATH=$PATH:/path/to/android-sdk/build-tools/version
export PATH=$PATH:/path/to/android-studio/jbr/bin
```

4. 保存文件并运行 source ~/.bashrc（或适用于您的 shell 配置文件的相应命令）以应用更改。

#### 3. 验证 PATH：

- 如果使用 Windows，最好重启您的设备。
- 打开新的终端或命令提示符。
- 运行以下命令以确保工具可访问：

```shell
apksigner -version
keytool -help
zipalign -version
```

如果命令返回版本信息或帮助文本，则工具已成功添加到您的 PATH。

## 签名您的 APK

要签名您的 APK，您需要使用 keytool、zipalign 和 apksigner。请按照以下步骤操作：

#### 1. 生成密钥库：

使用 keytool 生成密钥库文件。此文件将包含用于签名您的 APK 的密钥。

```shell
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -
validity 10000 -alias my-key-alias
```

系统将提示您输入一些信息和密钥库的密码。

#### 2. 构建您的 APK：

在终端中运行以下命令。

```shell
npm run tauri android init
npm run tauri icon /path/to/your/icon.png
npm run tauri android build
```

需要注意的是，如果您在运行 tauri android init 后没有设置图标，您的应用将使用默认的 Tauri 徽标。

#### 3. 对齐 APK：

使用 zipalign 优化 APK 文件。此步骤对于 APK 被 Google Play Store 接受是必要的。您必须在使用 apksigner **之前**运行 zipalign，否则您的 APK 将无效。

```shell
zipalign -v -p 4 path/to/your-app-unsigned.apk path/to/your-app-unsigned-
aligned.apk
```

#### 4. 签名 APK：

使用 apksigner 用您的密钥库签名对齐的 APK。

```shell
apksigner sign --ks my-release-key.jks --out path/to/your-app-release.apk
path/to/your-app-unsigned-aligned.apk
```

#### 5. 验证 APK：

使用 apksigner 验证 APK 是否已正确签名。

```shell
apksigner verify path/to/your-app-release.apk
```

如果验证成功，您的 APK 现在已签名。完成后，您可以将您的发布版本上传到 Google Play Developer Console。

