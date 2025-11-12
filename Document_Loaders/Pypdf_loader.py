from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write summary on following {communication_traits}",
    input_variables=['communication_traits']
)


loader = PyPDFLoader("all_queries.pdf")

docs = loader.load()


# print(type(docs))
# print(docs[0].page_content)

chain = prompt | model | parser

# response = chain.invoke({'communication_traits':docs[0].page_content})

# print(response)

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)