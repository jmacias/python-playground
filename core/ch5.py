# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% Errors

# NameError: name 'name_error' is not defined
print(name_error)

# %% Index Errors
l = [1, 2]
l[4]  # IndexError: list index out of range

# %% Key Error
m = {"a": 2}
m["b"]  # KeyError: 'b'

# %%
m = {"a": 2}
m.intersection  # AttributeError: 'dict' object has no attribute 'intersection'

# %% Throw => raise NotImplemented Error


def raiseError():
    raise NotImplementedError("Not yet")


raiseError()  # NotImplementedError: Not yet

# %% Other Errors Tab Errors, Type errors

5 + 'hi'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# %% ValueError
int('30.3')  # ValueError: invalid literal for int() with base 10: '30.3'

# %% Create your own errors

# Custom Exceptions are encourage to extend Exception


class MyCustomError(TypeError):  # Just inherit from an Error
    """
    My Custom Error class documentations
    ## Doc String
    """

    def __init__(self, msg, code):
        super().__init__(f'Error code {code}: {msg}')
        self.code = code


# raise MyCustomError("auch!!!", 100)
e = MyCustomError("", 1909)
print(e.__doc__)

# %% Handling Errors
try:
    print("Inside try")
    raise MyCustomError("Test", 100)
except TypeError:
    print("Type Error happend")
except (RuntimeError, NameError) as err:  # capture the err in a var
    print("Fot runtime and name")
    print(err)
    raise  # raise the error capture
else:
    print("Only if no excption is raised")
finally:
    print("FINALLY ALWAYS RUN")
