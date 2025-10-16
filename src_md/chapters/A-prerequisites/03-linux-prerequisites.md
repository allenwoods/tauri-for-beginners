# Linux 前置要求

## 系统包

在开始开发应用之前，为您的 Linux 发行版安装必要的依赖项是至关重要的。

#### Debian/Ubuntu

对于 Debian 和 Ubuntu 用户，您可以通过运行以下命令安装所需的包：

```shell
sudo apt update
sudo apt install libwebkit2gtk-4.1-dev \
    build-essential \
    curl \
    wget \
    file \
    libxdo-dev \
    libssl-dev \
    libayatana-appindicator3-dev \
    librsvg2-dev
```

请注意，这些包从 Debian Bookworm 和 Ubuntu Noble 套件开始可用。

### Arch Linux

Arch Linux 用户可以使用以下命令安装必要的包：

```shell
sudo pacman -Syu
sudo pacman -S --needed \
    webkit2gtk-4.1 \
    base-devel \
    curl \
    wget \
    file \
    openssl \
    appmenu-gtk-module \
    libappindicator-gtk3 \
    librsvg
```

#### Fedora/RHEL

对于 Fedora 和 RHEL 用户，使用以下命令安装所需的包：

```shell
sudo dnf check-update
sudo dnf install webkit2gtk4.1-devel \
    openssl-devel \
    curl \
    wget \
    file \
    libappindicator-gtk3-devel \
    librsvg2-devel
sudo dnf group install "C Development Tools and Libraries"
```

#### Gentoo

Gentoo 用户可以通过运行以下命令安装必要的包：

```shell
sudo emerge --ask \
    net-libs/webkit-gtk:4.1 \
    dev-libs/libappindicator \
    net-misc/curl \
    net-misc/wget \
    sys-apps/file
```

#### openSUSE

对于 openSUSE 用户，可以使用以下命令安装所需的包：

```shell
sudo zypper up
sudo zypper in webkit2gtk3-devel \
    libopenssl-devel \
    curl \
    wget \
    file \
    libappindicator3-1 \
    librsvg-devel
sudo zypper in -t pattern devel_basis
```

## Node.js

Node.js 在 Linux 上可以通过多种方式安装。首选方法是使用您发行版的默认包管理器。如果失败，您可以使用其他方法。

### 1. 通过发行版默认包管理器安装

#### Debian, Ubuntu 和 Raspbian

对于基于 Debian 的发行版，使用以下命令：

```shell
sudo apt update
# Only one or both of these packages may be required
sudo apt install npm
sudo apt install nodejs
```

验证安装：

```shell
npm -v
# 10.8.2
node -v
# v22.6.0
```

#### Arch Linux

对于 Arch Linux，使用：

```shell
sudo pacman -Syu
sudo pacman -S --needed \
    npm \
    nodejs
```

#### Fedora 和 RHEL

对于 Fedora 和 RHEL，使用：

```shell
sudo dnf check-update
sudo dnf install \
    nodejs \
    npm
```

### 通过 Node 包管理器安装

Node.js 有用于管理安装和更新的包管理器。

#### FNM (Fast Node Manager)

要安装 FNM 和 Node.js，运行：

```shell
# installs fnm (Fast Node Manager)
curl -fsSL https://fnm.vercel.app/install | bash
# activate fnm
source ~/.bashrc
# download and install Node.js
fnm use --install-if-missing 20
# verifies the right Node.js version is in the environment
node -v # should print `v20.17.0`
# verifies the right npm version is in the environment
npm -v # should print `10.8.2`
```

#### NVM (Node Version Manager)

要安装 NVM 和 Node.js，运行：

```shell
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
# download and install Node.js (you may need to restart the terminal)
nvm install 20
# verifies the right Node.js version is in the environment
node -v # should output something similar to `v20.17.0`
# verifies the right npm version is in the environment
npm -v # should output something similar to `10.8.2`
```

#### 使用 Snap 安装

要使用 Snap 安装 Node.js，确保您已安装 Snapcraft，然后运行：

```shell
sudo snap install node --channel=22/stable --classic
```

此 snap 还提供 nodejs、npm、npx 和 yarn。

## Rust

Rust 是一种低级编程语言，编译快速高效。它提供控制并简化依赖管理。

### 安装

推荐的安装方法是使用提供的脚本：

```shell
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

使用默认安装。要使用更新、不太稳定的 Rust 功能，请更改您的默认工具链：

```shell
rustup default stable # Change 'stable' to either 'nightly' or 'beta'
```

## Android

- 1. 从 [Android Developer Website](https://developer.android.com/studio) 下载并安装 Android Studio
- 2. 设置 JAVA\_HOME 环境变量：

```shell
export JAVA_HOME=/opt/android-studio/jbr
```

- 3. 在 Android Studio 中打开项目，点击设置图标，选择 SDK Manager。安装以下内容：
  - Android SDK Platform (API Level 24 及更高版本)
  - Android SDK Platform-Tools
  - NDK (Side by side)
  - Android SDK Build-Tools
  - Android SDK Command-line Tools
- 4. 设置 ANDROID\_HOME 和 NDK\_HOME 环境变量：

```shell
export ANDROID_HOME="$HOME/Android/Sdk"
export NDK_HOME="$ANDROID_HOME/ndk/$(ls -1 $ANDROID_HOME/ndk)"
```

5. 使用 rustup 添加以下目标：

```shell
rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86\_64-linux-android
```

## 系统包

在开始开发应用之前，为您的发行版安装适当的依赖项是至关重要的。

#### Debian/Ubuntu

```shell
sudo apt update
sudo apt install libwebkit2gtk-4.1-dev \
  build-essential \
  curl \
  wget \
  file \
  libxdo-dev \
  libssl-dev \
  libayatana-appindicator3-dev \
  librsvg2-dev
