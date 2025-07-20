from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('blockchain.txt', encoding='utf-8')

doc = loader.load()

print(type(doc))

print(doc)

print(len(doc))

print(doc[0])

print(doc[0].page_content)

print(doc[0].metadata)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary of the blog {blog_content}',
    input_variables=['blog_content']
)

model = GoogleGenerativeAI(
    model = 'gemini-2.0-flash'
)

chain = prompt | model | parser

print(chain.invoke({'blog_content': doc[0].page_content}))
