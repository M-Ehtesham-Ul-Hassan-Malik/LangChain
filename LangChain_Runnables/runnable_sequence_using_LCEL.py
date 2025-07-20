from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain this joke  briefly: {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    temperature= '0.7'
)

parser = StrOutputParser()

# chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
chain = prompt1 | model | parser | prompt2 | model | parser # use of LCEL (LangChain Expression Language)

result = chain.invoke({'topic', 'blockchain'})

print(result)
