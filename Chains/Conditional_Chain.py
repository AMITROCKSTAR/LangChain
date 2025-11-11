from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch,RunnableLambda



load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()


## Validation schema

class feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')


parser2 = PydanticOutputParser(pydantic_object=feedback)
prompt1 = PromptTemplate(
    template="Classify the sentiment of following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables = ['feedback'],
    partial_variables = {'format_instructions':parser2.get_format_instructions()}
)

Classifier_chain = prompt1 | model | parser2

# result = Classifier_chain.invoke({'feedback':'It was wonderful experiance with Mauritous tour'}).sentiment

# print(result)
prompt2 = PromptTemplate(
    template="Write appropriate response this positive feedback \n {feedback}",
    input_variables= ['feedback']
)

prompt3 = PromptTemplate(
    template="Write appropriate response this negative feedback \n {feedback}",
    input_variables= ['feedback']
)


branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model | parser),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

## Final Chain

chain = Classifier_chain | branch_chain

result = chain.invoke({'feedback':'Mouritous tour was my very good experience'})

print(result)

chain.get_graph().print_ascii()