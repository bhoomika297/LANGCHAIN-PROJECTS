import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes

load_dotenv()

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description="A Simple API Server"
)


llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("{topic}")

add_routes(
    app,
    prompt1|llm,
    path="/ASK"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)






