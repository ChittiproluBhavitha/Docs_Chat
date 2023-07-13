from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
import os

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

def split_chunks(sources):
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=32)
    for chunk in splitter.split_documents(sources):
        chunks.append(chunk)
    return chunks

def create_index(chunks):
    texts = [doc.page_content for doc in chunks]
    metadatas = [doc.metadata for doc in chunks]

    search_index = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    return search_index

folder_path = r"C:\Users\Bhavitha\Docs_Chat\Sources"
if not os.path.isdir(folder_path):
    print("Invalid folder path")
    exit()
    
doc_list = [s for s in os.listdir(folder_path) if s.endswith(('.pdf', '.txt'))]
num_of_docs = len(doc_list)

docs = []

for doc_file in doc_list:
    doc_path = os.path.join(folder_path, doc_file)
    if doc_file.endswith('.pdf'):
        loader = PyPDFLoader(doc_path)
        loaded_docs = loader.load()
        docs.extend(loaded_docs)
    elif doc_file.endswith('.txt'):
        loader = TextLoader(doc_path)
        loaded_docs = loader.load()
        docs.extend(loaded_docs)

chunks = split_chunks(docs)
db0 = create_index(chunks)

for i in range(1, num_of_docs):
    doc_file = doc_list[i]
    doc_path = os.path.join(folder_path, doc_file)

    if doc_file.endswith('.pdf'):
        loader = PyPDFLoader(doc_path)
        loaded_docs = loader.load()
    elif doc_file.endswith('.txt'):
        loader = TextLoader(doc_path)
        loaded_docs = loader.load()
    else:
        # Handle unsupported file types or unknown extensions
        print(f"Unsupported file type: {doc_file}")
        continue

    chunks = split_chunks(loaded_docs)
    dbi = create_index(chunks)

    db0.merge_from(dbi)

# Save the database locally
db0.save_local("my_faiss_index")
