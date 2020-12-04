# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% OO

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
        Database.insert(self.to_dict)


class Database():
    content = {'users': []}  # Class Variable at class level ( GIL)

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder):
        cls.content['users'] = [u for u in cls.content['users'] if finder(u)]

    @classmethod
    def find(cls, finder):
        return [u for u in cls.content['users'] if finder(u)]
