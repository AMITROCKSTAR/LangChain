## The Tool and ToolMessage interfaces make it possible to distinguish between the parts of the tool output meant for the model (this is the ToolMessage.content) and those parts which are meant for use outside the model (ToolMessage.artifact).

##How to return artifacts from a tool

## Defining the tool

##If we want our tool to distinguish between message content and other artifacts, we need to specify response_format="content_and_artifact" when defining our tool and make sure that we return a tuple of (content, artifact)

import random
from typing import List,Tuple

from langchain_core.tools import tool

@tool(response_format="content_and_artifact")
def get_random_ints(min:int,max:int,size:int)->Tuple[str,List[int]]:
    """Generate size random ints in range [min,max]."""

    array = [random.randint(min,max) for _ in range(size)]
    content = f"Successfully generated array of {size} random ints in {[min,max]}"

    return content,array

## Invoking the tool with the tool call
# print(get_random_ints.invoke({"min":5,"max":10,"size":10}))

print(get_random_ints.invoke(
    {
        "name": "generate_random_ints",
        "args": {"min": 0, "max": 9, "size": 10},
        "id": "123",  # required
        "type": "tool_call",  # required
    }
))