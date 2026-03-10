import google.generativeai as genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# 使用稳定的 gemini-pro 模型
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("请用中文介绍 GitHub 的用途。")
print(response.text)
