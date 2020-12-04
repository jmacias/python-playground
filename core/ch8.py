# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code


# %% Typing
from typing import List, Union, Dict

"""
Py is dynamic you don't have to specify the type of the var's
But

you can tell py the types of par and returns, but not enforce
"""


def f(p) -> None:
    pass


def listOfDict() -> List[Dict[str, Union[str, int]]]:
    """
    return a list of dic from str->str|int
    """
    return []


Book = Dict[str, Union[str, int]]


def createBook(name: str, auth: str) -> Book:
    # return dict(  # this also works
    #     name=name,
    #     auth=auth
    # )
    return {
        "name": name,
        "auth": auth
    }


# Type vars
b: Book = createBook("Juan", "Macias")
print(b["name"])


# %%
