"""
We will use Pandas for data manipulation
Main Data Structures: Series and Dataframe
"""


"""
Series:
    * 1 Dim data, labeled array, can hold any data
    * Series indexes can use any label, rather than 0 to n, can be banana, apple... etc.
    * More operations
    * Faster for common Operations

Dataframes:
    * 2D Label data structure w/ cols of diff types
    * Each col is a Series - a DF is a collection of Series

"""
#%%
import pandas as pd

#%%
s=pd.Series([1,2,3,4,5,6,7])
print(s) # Auto discover type

#%%
index_day = pd.Series(["Monday", "Tuesday", "Wednesday", "Thursday", "Fryday", "Saturday", "Sunday"])
data = [1,2,3,4,5,6,7]
s=pd.Series(data, index=index_day)
print(s)

#%%
print(s[0])
print(s["Sunday"])
s["Sunday"] = 8
print(s["Sunday"])

print(f"Mean: {s.mean()}")

#%%
print(s)
print("=======")
print(s+s) # Uses Labels to match operations
print("=======")
print(s*3)

#%% DataFrames
df = pd.DataFrame({'first':s, 'second': s*2})
print(df)

#%%
col_names=['city', 'population']
index_country = ['usa', 'mexico']
r1 = ['Houston', 200000]
r2 = ['MexicoCity', 43000]
data=[r1,r2]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=index_country, columns=col_names)
print(df)

#%% Dictionaries and DF
cities=["Houston", "MexicoCity"]
population = [20000, 230000]
# Dict as data keys are col
data = {'city': cities , 'population': population}

print(data)
df=pd.DataFrame(data)
print(df)
df=pd.DataFrame(data, index=index_country)
print(df)
#%%
"Select Col"
print(df['city'])
#%%
#Select Row - just like slices Col:Row
print(df)
print("---")
print("select row by label index - Start in 1")
print(df[:'usa'])
print("select row by number index  - Start in 1")
print(df[:1])
