from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage ,HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()


# model = ChatOpenAI()
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

while True:
    try:
        user_input = input("You: ")
        chat_history.append(HumanMessage(content=user_input))
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            print("Chat History:", chat_history)
            break
        
        # response = model.invoke(user_input)
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))
        print(f"AI: {response.content}")
    except Exception as e:
        print(f"An error occurred: {e}")
