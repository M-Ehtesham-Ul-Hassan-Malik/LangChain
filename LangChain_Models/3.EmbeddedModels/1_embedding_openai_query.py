from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions= 128
)

result = embeddings.embed_query("Lahore is the heart of Pakistan, known for its rich culture and history.")

print(str(result))
