from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os

load_dotenv()

# print("API Key found:", os.getenv("GROQ_API_KEY") is not None)

# print(os.getenv("GROQ_API_KEY"))


llms = ChatGroq(model="openai/gpt-oss-20b", temperature = 1.5)

## UI

st.header("Research Assistent")
### User input

paper_input = st.selectbox("Select Research Paper" , ["Attention is all you need","Bert","Gpt-3","The Groq Software-defined Scale-out Tensor Streaming Multiprocessor : From chips-to-systems architectural overview","Reasoning Models Don't Always Say What They Think"])
style_input = st.selectbox("Select Explanation Style", ["Begginer-friendly","Technical","Code-Oriented","Mathematical"])
input_length = st.selectbox("Select Explanation length", ["Short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(detailed explaination"])
## Prompt template

template = PromptTemplate(
    template="""Please summarise the research paper titled "{paper_input}" with the following specifications:
    Explanation style: {style_input}
    Explanation length: {input_length}
    
    1. Mathematical details :
                              -- Include relevant mathematical equations if present in the paper.
                              -- Explain the mathematical concepts using simple , intuitive code snippets where applicable.
                              
    2. Analogies :
                   Use relatable analogies to simplify complex  ideas.
                If certain information is not present in the paper , respond with "insufficient information available" instead of guessing.
                Ensure the summary is clear , accurate , and alligned with the provided style and length""",

    input_variables = ['paper_input','style_input','input_length']   
)

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'input_length': input_length})
# print(response.content)

# name = st.text_input("Enter your prompt")

if st.button("Summarize"):
    response = llms.invoke(prompt)

    st.write(response.content)