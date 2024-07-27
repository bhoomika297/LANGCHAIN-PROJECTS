import requests
import streamlit as st


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/ASK/invoke",
    json = {'input':{'topic':input_text}})
    
    return response.json()['output']

st.title("Langchain Demo With LLAMA2 API")
input_text = st.text_input("Write Anything to ASK")

if input_text:
    st.write(get_ollama_response(input_text))