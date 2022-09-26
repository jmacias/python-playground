"""
We will use Pandas for data manipulation
Loading Data - Diff Data Sources, examples in CSV (readCSV)and Excel(readExcel)
"""
#%%
import pandas as pd

#%% Loading Data

df_powers=pd.read_csv('superhero_powers.csv')
df_dc=pd.read_excel('superhero_info.xlsx', sheet_name="DC Comics")
df_marvel=pd.read_excel('superhero_info.xlsx', sheet_name="Marvel Comics")

#%% Preview Data
df_dc.head(n=1)
#%%
df_dc.tail()
#%% Nice summary to see missing values and type
df_dc.info()

#%% For large number of colls
df_powers.info() # No col info show by default
#%% Use verbose
df_powers.info(verbose=True) 
#%%
df_powers.columns
#%%
df_powers.shape  # cols and rows

"""
PANDAS DATA TYPES (dtypes)
* All col must have same data type
* Comes from NumPy + extensions

"""
#%% Converting DTypes 
# to_numeric
# to_datetime
# you can specify the dtype of col on read_*
df_w=pd.read_csv("weather.csv")
df_w.info()
#%%
df_w.dtypes

#%% Lets convert date to datetime and other cols
df_w['temperature_high']=df_w['temperature_high'].astype('int8')
df_w['rained']=df_w['rained'].astype('bool')
df_w=df_w.astype({
    'overcast':'category',
    'comments':'string'
})
df_w.dtypes
# unknow str in a num col
df_w['temperature_low']=pd.to_numeric(df_w['temperature_low'], errors='coerce')
df_w.dtypes
# datetimes
# df_w['date']=df_w['date'].astype('datetime')
df_w['date']=pd.to_datetime(df_w['date'])
df_w.dtypes

# Fixing on reading
df_powers=pd.read_csv('superhero_powers.csv', dtype={
    'hero_names':'string'
})
df_powers.info(verbose=True)

#%% PANDAS EXPORTING DATA 

df_powers.to_pickle("hpower.pkl")
df_powers_pkl=pd.read_pickle("hpower.pkl")
# Keeps data types - pickle is python specific format
df_powers_pkl.dtypes

#%% Manipulate the DF - MERGE

left = pd.DataFrame({"col1":[1,2,3,4,5], "col2":['a','b','c','d','e']} )
right=pd.DataFrame({"col1":[3,4,5,6,7], "col2":['f','g','h','i','j']})
#%%
print(right)
#%%
print(left)

#%% Merge on common Col
pd.merge(left,right, on="col1", how="inner")
#%% Merge on common Col
pd.merge(left,right, on="col1", how="outer")
#%% Merge on common Col
pd.merge(left,right, on="col1", how="left")
#%% Merge on common Col
pd.merge(left,right, on="col1", how="right")

#%% Manipulate the DF - CONCAT - Same Cols DF
df1 = pd.DataFrame({'account_id': [1, 2, 3, 11382], 
                    'gender': ['female', 'male', 'female', 'male'], 
                    'age': [55, 25, 29, 39]})


df2 = pd.DataFrame({'account_id': [4, 5, 6, 7], 
                    'gender': ['female', 'male', 'female', 'male'], 
                    'age': [19, 28, 14, 15]})

pd.concat([df1, df2], ignore_index=True)
#%% Lets combine Heroes DF
df_powers
# df_marvel
hero=pd.merge(df_marvel, df_powers, left_on='name', right_on='hero_names', how="inner")
hero.head()

#%% Renaming Cols
hero.info(verbose=True)

#%%
hero.columns=hero.columns.str.lower()
#%%
hero.info(verbose=True)
#%% Renaming Cols
# Reassing since rename returns a new copy
hero=hero.rename(columns={'hero_names':'hero names'})
hero.info(verbose=True)
#%% Rename takes functions
hero=hero.rename(columns=str.upper)
hero.info(verbose=True)

#%% Re-assign since rename returns a new copy
hero=hero.rename(mapper=str.lower, axis=1)
hero.info(verbose=True)

#%% Selecting Columns 
hero["name"]
#%% select more than one col
hero[['name', 'gender']]
#%% Select by type
hero.select_dtypes(include="number")
hero.select_dtypes(exclude="number")
hero.select_dtypes(include=["int64","category"])

#%% Selecting Rows and Index 
hero.loc[0]
#%% 
hero.loc[[0,1]]
#%% 
hero.loc[0:4] # Inclusive both
#%% you can retrieve rows by setting the index to the desire col
hero_name = hero.set_index('name')
hero_name.index
hero_name.loc['Abomination']
#%%
hero_name.loc[['Weapon XI', 'Winter Soldier']]
#%%
hero_name.iloc[0]
hero_name.iloc[1:3] # Inclusive, Exclusive 
# %% Using filter
hero_name['alignment'] == 'bad' # you can use == on the selection to filter

# %% Using filter
hero_name['alignment'] == 'bad' # you can use == on the selection to filter
# %% Using filter to get all the cols
hero_name[hero_name['alignment'] == 'bad'] # you can use == on the selection to filter
# %% Using filter to get all the cols
hero_name.loc[hero_name['alignment'] == 'bad']
 # you can use == on the selection to filter
#%%
# The next one on iloc failed because we are returning (labels,values) not values
# hero_name.iloc[hero_name['alignment'] == 'bad']
hero_name.iloc[(hero_name['alignment'] == 'bad').values]

# %% Using more conditions

hero_name[(hero_name['alignment'] == 'bad') & (hero_name['height'] >= 200)] # you can use == on the selection to filter
# It must use bitwise operators (& | ~ ) and parenthesis 
# %% Using more conditions - isin
hero_name[hero_name['alignment'].isin(['bad'])] # you can use == on the selection to filter

#%% Selecting Rows and Cols

#df.loc[labels, cols] => Select using labels for rows and cols
# #df.iloc => Select using positions
hero.loc[0,:]
hero.loc[[0,3],:]
hero.loc[[0,3]]
hero.loc[0:3]

#%%
hero.loc[0,"race"]
#%%
hero.iloc[0,3]

#%% 
hero.loc[2:4,"race":"height"]
hero.loc[2:4,["race", "hair color","height"]]
#Using iloc - Notice the slice diff, last is exclusive in iloc
hero.iloc[2:5,3:6]
hero.iloc[[2,3,4,5],3:6]
hero.iloc[[2,3,4,5],[3,4,5]]


#%%  Modifying Values 
# Change Cell - "=" modify in place, no need to reassign 
hero.loc[2,'race'] = 'Unknown'
hero.loc[2,'race']
hero.iloc[2,3] = 'Human'
hero.iloc[2,3] 
hero.head()

# Modifying Col on certain value
hero.loc[hero['race']=='-', 'race' ] = 'Unknown' 
hero.loc[hero['race']=='Unknown']
# %%Copy row
hero.loc[1000] = hero.iloc[3]
hero.tail()
#%% Modify Col - form cm to feet
hero['height']=hero['height']*0.0328
hero.head()
#%% Selecting using vars
num_cols = hero.select_dtypes(include='number').columns
type(num_cols)
hero[num_cols]

#%% Generating new cols based on other cols
type((hero['weight']/hero['height']/3.28)**2)
# Since it returns a Series it will use the index for assignment
# Using = uses the index of the Series to assign values 
hero['bmi']=(hero['weight']/hero['height']/3.28)**2
hero.head()
#%% Copy
hero_copy = hero.copy()
hero_copy.info(verbose=True)

#%% Sorting
hero.sort_values(by="race")
# Viewing the largest or smallest values
hero.nlargest(n=10,columns="height")['height']
# %%
