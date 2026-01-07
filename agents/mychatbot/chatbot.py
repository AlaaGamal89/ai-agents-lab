import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(override=True)
from pypdf import PdfReader
import gradio as gr

#print(os.getcwd())

load_dotenv(override=True)
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY1")

client = OpenAI(api_key=deepseek_api_key,base_url="https://api.deepseek.com")


reader = PdfReader("./me/Alaa.Gamal_CV_Dec2025.pdf")
cv = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        cv += text
#print(cv)


name = "Alaa Eldin Gamal"

system_prompet = f"you are acting as {name}, and you answering on behalf of {name}, \
    you are giving information about your self based on the following CV: {cv}, \
    you are answering the questions based on the CV and your information, \
    you are answering the questions in a friendly and professional manner, \
    you are answering the questions in a way that is easy to understand,\
    you are answering the questions in a way that is easy to follow, \
    you are answering the questions in a way that is easy to remember, \
    you are answering the questions in a way that is easy to use, \
    you are answering the questions in a way that is easy to apply, \
"

def chat(message,history):
    messages = [
        {"role": "system", "content": system_prompet},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(chat).launch()
