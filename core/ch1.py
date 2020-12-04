# The complete python course
# PRE Requisites
# Get python...
# don't mess up your environment
# Configure your CODE Editor

# Start
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code
# %%
# This line is a comment and start with the character `#`
# The comments are not executed by Python
# Variables...
name = "value"
print(name)  # print is a function that writes to console
# variables can change the value and type
name = 2  # different type this is a number
print(name)
# For long var name Py uses snake_case
my_name = 123
# and by convention Upper case for constants - vars that are
# not intended to change
PY_VALUE = 3.1416
print(PY_VALUE)

# %%
# Numbers
# there are 2 types of numbers in Py: int and float
print(type(1))
print(type(1.2))
math_operations = 1 + 3 * 4 / 2 - 2  # Math works as expected
math_operations_parentheses = ((1 + ((3 * 4) / 2)) - 2)
print(math_operations)
print(math_operations_parentheses)
# division always returns a float
print(type(1/1))  # Here we nest functions to avoid unnecessary vars
# division that returns int by removing the values from the decimal point
print(type(1//1))
# Module gives you the reminder of the division of int
int_div = 13 // 5
reminders = 13 % 5
print(int_div)  # 2
print(reminders)  # 3
print(10 % 2)  # Even numbers always return 0 when module 2
print(11 % 2)  # Odd numbers always return 1 when module 2

# %% Strings and String Formating
my_str = "Hola Mundo"
# or
my_str = 'Hola Mundo'
# if your str has quotes use the adequate one to define it
my_str = "Hola 'Mundo'"
# or scape the character using `\`
my_str = "Hola \"Mundo\""
print(my_str)
# multi line strings use triple quotes
my_str = """==========
Hola Mundo
==========
"""
print(my_str)
"""
You can use multiline string as comments since they
are not stored to any variable ...
"""

# Concat strings" you can use `+`
print("Hola" + " "+"Mundo")
# print("Hola" + " "+ 4)  # + can only concatenate str this has an error
print("Hola" + " " + str(4))  # using the `str` function this works

# String formating
age = 40
# from Py 3.6 you can use  F-STRINGs for string intrapolation
print(f"Your age is {age}")
# you can do that using `format` method in string
print("Your age is {}".format(age))
# Here we use named params
print("Your age is {age_param}".format(age_param=age))

# %%  Getting data using input function
age = input("Enter your age: _")
print(age)
age_num = int(age)  # parse function str to int
is_over_age = age_num >= 18
print(f"Are you over age ? {is_over_age}")
working_age = age_num > 18 or age_num < 65
print(f"Are you working ? {working_age}")
# %%
name = ""
surname = "Macias"
# If evaluated to false gives you the second value
greeting = name or f"Mr. {surname}"
print(greeting)

print(f"Zero evals to: {bool(0)}")
print(f"Empty Str evals to: {bool('')}")
print(f"Empty [] evals to: {bool([])}")
print(f"Empty 123 evals to: {bool(123)}")
# Shortcuts like JS
x = True and "test"  # If first eval true it returns second  value
print(x)
x = False and "test"
print(x)

# %% List
# Not typed, can contain any type and value
friends = ["1", "2", "3", 4, ["name", "lastname"]]
friends[0]  # first element
friends[3]
len(friends)
print(friends[4][0])
print(friends)
# add
friends.append(5)
print(friends)
# remove
friends.remove(["name", "lastname"])  # must match exactly
print(friends)


# %% Tuples
tu = (1, 2, 3)
print(tu)
tu = tu + (4,)  # there is no append you can use plus to add
print(tu)
# %%  Sets
s = {1, 2, 3}
print(s)
s.add(1)
print(s)
s.remove(1)
print(s)
s.add(1)
# Membership
print(9 in s)
print(1 in s)
print(1 not in s)

# Operations in set
s2 = {2, 4}
print(f"s1 = > {s}")
print(f"s2 = > {s2}")
s_diff = s.difference(s2)
print(f"Diff s s2 {s_diff}")
s_inter = s.intersection(s2)
print(f"Intersection s s2 {s_inter}")
s_sym_dif = s.symmetric_difference(s2)
print(f"sym Dif s s2 {s_sym_dif}")

# %% Dictionaries
d = {"a": 1, "b": 2}
print(d)
print(len(d))
print(d["a"])
d["c"] = 3
print(d)
# dict functions
d2 = [(1, "a")]
print(dict(d2))

# %% sum function using different collections
print(sum([1, 2, 3]))  # a List
print(sum({1, 2, 3}))  # a Set
print(sum((1, 2, 3)))  # a tuple

# %% Join List
l = ["1", "2", "3"]
pl = ", ".join(l)  # Must be already strings, on numbers this will fail
print(pl)
