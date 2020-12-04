# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% OO


from typing import List
from abc import ABCMeta, abstractmethod

# %%


class User:
    """
    User Doc
    """

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self):
        return "Logged in"

    def __repr__(self):
        return f'User<{self.name}>'


class Admin(User):
    """
    Admin Doc
    """

    def __init__(self, name, password, access):
        super(Admin, self).__init__(name, password)
        self.access = access

    def __repr__(self):
        return f'Admin<name {self.name}, access: {self.access}>'

    def to_dict(self):
        return {
            'name': self.name,
            'password': self.password,
            'access': self.access
        }

    def save(self):
        Database.insert(self.to_dict())


class Database():
    content = {'users': []}  # Class Variable at class level ( GIL)

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder):
        cls.content['users'] = [
            u for u in cls.content['users'] if not finder(u)]

    @classmethod
    def find(cls, finder):
        return [u for u in cls.content['users'] if finder(u)]

# %%


a = Admin('admin', 'password', 'admin')
a.save()

# Database.insert(a)
#
# u = User('u', 'p')
# Database.insert(u)

# Database.remove(lambda u: True)
Database.find(lambda u: True)

# %% Naive duplication save and to_dict


class Store:
    def __init__(self, name,):
        self.name = name

    def __repr__(self):
        return f'Store<name {self.name}>'

    def to_dict(self):
        return {
            'name': self.name
        }

    def save(self):
        Database.insert(self.to_dict())

# %%Add a thrid class Savable


class Saveable:
    def save(self):
        Database.insert(self.to_dict())


class Admin(User, Saveable):  # Search save first in User and Saveable
    """
    Admin Doc
    """

    def __init__(self, name, password, access):
        super(Admin, self).__init__(name, password)
        self.access = access

    def __repr__(self):
        return f'Admin<name {self.name}, access: {self.access}>'

    def to_dict(self):
        return {
            'name': self.name,
            'password': self.password,
            'access': self.access
        }


a = Admin('admin', 'password', 'admin')
a.save()  # Saves comes from Saveable

# Database.insert(a)
#
# u = User('u', 'p')
# Database.insert(u)

# Database.remove(lambda u: True)
Database.find(lambda u: True)

# %%
# Database.find(lambda u: True)


class Anymal(metaclas=ABCMeta):  # ABC= Abstract Base Class
    # FAILING EXAMPLE

    # Since is abstract should not have a Constructor
    # def __init__(self, name):
    #     self.name = name

    def walking(self):
        print('Walking...')

    @abstractmethod  # Do not instantiate Anymal and force the impl in subclass
    def num_legs(self):
        return 4


class Dog(Anymal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Anymal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


d = Dog('fido')
print(d.num_legs())

# %%


class Saveable:  # Not instantiable a la Interface
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass


class Admin(User, Saveable):
    """
    Admin Doc
    """

    def __init__(self, name, password, access):
        super(Admin, self).__init__(name, password)
        self.access = access

    def __repr__(self):
        return f'Admin<name {self.name}, access: {self.access}>'

    def to_dict(self):  # Force to_dict by Saveable
        return {
            'name': self.name,
            'password': self.password,
            'access': self.access
        }


a = Admin('test', 'pass', 'acc')
a.save()

Database.find(lambda u: True)

# %% Properties Setters

"""
GLA -> LHR -> CAN
 
2 segs
"""


class Segment:
    def __init__(self, o, d) -> None:
        super().__init__()
        self.o = o
        self.d = d


class Flight:
    def __init__(self, segments=List[Segment]) -> None:
        self.segments = segments

    @property
    def departure(self):
        return self.segments[0].o

    @departure.setter  # allow property setting by wrapping with name_property.setter
    def departure(self, val):
        self.segments[0].o = val


f = Flight([Segment('MTY', 'HOU')])

print(f.departure)  # READING PROPERTY
f.departure = 'SA'  # SETTING PROPERTY
print(f.departure)
