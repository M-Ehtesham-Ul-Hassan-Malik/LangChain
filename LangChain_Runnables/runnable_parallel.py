from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about the topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about the topic {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    temperature = 0.2
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'linkedin_post': RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({'topic':'Machine Learning'})

print(result)