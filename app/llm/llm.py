from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()


llm = ChatOpenAI(

    base_url="https://api.cerebras.ai/v1",

    api_key=os.getenv("CEREBRAS_API_KEY"),

    model="llama3.1-8b",

    temperature=0
)