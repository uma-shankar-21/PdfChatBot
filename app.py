# app.py

import streamlit as st
from agents.ingestion_agent import ingest
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from mcp import MCPMessage

# Initialize session state
if "docs" not in st.session_state:
    st.session_state.docs = []
if "retrieval_agent" not in st.session_state:
    st.session_state.retrieval_agent = RetrievalAgent()
if "llm_agent" not in st.session_state:
    st.session_state.llm_agent = LLMResponseAgent()

st.title("Agentic RAG Chatbot (MCP)")

uploaded_files = st.file_uploader("Upload files", type=["pdf", "pptx", "csv", "docx", "txt", "md"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        text = ingest(file, file.name)
        st.session_state.docs.append(text)
    st.session_state.retrieval_agent.add_documents(st.session_state.docs)
    st.success("Documents processed and indexed!")

query = st.text_input("Ask a question about your documents:")

if st.button("Get Answer") and query:
    # Retrieval Agent
    retrieval_msg = MCPMessage(
        sender="CoordinatorAgent",
        receiver="RetrievalAgent",
        msg_type="RETRIEVAL_REQUEST",
        payload={"query": query}
    )
    top_chunks = st.session_state.retrieval_agent.retrieve(query)
    retrieval_response = MCPMessage(
        sender="RetrievalAgent",
        receiver="LLMResponseAgent",
        msg_type="RETRIEVAL_RESULT",
        payload={"retrieved_context": top_chunks, "query": query}
    )

    # LLM Agent
    answer = st.session_state.llm_agent.generate(query, top_chunks)
    llm_response = MCPMessage(
        sender="LLMResponseAgent",
        receiver="CoordinatorAgent",
        msg_type="LLM_ANSWER",
        payload={"answer": answer, "source_chunks": top_chunks}
    )

    st.markdown(f"**Answer:** {answer}")
    with st.expander("Show source context"):
        for chunk in top_chunks:
            st.write(chunk)

