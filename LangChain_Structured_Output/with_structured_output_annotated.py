from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0
# )

model = ChatOpenAI()

# schema
class Review(TypedDict):

    key_themes: Annotated[list[str], 'Key themes of the review']
    summary: Annotated[str, 'Breif summary of the review'] 
    sentiment: Annotated[str, 'Return sentiment of the review either positive, negative or neutral']
    pros: Annotated[Optional[list[str]], 'List of pros mentioned in the review']
    cons: Annotated[Optional[list[str]], 'List of cons mentioned in the review']

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I purchased a gaming laptop from this store, and it’s exceeded my expectations. The packaging was secure, delivery was fast, and the machine handles heavy tasks like a breeze. Great deal!
""")

print(result)
# print(result['summary'])
# print(result['sentiment'])

