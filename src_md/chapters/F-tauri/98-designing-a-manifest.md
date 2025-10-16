# 设计清单

## 为开源软件设计清单

#### 1. 获取所需的工具

首先，您需要收集构建 Flatpak 所需的工具。使用以下命令添加所需的子模块并安装必要的依赖项：

```shell
git submodule add https://github.com/flatpak/flatpak-builder-tools.git
cd flatpak-builder-tools/node/flatpak_node_generator
pipx install . # 将此更改为您首选的安装方法
```

#### 2. 生成您的源

根据您使用的是 Yarn 还是 NPM，您需要生成您的 Node 和 Cargo 源。

#### Yarn

要使用 Yarn 生成您的 Node 源，请使用以下命令：

```shell
flatpak-node-generator --no-requests-cache -o node-sources.json yarn
/path/to/your/lock/file/yarn.lock
```

接下来，生成您的 Cargo 源：

```shell
python3 flatpak-builder-tools/cargo/flatpak-cargo-generator.py -o cargo-
sources.json src-tauri/Cargo.lock
```

#### NPM

如果您使用的是 NPM，请使用此命令生成您的 Node 源：

```shell
flatpak-node-generator --no-requests-cache -o node-sources.json npm /path/to/your/lock/file/package-lock.json
```

然后，生成您的 Cargo 源：

```shell
python3 flatpak-builder-tools/cargo/flatpak-cargo-generator.py -o cargosources.json src-tauri/Cargo.lock
```

### 3. 创建您的清单

现在，创建您的 Flatpak 清单。此文件定义您的应用程序的配置和构建说明。以下是示例清单：

 

```
id: org.your.id
runtime: org.gnome.Platform
runtime-version: '47'
sdk: org.gnome.Sdk
command: tauri-app
finish-args:
  - --socket=wayland # Permission needed to show the window
  - --socket=fallback-x11 # Permission needed to show the window
  - --device=dri # OpenGL, not necessary for all projects
  - --share=ipc
sdk-extensions:
  - org.freedesktop.Sdk.Extension.node20
  - org.freedesktop.Sdk.Extension.rust-stable
build-options:
  append-path: /usr/lib/sdk/node20/bin:/usr/lib/sdk/rust-stable/bin
modules:
  - name: your-command
    buildsystem: simple
    env:
        HOME: /run/build/your-module
        CARGO_HOME: /run/build/your-module/src-tauri
        XDG_CACHE_HOME: /run/build/your-module/flatpak-node/cache
        yarn_config_offline: 'true'
        yarn_config_cache: /run/build/your-module/flatpak-node/yarn-cache
    sources:
      - type: git
        url: https://github.com/Your-Github-Username/Your-Git-Repo.git
        tag: v1.2.2
      - cargo-sources.json
      - node-sources.json
    build-commands:
      - echo -e 'yarn-offline-mirror "/run/build/your-module/flatpak-node/yarn-
mirror"\nyarn-offline-mirror-pruning true' > /run/build/your-module/.yarnrc
      - mkdir -p src-tauri/.cargo && echo -e '[source.crates-io]\nreplace-with =
"vendored-sources"\n\n[source.vendored-sources]\ndirectory = "/run/build/your-
module/cargo/vendor"' > src-tauri/.cargo/config.toml
      - yarn install --offline --immutable --immutable-cache --inline-builds
      - yarn run tauri build -- -b deb
      - ar -x src-tauri/target/release/bundle/deb/*.deb
      - tar -xf src-tauri/target/release/bundle/deb/your-app/data.tar.gz
      - install -Dm755 src-tauri/target/release/bundle/deb/your-
app/data/usr/bin/your-command /app/bin/your-command
      - install -Dm644 src-tauri/target/release/bundle/deb/your-
app/data/usr/share/applications/Rosary-Music.desktop
/app/share/applications/org.your.id.desktop
      - install -Dm644 src-tauri/target/release/bundle/deb/your-
app/data/usr/share/icons/hicolor/128x128/apps/your-app.png
/app/share/icons/hicolor/128x128/apps/your-app.png
      - install -Dm644 src-tauri/target/release/bundle/deb/your-
app/data/usr/share/icons/hicolor/32x32/apps/your-app.png
```

 

```
/app/share/icons/hicolor/32x32/apps/your-app.png
      - install -Dm644 src-tauri/target/release/bundle/deb/your-
app/data/usr/share/icons/hicolor/256x256@2/apps/your-app.png
/app/share/icons/hicolor/512x512/apps/your-app.png
      - install -Dm644 src-tauri/target/release/bundle/deb/your-
app/data/usr/share/icons/hicolor/scalable/apps/your-app.svg
/app/share/icons/hicolor/scalable/apps/your-app.svg
      - install -Dm644 src-tauri/target/release/bundle/deb/your-
app/data/usr/share/metainfo/org.your.id /app/share/metainfo/org.your.id
```

