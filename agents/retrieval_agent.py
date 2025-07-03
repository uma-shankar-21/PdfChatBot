# agents/retrieval_agent.py

from vector_store import VectorStore

class RetrievalAgent:
    def __init__(self):
        self.vector_store = VectorStore()

    def add_documents(self, docs):
        self.vector_store.add_texts(docs)

    def retrieve(self, query, top_k=3):
        return self.vector_store.search(query, top_k)
