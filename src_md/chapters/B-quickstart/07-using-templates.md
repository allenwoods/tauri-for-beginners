# 使用模板

## 命令

创建新的 Tauri 应用程序很简单，您可以根据首选环境从多个命令中选择。让我们探索可用的不同选项：

#### Shell 脚本

对于基于 Unix 的系统，您可以使用以下 shell 脚本来创建新的 Tauri 应用程序。此方法快速高效，让您立即开始：

```shell
sh <(curl https://create.tauri.app/sh)
```

#### PowerShell

如果您是 Windows 用户，PowerShell 命令是正确选择。此命令将无缝设置您的新 Tauri 应用程序：

```powershell
irm https://create.tauri.app/ps | iex
```

### npm

对于那些喜欢使用 npm 的用户，您可以使用以下命令创建新的 Tauri 应用程序。此方法与 npm 生态系统集成良好，使其成为开发者的热门选择：

```shell
npm create tauri-app@latest
```

#### yarn

Yarn 用户也可以轻松创建新的 Tauri 应用程序。以下命令利用 yarn 的功能高效设置您的项目：

```shell
yarn create tauri-app
```

#### pnpm

如果您是 pnpm 的粉丝，您可以使用以下命令创建新的 Tauri 应用程序。Pnpm 以其速度和高效的包管理而闻名：

```shell
pnpm create tauri-app
```

#### deno

对于使用 deno 的开发人员，以下命令将帮助您创建新的 Tauri 应用程序。Deno 为 JavaScript 和 TypeScript 提供安全的运行时：

```shell
deno run -A npm:create-tauri-app
```

#### bun

如果您喜欢使用 bun，您可以使用以下命令创建新的 Tauri 应用程序。Bun 是一个快速的一体化 JavaScript 运行时：

```shell
bun create tauri-app
```

#### cargo

Rust 爱好者可以使用 cargo 创建新的 Tauri 应用程序。以下命令将引导您完成此过程，利用 Rust 的强大功能：

```shell
cargo install create-tauri-app --locked cargo create-tauri-app
```

## 自定义选项

当您运行 create-tauri-app 命令时，系统将提示您选择各种选项来定制项目以满足您的特定需求。这些自定义选项确保您的 Tauri 应用程序完全按照您想要的方式设置。

#### 包管理器

您将做出的第一个选择之一是选择您首选的包管理器。您可以从以下选项中选择：

- **yarn**
- **npm**
- **bun**

## Rust 模板

使用 Rust 创建 Tauri 应用程序时，您有几个 UI 模板可供选择。每个模板都迎合不同的开发偏好和风格，让您选择最适合您需求的模板：

- **Vanilla**: 这个最小模板为您的基于 Rust 的 Tauri 应用程序提供了一个干净的起点，不包含额外的框架。
- **Yew**: 一个用于使用 WebAssembly 构建多线程前端 Web 应用程序的现代 Rust 框架。Yew 以其性能和易用性而闻名。
- **Leptos**: 一个用于使用 Rust 构建快速、交互式 Web 应用程序的全栈框架。Leptos 为 Web 开发提供全面的解决方案。
- **Sycamore**: 一个受 React 启发的用于在 Rust 中创建 Web 应用程序的响应式框架。Sycamore 专注于简单性和响应性。

## TypeScript / JavaScript 模板

对于使用 TypeScript 或 JavaScript 的开发人员，Tauri 提供各种 UI 模板来匹配您首选的框架。这些模板为您的项目提供坚实的起点：

- **Vanilla**: 一个不包含任何额外框架的基本模板，适合那些喜欢从头开始的人。
- **Vue**: 一个用于构建用户界面的渐进式框架，以其简单性和灵活性而闻名。Vue 是现代 Web 开发的热门选择。
- **Svelte**: 一个生成最小且高效的 JavaScript 代码的编译器，提供构建 Web 应用程序的独特方法。Svelte 以其性能和开发体验而闻名。

- **React**: 一个用于构建用户界面的流行库，特别是单页应用程序，具有基于组件的架构。React 在行业中广泛使用。
- **Solid**: 一个用于创建用户界面的声明式 JavaScript 库，专注于细粒度响应性。Solid 提供现代 UI 开发方法。
- **Angular**: 一个使用 HTML 和 TypeScript 构建单页客户端应用程序的平台和框架。Angular 为大型应用程序提供全面的解决方案。
- **Preact**: 一个具有相同现代 API 的快速 3kB React 替代品，为构建 Web 应用程序提供轻量级解决方案。Preact 非常适合性能关键的应用程序。

您还可以根据您的偏好和项目要求选择项目的风格，**TypeScript** 或 **JavaScript**。

## .NET 模板

对于使用 .NET 的开发人员，Tauri 提供使用 Blazor 构建 Web 应用程序的模板。Blazor 允许您为 Tauri 应用程序利用 .NET 的强大功能：

**Blazor**: 一个使用 C# 而不是 JavaScript 构建交互式 Web UI 的框架。Blazor 使您能够使用熟悉的 .NET 创建丰富的 Web 应用程序。更多信息可以在 [Blazor](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor/) 找到。

通过选择适当的模板和风格，您可以定制 Tauri 项目以满足您的特定开发需求和偏好。这种灵活性确保您可以使用最舒适的工具和框架构建应用程序，从而获得更高效和愉快的开发体验。

一旦您生成了模板，为了打开开发窗口，您必须首先进入项目根目录，并为您首选的包管理器运行适当的命令。

例如：

```shell
pnpm run tauri dev
```

