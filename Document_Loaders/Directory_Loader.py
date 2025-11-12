from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path="Books",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

# docs = loader.load()
## Lazy_Load to load huge amount of pdf at once
# print(len(docs))
docs = loader.lazy_load()

# print(docs[15].page_content)
# print(docs[15].metadata)

for doc in docs:
    print(doc.metadata)