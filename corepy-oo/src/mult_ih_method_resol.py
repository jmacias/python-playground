"""
* Multi Inheritance
* Inspec tools
* Method Resolution
* Super
"""

# %%


class BaseClass:
    def __init__(self) -> None:
        print("Base Init")

    def f(self):
        print("Base.f()")


class Base2:
    def __init__(self) -> None:
        print("Base2 Init")

    def f(self):
        print("Base2.f()")


class Subclass(BaseClass, Base2):  # In order resolution

    def __init__(self) -> None:
        # Need to call parent explicitly
        s = super()  # Get the proxy obj
        print(s)  # <super: <class 'Subclass'>, <Subclass object>>
        # <bound method BaseClass.__init__ of <__main__.Subclass object at 0x1063f12e0>>
        print(s.__init__)
        # Super can recive params
        # super(class-obj, instance-or-class)
        # WHere to trim MRO, and provide MRO
        s.__init__()  # Follow method resolution
        print("Sub Init")

    def f(self):
        # Just redefine
        # or call super  explicitly
        super().f()
        print("Sub.f()")


c = Subclass()
c.f()
print("===")
print(isinstance(c, BaseClass))
print("===")
print(isinstance(c, Subclass))

"""
More than one parent class
"""
print(Subclass.__bases__)
print(" Determine the order and method to resolve")
Subclass.__mro__  # Method resolution order c3 algorithm and avoid compilation
# (__main__.Subclass, __main__.BaseClass, __main__.Base2, object)
"The ultimate class =>  object"
dir(object)
