# Docs_Chat
Chat with all documents present in a directory . This provides response along with source path from which is the response is retrieved

# Project_setup

## Step 1 -- environment setup:
1. open vscode

```   
python -m venv myenv
```

3. myenv in above code is virtual environment name we give
   
## Step 2 -- Activating virtual environment setup:

```
.\myenv\scripts\activate
```

3. To activate virytual environment created

## Step 3 -- Installing required libraries: 
4. Now we have to install required library packages
5. For that run requiremnts.txt file
   

```
pip install -r requirements.txt
```

## Step 4 -- Building Indices:
6. Run create_index.py file to build indices for similarity search(my_faiss_index forms by running this file)
   
```
python create_index.py
```


## Step 5 -- Streamlit file for Chatbot on Docs
7. Run docs_chat.py file to build chatbot interface .

```
streamlit run docs_chat.py
```

# References:
1. For Docs_Chat Model building logic
https://artificialcorner.com/gpt4all-is-the-local-chatgpt-for-your-documents-and-it-is-free-df1016bc335
2. For Streamlit chatbot interface building
https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/

# Collab Notebook:
It is the model code for question and answers on documents
   
