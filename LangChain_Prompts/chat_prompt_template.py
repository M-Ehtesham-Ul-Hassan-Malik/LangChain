from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant of {domain}."),
    ("human", "Explain in the easiest way possible about {topic}."),
])

prompt = chat_template.invoke({
    "domain": "computer science",
    "topic": "machine learning"
})

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    temperature=0.2,
)

print(prompt)
response = model.invoke(prompt)
print("Response from the model:")
print(response.content)


