from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes ## helps create APIs
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

## init groq llm model
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="Gemma2-9b-it",
               temperature=0.1,
               max_tokens=100,
               max_retries=2,
               api_key=GROQ_API_KEY)

## 1. Create prompt template
system_template = "Translate the following text into {target_language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{source_text}")
])

## 2. Create output parser
output_parser = StrOutputParser()

## 3. Create LCEL chain
chain = prompt_template | llm | output_parser

## 4. Create FastAPI app
app = FastAPI(title="LangChain Server",
              version="1.0",
              description="A simple API server using Langchain runnable interface")

## Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

## define simple route
@app.get("/")
def read_root():
    return {"message": "Welcome to LangChain Server"}

## 5. Add chain routes to FastAPI app
add_routes(
        app, 
        chain,
        path="/chain"
)

## 6. Run FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, 
                host="127.0.0.1", # or "localhost"
                port=8001)