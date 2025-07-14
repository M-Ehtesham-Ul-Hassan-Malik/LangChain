from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["HF_Home"] = "./hf_cache"  # Set Hugging Face cache directory

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# text = "Lahore is the heart of Pakistan, known for its rich culture and history."
# vector = embeddings.embed_query(text)

documents = [
    "Lahore is the heart of Pakistan, known for its rich culture and history.",
    "Karachi is the largest city in Pakistan, known for its bustling economy and port.",
    "Islamabad is the capital city of Pakistan, known for its modern architecture and greenery."
]
vector = embeddings.embed_documents(documents)

print(str(vector))