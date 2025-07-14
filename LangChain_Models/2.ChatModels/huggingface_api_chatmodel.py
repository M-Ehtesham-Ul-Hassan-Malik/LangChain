from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

# 1. First, create a HuggingFaceEndpoint object
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # Use a chat-compatible model
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0,
)

# 2. Then, wrap it with ChatHuggingFace
chat_model = ChatHuggingFace(llm=llm)

# 3. Invoke using a list of messages
result = chat_model.invoke("What is the capital of Pakistan?")
print(result.content)
