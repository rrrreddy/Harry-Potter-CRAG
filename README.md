---
title: Harry Potter CRAG
emoji: 🚀
colorFrom: blue
colorTo: blue
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Harry Potter Conversational RAG Chatbot

This project implements a conversational chatbot using Retrieval-Augmented Generation (RAG) with chat history awareness. The chatbot is trained to answer questions about the Harry Potter books and remembers the context of previous interactions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Harry Potter Conversational RAG Chatbot uses Langchain, Cohere, Pinecone, and Streamlit to create an interactive chatbot that can answer questions about the Harry Potter series. I uses advanced Cohere LLM model, Pinecone vector database, Retrieval-Augmented Generation (RAG), and Streamlit to provide accurate and context-aware responses.

## Features

- Conversational RAG with chat history awareness.
- Real-time question answering based on the Harry Potter books.
- Streamlit-based user interface for easy interaction.
- Deployed on Hugging Face Spaces for accessibility.

## Installation

### Prerequisites

- Python 3.11
- Docker (for deployment)

### Setup

1. Clone the repository:

```sh
git https://github.com/rrrreddy/Harry-Potter-CRAG.git
cd Harry-Potter-CRAG
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Create a .env file in the root directory and add your API keys:
```
COHERE_API_KEY=YOUR_API_KEY
PINECONE_API_KEY=YOUR_API_KEY
PINECONE_ENVIRONMENT=YOUR_ENVIRONMENT
OPENAI_API_KEY=YOUR_API_KEY
```
Replace your_cohere_api_key, your_langchain_api_key, and your_pinecone_api_key with your actual API keys.


### Usage

1. Start the Streamlit application:
```
streamlit run app.py
```
2. Open the Streamlit app in your browser:
```
http://127.0.0.1:8501
```
## File Structure
Harry-Potter-CRAG/
├── app.py
├── requirements.txt
├── .env
├── HarrypotterCRAG.log
├── src/
│   ├── utils.py
│   ├── chat.py
│   ├── data_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever_chain.py
│   ├── qa_chain.py
│   └── conversation_chain.py
└── .gitignore

# Description
- `app.py`: Main entry point for the Streamlit application.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variables configuration.
- `HarrypotterCRAG.log`: Log file for debugging and tracking.
- `src/`: Directory containing all source code files:
- `utils.py`: Utility functions for setting up the environment.
- `data_loader.py`: Code for loading and splitting the PDF into chunks.
- `embeddings.py`: Code for creating embeddings.
- `vector_store.py`: Code for creating and managing the vector store.
- `retriever_chain.py`: Code for creating the history-aware retriever chain.
- `qa_chain.py`: Code for creating the question-answering chain.
- `conversation_chain.py`: Code for building the conversational RAG chain.

License
This project is licensed under the MIT License. See the `LICENSE` file for details.