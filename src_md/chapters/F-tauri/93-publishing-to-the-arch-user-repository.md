# 发布到 Arch User Repository

## 介绍

Arch User Repository 是由 archlinux 社区管理的 git 仓库集合。在每个仓库中都有一个构建脚本，保存在 PKGBUILD 文件中，以及一个 .SRCINFO 文件，包含构建脚本使用的源信息。

## 设置

首先访问 https://aur.archlinux.org 并创建一个账户。确保添加适当的 ssh 密钥。接下来，使用此命令克隆一个空的 git 仓库。

```shell
git clone https://aur.archlinux.org/your-repo-name
```

完成上述步骤后，创建一个名为 PKGBUILD 的文件。创建文件后，您可以继续下一步。

### 编写 PKGBUILD 文件

```bash
pkgname=<pkgname>
pkgver=1.0.0
pkgrel=1
pkgdesc="Description of your app"
arch=('x86_64' 'aarch64')
url="https://github.com/<user>/<project>"
license=('mit')
depends=('cairo' 'desktop-file-utils' 'gdk-pixbuf2' 'glib2' 'gtk3' 'hicolor-icon-
theme' 'libsoup' 'pango' 'webkit2gtk')
options=('!strip' '!emptydirs')
install=${pkgname}.install
source_x86_64=
("https://github.com/<user>/<project>/releases/download/v$pkgver/appname_"$pkgver"
_amd64.deb")
source_aarch64=
("https://github.com/<user>/<project>/releases/download/v$pkgver/appname_"$pkgver"
_arm64.deb")
```

- 在文件顶部，定义您的包名并将其分配给变量 pkgname。
- 设置您的 pkgver 变量。通常最好在 source 变量中使用此变量以提高可维护性。
- pkgdesc 变量显示在您的 aur 仓库页面上，告诉访问者您的应用程序的功能。
- arch 变量控制哪些架构可以安装您的包。
- url 变量虽然不是必需的，但有助于使您的包看起来更专业。
- install 变量定义运行安装命令的文件。
- depends 变量包括运行您的应用程序所需的项目列表。对于任何 Tauri 应用程序，您必须包含上述所有依赖项。
- source 变量是必需的，定义您的上游包的位置。您可以通过在变量名末尾添加架构来使源特定于架构。

### 生成 SRCINFO

为了将您的仓库推送到 aur，您必须生成一个 srcinfo 文件。可以使用此命令完成。

```shell
makepkg --printsrcinfo >> .SRCINFO
```

#### 测试

测试应用程序非常简单。您只需要在包含 pkgbuild 文件的同一目录中运行 makepkg -f 并查看是否有效。

### 发布

最后，在测试阶段结束后，您可以使用这些命令将应用程序发布到 arch user repository。

```shell
git add .
git commit -m "Initial Commit"
git push
```

如果一切顺利，您的仓库现在应该出现在 aur 网站上。

## 示例

#### 从 Debian 包提取

```bash
# Maintainer:
# Contributor:
pkgname=<pkgname>
pkgver=1.0.0
pkgrel=1
pkgdesc="Description of your app"
arch=('x86_64' 'aarch64')
url="https://github.com/<user>/<project>"
license=('mit')
depends=('cairo' 'desktop-file-utils' 'gdk-pixbuf2' 'glib2' 'gtk3' 'hicolor-icon-
theme' 'libsoup' 'pango' 'webkit2gtk')
options=('!strip' '!emptydirs')
install=${pkgname}.install
source_x86_64=
("https://github.com/<user>/<project>/releases/download/v$pkgver/appname_"$pkgver"
_amd64.deb")
source_aarch64=
("https://github.com/<user>/<project>/releases/download/v$pkgver/appname_"$pkgver"
_arm64.deb")
sha256sums_x86_64=
('ca85f11732765bed78f93f55397b4b4cbb76685088553dad612c5062e3ec651f')
sha256sums_aarch64=
('ed2dc3169d34d91188fb55d39867713856dd02a2360ffe0661cb2e19bd701c3c')
package() {
    # Extract package data
    tar -xz -f data.tar.gz -C "${pkgdir}"
}
```

```bash
post_install() {
    gtk-update-icon-cache -q -t -f usr/share/icons/hicolor
    update-desktop-database -q
}
post_upgrade() {
    post_install
}
post_remove() {
    gtk-update-icon-cache -q -t -f usr/share/icons/hicolor
    update-desktop-database -q
}
```

#### 从源码构建

```bash
# Maintainer:
pkgname=<pkgname>-git
pkgver=1.1.0
pkgrel=1
pkgdesc="Description of your app"
arch=('any')
url="https://github.com/<user>/<project>"
license=('mit')
depends=('cairo' 'desktop-file-utils' 'gdk-pixbuf2' 'glib2' 'gtk3' 'hicolor-icon-
theme' 'libsoup' 'pango' 'webkit2gtk')
makedepends=('git' 'file' 'openssl' 'appmenu-gtk-module' 'libappindicator-gtk3'
'librsvg' 'base-devel' 'curl' 'wget' 'rustup' 'npm' 'nodejs' 'dpkg')
provides=('<pkgname>')
conflicts=('<binname>' '<pkgname>')
options=('!strip' '!emptydirs')
source=('git+https://github.com/<user>/<project>')
sha256sums=('SKIP')
prepare() {
    cd <project>
    npm install
    npm run tauri build
}
package() {
    cd "$srcdir"/<project>/src-tauri/target/*unknown-linux*/release/bundle/deb
    dpkg-deb -x *.deb here
    cd here
    install -Dm755 usr/bin/myapp "$pkgdir"/usr/bin/myapp
    # Install desktop file
    install -Dm644 usr/share/applications/myapp.desktop
"$pkgdir"/usr/share/applications/myapp.desktop
    # Install icons
    install -Dm644 usr/share/icons/hicolor/128x128/apps/myapp.png
"$pkgdir"/usr/share/icons/hicolor/128x128/apps/myapp.png
    install -Dm644 usr/share/icons/hicolor/256x256@2/apps/myapp.png
"$pkgdir"/usr/share/icons/hicolor/256x256@2/apps/myapp.png
    install -Dm644 usr/share/icons/hicolor/32x32/apps/myapp.png
"$pkgdir"/usr/share/icons/hicolor/32x32/apps/myapp.png
    # Extract package data
}
```

 

