from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

prompt1 = PromptTemplate(
    template="Write a blog on the topic: {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Extract the 5 key points from the blog: {blog}",
    input_variables=["blog"],
)

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "The Rise of Agentic AI"})

print(result)

chain.get_graph().print_ascii()