from abc import ABC,abstractmethod
import random


class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass


class NakliLLM(Runnable):

    def __init__(self):
        print('LLM Created')

    def invoke(self,input_data):
        
        response_list = [
            "India is my country",
            "I am strong",
            "I love myself"
        ]

        return {'response':random.choice(response_list)}

llm = NakliLLM()



class NakliPromptTemplate(Runnable):

    def __init__(self,template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self,input_dict):
        return self.template.format(**input_dict)

## Making prompt object
template = NakliPromptTemplate(
    template='Write a poem about {topic}',
    input_variables=['topic']
)
template2 = NakliPromptTemplate(
    template='Write a joke on {response}',
    input_variables=['response']
)


class RunnableConnector(Runnable):

    def __init__(self,runnable_list):
        self.runnable_list=runnable_list

    def invoke(self,input_data):

        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)

        return input_data


# chain = RunnableConnector([template,llm])


class StrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self,input_data):
        return input_data['response']



parser = StrOutputParser()

## Making multiple chains

chain1 = RunnableConnector([template,llm])
chain2 = RunnableConnector([template2,llm,parser])

chain = RunnableConnector([chain1,chain2])
response = chain.invoke({'topic':'Love'})
print(response)