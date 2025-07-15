from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


# model = ChatOpenAI()
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    temperature=0.2,
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about the LangChain framework."),
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

# print(response.content)
print(messages)  # Display the full message history including the AI response
