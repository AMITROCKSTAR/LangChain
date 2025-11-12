from langchain_community.document_loaders import WebBaseLoader

url = "https://www.ibm.com/think/topics/chatgpt"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs)