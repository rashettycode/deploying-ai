import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Load the OpenAI API key
load_dotenv("../05_src/.secrets")


#  --- tools_semantic.py ---
# Simple semantic search using OpenAI embeddings + FAISS (in-memory)

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

# Build a small demo dataset
docs = [
    Document(page_content="Alpha Vantage provides financial market data APIs for stocks and forex."),
    Document(page_content="The S&P 500 index tracks the performance of the 500 largest US companies."),
    Document(page_content="Machine learning can help predict short-term price movements."),
    Document(page_content="Diversification reduces portfolio risk."),
]

# Create embeddings and vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = FAISS.from_documents(docs, embeddings)

def search_docs(query: str) -> str:
    """Return the most relevant text from the stored documents."""
    results = db.similarity_search(query, k=1)
    if not results:
        return "No relevant information found."
    return f"Relevant info: {results[0].page_content}"
