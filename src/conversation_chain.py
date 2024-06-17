from langchain.chains import create_retrieval_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_cohere import ChatCohere
from src.utils import setup_environment
from src.data_loader import load_and_split_pdf
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store
from src.retriever_chain import create_history_aware_retriever_chain
from src.qa_chain import create_question_answer_chain
import os
import logging

setup_environment()

# Load and process data
file_url = "https://kvongcmehsanalibrary.wordpress.com/wp-content/uploads/2021/07/harrypotter.pdf"
split_pages = load_and_split_pdf(file_url)

# Create embeddings
embeddings = create_embeddings()

# Create vector store
vectorstore = create_vector_store(embeddings, split_pages, os.environ.get('PINECONE_API_KEY'))

# Create retriever chain
history_aware_retriever = create_history_aware_retriever_chain(vectorstore)

# Create QA chain
chat_model = ChatCohere(model="command-nightly", temperature=0.3)
question_answer_chain = create_question_answer_chain(chat_model)

# Create RAG chain
try:
    rag_chain = create_retrieval_chain(retriever=history_aware_retriever, combine_docs_chain=question_answer_chain)
except Exception as e:
    logging.error(f"Error creating RAG chain: {e}")

# Build conversational RAG chain
store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)
