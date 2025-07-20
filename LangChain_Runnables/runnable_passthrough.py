from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel

load_dotenv()

# passthrough = RunnablePassthrough()
# print(passthrough.invoke("hello"))
# print(passthrough.invoke({"name": "Ehtesham"}))

prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain this joke briefly {text}",
    input_variables=["text"]
)

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    temperature=0.7
)

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt1, model, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

print(final_chain.invoke("Table Tennis"))
 