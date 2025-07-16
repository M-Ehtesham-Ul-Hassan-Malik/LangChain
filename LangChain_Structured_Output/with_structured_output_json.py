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
json_schema =  {
    "title": "Review",
    "description": "A structured review of a product",
    "type": "object",
     "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Key themes of the review"
        },
        "summary": {
            "type": "string",
            "description": "Brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "Return sentiment of the review either positive, negative or neutral"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "List of pros mentioned in the review"
        },
        "cons": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "List of cons mentioned in the review"
        },
     },

    "required": ["key_themes", "summary", "sentiment", "pros", "cons"]


}


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""
I purchased a gaming laptop from this store, and it’s exceeded my expectations. The packaging was secure, delivery was fast, and the machine handles heavy tasks like a breeze. Great deal!
""")

print(result)
# print(result['summary'])
# print(result['sentiment'])

