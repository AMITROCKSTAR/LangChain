from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

passthrough = RunnablePassthrough()
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the following joke {text}",
    input_variables = ['text']
)

joke_gen_chain = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':prompt2 | model | parser
})

chain = joke_gen_chain | parallel_chain

print(chain.invoke({'topic':'Love'}))
