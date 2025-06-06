from setuptools import setup, find_packages

setup(
    name="chat_with_pdf",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-community",
        "langchain-google-genai",
        "faiss-cpu",
        "python-dotenv",
    ],
) 