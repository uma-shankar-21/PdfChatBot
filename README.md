# PdfChatBot
Agentic RAG Chatbot for Multi-Format Document QA (MCP Architecture)
A Retrieval-Augmented Generation (RAG) chatbot that answers user questions from uploaded documents (PDF, PPTX, CSV, DOCX, TXT/Markdown) using an agent-based architecture and Model Context Protocol (MCP).
Built with Python, Streamlit, Hugging Face Transformers, and FAISS.

Deployed in Streamlit (Link) : https://pdffchatbot.streamlit.app/

🚀 Features
Multi-Format Document Support: PDF, PPTX, CSV, DOCX, TXT, Markdown

Agentic Architecture: Ingestion, Retrieval, and LLM Response agents

Model Context Protocol (MCP): Structured message passing between agents

Local LLM (Free!): Uses Hugging Face Transformers (no API key needed)

Semantic Search: FAISS vector store with Sentence Transformers embeddings

Chatbot UI: Streamlit web app for uploads, questions, and answers with context

🏗️ Architecture
![Architecture Diagram with your actual diagram filename -->

IngestionAgent: Parses and preprocesses uploaded documents

RetrievalAgent: Embeds and semantically retrieves relevant chunks

LLMResponseAgent: Forms prompt and generates answers using a local LLM

CoordinatorAgent (in app): Orchestrates workflow and message passing via MCP

💻 Tech Stack
Frontend: Streamlit

Document Parsing: PyPDF2, python-docx, python-pptx, pandas

Embeddings: Sentence Transformers (all-MiniLM-L6-v2)

Vector Store: FAISS

LLM: Hugging Face Transformers (google/flan-t5-base or similar)

Agent Protocol: Custom MCP (in-memory Python dicts)

⚡ Quickstart
1. Clone the Repo
bash
git clone https://github.com/your-username/agentic_rag_chatbot.git
cd agentic_rag_chatbot
2. Setup Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Run the App
bash
streamlit run app.py
4. Use the Chatbot
Upload documents (PDF, PPTX, CSV, DOCX, TXT, MD)

Ask questions about your documents

View answers and source context

🧩 Folder Structure
text
Main folder : agentic_rag_chatbot/
a sub under main folder 
agents(── ingestion_agent.py ── retrieval_agent.py ── llm_response_agent.py)
below under agentic_rag_chatbot  folder
(mcp.py── vector_store.py── app.py── requirements.txt)
