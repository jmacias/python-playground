# Many lang features use dunder methods __methods__

# %% Class atts

class MyClass:
    MyAtt = 123

    def __init__(self, instance_att) -> None:
        super().__init__()  # Call to parent!
        self.instance_att = instance_att
        # print(MyAtt) ERROR we need to qualify MyAtt
        print('Explicit is better than implicit!')
        print(MyClass.MyAtt)
        print(self.MyAtt)  # Can be accessed
        # But can be rebound at the instance level
        self.MyAtt = "abc"
        print(f"{self.MyAtt}  VS  {MyClass.MyAtt}")
        # remember scopes in Python
        # Local fn, Enclosing fn, Global module, Built-in module
        print('USE CLASS NAME to access class atts!!!')

    @staticmethod
    def static_method_of_the_class():
        print("Still to access the instance be explicit")
        # MyAtt  # ERROR MyClass does not provide scope
        print(f"{MyClass.MyAtt}")

    @classmethod
    def prefer_over_static_if_need_to_access_cls_or_cls_att(cls):
        print(f"And use the cls, just like instance methods, {cls.MyAtt}")

    @classmethod
    # if you change the class name no need to
    def good_for_factory_methods(cls):
        # modify this code
        # and  Child classes will pass correct class :D
        print(f"Lest build an Obj of {cls}")
        return cls("test")


MyClass("hello")
MyClass.static_method_of_the_class()  # to Avoid free Fns
MyClass.prefer_over_static_if_need_to_access_cls_or_cls_att()
print(MyClass.good_for_factory_methods())
print("""
 This you should already derive but....
 =>For polymorphic behavior access class methods using instance
 => Base classes should have not Knowledge of subclass ( use **kwargs in constructors)
""")

# Properties

print("""
    Getters and Setters are not python
    encapsulate in properties which behave like attrs
""")


class MyAtts:

    def __init__(self) -> None:
        self._my_att = 1

    @property
    def my_att(self):
        return self._my_att

    @property
    def my_p(self):
        return self._my_att

    # decorating the getter w/ a setter
    @my_p.setter
    def my_p(self, val):
        self._my_att = val


a = MyAtts()
print(a.my_att)

# ERROR - No setter defined can't do
# MyAtts().my_att = 2
a.my_p = 2213
print(a.my_att)
print(a.my_p)
