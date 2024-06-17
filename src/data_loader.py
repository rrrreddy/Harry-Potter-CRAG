from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

def load_and_split_pdf(file_url):
    loader = PyMuPDFLoader(file_url)
    try:
        pages = loader.load()
        logging.info(f"Successfully loaded {len(pages)} pages.")
    except Exception as e:
        logging.error(f"Error loading PDF: {e}")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    try:
        split_pages = text_splitter.split_documents(documents=pages)
        logging.info(f"Pages split into {len(split_pages)} chunks.")
    except Exception as e:
        logging.error(f"Error splitting pages: {e}")
    
    return split_pages
