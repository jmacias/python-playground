# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %%
friend = "Gabo"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello Friend")
else:
    print("Not Friend")
# to terminate the if scope is based on spaces
print("out of the if")

if 5:
    print("Python evaluates the expresion ... so it prints")

# %% else if
my_in = int(input("Give an Int"))
if my_in > 0:
    print("Positive")
elif my_in == 0:
    print("ZR")
else:
    print("Negative")

# %% While loop = repeat things until something changes
is_learning = True
while is_learning:
    print("You are learning")
    # Never changes will run for ever....
    is_learning = input("Continue.... (True or False)")

# %% While loop = repeat things defined # of time
els = [1, 2, 3, 4, 5, 6]

for _ in els:  # Use _ if not plan to use it
    print(_)
print("-------")
for i in range(10):  # Generates a list
    print(i)

# %% De structuring :D
l = [(1, 2), (2, 4)]
print(l)
# Destruct in for exp
for f, s in l:
    print(f"f {str(f)}, s {str(s)}")
# Destructuring List
f, s = l
print(f"f {f}, s {s}")
# Destructuring List and the tuple
(ff, ss), s = l
print(f"ff {ff}, ss {ss}")

friends = {"juan": 29, "gabo": 28}
for key in friends:  # by default iterate over keys
    print(key)

for v in friends.values():  # iterate over values
    print(v)

for k, v in friends.items():  # iterate over items (tuples)
    print(f"{k}, {v}")

# %% Print Prime Numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break  # This will break the second for loop
    else:  # Execute the following only if there was not a break
        print(f"{n} is a prime number!")
# %% List Slicing and tuple slicing
l = [1, 2, 3, 4, 5, 6]
print(l[1:4])
print(l[:4])
print(l[2:])
print(l[-2:])  # From the end (negative to ..) Last 2

# %% List Comprehencion
n = [0, 1, 2, 3, 4]
nl = [num*2 for num in n]
print(nl)
# you can filter out as well
nl = [num*2 for num in n if num % 2 == 1]
print(nl)
nl = {num*2 for num in n if num % 2 == 1}  # you can create a SET
print(nl)
nl = {num: num*2 for num in n if num % 2 == 1}  # you can create a Dict
print(nl)

# %% ZIP FUNCTION
a = ["a", "b", "c"]
b = [1, 2, 3, 4]
c = [100, 200, ]
print(list(zip(a, b)))
print(dict(zip(a, b)))
print(list(zip(a, b, c)))  # the zip will contains at must the short list len

# %% FNS


def hola():
    name = input("enter your name:")
    print(name)
    # No return value , return None value


print(type(hola()))
print(type(None))

# %% Named Args

print(1, 2, 3, 4, 4, sep="____")
# Dont use var as named arg vars .....

# %% Lambda FN

(lambda x, y: x / y)(1, 19)

# Anonymous functions

# Higher Order Fn


def before_after(func):
    print("before")
    func()
    print("afert")


# We pass a function as a parameter
before_after(hola)
