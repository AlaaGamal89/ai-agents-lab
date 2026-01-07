import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(override=True)
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY1")

if deepseek_api_key:
    print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
    print("DeepSeek API Key not set")

print(deepseek_api_key)

client = OpenAI(api_key=deepseek_api_key,base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "what 4+6"}
    ]
)
print(response.choices[0].message.content)