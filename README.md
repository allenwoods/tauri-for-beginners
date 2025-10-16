# 学习 Tauri

[HTML, CSS, JavaScript, and Rust for Beginners: A Guide to Application Development with Tauri](https://v2.tauri.app/assets/learn/community/HTML_CSS_JavaScript_and_Rust_for_Beginners_A_Guide_to_Application_Development_with_Tauri.pdf) 中文翻译

## 📚 在线文档

本教程的在线版本已通过 GitHub Pages 自动部署：

**🌐 [查看在线文档](https://allenwoods.github.io/tauri-for-beginners/)**

## 🚀 本地开发

### 前置要求

- [mdBook](https://rust-lang.github.io/mdBook/) - 用于构建文档

### 安装 mdBook

```bash
# 使用 cargo 安装
cargo install mdbook

# 或使用包管理器
# macOS
brew install mdbook

# Ubuntu/Debian
sudo apt install mdbook
```

### 本地构建和预览

```bash
# 克隆仓库
git clone https://github.com/allenwoods/learn-tauri.git
cd learn-tauri

# 构建文档
mdbook build

# 本地预览（支持热重载）
mdbook serve
```

访问 http://localhost:3000 查看本地预览。

## 📖 内容结构

本教程包含以下章节：

- **前置要求** - 环境配置和项目设置
- **HTML** - 超文本标记语言基础
- **CSS** - 样式表语言
- **JavaScript** - 编程语言基础
- **Rust** - 系统编程语言
- **Tauri** - 跨平台应用开发框架

## 🔄 自动部署

文档通过 GitHub Actions 自动部署到 GitHub Pages：

- 推送到 `main` 或 `master` 分支时自动触发构建
- 使用 mdBook 构建静态网站
- 部署到 GitHub Pages

### GitHub Pages 配置步骤

1. 进入仓库设置 (Settings)
2. 找到 "Pages" 部分
3. 设置源为 "GitHub Actions"
4. 确保工作流权限已启用：
   - Settings → Actions → General → Workflow permissions
   - 选择 "Read and write permissions"

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进本教程！

## 📄 许可证

本项目基于原文档进行翻译和整理。