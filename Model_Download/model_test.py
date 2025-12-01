from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = r"D:\Projects\CodeQL_MCP_Demo\deepseek-coder-1.3b"  # 你下载的目录

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

print("模型已从本地加载成功！")