from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever

def create_history_aware_retriever_chain(vectorstore):
    chat_model = ChatCohere(model="command-nightly", temperature=0.3)

    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ]
    )

    try:
        history_aware_retriever = create_history_aware_retriever(llm=chat_model, retriever=vectorstore.as_retriever(), prompt=contextualize_q_prompt)
    except Exception as e:
        logging.error(f"Error creating history-aware retriever: {e}")

    return history_aware_retriever
