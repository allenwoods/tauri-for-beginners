# Snapcraft

Snapcraft 是 Linux 的通用软件打包器。上传到 Snapcraft.io 的软件可以显示在 Discover 和 Gnome Software 等软件商店中

#### 步骤 1. 在您选择的发行版上安装 Snap

#### Debian

```shell
sudo apt install snapd
```

#### Arch

```shell
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
sudo systemctl enable --now snapd.socket
sudo systemctl start snapd.socket
sudo systemctl enable --now snapd.apparmor.service
```

#### Fedora

```shell
sudo dnf install snapd
# 启用经典 snap 支持
sudo ln -s /var/lib/snapd/snap /snap
```

#### 步骤 2. 安装基础 snap

```shell
sudo snap install core22
```

#### 3. 安装 snapcraft

```shell
sudo snap install snapcraft --classic
```

 

## 配置

- 1. 创建 UbuntuOne 账户。
- 2. 访问 Snapcraft 网站并注册应用程序名称。
- 3. 在您的项目根目录中创建 snapcraft.yaml 文件。
- 4. 调整 snapcraft.yaml 文件中的名称。

```yaml
name: appname
base: core22
version: '0.1.0'
summary: Your summary # 79 char long summary
description: |
  Your description
grade: stable
confinement: strict
layout:
  /usr/lib/$SNAPCRAFT_ARCH_TRIPLET/webkit2gtk-4.1:
    bind: $SNAP/usr/lib/$SNAPCRAFT_ARCH_TRIPLET/webkit2gtk-4.1
apps:
  appname:
    command: usr/bin/appname
    desktop: usr/share/applications/appname.desktop
    extensions: [gnome]
    #plugs:
    # - network
    # Add whatever plugs you need here, see https://snapcraft.io/docs/snapcraft-
interfaces for more info.
    # The gnome extension already includes [ desktop, desktop-legacy, gsettings,
opengl, wayland, x11, mount-observe, calendar-service ]
package-repositories:
  - type: apt
    components: [main]
    suites: [noble]
    key-id: 78E1918602959B9C59103100F1831DDAFC42E99D
    url: http://ppa.launchpad.net/snappy-dev/snapcraft-daily/ubuntu
parts:
  build-app:
    plugin: dump
    build-snaps:
      - node/20/stable
      - rustup/latest/stable
    build-packages:
      - libwebkit2gtk-4.1-dev
      - build-essential
      - curl
      - wget
      - file
      - libxdo-dev
      - libssl-dev
      - libayatana-appindicator3-dev
      - librsvg2-dev
      - dpkg
    stage-packages:
      - libwebkit2gtk-4.1-0
      - libayatana-appindicator3-1
```

 

```yaml
source: .
    override-build: |
      set -eu
      npm install
      npm run tauri build -- --bundles deb
      dpkg -x src-tauri/target/release/bundle/deb/*.deb $SNAPCRAFT_PART_INSTALL/
      sed -i -e
"s|Icon=appname|Icon=/usr/share/icons/hicolor/32x32/apps/appname.png|g"
$SNAPCRAFT_PART_INSTALL/usr/share/applications/appname.desktop
```

### 说明

- name 变量定义您的应用程序名称，必须设置为您之前注册的名称。
- base 变量定义您使用的核心。
- version 变量定义版本，应在每次更改源仓库时更新。
- apps 部分允许您暴露桌面和二进制文件，使用户能够运行您的应用程序。
- package-repositories 部分允许您添加包仓库以帮助满足您的依赖项。
- build-packages / build-snaps 定义您的 snap 的构建依赖项。
- stage-packages / stage-snaps 定义您的 snap 的运行时依赖项。
- override-pull 部分在拉取源之前运行一系列命令。
- craftctl default 执行默认的拉取命令。
- organize 部分将您的文件移动到适当的目录，以便二进制文件和桌面文件可以暴露给 apps 部分。

#### 构建您的 Snap

构建您的 snap 时，确保在与清单相同的目录中运行此命令

```shell
sudo snapcraft
```

#### 测试

```shell
snap run your-app
```

#### 手动发布

```shell
snapcraft login # 使用您的 UbuntuOne 凭据登录
snapcraft upload --release=stable mysnap_latest_amd64.snap
```

#### 自动构建

- 1. 将您的清单添加到 GitHub 上的项目根目录
- 2. 在您的应用程序开发者页面上点击构建选项卡。
- 3. 点击使用 GitHub 登录。
- 4. 输入您仓库的详细信息。

