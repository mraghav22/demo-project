import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
response = chat.invoke("Hello, how are you?")
print(response)
