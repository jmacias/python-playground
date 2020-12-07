# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# Pytest Already in Pipfile
# Course uses unittest

# %% TEST
from typing import Union
import pytest


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero")

    return dividend / divisor

# %%
# Default behavior of VS CODE any file starting w test_ or
# ending with _test and methods start with test_


def test_divide():  # Configure VS CODE to find test methods
    assert divide(1, 1) == 1.0


def test_divide_negative():
    # Test Approx values
    assert pytest.approx(-5.0) == divide(15, -3)


def test_assert_exp():
    # Test Exceptions
    with pytest.raises(ValueError):
        divide(25, 0)
