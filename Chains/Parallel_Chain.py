from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
model2 = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template='Generate short and simple notes on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate 5 short question and answers on {topic}",
    input_variables = ['topic']
)

prompt3 = PromptTemplate(
    template="Merge the provided following quiz and notes into single documents \n notes -> {notes} and quiz --> {quiz}",
    input_variables = ['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain  = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below)."""

response = chain.invoke({'topic':text})

print(response)

chain.get_graph().print_ascii()