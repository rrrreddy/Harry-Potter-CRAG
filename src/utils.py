import os
from dotenv import load_dotenv
import logging

def setup_environment():
    load_dotenv()
    logging.basicConfig(filename='HarrypotterCRAG.log', level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        if "COHERE_API_KEY" not in os.environ:
            os.environ["COHERE_API_KEY"] = "your_cohere_api_key"
        if "LANGCHAIN_API_KEY" not in os.environ:
            os.environ["LANGCHAIN_API_KEY"] = "your_langchain_api_key"
        if "PINECONE_API_KEY" not in os.environ:
            os.environ["PINECONE_API_KEY"] = "your_pinecone_api_key"
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "HarryPotter-book-Chatbot"
        logging.info("Environment variables set.")
    except Exception as e:
        logging.error(f"Error setting environment variables: {e}")
