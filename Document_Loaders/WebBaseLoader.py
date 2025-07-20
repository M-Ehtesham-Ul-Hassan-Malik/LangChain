from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


url = 'https://medium.com/@malikehtesham/logistic-regression-explained-by-someone-who-misused-it-first-80686aaa0d89'
loader = WebBaseLoader(url)

docs = loader.load()    

model = GoogleGenerativeAI(
    model = 'gemini-2.0-flash'
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the question \n{question} from the following text \n {text} ',
    input_variables=['question', 'text']
    )

chain = prompt | model | parser

print(chain.invoke({'question': 'Want to explore more?', 'text': docs[0].page_content}))

# print(len(docs))
# print()

# print(docs[0].page_content)
# print()

# print(docs[0].metadata)
# print()