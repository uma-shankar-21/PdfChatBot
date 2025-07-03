# vector_store.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.texts = []
        self.embeddings = None
        self.index = None

    def add_texts(self, texts):
        new_embeddings = self.model.encode(texts)
        if self.embeddings is None:
            self.embeddings = new_embeddings
        else:
            self.embeddings = np.vstack([self.embeddings, new_embeddings])
        self.texts.extend(texts)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings.astype(np.float32))

    def search(self, query, top_k=3):
        query_emb = self.model.encode([query])
        D, I = self.index.search(np.array(query_emb).astype(np.float32), top_k)
        return [self.texts[i] for i in I[0]]
