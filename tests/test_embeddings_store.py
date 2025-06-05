import os
import sys

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pdf_loader import extract_text_from_pdf, split_text_into_chunks
from src.embeddings_store import create_vectorstore

def test_embeddings_generation():
    # Step 1: Load a sample PDF
    pdf_path = os.path.join(os.path.dirname(__file__), "..", "src", "Sai_Vams_Resume.pdf")
    print(f"📄 Loading PDF from: {pdf_path}")
    
    text = extract_text_from_pdf(pdf_path)
    print("✅ PDF text extracted.")
    print("Preview (first 500 chars):\n", text[:500])

    # Step 2: Split text into chunks
    chunks = split_text_into_chunks(text)
    print(f"✅ Text split into {len(chunks)} chunks.")
    print("First chunk preview:\n", chunks[0])

    # Step 3: Generate embeddings and store in FAISS
    vectorstore = create_vectorstore(chunks)
    print("✅ Embeddings created and stored in FAISS.")

if __name__ == "__main__":
    test_embeddings_generation()
