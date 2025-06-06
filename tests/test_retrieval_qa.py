import os
import pytest
from pathlib import Path
from src.retrieval_qa import build_qa_chain

def test_retrieval_qa():
    print("🔁 Loading QA chain using FAISS and Google Gemini...")
    
    # Check if GOOGLE_API_KEY is set
    if not os.getenv("GOOGLE_API_KEY"):
        pytest.skip("GOOGLE_API_KEY environment variable not set")
    
    # Check if FAISS index exists
    if not Path("faiss_index").exists():
        pytest.skip("FAISS index not found. Please run the indexing script first.")
    
    try:
        qa_chain = build_qa_chain()
        print("✅ QA chain loaded successfully.")

        # Test with a sample question
        sample_question = "What is this document about?"
        print(f"\n❓ Asking: {sample_question}")

        response = qa_chain.invoke(sample_question)
        print(f"\n✅ Response: {response}")
        
        # Basic assertions
        assert response is not None
        assert isinstance(response, dict)
        assert 'query' in response
        assert 'result' in response
        assert isinstance(response['result'], str)
        assert len(response['result']) > 0
        
    except Exception as e:
        print(f"\n❌ Error while testing QA chain: {str(e)}")
        raise

if __name__ == "__main__":
    test_retrieval_qa()
