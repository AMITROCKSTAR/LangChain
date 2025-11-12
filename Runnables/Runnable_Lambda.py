from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

passthrough = RunnablePassthrough()
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

# prompt2 = PromptTemplate(
#     template="Explain the following joke {text}",
#     input_variables = ['text']
# )

def word_count(text):
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(chain.invoke({'topic':'Love'}))

