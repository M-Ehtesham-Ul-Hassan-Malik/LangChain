from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal, TypedDict, Annotated, Optional
from pydantic import BaseModel, Field
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

# model = ChatOpenAI()

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description='Key themes of the review')
    summary: str = Field(description='Brief summary of the review')
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description='Return sentiment of the review either positive, negative or neutral')
    pros: Optional[list[str]] = Field(default=None, description='List of pros mentioned in the review')
    cons: Optional[list[str]] = Field(default=None, description='List of cons mentioned in the review')
    name: Optional[str] = Field(default=None, description='Name of the reviewer')



structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I purchased a gaming laptop from this store, and it’s exceeded my expectations. The packaging was secure, delivery was fast, and the machine handles heavy tasks like a breeze. Great deal!
""")

print(result)
# print(result['summary'])
# print(result['sentiment'])

