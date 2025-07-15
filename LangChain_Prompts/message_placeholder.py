from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


# chat template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant of {domain}."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}."),
])


chat_history = []
# load chat history
with open("chat_history.txt", "r") as file:
    chat_history_content = file.read().strip()
    chat_history = chat_history_content.split("\n")

# print("Chat History Loaded: \n", chat_history)

# create prompt
prompt = chat_template.invoke({
    "domain": "customer support",
    "chat_history": chat_history,
    "query": "What is the status of my refund request?"
})

# print(prompt) 

# initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
)
# invoke model with prompt
response = model.invoke(prompt)
print("Response from the model:")
print(response.content)




