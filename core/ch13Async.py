# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# Async Python
# THE GIL - LOCK to run python...Same problem as NODE in the begining
# Multithread is only good when there is a lot of waiting ( like Network )
# that use case is when it make sense in py to use multithread

# Multiprocess 2 or more pythons gils good for computations

# %% Multi tasking - One After the other Single Thread
import asyncio
#import nest_asyncio
import aiohttp
from types import coroutine
from collections import deque
import queue
import logging
import random
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import process
from threading import Thread
import time

# %%


def ask():
    """
    """
    start = time.time()
    name = input("Enter Name: ")
    greet = f'Hello, {name}'
    print(greet)
    print(f'ASK USER {time.time() -  start}')


def complex():
    str = time.time()
    print("Start process")
    [x**2 for x in range(20000000)]
    print(f'Complex {time.time() -  str}')


start = time.time()
ask()
complex()
print(f'Single THread total time {time.time() - start}')

# %% Multi tasking - Using Thread


start = time.time()
t1 = Thread(target=ask)
t2 = Thread(target=complex)
t1.start()
t2.start()
t1.join()
t2.join()
# Consume as long as the longest task since they
# are executed in parallel
print(f'Single THread total time {time.time() - start}')

# %% But if both are compute

start = time.time()
t1 = Thread(target=complex)
t2 = Thread(target=complex)
t1.start()
t2.start()
t1.join()
t2.join()
# Is worst because the computer is busy
print(f'Single THread total time {time.time() - start}')

# %% THreadPoolExecutor

# Dont need to call shutdown
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex)
    pool.submit(ask)
"""
don't kill threads LOCK GIL might never release GIL!!!!!
DEATHLOOK
"""
# %% Launching multiple process - Does not work w/ interactive python...
# To pass param to process the param must be serialized using pickle

start = time.time()
process2 = Process(target=ask)
process = Process(target=complex)
process.start()
process2.start()
process.join()
process2.join()
# Does not work because they do not share the terminal
print("AFTER JOINIGN")
print(f'Single THread total time {time.time() - start}')
# %% when you have multicore machine
#from concurrent.futures import ProcessPoolExecutor
# For Process Pool Exc

start = time.time()
process2 = Process(target=complex)
process = Process(target=complex)
process.start()
process2.start()
process.join()
process2.join()
# Does not work becouse they do not share the terminal
print("AFTER JOINIGN")
print(f'Single THread total time {time.time() - start}')

# %% Sharing State in multithreaded code

# Atomic Opt - Ops that cannot be interrumpet - like print line
counter = 0


# log = logging.getLogger('THREAD_LOG')
# logging.basicConfig(
#     filename="logs-Threads.txt",
#     level=logging.DEBUG,
#     format='%(asctime)s %(levelname)s:    %(message)s'
# )


def m_increment():
    global log
    global counter

    # Adding Random Sleeps - Fusin Technique
    time.sleep(random.random())
    counter += 1  # Share state ....
    time.sleep(random.random())
    print(f'New counter value {counter}')
    time.sleep(random.random())
    print('===')


for x in range(10):
    t = Thread(target=m_increment)
    time.sleep(random.random())
    # Rather than getting 1.2.3.4.
    # We might get 3.3.5.5.6.7.
    t.start()

"""
SHARED STATE!!!! is dangerous!!  
"""

# %% Using Queue to Make work in order

counter = 0
jobs_q = queue.Queue()  # When we see something printed
counter_q = queue.Queue()  # Inc counter by


def inc_mng():
    global counter
    while True:
        inc = counter_q.get()  # Wait until item is available and locks
        time.sleep(random.random())
        old_c = counter
        time.sleep(random.random())
        counter = old_c + inc
        time.sleep(random.random())
        jobs_q.put((f'New Counter value {counter}', '==='))
        time.sleep(random.random())
        counter_q.task_done()  # Unlock the queue, another thread can get


Thread(target=inc_mng, daemon=True).start()  # Run Forever


def print_mng():
    while True:
        for l in jobs_q.get():
            time.sleep(random.random())
            print(l)
            time.sleep(random.random())

        jobs_q.task_done()


Thread(target=print_mng, daemon=True).start()  # Run Forever


def inc_counter():
    counter_q.put(1)


workers = [Thread(target=inc_counter) for t in range(10)]


for t in workers:
    t.start()

for t in workers:
    t.join()

counter_q.join()
jobs_q.join()

'''
You need Thread safe QUEUE to matin order between threads 
Put a queue in front of it
'''

# %% Generators for Threads...


def countdown(n):
    while n > 0:
        yield n
        n -= 1


c1 = countdown(10)
c2 = countdown(20)

# Since we park the generator w/ yield we can do other work while
# the other things are wating

# 2 Tasks yielding control of the main thread
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))

# %% Using Generator insted of Threads for Multitasking

# Multitasking, doing things that looks like happening at the same time,
#  but they are really not, they are sharing while wait for IO

#  Parallelism is actually doing things at the same time
# In Py you cannot do parall due to the GIL unless you launch diff process

tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print("Tasks Finish")

'''
Multitasking without using Threads... 
next is cheaper rather than Switching threads
'''

# %% Yield from another iterator

friends = deque(('Jose', 'Gabo', 'Pablo', 'Elvis'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration as st:
            pass


friends_g = get_friend()
g = greet(friends_g)
# COmposing Generators PARK the whole computation ( composed yields)
# Until we call next
print(next(g))
print(next(g))

# %% Yield to receive data # PRIMING GENERATORS #


def hola():
    name = yield
    print(f'Hola {name}')


g = hola()
g.send(None)  # Priming the generator
g.send('Gabo')  # Send Values to it

# %%  Asyn Py
f = deque(('Juan', 'Gabo', 'Elvi'))

# This kind of generator that accept data and park
# are known as COROUTINE


def f_up():
    while f:
        friend = f.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)
    while True:  # Running forever waiting for input
        gretting = yield
        g.send(gretting)  # Sends input to another fn


greeter = greet(f_up())
greeter.send(None)
greeter.send('Hello')
print('Hello Multitasking')
greeter.send('How are you')

# %% Async and Wait ... Yield was weird
#from types import coroutine

f = deque(('Juan', 'Gabo', 'Elvi'))

# This kind of generator that accept data and park
# are known as COROUTINE


@coroutine
def f_up():
    while f:
        friend = f.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    # NEw AsYNC - Wait for a corouting
    print('Starting')
    r = await g
    print(r)
    print('Finish')

    # g.send(None)
    # while True:  # Running forever waiting for input
    #     gretting = yield
    #     g.send(gretting)  # Sends input to another fn


greeter = greet(f_up())
greeter.send(None)
greeter.send('Hello')
print('Hello Multitasking')
greeter.send('How are you')
greeter.send('How are you')
greeter.send('How are you')
greeter.send('How are you')
greeter.send('How are you')

# %% Async and Wait ... Yield was weird
# asyncio
# aiohttp

# nest_asyncio.apply()


async def fetch_page(url):
    async with aiohttp.ClientSession as session:
        async with session.get(url) as response:
            return response.status

loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_page('http://google.com'))
tasks = [fetch_page('http://google.com') for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start}')

# %%
