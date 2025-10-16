# Windows 前置要求

## Microsoft C++ Build Tools

Tauri 使用 Microsoft C++ Build Tools 进行开发。因此，在开始制作应用之前，您需要安装它。可以通过访问 [https://visualstudio.microsoft.com/visual-cpp-build-tools/.](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 来完成。

进入页面后，点击 **Download Build Tools** 开始下载。下载完成后，点击可执行文件。

确保选中"Desktop Development with C++"选项并开始安装。

## Git

- 步骤 1. 访问 <https://git-scm.com/download/win> 并下载 64 位安装程序
- 步骤 2. 点击安装程序启动向导。
- 步骤 3. 通过向导选择所有推荐选项。
- 步骤 4. 重启计算机。
- 步骤 5. 通过运行以下命令验证是否已安装

```shell
git --help
```

## 常用命令

#### 克隆仓库

git clone https://github.com/RoseBlume/book.git

#### 创建和推送提交

在项目主目录中运行这些命令

```shell
git add .
git commit -m "First Commit"
git push
```

## NodeJS

如果您计划使用 JavaScript 前端，NodeJS 是必需的依赖项。要安装它，您必须访问 [https://nodejs.org](https://nodejs.org/) 并点击 **Download** 按钮。

安装程序下载完成后，点击它以打开安装向导。完成向导的所有安装步骤并使用所有推荐选项。

## Rust

步骤 1. 访问 <https://www.rust-lang.org/tools/install> 步骤 2. 下载 64 位 Rustup-Init.exe 脚本

步骤 3. 点击下载的可执行文件

建议使用默认安装。如果您希望使用更新、不太稳定的 Rust 功能，可以将默认工具链更改为 nightly。需要注意的是，您始终可以通过运行以下命令稍后更改工具链。

```shell
rustup default stable # Change 'stable' to either 'nightly' or 'beta'
```
