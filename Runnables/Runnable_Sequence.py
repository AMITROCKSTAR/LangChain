from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Write  line of joke on this {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template="Describe this content {content}",
    input_variables = ['content']
)
model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

response = chain.invoke({'topic':'Love'})

print(response)