import google.generativeai as genai
import os

# 从环境变量读取 API 密钥（GitHub Actions 会通过 secrets 注入）
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 使用 Gemini 模型
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("请用中文介绍 GitHub 的用途。")
print(response.text)
