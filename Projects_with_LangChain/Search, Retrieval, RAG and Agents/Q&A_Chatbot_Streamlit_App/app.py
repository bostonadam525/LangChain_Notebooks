import streamlit as st 
import openai 
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os 
from dotenv import load_dotenv

load_dotenv()

## initiate LangSmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Q&A Chatbot with OpenAI"


## Setup Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful chatbot assistant. Please respond to the user queries."),
        ("user","Question:{question}"),
    ]
)

## generate response function
def generate_response(question, api_key, llm, temperature, max_tokens):
    try:
        ## 1. set api key as environment variable
        os.environ['OPENAI_API_KEY']= api_key
        ## 2. set llm
        llm=ChatOpenAI(model=llm, temperature=temperature, max_tokens=max_tokens)
        ## 3. output parser
        output_parser=StrOutputParser()
        ## 4. create chain
        chain = prompt | llm | output_parser
        ## 5. generate response
        answer = chain.invoke({'question': question})

        return answer       
    except Exception as e:
        return f"An error occurred: {str(e)}"

## Streamlit App Title
st.title("Q&A Chatbot with OpenAI")

## Sidebar for settings
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

## Drop down in side bar to select LLM
llm=st.sidebar.selectbox("Select an Open AI Model",["gpt-4o","gpt-4-turbo","gpt-4"])

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=500, value=150)

## Main interface for user input
st.write("Go ahead and ask me a question!")
user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    else:
        response = generate_response(user_input, api_key, llm, temperature, max_tokens)
        st.write("Assistant:", response)
else:
    st.write("Please provide a question to get a response.")
