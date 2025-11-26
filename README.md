# CodeQL_MCP_Demo

一个集成了 CodeQL 的代码分析智能体，由本地大模型驱动，提供一站式的代码安全分析服务。

Fork自CodeQL_MCP仓库 [CodeQL_MCP](https://github.com/Sinnermen10086/CodeQL_MCP)。

## 1.环境搭建

### 1.1 安装依赖

```bash
pip install -r requirements.txt
```

### 1.2 下载模型并测试

在 Model_Download 目录下运行 download_model.py 脚本，下载模型。

注意修改 download_model.py 脚本中的 local_dir 变量，指定模型的下载目录。

```python
# 指定本地下载目录
local_dir = "./deepseek-coder-1.3b"
```

测试模型，运行 Model_Download 目录下的 model_test.py 脚本，验证模型是否能够加载成功。

### 1.3 下载 CodelQL 和 CodeQL 数据库

CodeQL下载链接 [CodeQL](https://github.com/github/codeql-cli-binaries/releases)

在CodeQL应用目录下，下载CodeQL查询库：

```bash
git clone git@github.com:github/codeql.git
```

在代码中，查询库是在 \codeql\codeql-main 下，这个自己调整对应目录即可。

### 1.4 修改配置文件

在 config.py 文件中，配置对应路径，包括模型路径、CodeQL路径、查询库路径等。

- CODEQL_ROOT_QUERY : CodeQL查询根目录路径
- CODEQL_PATH : CodeQL主安装路径
- CODEQL_BIN : CodeQL可执行文件完整路径
- CODEQL_QUERIES : CodeQL查询文件目录路径
- OUTPUT_DIR : 分析结果输出目录
- DEVICE : 设备配置（CUDA或CPU）
- MODEL_PATH : 本地模型路径

## 2. 运行示例

对于对话示例，运行 main_cli_with_codeql_demo.py 脚本，输入项目路径，即可开始自动进行代码安全分析。

```bash
python main_cli_with_codeql_demo.py

[Model] 模型加载中...[Model] 模型加载完成！

=== MCP 安全分析系统 (输入 quit 或 exit 结束) ===
提示: 你可以直接输入项目路径进行自动分析，或者询问安全相关问题

 请输入项目路径（目录）：C:\Users\Aono\Desktop\Project\CodeQL_MCP_Test\Target_Test\
```

对于 MCP 示例，运行 main_mcp_demo.py 脚本，项目路径作为参数输入，即可开始自动进行代码安全分析。

```bash
python main_mcp_demo.py C:\Users\Aono\Desktop\Project\CodeQL_MCP_Test\Target_Test\

正在加载模型... [Model] [MCP] 模型加载完成......
==================================================
开始分析项目: C:\Users\Aono\Desktop\Project\CodeQL_MCP_Test\Target_Test\
==================================================

```

分析结果会输出到 OUTPUT_DIR 目录下。



