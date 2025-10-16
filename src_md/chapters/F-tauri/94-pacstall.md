# Pacstall

Pacstall 类似于 Arch User Repository，但它适用于基于 debian 的发行版。它正在快速获得流行。

步骤 1. 在 https://github.com/pacstall/pacstall-programs 创建 pacstall-programs 的分支
步骤 2. 在 packages 目录中创建一个以您应用程序名称命名的文件夹
步骤 3. 创建您的 pacscript。使用在 GitHub 上自动发布的 debian 包是最简单的。所有使用 debian 包源的 pacscripts 都必须以 -deb 为后缀。使用 debian 源使安装您的应用程序更快。

```bash
pkgname="appname-deb"
gives="${pkgname/-deb/}"
pkgver="2.0.3"
pkgdesc="A Bible App developed with tauri"
arch=('amd64' 'arm64' 'armhf')
url="https://github.com/Username/Your_Repository"
maintainer=("Firstname Lastname <email>")
depends=('libwebkit2gtk-4.1-dev' 'build-essential' 'curl' 'wget' 'file' 'libxdo-
dev' 'libssl-dev' 'libayatana-appindicator3-dev' 'librsvg2-dev')
source=
("https://github.com/your_username/your_repository/releases/download/v${pkgver}/ap
p_${pkgver}_${CARCH}.deb")
sha256sums_amd64=
('81c917fdce366aa6d417fdae65306c5f4860fb9dc26c8ffa9a9b62c0d206c54a')
sha256sums_arm64=
('bad20bfad1c337db35ee3f95d59ad5e70c4947b64aa6118de0953ddfec4c1538')
sha256sums_armhf=
('8a8140bf7dcea4852a265b55bca332bb904d249627521b1bd1a985b383fd8307')
```

- pkgname 变量被赋予您的应用程序名称，后缀为 -deb
- gives 变量定义您的可执行文件名称
- pkgver 变量是您应用程序的版本，在定义源时可以使用以提高可维护性
- pkgdesc 是必需变量，包含您应用程序的简短描述
- arch 变量包含有关您应用程序支持哪些架构的信息
- url 变量链接到您应用程序的主页
- maintainer 变量定义当前谁在维护 pacscript
- depends 变量包含您的应用程序所依赖的包列表
- source 变量使用先前定义的变量以提高可维护性，并链接到您应用程序的 deb 文件

步骤 4. 克隆 pacstall-programs 仓库

```shell
git clone https://github.com/pacstall/pacstall-programs
```

步骤 5. 进入仓库主目录

```shell
cd pacstall-programs
```

步骤 6. 为您的包生成 SRCINFO

```shell
./scripts/srcinfo.sh add \${pkgname}
```

步骤 7. 将您的更改上传到 GitHub
步骤 8. 使用以下标题格式打开 Pull request

```
add: `pkgname`
```
 

