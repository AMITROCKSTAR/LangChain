# ### The StrOutPut parser is the simplest output parser in LangChain. It is used to parse the output of llm and it return it as aplain string
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# response = llm.invoke("Capital of India")

# print(response.content)

template1 = PromptTemplate(
    template="Write detailed paragraph on this {topic} ",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template = "Write summary on this {text} in  line",
    input_variables = ["text"]
)

# prompt1 = template1.invoke({'topic':"Cricket"})

# response1 = llm.invoke(prompt1)

# prompt2 = template2.invoke({'text':response1.content})

# response2 = llm.invoke(prompt2)

# print(response2.content)



##-----------------------------------------String output parsers ---------------------------------------------------------------------

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()


chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({'topic' :" Music "})

print(result)

