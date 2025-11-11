from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
load_dotenv()

model = ChatGroq(model="qwen/qwen3-32b") 

response = model.invoke("Uttar Pradesh best dish, give answer in bullet points")

print(response.content)