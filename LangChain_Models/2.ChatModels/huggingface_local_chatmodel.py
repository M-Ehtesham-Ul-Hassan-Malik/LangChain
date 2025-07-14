from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import HumanMessage
from transformers import pipeline
import os

# Optional: cache location for transformers
os.environ['HF_HOME'] = 'D:/My Learning/AI/Summer 2025/LangChain/LangChain_Models/2.ChatModels/huggingface_cache'

# Create a Transformers pipeline first (local model or cached)
pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-beta",
    tokenizer="HuggingFaceH4/zephyr-7b-beta",
    device_map="auto",
    max_new_tokens=150,
    temperature=0.0
)

# Pass pipeline to LangChain
llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm)

# Call with proper chat input
result = chat_model.invoke([HumanMessage(content="What is the capital of Pakistan?")])
print(result.content)
