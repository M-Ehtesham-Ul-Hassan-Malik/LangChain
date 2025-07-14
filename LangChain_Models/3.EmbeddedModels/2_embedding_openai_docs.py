from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small", 
    dimensions=128
)

# Embed the documents
result = embeddings.embed_documents([
    "Lahore is the heart of Pakistan, known for its rich culture and history.",
    "Karachi is the largest city in Pakistan, known for its bustling economy and port.",
    "Islamabad is the capital city of Pakistan, known for its modern architecture and greenery."
])

print(str(result))

# This code embeds a list of documents using OpenAI's text embedding model and prints the results.