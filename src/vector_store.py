from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as LangchainPinecone
import time
import logging

def create_vector_store(embeddings, split_pages, api_key, index_name="harrypotter-index"):
    pc = Pinecone(api_key=api_key)
    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)

    index = pc.Index(index_name)

    try:
        if index_name not in existing_indexes:
            vectorstore = LangchainPinecone.from_texts([doc.page_content for doc in split_pages], embeddings, index_name=index_name)
            logging.info(f"Successfully embedded chunks in Pinecone index {index_name}.")
        else:
            vectorstore = LangchainPinecone.from_existing_index(index_name=index_name, embedding=embeddings)
            logging.info(f"Index {index_name} already exists, loaded embeddings.")
    except Exception as e:
        logging.error(f"Embedding failed: {e}", exc_info=True)
    
    return vectorstore
