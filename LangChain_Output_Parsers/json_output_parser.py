from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the title, author, publisher and price of the imaginary book on blockchain \n{format_instructions}',
    input_variables=[''],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template.format()
# print(prompt)
# result = model.invoke(prompt)
# parsed_result = parser.parse(result.content)

chain = template | model | parser 

result = chain.invoke({})

print(result)  # This will print the parsed JSON output
