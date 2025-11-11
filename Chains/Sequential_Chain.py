from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Give detailed explaination on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Make summary on this {text} in 3 points",
    input_variables=['text']
)

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({'topic':'Love'})

print(response)

## Visualising chain

chain.get_graph().print_ascii()