# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# Advanced Functions
# %% Generators

# Async build  on top of this
# GEN => A fun that remembers the state is in between executions

def hund_num():
    """
    Return 100 num
    """
    # nums = []  # Commented out impl old in memory all the nums
    i = 0
    while i < 100:
        # nums.append(i)
        yield i  # liker return but will generate the numbers 1 by 1
        i += 1

    # return nums


g = hund_num()
print(g)  # now it prints only is a generator since we do
# not get the number
print("==========")
print(next(g))
print(next(g))
print("==========")
print(list(hund_num()))  # Turn a generator to a list
print("==========")
# Kind of lazy, use the number until you use it

print([x * 2 for x in hund_num()])

# %%  Generator Classes and Iterators
# All generators are iterators
# But not all iterators are generators ...


class FirstHundred:
    def __init__(self):
        self.number = 0

    # All OBJs that have next are iterators
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundred()
print(next(my_gen))
print(next(my_gen))


# %%  Generator Classes and Iterators 2
# and an Iterators is not iterable by default
for i in my_gen:
    print(i)  # Raise error is not iterable

# %%  Iterable


class FirstHundIterable:
    def __iter__(self):  # Yes you can put it in FirstHundred
        return FirstHundred()  # Rerturn a Iterator

# Iterables are __iter__ or __len__ and __getitem__


print(sum(FirstHundIterable()))


for i in FirstHundIterable():
    print(i)  # Raise error is not iterable

my_list_from_LISTCOM = [x for x in [1, 2, 3, 4]]
print(my_list_from_LISTCOM)

my_list_from_GENERATOR_compr = (x for x in [1, 2, 3, 4])  # Use Parenthesis
print(my_list_from_GENERATOR_compr)
print(next(my_list_from_GENERATOR_compr))

print('Does a Generator Comp can be in a for loop')
print(type((x for x in [1, 2, 3, 4])))
for i in (x for x in [1, 2, 3, 4]):
    print(i)
# %% Filter Functions
f = ["Juan", "Gabo", "Malu", "Diego"]


def starts_w_d(f):
    return f.startswith("D")


filtered = filter(starts_w_d, f)
print(filtered)
print(next(filtered))
print(list(filtered))
# print(next(filtered)) Stop Iteration Error
# Generator EXP
filtered2 = (x for x in f if x.startswith("D"))
print(filtered2)
print(next(filtered2))
print(list(filtered2))

# %% MAP Functions
# Iterable -> Iterable
f_l = map(lambda x: x.lower(), f)
print(next(f_l))
f_l2 = (x.lower() for x in f)
print(next(f_l2))

# %% Any and ALL
any_ex = (x for x in f if x.startswith("K"))
if any(any_ex):
    print("You have friends w/ K")
else:
    print("No K")

# What eval to false?
print("===")
print(bool(""))
print("===")
print(bool(None))
print("===")
print(bool(0))
print("===")
print(bool(()))
print("===")
print(bool([]))
print("===")
print("===")
print(bool({}))
print("""
Sooooooo any and all
""")
print("===")
print(any(["", [], {}, None]))
print(any(["", [], {}, None, "Juan"]))
print("=== ALL")
print(all(["", [], {}, None]))
print(all([(1,), {"a"}, 1, "Juan"]))

# %% Enumerators
print("Enumerators")

top_f = ["Gobo", "Elvi", "Pablo"]

for i in range(3):
    print(f'My top {i+1} is {top_f[i]}')

print("Index and the Item you can use enumerate")
for i, f in enumerate(top_f):
    print(f'My top {i+1} is {f}')


# %%
