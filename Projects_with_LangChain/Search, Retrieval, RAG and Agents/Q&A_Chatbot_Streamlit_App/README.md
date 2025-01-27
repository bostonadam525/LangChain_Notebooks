# Q&A Chatbot Streamlit App
* Project by Adam Lang
* Date: 1/27/2025


# Overview
* A chatbot that interacts with various LLMs via the Open AI API with a user interface in streamlit.
* This application also uses LangSmith for tracing the application user outputs. 



# Steps to Reproduce this:
1. Create virtual environment: `python -m venv venv`
2. Activate venv: `source venv/bin/activate`
3. Create `requirements.txt` file.
4. Anytime you are running or updating the application run this do the following:
   * Make sure the `venv` is activated, then run this....
   *  `pip install -r requirements.txt`
5. Create a `.env` file with your LangChain API key for LangSmith.
   * You need a LangSmith account to do this. 
6. Create `app.py` file.


# To run the app
* Run this code: `streamlit run app.py`


# Demo of User Interface
* This is an example of the application in action:

![image](https://github.com/user-attachments/assets/9eb361f7-1ab6-4b80-b5f8-ffc611e80bbe)


# Example of LangSmith Tracing Outputs
* This is an example of the LangSmith tracing outputs from this app:

![image](https://github.com/user-attachments/assets/cff4f83b-6805-41b9-beb3-13df6a490b70)
