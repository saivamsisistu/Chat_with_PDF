import os
import streamlit as st
from pathlib import Path
from pdf_loader import extract_text_from_pdf, split_text_into_chunks
from embeddings_store import create_vectorstore
from retrieval_qa import build_qa_chain

# Configure Streamlit page
st.set_page_config(page_title="Chat with Your PDF", page_icon="📄", layout="wide")
st.title("📄 Chat with Your PDF")

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "file_processed" not in st.session_state:
    st.session_state.file_processed = False

# Check for API key
if not os.getenv("GOOGLE_API_KEY"):
    st.error("⚠️ GOOGLE_API_KEY is not set. Please set it in your environment variables.")
    st.stop()

# File upload section
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and not st.session_state.file_processed:
    # Create a temporary file
    temp_pdf = Path("temp.pdf")
    
    try:
        # Save uploaded file
        with temp_pdf.open("wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("📑 Extracting and splitting text..."):
            raw_text = extract_text_from_pdf(str(temp_pdf))
            chunks = split_text_into_chunks(raw_text)

        with st.spinner("🔄 Generating embeddings and creating vector store..."):
            create_vectorstore(chunks)

        st.success("✨ PDF processed successfully! You can now ask questions about it.")
        st.session_state.qa_chain = build_qa_chain()
        st.session_state.file_processed = True
        
    except Exception as e:
        st.error(f"❌ Error processing PDF: {str(e)}")
    
    finally:
        # Cleanup temporary file
        if temp_pdf.exists():
            temp_pdf.unlink()

# Display chat interface if file is processed
if st.session_state.file_processed:
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.write(f'🧑 **You:** {message["content"]}')
            else:
                st.write(f'🤖 **Assistant:** {message["content"]}')
    
    # Chat input
    with st.form(key="chat_form", clear_on_submit=True):
        user_question = st.text_input("Type your question here...", key="user_question")
        submit_button = st.form_submit_button("Ask")
        
        if submit_button and user_question:
            with st.spinner("🤔 Thinking..."):
                try:
                    # Get response from QA chain
                    response = st.session_state.qa_chain.invoke(user_question)
                    
                    # Add to chat history
                    st.session_state.chat_history.append({"role": "user", "content": user_question})
                    st.session_state.chat_history.append({"role": "assistant", "content": response["result"]})
                    
                    # Rerun to update chat display
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error getting response: {str(e)}")
    
    # Add a clear chat button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# Add a footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and LangChain")