# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% OOP

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    # dunder methods... Magic Methods
    def __repr__(self):
        return f"<Student: {self.name}>"

    # Want to behave like a iterable implement
    #  __getitem__ and __len___

    @classmethod
    def funcname(cls):
        print(cls)


stud_one = Student("Juan Macias", [70, 80, 90])

print(stud_one.__class__)
print(stud_one.name)
print(stud_one.average())
print(Student.average(stud_one))
# Objects is sintactic sugar for Class functions w/ obj call as first param
print(stud_one)  # Thanks to dumber methods

# %% Inheritance


class WorkingStudent(Student):  # The Parent Class
    def __init__(self, new_name, new_grades, salary):  # Salary is the new property
        # Calling super first
        super().__init__(new_name, new_grades)
        self.salary = salary

    def new_salary(self):
        return self.salary

    @property
    def new_salary_p(self):
        return self.salary

    @staticmethod
    def static_methods():  # no self object
        print("Hello from Class")


ws = WorkingStudent("Juan Coronado", [90, 90, 90], 1000)

print(ws)
print("Salary: ")
print(ws.new_salary())  # this has to be call as a method
print(ws.new_salary_p)  # this acts as a property rather than a method

print(WorkingStudent.new_salary(ws))
# Methods are just sugar on top of static methos called
# passing the object as first parameter
print(WorkingStudent.static_methods())

# Class methods pass the class that was call from...
print(WorkingStudent.funcname())
