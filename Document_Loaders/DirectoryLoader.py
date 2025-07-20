from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    'Books/',                    # path to the directory
    glob='*.pdf',               # type of files which you want to load form the directory
    loader_cls=PyPDFLoader      # loader class
)

# docs = loader.load() # slower
docs = loader.lazy_load()  #faster 

# print(len(docs))
# print()

# print(docs[0].page_content)
# print()

# print(docs[0].metadata)
# print()

for documents in docs:
    print(documents.metadata)
    print()