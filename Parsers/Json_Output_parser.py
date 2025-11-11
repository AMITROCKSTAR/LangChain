## It forces LLM to give its output in json formate

## Cons : We cannot force JsonOutputParser to follow pre-defined schema

from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")


parser = JsonOutputParser()

template = """
You are a helpful assistant. 
Return details of a fictional person with fields:
- name (string)
- age (integer)
- city (string)

{format_instruction}

Return only valid JSON, nothing else.
"""
 
template1 = PromptTemplate(
    template = template,
    input_variables=[],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

# prompt = template1.format()

# response = llm.invoke(prompt)

# ## Parsing

# result = parser.parse(response.content)

chain = template1 | llm | parser
result = chain.invoke({})
print(result)

