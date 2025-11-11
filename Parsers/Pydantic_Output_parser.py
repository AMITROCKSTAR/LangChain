## Pydantic parse is output parser in langchain that uses Pydantic Models to enforce schema validation when processing LLM responses

## Why use PydanticOutPutParser 

# Strict Schema Enforcement : Ensures llm response follows well structured/defined output format.
# Type Safety : Automatically Converts LLM outputs into python objects
# Easy Validation : Uses Pydantic's built-in validation to catch incorrect or missing data.
# Seamless integration : Works well with other LangChain components

from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

## Creating pydantic object which will work as Schema

class Person(BaseModel):
    name:str = Field(description='Name of the person')
    age:int = Field(gt=18,description='Age of the person , greater than 18')
    city:str = Field(description='City of the person belongs to')


## Creating pydantic parser having Person class as pydantic object

parser = PydanticOutputParser(pydantic_object=Person)

## Template

template = PromptTemplate(
    template='Generate the name,age,city of the fictional {place} person \n {format_instruction}',
    input_variables =['place'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'indian'})

# result = llm.invoke(prompt)

# response = parser.parse(result.content)

## Using Chains

chain = template | llm | parser

response = chain.invoke({'place':'Switzerland'})

print(response)