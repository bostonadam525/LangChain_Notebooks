# Langserve FastAPI Template
* This is a template project to use for creating a simple Langchain application with deployment on a FastAPI server.



# Project Setup
1. Setup a `requirements.txt` file. See the file in this folder as an example.
2. Create a virtual environment: `python -m venv venv`
3. Activate the venv: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`


# Files in this template project
1. `app.py`
   * This file has the 4 basic ways to run a langchain application including:
     1. Messages (SystemMessage, HumanMessage)
     2. Output Parsers
     3. LCEL Syntax using langchain chains
     4. Prompt Templates with LCEL
   * This particular implementation uses the GROQ open source API to use the `Gemma2-9b-it` LLM.
    
2. `server.py`
   * This file contains a full application implementation as a basic template.
   * This includes:
     1. Langchain implementation.
     2. FastAPI server deployment via Langserve.
    
3. `.env`
   * You will need your own GROQ_API_KEY here.
  
4. `static`
   * *In FastAPI, static files such as images, CSS files, JavaScript files, or PDFs are typically served directly by the web server instead of being handled by your application code. This improves performance and allows the webserver to efficiently serve these static files.*
   * I did not develop the static directory here but use it as a placeholder template for developing a FastAPI application. 
   * Examples of how to do this:
     * [FastAPI — Render Template & Redirection](https://medium.com/featurepreneur/fastapi-render-template-redirection-c98a26ae1e2a)
     * [Serving with speed: Static Files in FastAPI](https://medium.com/featurepreneur/serving-with-speed-static-files-in-fastapi-66af61c203e9)

6. `requirements.txt`
