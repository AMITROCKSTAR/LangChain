from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template="Generate linkedin post on this {topic}",
    input_variables=['topic']
)

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {'tweet':RunnableSequence(prompt1,model,parser),
     'linkedin_post':RunnableSequence(prompt2,model,parser)}
)

response = parallel_chain.invoke({'topic':'AI'})

print(response)