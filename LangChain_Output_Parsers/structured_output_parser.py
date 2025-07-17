from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="A fact about blockchain"),
    ResponseSchema(name="fact_2", description="A second fact about blockchain"),
    ResponseSchema(name="fact_3", description="A third fact about blockchain"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Provide three interesting facts about {topic}. \n{format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# Create a chain that combines the template, model, and parser
chain = template | model | parser
result = chain.invoke({'topic': 'Blockchain with AI'})
print(result) 