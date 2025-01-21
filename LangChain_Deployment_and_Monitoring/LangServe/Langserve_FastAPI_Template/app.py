import os 
import time 
import requests
from dotenv import load_dotenv, find_dotenv
## langchain imports
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser ## string output parser
from langchain_core.prompts import ChatPromptTemplate ## prompt templates


## open ai key
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

## groq api key
load_dotenv(find_dotenv())
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

## function to initialize groq model
def init_groq_model(api_key, retries=3, backoff_factor=1):
    for attempt in range(retries):
        try:
            # Initialize the GROQ model
            groq_model = ChatGroq(api_key=api_key)
            return groq_model
        except groq.InternalServerError as e:
            if attempt < retries - 1:
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                raise

## init groq model
groq_model = init_groq_model(GROQ_API_KEY)

## init GROQ model with Gemma2-9b-it
llm = ChatGroq(model="Gemma2-9b-it",
               temperature=0.1,
               max_tokens=100,
               max_retries=2,
               api_key=GROQ_API_KEY)

## 1. Messages approach --> create list of messages to pass to llm model
messages = [
    SystemMessage(content="Translate the following from English to French"),
    HumanMessage(content="Hello, how are you today? What is the weather?")
]

## invoke messages
response = llm.invoke(messages)
print(response)


## 2. Output parser approach --> string output parser
def string_output_parser(response):
    parser = StrOutputParser()
    result = parser.invoke(response)

    return result

## invoke string output parser
result = string_output_parser(response)
print(result)

## 3. LCEL chain approach --> use LCEL to chain components
def lcel_chain(messages):
    # chain components
    chain = llm | string_output_parser
    response = chain.invoke(messages)
    return response

## invoke lcel chain
response = lcel_chain(messages)
print(response)


## 4. Prompt Template with LCEL chain approach
prompt_template = "Translate the following into {language}:"

## create prompt
prompt = ChatPromptTemplate.from_messages(
    [("system",prompt_template),("user","{text}")]
)

## invoke prompt
result = prompt.invoke({"language":"French","text":"Hello, how are you today? What is the weather?"})
result.to_messages()

## create final chain
chain = prompt | llm | string_output_parser

## invoke chain
result = chain.invoke({"language":"French","text":"Hello"})
print(result)