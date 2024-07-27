import os

import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Ensure necessary environment variables are set
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Check if LANGCHAIN_API_KEY is set
if os.environ["LANGCHAIN_API_KEY"] is None:
    st.error("LANGCHAIN_API_KEY environment variable is not set.")
else:
    # Prompt Template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Please respond to the user queries"),
            ("user", "Question: {question}")
        ]
    )

# Streamlit framework
st.title('Langchain Demo With LLAMA2')
input_text = st.text_input("Search the topic you want")

# OpenAI llm
llm = Ollama(model="llama2")


# #openAI llm

# llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))