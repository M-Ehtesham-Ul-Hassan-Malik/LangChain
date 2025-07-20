from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='train.csv'
)

docs = loader.load()

print(len(docs))
print()

print(docs[8].page_content)
print()

print(docs[8].metadata)
print()
