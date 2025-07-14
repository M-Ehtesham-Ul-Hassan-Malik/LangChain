from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  

load_dotenv()

model = ChatOpenAI(model="gpt-4-turbo", temperature=0.7, max_completion_tokens=150)

result = model.invoke("What is the capital of France?")
print(result.content)
# Output: The capital of France is Paris.