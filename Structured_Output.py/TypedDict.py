from typing import TypedDict

class Person(TypedDict):

    name: str
    age : int

## Use

person_1 :  Person = {'name':'Amit','age':25}

print(person_1)