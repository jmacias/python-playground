"""
Class Decorators
 * Programattically transform class def
 * Similar to Fns decorators
 * Overlap w/ Metaclasses - less powerful but easier to use

Create WRAPPERS of classes w/ same interface

Add __repr__ using decorator
"""

# %%

# Modules are singletons

import inspect


def auto_repr(cls):
    print(f"decorating {cls} w auto repr")
    members = vars(cls)
    for name, member in members.items():
        print(name, member)

    # Allow only not defined classes
    if "__repr__" in members:
        raise TypeError("already there")

    sig = inspect.signature(cls.__init__)
    params = list(sig.parameters)[1:]
    print(params)

    def my_repr(self):
        return f"<<<{cls} - {params} >>>>"

    # Add atts to classes - Manipulate Class!!
    setattr(cls, "__repr__", my_repr)
    return cls


@auto_repr
class Simple:
    def __init__(self, name) -> None:
        self.name = name


@auto_repr
class Simple2:
    def __init__(self, value) -> None:
        self.value = value


s = Simple("test")
s2 = Simple2("test")
print(s)
print(s2)

# %%
