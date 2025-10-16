# 依赖管理

要编辑 Cargo 中的依赖项，你需要修改 Rust 项目中的 `Cargo.toml` 文件。此文件包含项目依赖项的配置。

要添加新依赖项，你可以使用以下语法：

```toml
[dependencies]
dependency_name = "version"
```

将 `dependency_name` 替换为你想要添加的依赖项名称，将 `version` 替换为所需的版本号或版本约束。

例如，要添加版本为 1.0 的 `serde` 依赖项，你可以这样写：

```toml
[dependencies]
serde = "1.0"
```

要更新现有依赖项，只需在 `Cargo.toml` 文件中更改版本号。

修改 `Cargo.toml` 文件后，你可以运行 `cargo build` 或 `cargo update` 来获取和更新文件中指定的依赖项。

记住在进行任何更改后保存 `Cargo.toml` 文件。

