# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% Loops

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
    f_age['Foo']
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
f_age['Joe'] = 50

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

# Lambda Fns or anonymous functions
