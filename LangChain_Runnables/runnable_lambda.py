from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash'
)

prompt1 = PromptTemplate(
    template='Generate a joke on the topic {topic}',
    input_variables=['topic']
)

def word_count(text: str) -> int:
    return len(text.split())


parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'counter': RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({'topic':'Algorand'})

print(result)
