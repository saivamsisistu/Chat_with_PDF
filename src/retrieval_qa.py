import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from src.embeddings_store import embedding_model  # reuse same embedding model

llm = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.0-flash"
)

def build_qa_chain():
    """
    Load FAISS index and create a retrieval-based QA chain using Google Gemini.
    """
    vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
