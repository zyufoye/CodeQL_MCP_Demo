import os
import torch

CODEQL_ROOT_QUERY = r"D:\Projects\codeql-win64\codeql\codeql-main"

# CodeQL路径配置
CODEQL_PATH = r"D:\Projects\codeql-win64\codeql"
CODEQL_BIN = os.path.join(CODEQL_PATH, "codeql.exe")
CODEQL_QUERIES = r"D:\Projects\codeql-win64\codeql\codeql-main"

OUTPUT_DIR = r"D:\Projects\CodeQL_MCP_Demo\CodeQL_MCP_Demo\results"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# DeepSeek API 配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")  # 从环境变量获取API密钥
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"  # 或使用其他可用模型如 "deepseek-coder"
