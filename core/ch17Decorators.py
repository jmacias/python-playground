# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% Decorators

"""
Higher Order Functions, Functions that accept a fn an returns a fn
"""
import functools
user = {'name': 'Juan Macias', 'access_level': 'admin'}


def user_has_permissions(fun):  #
    def sec_fn():
        if user.get('access_level') == 'admin':
            return fun()
        # raise RuntimeError

    return sec_fn


def my_fn():
    return 'Hola'


my_sec_fn = user_has_permissions(my_fn)
print(my_sec_fn())

# %% Decorators 2 - @ Syntax


@user_has_permissions  # Translate to user_has_permissions (my_fn2)
def my_fn2():
    return 'Hola'


print(my_fn2())

print(my_fn2.__name__)  # Ups it should be my_fn2 Use Fn Tools
# %% Using functools


def user_has_permissions(fun):  # DECORATOR
    @functools.wraps(fun)  # Keep Name and Doc String
    def sec_fn():
        if user.get('access_level') == 'admin':
            return fun()
        # raise RuntimeError

    return sec_fn


print(my_fn2.__name__)  # FIX

# %% Decorators parameters


def third_level(level):
    def user_has_permissions(fun):  # DECORATOR
        @functools.wraps(fun)  # Keep Name and Doc String
        def sec_fn():
            if user.get('access_level') == level:
                return fun()
            # raise RuntimeError

        return sec_fn

    return user_has_permissions


# Translate to third_level('admin') (my_fn2)
@third_level('admin')
def my_fn2():
    return 'Hola'


print(my_fn2())

# %% Decorating fn multiple args


def add_all(x, y, z):
    return x + y + z


vals = {'x': 1, 'y': 2, 'z': 4}

print(add_all(**vals))  # Pass vars as named args

# You can use Start Args to accept args


def add_all(*args):
    return sum(args)


print(add_all(1, 2, 4))


def add_all(**args):
    return sum(args.values())


print(add_all(**vals))


# %% Making decorators generic for any fn


def third_level(level):
    def user_has_permissions(fun):  # DECORATOR
        @functools.wraps(fun)  # Keep Name and Doc String
        def sec_fn(*args, **kargs):
            if user.get('access_level') == level:
                return fun(*args, **kargs)
            # raise RuntimeError

        return sec_fn

    return user_has_permissions


@third_level('admin')
def add_all(x, y, z):
    return x + y + z


@third_level('admin')
def hola():
    return "Hola"


@third_level('admin')
def hola2(name, **named_args):
    return f"Hola {name}, {named_args}"


print(hola())
print(add_all(1, 2, 3))
print(hola2('juan', test='hellp', k=2))
