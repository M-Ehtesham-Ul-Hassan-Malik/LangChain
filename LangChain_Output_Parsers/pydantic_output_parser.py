from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field  

load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class book(BaseModel):
    title: str = Field(description="The title of the book") 
    price: float = Field(gt=15, description="The price of the book") # greater than 15 
    author: str = Field(description="The author of the book") 
    publisher: str = Field(description="The publisher of the book")

parser = PydanticOutputParser(pydantic_object=book) 


template = PromptTemplate(
    template='Give me the title, author, publisher and price of the imaginary book on {topic} \n{format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)


# prompt = template.invoke({'topic': 'blockchain'})
# print(prompt)  # This will print the formatted prompt
# result = model.invoke(prompt)
# parsed_result = parser.parse(result.content)
# print(parsed_result)  # This will print the parsed Pydantic model output

chain = template | model | parser
result = chain.invoke({'topic': 'Data Science'})
print(result)  # This will print the parsed Pydantic model output