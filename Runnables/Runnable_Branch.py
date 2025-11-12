from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableParallel,RunnableSequence,RunnablePassthrough
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
    template="Summarize the following text {text}",
    input_variables = ['text']
)

report_gen_chain = RunnableSequence(prompt1,model,parser)

Branch_chain = RunnableBranch((lambda x:len(x.split())>10,RunnableSequence(prompt2,model,parser)),
                              RunnablePassthrough())

chain = RunnableSequence(report_gen_chain,Branch_chain)

print(chain.invoke({'topic':'Love vs Hate'}))
