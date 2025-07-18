from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model1 = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
model2 = ChatHuggingFace(llm=llm)
# model3 = ChatAnthropic(model="claude-2")

prompt1 = PromptTemplate(
    template= "Generate a short and simple notes from the following text: {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="""From the following text, generate 5 question and answer pairs in the following format:

Q1: ...
A1: ...
Q2: ...
A2: ...
Q3: ...
A3: ...
Q4: ...
A4: ...
Q5: ...
A5: ...

Text:
{text}""",
    input_variables=["text"]
)


prompt3 = PromptTemplate(
    template="""
You are a document compiler. Merge the following notes and question-answer pairs into a well-structured markdown document.

Include both sections clearly under separate headings.

### Notes
{notes}

### Questions and Answers
{questions}
""",
    input_variables=["notes", "questions"],
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "questions": prompt2 | model2 | parser 
})

merge_chain = prompt3 | model1 | parser

chain  =  parallel_chain | merge_chain


text = """
LangChain
🔹 What is LangChain?
LangChain is a powerful open-source framework that helps developers build applications powered by Large Language Models (LLMs). It abstracts away complexity and provides modular building blocks for:

Interacting with LLMs (like OpenAI’s GPT, Anthropic’s Claude, etc.)
Connecting LLMs with external tools, APIs, documents, and databases
Creating intelligent agents, chatbots, retrieval-based systems, and more
🔸 Why is LangChain Needed?
While LLMs are powerful, using them in real-world applications requires more than just sending prompts. You often need to:

Chain multiple steps together (e.g., extract → reason → generate)
Connect to data sources (PDFs, websites, databases)
Build chatbots that can remember and react
Use tools/APIs dynamically (e.g., do math, call a calendar)
Maintain context in conversations
Store knowledge or memory for the LLM to use
LangChain provides all the utilities to orchestrate these pieces into a full AI system.

🧩 Core Components of LangChain
Component	Description
LLMs & ChatModels	Integrates models from OpenAI, Hugging Face, Anthropic, Google, etc.
Prompts	Create flexible and reusable prompt templates
Chains	Combine multiple LLM calls into a single pipeline (e.g., extract → transform → respond)
Agents	Let the LLM decide which tools to use based on user input
Tools	External APIs or functions the LLM can use (e.g., calculator, web search)
Memory	Stores conversation history or facts between steps
Retrievers	Pull relevant data from documents, databases, or vector stores
VectorStores	Store text embeddings for similarity search (used in RAG, QA, etc.)
Callbacks	Track events and log/debug complex chains
Use Cases of LangChain
LangChain is used to build intelligent LLM-powered applications, such as:

1. 🤖 Chatbots / Virtual Assistants
Multi-turn conversations
Memory-enabled interactions
Tool integration (e.g., booking APIs)
2. 📚 Retrieval-Augmented Generation (RAG)
Ask questions over PDFs, Notion docs, websites, and databases
Combine vector search with LLMs for accurate answers
3. 🧠 Agents
LLM selects and uses tools dynamically
Examples: booking systems, autonomous AI helpers, developer copilots
4. 📄 Document QA Systems
Upload documents and ask questions in natural language
Example: Chat with legal contracts or academic papers
5. 🛠️ Code Generation Pipelines
Prompt-based coding
Generate, fix, or refactor code based on user input
6. 🔁 Custom Workflows
Combine APIs, functions, LLM logic, and memory to build custom pipelines
Summary
Aspect	Details
Framework Name	LangChain
Purpose	Build complex, real-world LLM applications
Why Needed	Simplifies LLM workflows, integration with tools, memory, and data
Core Components	LLMs, Prompts, Chains, Agents, Tools, Memory, Retrievers, VectorStores
Use Cases	Chatbots, RAG systems, agents, document QA, code generation, workflows
"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()