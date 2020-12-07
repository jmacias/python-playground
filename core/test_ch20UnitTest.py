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


# follow : https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# How to mock?


# Fixtures

@pytest.fixture
def empty_array():
    '''Empty Arrya'''
    return []


@pytest.fixture
def numbers():
    return [1, 2, 3]


def test_sum_all(numbers):  # You pass the named fixture
    assert sum(numbers) == 6


def test_sum_empty(empty_array):  # You pass the named fixture
    assert sum(empty_array) == 0


# List Fixtures using pytest --fixtures

# %%
@pytest.mark.parametrize("param1,param2", [
    (1, 1),
    (2, 2),
])
def test_sum_param(empty_array, param1, param2):
    empty_array = []
    empty_array.append(param1)
    empty_array.append(param2)
    assert sum(empty_array) == param1 + param2

# TODO: Mocking


'''                                                                       
test_ch20UnitTest.py::test_sum_param[1-1] PASSED
test_ch20UnitTest.py::test_sum_param[2-2] PASSED
'''
