import os
import torch

CODEQL_ROOT_QUERY = r"D:\Code\codeql-win64\codeql\codeql-main\codeql-main"

# CodeQL路径配置
CODEQL_PATH = r"D:\Code\codeql-win64\codeql"
CODEQL_BIN = os.path.join(CODEQL_PATH, "codeql.exe")
CODEQL_QUERIES = r"D:\Code\codeql-win64\codeql\codeql-main\codeql-main"

OUTPUT_DIR = r"D:\Code\CodeQL_MCP_Demo\CodeQL_MCP_Demo\results"

DEVICE      = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_PATH = r"D:\Code\CodeQL_MCP_Demo\deepseek-coder-1.3b"
