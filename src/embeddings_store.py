import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Set embeddings model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # This is the default embedding model from Google
    google_api_key=GOOGLE_API_KEY,
)

def create_vectorstore(chunks):
    """
    Generate embeddings for chunks and store them in FAISS vector DB using Google embeddings.
    
    Args:
        chunks (list): List of text chunks to embed
        
    Returns:
        FAISS: The vector store instance
        
    Raises:
        ValueError: If chunks is empty
        Exception: For other embedding or storage errors
    """
    if not chunks:
        raise ValueError("No text chunks provided for embedding")
        
    try:
        vectorstore = FAISS.from_texts(chunks, embedding_model)
        vectorstore.save_local("faiss_index")
        return vectorstore
    except Exception as e:
        raise Exception(f"Error creating vector store: {str(e)}")
