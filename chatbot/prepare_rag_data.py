import pandas as pd
from langchain_core.documents import Document
import os

def load_chat_pairs():
    # Path to CSV in data/ folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "mental_health_final_with_gaps.csv")

    df = pd.read_csv(csv_path)

    documents = []
    for _, row in df.iterrows():
        question = str(row["input"])
        answer   = str(row["response"])
        documents.append(
            Document(
                page_content=question,
                metadata={"answer": answer}
            )
        )

    return documents

if __name__ == "__main__":
    docs = load_chat_pairs()
    print(f"Loaded {len(docs)} clean QA pairs")