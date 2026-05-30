from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

class RAGChatbot:

    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        faiss_path = os.path.join(base_dir, "faiss_index")

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = FAISS.load_local(
            faiss_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def get_response(self, user_query: str) -> str:
        results = self.db.similarity_search(user_query, k=1)
        if not results:
            return "I'm here to support you. Could you tell me more about how you're feeling?"
        return results[0].metadata["answer"]