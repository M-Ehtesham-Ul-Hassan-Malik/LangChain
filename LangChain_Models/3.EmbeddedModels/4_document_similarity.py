from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

documents = [
    "Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan. He served as the first Governor-General of Pakistan. He is revered as the Father of the Nation. His leadership and vision were instrumental in the creation of Pakistan.",
    "Allama Iqbal was a philosopher, poet, and politician in British India who is regarded as one of the most important figures in Urdu literature. He is also known as the 'Spiritual Father of Pakistan'.",
    "Liaquat Ali Khan was the first Prime Minister of Pakistan. He played a key role in the early years of Pakistan's formation and development.",
    "Fatima Jinnah was a prominent Pakistani dental surgeon and a politician. She was the sister of Muhammad Ali Jinnah and played an important role in the Pakistan Movement. She was also a candidate for the presidency of Pakistan in 1965. She is often referred to as Madar-e-Millat (Mother of the Nation).",
    "Zulfikar Ali Bhutto was a Pakistani politician who served as the Prime Minister of Pakistan in the 1970s and 1980s. He was the founder of the Pakistan People's Party (PPP) and played a significant role in shaping modern Pakistan.",
    "Benazir Bhutto was the first woman to head a democratic government in a majority Muslim nation. She served as Prime Minister of Pakistan in the late 1980s and mid-1990s."
]

# Generate embeddings for the documents
document_embeddings = embeddings.embed_documents(documents)

# querry
query = "Tell me about sisters of Quaid-e-Azam Muhammad Ali Jinnah"

# Generate embedding for the query
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity between the query embedding and document embeddings
similarities = cosine_similarity([query_embedding], document_embeddings)[0] 

# print("Similarities:", similarities)

# Sort documents based on similarity scores
sorted_indices = np.argsort(similarities)[::-1]
# print(sorted_indices)

index, score = sorted_indices[0], similarities[sorted_indices[0]] 
print("Query:", query)
print(f"Most similar document index: {index}, Score: {score}")
print("Most similar document:", documents[index])
