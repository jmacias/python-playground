# The complete python course
# We will use ipy integration in code to execute chunks of code
# to execute a chunk of code just use `# %%` And
# Ctrl+ Enter will execute the code

# %% Files In Python

# Open file in read mode, there is a limit in the number of files opens
import json  # Default JSON Module w/ Python
my_file = open('data.txt',  'r')
file_content = my_file.read()
my_file.close()
print(file_content)


user_name = input("Enter your name: ")
# Keep files opens as short as possible
my_f_w = open('data.txt', 'w')  # Open in overide mode
my_f_w.write(user_name)
my_f_w.close()

# %% Copying Files
# copy 3 names from people to nearby by the input by the user
names = []
for i in range(3):
    name = input(f"Friend {i+1}: ")
    names.append(name)
print(names)

people_f = open('people.txt', 'r')  # Open in read mode
peopleNames = {
    name.strip(): name.strip()
    for name in people_f.readlines()
}
people_f.close()

nbf_f = open('nearby_friends.txt', 'w')  # Open in overide mode
for name in names:
    if name in peopleNames:
        nbf_f.write(name + '\n')

nbf_f.close()

# the solution used set(list) and then intersection to find the content

# %% CSV Files
f = open('csv.txt', 'r')
ls = f.readlines()
f.close()

lines = [l.strip() for l in ls[1:]]  # do not read the head

for l in lines:
    p = l.split(',')
    name = p[0]
    age = p[1]

    print(f'{name.title()} is {age}')

# %% JSON Files

f = open('friends.json', 'r')
#content =  f.read()
content = json.load(f)
f.close()

print(content['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

f = open('cars.json', 'w')
json.dump(cars, f)
f.close()

j = json.loads('{"name": "Juan"}')

print(j['name'])

# %% Using resource/ctx Management = The with statement

with open('friends.json', 'r') as file:
    content = json.load(file)

print(content)

# %% Importing a file...
# file operations let's get the files
# Execute the file

# import file_operations # Module Mode, and run as module mode

file_operations.save_to_file('JM', "mylib.txt")


# %% importing methods from the module
# from file_operations import save_to_file, read_file

save_to_file('JM2', "mylib.txt")
l = read_file('mylib.txt')
print(l)


# %% importing methods from the module
# from utils.file_operations2 import save_to_file, read_file
# old py versions required a __init__.py file to make it a
# Package

save_to_file('JM2', "mylib.txt")
l = read_file('mylib.txt')
print(l)


# %% importing with alias
# %% importing methods from the module
# import utils.file_operations2 as fops # importing with alias

fops.save_to_file('JM2', "mylib.txt")
l = fops.read_file('mylib.txt')
print(l)

# %% importing methods from the module
# from utils.file_operations2 import read_file as rf

l = rf('mylib.txt')
print(l)
# %% importing modules

print(__name__)

# you can import relative but dont do it
# using `import .relative.folder.name`
# or using `import ..parent.relative.folder.name`
# you cannot run them as script

# Python Path know how to handle the complete names
# use complete names

# %% Import errors

# Circular imports are hard , better import modules

# %% Execute code only when running as script

if __name__ == "__main__":
    print("Running as Script")
