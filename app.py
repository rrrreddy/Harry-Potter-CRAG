import streamlit as st
from src.conversation_chain import conversational_rag_chain

st.title("Harry Potter Chatbot with Conversational RAG")

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = 'default_session'
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

session_id = st.session_state['session_id']
chat_history = st.session_state['chat_history']

# Function to display chat history
def display_chat_history():
    for message in chat_history:
        st.write(f"You: {message['human']}")
        st.write(f"Chatbot: {message['assistant']}")

# Display chat history at the top
display_chat_history()

# User input form at the bottom
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You: ", "")
    submit_button = st.form_submit_button(label='Ask')

if submit_button and user_input:
    # Invoke the conversational chain with history
    response = conversational_rag_chain.invoke(
        {"input": user_input, "chat_history": chat_history},
        config={"configurable": {"session_id": session_id}},
    )["answer"]
    
    # Update chat history
    chat_history.append({"human": user_input, "assistant": response})
    st.session_state['chat_history'] = chat_history

    # Clear the input field after submission
    st.experimental_rerun()
