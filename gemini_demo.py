import google.generativeai as genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# 列出所有可用模型
print("Available models:")
available_models = list(genai.list_models())
for m in available_models:
    print(f" - {m.name} supports: {m.supported_generation_methods}")

# 选择第一个支持 generateContent 的模型
chosen_model = None
for m in available_models:
    if 'generateContent' in m.supported_generation_methods:
        chosen_model = m.name
        break

if chosen_model:
    print(f"\\\\nUsing model: {chosen_model}")
    model = genai.GenerativeModel(chosen_model)
    response = model.generate_content("请用中文介绍 GitHub 的用途。")
    print("\\\\nResponse:")
    print(response.text)
else:
    print("No suitable model found.")
