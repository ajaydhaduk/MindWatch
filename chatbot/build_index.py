from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from chatbot.prepare_rag_data import load_chat_pairs
import os

def build_faiss_index():
    docs = load_chat_pairs()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)

    # Save to faiss_index/ in project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_path = os.path.join(base_dir, "faiss_index")
    db.save_local(save_path)

    print("FAISS index built and saved to faiss_index/")

if __name__ == "__main__":
    build_faiss_index()