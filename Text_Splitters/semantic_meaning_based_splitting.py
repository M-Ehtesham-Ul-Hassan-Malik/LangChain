from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
import os

load_dotenv()

text_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


text = """
Machine learning is a branch of artificial intelligence that enables computers to learn from data and improve their performance without being explicitly programmed. It powers everything from recommendation systems and fraud detection to autonomous vehicles. By recognizing patterns and making predictions, machine learning helps automate decision-making in countless industries, making technology more adaptive and intelligent over time. 
Table tennis, also known as ping pong, is a fast-paced indoor sport that requires quick reflexes, precision, and strategic thinking. Played on a rectangular table divided by a net, it demands sharp hand-eye coordination and the ability to anticipate an opponent’s next move. Whether for casual fun or professional competition, table tennis is a game of agility, focus, and continuous adaptation.
Blockchain is a decentralized and secure digital ledger technology that records transactions across multiple computers, ensuring transparency and immutability. Originally developed for cryptocurrencies like Bitcoin, it is now used in supply chain management, digital identity, healthcare, and smart contracts. Blockchain's distributed nature eliminates the need for intermediaries, making systems more secure, efficient, and trustworthy.

"""

splitter = SemanticChunker(
    embeddings = text_embeddings,
    breakpoint_threshold_type = 'standard_deviation',
    breakpoint_threshold_amount = 1
)

result = splitter.split_text(text)

print(result)
print()
print(len(result))
print()

for chunks in result:
    print(chunks)
    print()
