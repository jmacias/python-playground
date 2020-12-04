# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# Advanced  Py Dev
# %% Mutability and Immutability

# All numbers, tuples and Strings are Immutability
# So any operation returns a new Object

import logging
import re
import timeit
import time
from datetime import datetime, timezone, timedelta
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

x = "juan macias"
print(f'{id(x)} =value=> {x}')
x.capitalize()  # This did not affect original obj
print(f'{id(x)} =value=> {x}')
x = x.capitalize()  # This did not affect original obj
print(f'{id(x)} =value=> {x}')  # Now x points to diff obj
print("====")

x = 1
y = x
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')
x = x + 1  # This did not affect original obj
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')
print("====")
x = 1
y = x
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')
x += 1  # This did not affect original obj, is a new obj assigned to x
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')

# All other objects are mutable
# So any operation returns a new Object
print("====")
x = [1]  # List is mutablle
y = x
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')
x += [1]  # This modify original obj,
# When possible += will update in place... Python practice
# under the hood this call __isum__
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')

print("====")
x = [1]  # List is mutablle
y = x
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')
x = x + [1]  # This creates a new Object
#  + will create a new Object
# under the hood this call __sum__ and in list creates a new List
print(f'{id(x)} =value=> {x}')
print(f'{id(y)} =value=> {y}')

# %% Compare

y = [1, 2]
x = [1, 2]
print(x == y)  # == compare values
print(x is y)  # is compare obj ref

# %% Default params and dangers of it


def myd(x, y=[]):
    y.append(0)
    return (x, y)


print(myd(1))  # default y
print(myd(1))  # default y ... Y def is evaluated at compile, so Y def holds
# the same object between calls ....:S
print("==== FIX ")
# FIX


def myd(x, y=None):
    if not y:
        y = []
    y.append(0)
    return (x, y)


print(myd(1))  # default y
print(myd(1))  # provide default values for objects using none and create
# this behaves as expected

# %% Arg Unpacking


def my_unpack(a, b):
    return (a, b)


param1 = [1, 2]

print(my_unpack(*param1))
# Must match # of args , more will fail TypeError
# you can do named args
print(my_unpack(b=10, a=1))
param2 = {'a': 1000, 'b': 100000}
print(my_unpack(**param2))  # Unpack by named args :D
# Must match # of args and names, more will fail unexpected key arg

# %% Queues in Py & Collections


# Counter
dev_temp = [1, 2, 1, 1, 2, 3, 4, 5, 5]
temp_ctn = Counter(dev_temp)
print(temp_ctn[1])  # 3
print(temp_ctn[5])  # 2

# default dic
d = {'hello': 5}
# print(d['hi']) # Key Error
d = defaultdict(lambda: None, [('d', 2)])
print(d.default_factory)  # you can change the def factory
d['hello'] = 5
print(d['non_ex_to_be_added'])  # by trying to access is added
print(d)

# Order Dict
o = OrderedDict()
o['2'] = 2
o['1'] = 1
print(o)  # Order of insertion,//// IN PY 3.7 keeps order
o.move_to_end('2')
print(o.items())

# NAmed Tuple
acc = ('Juan', 100)
print(acc[0])

Account = namedtuple('Account', ['name', 'balance'])
account = Account('Juan', 1000)  # Less than a class but great for data

print(account)

# Deque - Thread safe!!!!! DOuble ended queue

f = deque(('Juan', 'Gabo', 'Elvi'))
print(f)
f.append('Sando')
print(f)
f.appendleft('Pablo')
print(f)
f.pop()
print(f)
f.popleft()
print(f)

# %% TimeZone - Time in part of the world
# What time is it ? You have to say where./..
# you can convert what time is it, if you don't say is UTC .. Universal time
# Everytime zone is relative to UTC
print(datetime.now())  # Naive no timezone info
t = datetime.now(timezone.utc)
print(t)  # Same ref +00:00 offset
tom = t + timedelta(days=1)  # minutes, sec, etc...
print(tom)

print(t.strftime('%d-%m-%Y'))
print(datetime.strptime('2020-01-10', '%Y-%m-%d'))  # Get date from str

# %% Time Execution


def powers(limit):
    """
    Expensive comp
    """
    return [x**2 for x in range(limit)]


start = time.time()
powers(50000)
end = time.time()

print(end-start)

# decorator ...


def m_rt(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)


m_rt(lambda: powers(40000))

# Run for you several times and get the exc time
print(timeit.timeit('[x**2 for x in range(5)]'))

# %% Regular Expresion
s = 'a1 a4 a7 a9 a2'
# Find a follow by number and space
ss = 'Juan, Gabo, Elvi'
# Chars ending coma and follow space
# Important Chars
# . "anything"
# + one or more of
# * zero or more of
# ? zero or one of
# \ scape char

# regexr.com
# import re

email = 'juan@macias.me'
expresion = '[a-z\.]+'
matches = re.findall(expresion, email)
print(matches)

price = 'Price: $189.39'
expresion = 'Price: \$(189.39)'  # get the groups thanks to ()
matches = re.search(expresion, price)
print(matches)
print(matches.group(0))
print(matches.group(1))

expresion = 'Price: \$([0-9,]*\.[0-9]*)'  # get the groups thanks to ()
matches = re.search(expresion, price)
print(matches)
print(matches.group(0))
print(matches.group(1))

# %% Python Logs

# import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:    %(message)s'
)

log = logging.getLogger('test_logger')

log.info('Infoooo')
log.warning('Warnnnn')
log.error('errorororor')

# %%
