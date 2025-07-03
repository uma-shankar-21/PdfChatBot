# agents/llm_response_agent.py

from transformers import pipeline

class LLMResponseAgent:
    def __init__(self):
        # You can choose a different model if you want
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

    def generate(self, query, context_chunks):
    # Limit to top 2 chunks and truncate
        short_chunks = [chunk[:300] for chunk in context_chunks[:2]]
        context = "\n".join(short_chunks)
        prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion: {query}\nAnswer:"
        result = self.generator(prompt, max_new_tokens=64)
        return result[0]['generated_text'].strip()