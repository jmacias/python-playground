# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# Already in Pipfile

# %% TEST
from typing import Union


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    return dividend / divisor

# %%
# Default behavior of VS CODE any file starting w test_ or
# ending with _test and methods start with test_


def test_divide():  # Configure VS CODE to find test methods
    assert divide(1, 1) == 1.0
