# RAG Document Q&A App with Llama LLM
* Project by Adam Lang
* Date: 1/28/2025

# Overview
* Purpose of this project/experiment is to chat with local PDF files (arxiv articles) using RAG with langchain.
* This app leverages the llama-3 LLM via GROQ API and OpenAI Embeddings.
* The interface allows you to create embeddings, then query the vector store in FAISS vector library, and retrieves the most similar passages within the documents to answer your query or question. 

# Steps to Reproduce Project
1. Make a directory folder: `mkdir <NAME OF PROJECT>
2. Create these files:
   * `app.py`
   * `.env`
   * `requirements.txt`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Before running the app make sure to install the requirements: `pip install -r requirements.txt`
6. Make sure to have your API keys stored in your .env file.


# To run this app
* Run this code: `streamlit run app.py`


# Demo of user interface
1. First you create your embeddings by clicking on the "Create Document Embeddings" button.

![image](https://github.com/user-attachments/assets/6a2c1cf8-224d-4e62-9534-bb6c7dafb8e1)

2. User is then given a system message that the vector database is ready.

![image](https://github.com/user-attachments/assets/a3ea52e1-a595-4126-a197-d5b7579efd4b)

3. You then ask a query of the research PDF papers and get the most similar documents. 
* The user receives not only the answer to their question but also the documents that you click on a drop down menu to view the most relevant documents to your question.

![image](https://github.com/user-attachments/assets/dece7155-9600-43ad-841c-0e96bad62b70)
