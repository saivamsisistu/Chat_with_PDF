import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set embeddings model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # This is the default embedding model from Google
    google_api_key=GOOGLE_API_KEY,
)

def create_vectorstore(chunks):
    """
    Generate embeddings for chunks and store them in FAISS vector DB using Google embeddings.
    """
    vectorstore = FAISS.from_texts(chunks, embedding_model)
    vectorstore.save_local("faiss_index")
    return vectorstore