```

由于 Debian 发行版使用点发布系统，只有在 Debian Bookworm 及更高版本中才能安装这些包。Ubuntu 也有类似情况，您必须使用 Noble 套件及更高版本。

#### Arch Linux

```shell
sudo pacman -Syu
sudo pacman -S --needed \
  webkit2gtk-4.1 \
  base-devel \
  curl \
  wget \
  file \
  openssl \
  appmenu-gtk-module \
  libappindicator-gtk3 \
  librsvg
```

#### Fedora/RHEL

```shell
sudo dnf check-update
sudo dnf install webkit2gtk4.1-devel \
  openssl-devel \
  curl \
  wget \
  file \
  libappindicator-gtk3-devel \
  librsvg2-devel
sudo dnf group install "C Development Tools and Libraries"
```

#### Gentoo

```shell
sudo emerge --ask \
  net-libs/webkit-gtk:4.1 \
  dev-libs/libappindicator \
  net-misc/curl \
  net-misc/wget \
  sys-apps/file
```

#### openSUSE

```shell
sudo zypper up
sudo zypper in webkit2gtk3-devel \
  libopenssl-devel \
  curl \
  wget \
  file \
  libappindicator3-1 \
  librsvg-devel
sudo zypper in -t pattern devel_basis
```

## Node.js

Node.js 在 Linux 上可以通过多种不同方式安装。首选方法是使用您的 Linux 发行版默认包管理器来安装 Nodejs 和 NPM。如果失败，可以使用其他 2 种方法。

#### 1. 通过发行版默认包管理器安装

#### Debian, Ubuntu 和 Raspbian

```shell
sudo apt update
# Only one or both of these packages may be required
sudo apt install npm
sudo apt install nodejs
```

然后运行这些命令以确保 npm 和 nodejs 都已安装

```shell
npm -v
# 10.8.2
node -v
# v22.6.0
```

#### Arch Linux

```shell
sudo pacman -Syu
sudo pacman -S --needed \
  npm \
  nodejs
```

#### Fedora 和 Red Hat Enterprise Linux

```shell
sudo dnf check-update
sudo dnf install \
  nodejs \
  npm
```

#### 通过 Node 包管理器安装

虽然不如简单，但 Nodejs 有用于管理 nodejs 安装和更新的包管理器

#### FNM (Fast Node Manager)

运行此脚本也会安装 FNM。如果由于某种原因您不想安装 FNM，请尝试使用其他方法。

```shell
# installs fnm (Fast Node Manager)
curl -fsSL https://fnm.vercel.app/install | bash
# activate fnm
source ~/.bashrc
# download and install Node.js
fnm use --install-if-missing 20
# verifies the right Node.js version is in the environment
node -v # should print `v20.17.0`
# verifies the right npm version is in the environment
npm -v # should print `10.8.2`
```

#### 使用 NVM (Node Version Manager) 安装

运行此脚本也会安装 NVM。如果由于某种原因您不想安装 NVM，请尝试使用其他方法。

```shell
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
# download and install Node.js (you may need to restart the terminal)
nvm install 20
# verifies the right Node.js version is in the environment
node -v # should output something similar to `v20.17.0`
# verifies the right npm version is in the environment
npm -v # should output something similar to `10.8.2`
```

#### 使用 Snap 安装（需要安装 Snap）

使用 Snap 安装很简单，但是您必须在运行这些命令之前完成安装 Snapcraft 的前置要求，否则会失败。

```shell
sudo snap install node --channel=22/stable --classic
```

此 snap 还提供 nodejs、npm、npx 和 yarn。

## Rust

Rust 是一种低级编程语言，旨在尽可能快地编译成最小的二进制文件，开销很小。它为用户提供大量控制并简化依赖管理。

### 安装

推荐的安装方法是使用提供的脚本。

```shell
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

建议使用默认安装。如果您希望使用更新、不太稳定的 rust 功能，可以将默认工具链更改为 nightly。需要注意的是，您始终可以通过运行以下命令稍后更改工具链。

```shell
rustup default stable # Change 'stable' to either 'nightly' or 'beta'
```

## Android

- 1. 从 Android Developer Website https://developer.android.com/studio 下载并安装 Android Studio
- 2. 在终端中设置 JAVA\_HOME 环境变量。位置可能因您的安装方法而异。

```shell
export JAVA_HOME=/opt/android-studio/jbr
```

- 3. 在您新安装的 Android Studio 版本中打开项目，点击右上角的设置图标。点击 SDK Manager，它应该在点击设置按钮后出现在下拉菜单中。安装以下内容。
- Android SDK Platform (API Level 24 及更高版本)
- Android SDK Platform-Tools
- NDK (Side by side)
- Android SDK Build-Tools
- Android SDK Command-line Tools
- 4. 设置 ANDROID\_HOME 和 NDK\_HOME 环境变量。位置可能因您的安装而异

```shell
export ANDROID_HOME="$HOME/Android/Sdk"
export NDK_HOME="$ANDROID_HOME/ndk/$(ls -1 $ANDROID_HOME/ndk)"
```

5. 使用 rustup 添加以下目标

```shell
rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86\_64-linux-android
```
