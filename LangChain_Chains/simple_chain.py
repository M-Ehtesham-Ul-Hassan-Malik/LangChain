from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="List 5 intrestin facts about {topic}",
    input_variables=["topic"],
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1,
    max_output_tokens=300,
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "Blockchain technology"})

print(result)

chain.get_graph().print_ascii()