from langchain.embeddings import SentenceTransformerEmbeddings
import logging

def create_embeddings():
    try:
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        logging.info("SentenceTransformer embeddings created.")
    except Exception as e:
        logging.error(f"Error creating SentenceTransformer embeddings: {e}")
    return embeddings
