import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "") 
print(DEEPSEEK_API_KEY)

# —— 加载模型 —— #
print("[Model] 使用DeepSeek API进行报告生成...")

# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": prompt},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)



def call_deepseek_api(prompt):
    """调用DeepSeek API生成响应"""
    if not DEEPSEEK_API_KEY:
        return "错误：请先在config.py中配置DEEPSEEK_API_KEY"
    
    client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")
 
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API调用失败: {str(e)}"

# print(call_deepseek_api("请生成一个关于代码安全的报告"))