## 提交到 Flathub

要将您的应用程序提交到 Flathub，请按照以下步骤操作：

- 1. 分叉 Flathub 仓库。
- 2. 克隆您分叉的仓库：

```shell
git clone --branch=new-pr git@github.com:your_github_username/flathub.git
```

3. 进入仓库：

```shell
cd flathub
```

4. 创建新分支：

```shell
git checkout -b your_app_name
```

- 5. 在 GitHub 上针对 new-pr 分支打开 pull request。
- 6. 您的应用程序现在将进入审查过程，在此过程中可能会要求您对项目进行更改。

## 为闭源软件设计清单

### 步骤 1. 安装 flatpak 和 flatpak-builder

要在本地构建 Flatpaks，您需要 flatpak 和 flatpak-builder 工具。根据您的发行版使用以下命令安装它们：

#### Debian

```shell
sudo apt install flatpak flatpak-builder
```

#### Arch

```shell
sudo pacman -S --needed flatpak flatpak-builder
```

#### Fedora

```shell
sudo dnf install flatpak flatpak-builder
```

#### Gentoo

```shell
sudo emerge --ask \
sys-apps/flatpak \
dev-util/flatpak-builder
```

#### 步骤 2. 安装 Gnome 运行时

使用以下命令安装 Gnome 运行时：

```shell
flatpak install flathub org.Gnome.Platform//46 org.Gnome.Sdk//46
```

### 步骤 3. 构建您的 tauri-app 的 .deb

按照这里的说明构建您的 Tauri 应用程序的 .deb 包。

#### 步骤 4. 创建清单

为闭源软件创建您的 Flatpak 清单：

 

```
id: org.your.id
runtime: org.gnome.Platform
runtime-version: '46'
sdk: org.gnome.Sdk
command: tauri-app
finish-args:
  - --socket=wayland # Permission needed to show the window
  - --socket=fallback-x11 # Permission needed to show the window
  - --device=dri # OpenGL, not necessary for all projects
  - --share=ipc
modules:
  - name: binary
    buildsystem: simple
    sources:
      - type: file
        url:
https://github.com/your_username/your_repository/releases/download/v1.0.1/yourapp_
1.0.1_amd64.deb
        sha256: 08305b5521e2cf0622e084f2b8f7f31f8a989fc7f407a7050fa3649facd61469 #
This is required if you are using a remote source
        only-arches: [x86_64] # This source is only used on x86_64 Computers
    build-commands:
      - ar -x *.deb
      - tar -xf data.tar.gz
      - 'install -Dm755 usr/bin/tauri-app /app/bin/tauri-app'
      - install -Dm644 usr/share/applications/yourapp.desktop
/app/share/applications/org.your.id.desktop
      - install -Dm644 usr/share/icons/hicolor/128x128/apps/yourapp.png
/app/share/icons/hicolor/128x128/apps/org.your.id.png
      - install -Dm644 usr/share/icons/hicolor/32x32/apps/yourapp.png
/app/share/icons/hicolor/32x32/apps/org.your.id.png
      - install -Dm644 usr/share/icons/hicolor/256x256@2/apps/yourapp.png
/app/share/icons/hicolor/256x256@2/apps/org.your.id.png
      - install -Dm644 org.your.id.metainfo.xml
/app/share/metainfo/org.your.id.rosary.metainfo.xml
```

Gnome 46 运行时包含标准 Tauri 应用程序的所有依赖项及其正确版本。

#### 步骤 5. 安装和测试应用程序

使用以下命令安装和测试您的 Flatpak 应用程序：

```shell
# 安装 flatpak
flatpak -y --user install <local repo name> <your flatpak id>
# 运行它
flatpak run <your flatpak id>
# 更新它
flatpak -y --user update <your flatpak id>
```

## 添加额外的库

如果您的最终二进制文件需要比默认 Tauri 应用程序更多的库，您需要将它们添加到您的 Flatpak 清单中。有两种方法可以做到这一点：

- 1. 对于快速的本地开发，您可以从本地系统包含已构建的库文件（.so）。但是，不建议将此用于 Flatpak 的最终构建，因为您的本地库文件不是为 Flatpak 运行时环境构建的。这可能会引入各种难以发现的错误。
- 2. 建议在 Flatpak 内部作为构建步骤从源码构建您的程序依赖的库。

 