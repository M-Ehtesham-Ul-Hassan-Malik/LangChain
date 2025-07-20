from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Java Interview Questions.pdf')

# pages = loader.load_and_split()

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

