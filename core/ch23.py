# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% Python Review Refresher


# %% Variable

# from ch13Async import greet


x = 15  # Python Evaluates the value expresion first, in this case 15, and left later

price = 9.99  # Diff types
discount = 0.2

type(price)

result = price * (1 - discount)

print(result)

name = "test"
name = "bob"
print(name)
print(name * 2)  # Multi has meaning for strings this double the string

a = 25
b = a

print(a)
print(b)
b = 17  # Change the reference
print(a)
print(b)

# %% String Formating

# Since 3.6

name = "Bob"
greeting = "Hello, Bob"
print(greeting)
# Embed var inside Strings
greeting = f"Hello, {name}"  # When evaluated , greeting is not dinamic
print(greeting)
name = "Rolf"
print(greeting)
greeting = "Hello, {name}"  # Make it a template
print(name)
print(greeting.format(name=name))  # Pass the current value using kargs
greeting = "Hello, {}"  # Make it a template
print(greeting.format(name))  # Pass the current value using position


# %% User Input and transformations of string->to other type
input_str = input("Input:")
input_int = int(input_str)
input_cal = input_int / 10.8
# Inside FStr you cna format numbers using `:.PresicionNumf `
print(f"{input_cal:.2f}")

# %% List Tuples and set

l = ["Bob", "Rolf", "Ann"]  # Mantain the order
t = ("Bob", "Rolf", "Ann")  # You cannot modify the tuple
s = {"Bob", "Rolf", "Ann"}

print(t[2])

l[0] = "Juan"
print(l)

"""  Error Type error
t[0] = 'Juan'
print(t)
"""
l.append("test")
s.add("Juan")
print(l)
print(s)

# %% Advance Set Ops

friends = {"Bob", "Rolf", "Ann"}
abroad = {"Bob", "Ann"}
local = friends.difference(abroad)
print(local)

all_f = local.union(abroad)
print(all_f)

friends_2 = {"Bob", "Rolf", "Ann", "Juan"}

inter = friends.intersection(friends_2)
print(inter)

# %% Booleans

print(5 == 5)
print((5 == 5) == True)
#  !=, >, < in tuples and list
print([] == [])
# is operator is memory  comparison
a = []
b = []
print(a == b)
print(a is b)

# %% if statements
# What evals to false
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))
print(bool(0.0))

print(bool(" 1 "))
print(bool([1]))
print(bool((1, 2)))
print(bool({1, 2}))
print(bool(-1))
print(bool(0.2))

# %% IN Keyword
l = [1, 2, 3]
s = "test"
m = {"a": 1, "b": 2, 2: "2"}
print(1 in l)
print(1.0 in l)
print("t" in s)
print("t" in m)
print("a" in m)
print(1 in m)
print(2 in m)

# %% Loops
l = ""
while not l:  # Loop while empty string
    l = input("Stop")

do_while_less_than_10 = 0

while do_while_less_than_10 < 11:
    print(do_while_less_than_10)
    do_while_less_than_10 += 1

# %% For Loops
items = [1, 2, 3, 4]

for i in items:
    print(i)

# go through indexes
for i in range(len(items)):
    print(items[i])

# You have to be aware of others funs like sum
# that reduce lists
print(sum(items))

# %%  List comprehension

nums = [1, 3, 5]
doubled = []

# for n in nums:
#     doubled.append(n*2)
# Rather than that use lisp comp
doubled = [n * 2 for n in nums if n != 5]
print(doubled)

# %% Dictionaries

f_age = {"Joe": 29}

print(f_age["Joe"])

try:
    f_age["Foo"]
except KeyError as e:
    print("Key Error" + str(e))

# Going through the items
for i, v in f_age.items():
    print(i)
    print(v)

for i in f_age.keys():
    print(i)
    print(f_age[i])


for i in f_age:  # By default goes to key
    print(i)
    print(f_age[i])

# Modify
f_age["Joe"] = 50

print(f_age["Joe"])

# %% Destructuring works in for loops
# by def py threat it like a Touple
x, y = 5, 6
print(x)
print(y)
x, y = (5, 6)
print(x)
print(y)

x, y = 5, 6
print(x)
print(y)

name, age, _ = ("Name", 49, "Tx")  # Underscore for don't care
print(name)

name, age, _ = ["Name", 49, "Tx"]  # Works with lists
print(name)

# * for rest
head, *tail = [1, 2, 3, 4]
print(head)
print(tail)
*head, tail = [1, 2, 3, 4]
print(head)
print(tail)

# %% Functions Args and params


def hello():
    print("Hola")


