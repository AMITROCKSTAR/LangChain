## Structured_Output_Parser : It is output parser in langchain that helps extract structured json data from LLM responses based on predefined field schema
# 
# It works by defining a list of fields (ResponseSchema)  that the model should return , ensuring the output follows a structured format .
from langchain_core.output_parsers import JsonOutputKeyToolsParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")
print(llm.invoke("Delhi"))