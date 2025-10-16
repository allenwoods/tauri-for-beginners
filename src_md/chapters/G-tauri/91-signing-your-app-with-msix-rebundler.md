# 使用 MSIX Rebundler 签名您的应用

本指南将引导您完成使用 MSIX Rebundler 签名应用程序的过程。

## 先决条件

在开始之前，请确保您具备以下条件：

- Windows 10 或更高版本
- 已安装 MSIX Packaging Tool
- 有效的代码签名证书

## 步骤

#### 1. 安装 MSIX Rebundler

从官方 MSIX Rebundler GitHub 仓库下载并安装 MSIX Rebundler。

#### 2. 准备您的应用

确保您的应用已打包为 MSIX 格式。如果没有，请使用 MSIX Packaging Tool 将您的应用转换为 MSIX。

#### 3. 签名您的应用

打开命令提示符并导航到包含您的 MSIX 包的目录。运行以下命令来签名您的应用：

```shell
msixrebundler sign --input <path-to-your-app.msix> --output <path-to-signed-
app.msix> --cert <path-to-your-certificate.pfx> --password <your-certificate-
password>
```

将 <path-to-your-app.msix>、<path-to-signed-app.msix>、<path-to-your-certificate.pfx> 和 <your-certificate-password> 替换为适当的值。

#### 4. 验证签名

要验证您的应用已正确签名，请使用 SignTool 实用程序：

```shell
signtool verify /pa /v <path-to-signed-app.msix>
```

确保验证过程完成且没有错误。

## 结论

您已成功使用 MSIX Rebundler 签名了您的应用。您的应用现在可以分发了。

有关更多信息，请参阅官方 MSIX 文档。