hello()

# Params and Args


def parameters(arg1, arg2):
    print(arg1)
    print(arg2)


parameters("1", "2")  # Positional has to first!
parameters(arg1="1", arg2="2")  # Named parameters

# Defaults args


def parameters(arg1, arg2=2):  # Required must go first
    print(arg1)
    print(arg2)


parameters(arg1="1")  # Named parameters, 2 by def

default_arg = 1


def parameters(arg1, arg2=default_arg):  # Eval Val at Def
    print(arg1)
    print(arg2)


parameters(arg1="1")
default_arg = 100  # even if you change it you get the eval one
parameters(arg1="1")  # not 100 for second

# What about objs

default_arg = {1: 1}


def parameters(arg1, arg2=default_arg):  # Eval Val at Def, but this time a ref
    print(arg1)
    print(arg2)


parameters(arg1="1")
default_arg[1] = 100  # ups you change the ob, the ref
parameters(arg1="1")  # you get 100 for the second :S

# %%
def padd(a, b):
    print(a + b)


result = padd(1, 2)

print("no return statement then it returns None")
print(result)

# %%
"""
Lambda Fns or anonymous functions
"""
# No name///
lambda x, y: x + y
# lets assign it to a var
add = lambda x, y: x + y

print(add(1, 23))
doubled = map(lambda x: x * x, [1, 2, 3])
print(list(doubled))

# %%
"""
Dictionary Comprehension
"""
users = {
    "first": "last",
    "first2": "last2",
}

user_cap = [u for u in users]  # By default it iterates the KEYS
user_cap
"""
Use items to get seq of k->v and de structure to pull them appart, and 
generate a new map, transforming k and v
"""
user_cap = {f.capitalize(): l.capitalize() for (f, l) in users.items()}
user_cap

# %%

"""
Unpacking Args
"""


def myf(*args):
    print(args)  # Get a tuple inoder of the args


myf(1, "q", [1, 2, 3])

myf(*(1, 2, 3))  # a tuple or list to positional args

myf(*[1, 2, 3])  # a tuple or list to positional args


def myf2(a, b, *args):
    print(a, b)
    print(args)  # Get a tuple inoder of the args


print("=====")
myf2(*(1, 2, 3))  # a tuple or list to positional args

myf2("a", *(1, 2, 3))  # a tuple or list to positional args

myf2("a", "b", *(1, 2, 3))  # a tuple or list to positional args


def myf3(a, b=None, *args, **kwargs):
    print(a, b)
    print(args)  # Get a tuple in oder of the args
    print(kwargs)  # Get a Map of the args


print("====")
# myf3() ERROR position are check at evaluation
# myf3("1", "2", 1,2,3, a=1) ERROR a is duplicated:S
myf3("1", "2", 1, 2, 3, c=1)


print("====")
myf3("1", "2")  # Only positional args are checked the rest are empty
print("====")
myf3(a=1)  # Since b has default value we can skep
myf3(a=1, b=3)
print("==== UNPACKING Keyword args ")
myf3(**dict(a=1, b=3, c=3))  # SInce a and b are provided we can pass the map
# and is called as named params


def myf5(*args, enforce_named_par_at_end):
    print(args)  # Get a tuple in oder of the args
    print(enforce_named_par_at_end)


try:
    myf5(1, 2, 4, 3)
except:
    print("Missing named arg at the end")


myf5(1, 2, 4, 3, enforce_named_par_at_end=2)

#%% OO Prog
"""
OO Prog
"""


class Student:
    # Class value
    TYPES = ("a", "b")

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    # Class method - Good for factory
    @classmethod
    def class_m(cls):
        print(cls)
        return cls

    @staticmethod  # a FN inside a class
    def scm():
        print("NO PARMAS")

    # Instance Method, you get self the instance to access data
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    # STR is preferred over repr on print
    # THe str method depends on this Interface
    def __str__(self) -> str:
        return "<MY STUDENT " + self.name + " >"

    def __repr__(self) -> str:
        return "<MY STUDENT REPR " + self.name + " >"


print(Student("name", [10, 10]).average_grade())

"""
dunder methods on OBJS

"""
print(Student("name", [10, 10]))

print(Student.class_m())
print(Student.scm())


#%%
# Inheritance
# on init call super().__init__() ....
# If you want to call parent method do it using super()

"""
TYPE INTING  > 3.5
"""
from typing import List


def my_av(se: List[int]) -> float:
    return sum(se) / len(se)


# Enable mypy to see the error

my_av([1, 2])


## __name___ change w/ the file you are in