from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_question_answer_chain(chat_model):
    system_prompt = (
        "You are an assistant for question-answering tasks for Harry Potter books."
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ]
    )

    try:
        question_answer_chain = create_stuff_documents_chain(llm=chat_model, prompt=qa_prompt)
    except Exception as e:
        logging.error(f"Error creating question-answering chain: {e}")
    
    return question_answer_chain
