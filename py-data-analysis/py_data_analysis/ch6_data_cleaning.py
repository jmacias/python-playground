"""
Data Cleaning

Detecting and Correcting data
"""
#%%
import pandas as pd
#%% Removing Unnecessary cols and rows
wdi  = pd.read_csv("world_development_indicators.csv")
wdi.info()

#%% Look at possible duplicated info
wdi[["country_name","Country Name","Country Code","planet"]].head()
#%% Lets see uniqueness 
wdi.nunique()
#%%
wdi['planet'].value_counts()

#%%
wdi['planet'].value_counts(normalize=True)

#% Checking if 2 cols have the same values
wdi[wdi['country_name'] != wdi['Country Name']]
wdi['country_name'].compare(wdi['Country Name'])
#%% Checking unique combinations of 2 cols
wdi[['country_name','Country Name']].value_counts()
#%% We have duplicate info
wdi=wdi.drop(columns=['Country Name',"Country Code",'planet'])
#%% We have duplicate info
wdi.info()

#%% Duplicate Rows

wdi.duplicated() # Boleans Series using to filter

#%% Remove Duplicates
wdi[wdi.duplicated()]
wdi = wdi.drop_duplicates(ignore_index=True)
wdi.shape

#%% MISSING DATA
"""
MISSING DATA 
* No data in a col in a row
* Missing at Random
* Missing w/ a Reason
"""

#%%
wdi.info() # Any col w/ missing data will have less count than the entries

#%%
wdi['alcohol_consumption_per_capita'] # all NaN are missing values
# read_csv can specify missing values, lets say 999 represent a missing value
# you can specify that
#%%
type(wdi.describe().T)
wdi.describe().T.loc['alcohol_consumption_per_capita']

#%% Get the sum of the NA values per column
wdi.isna().sum()
#%%
wdi['alcohol_consumption_per_capita'].value_counts(dropna=False)

#%% Lets find missing col by row
num_missing_by_row=wdi.isna().sum(axis=1)
(num_missing_by_row>0).sum()
#% Rows w/ missing value
wdi[num_missing_by_row>0]

#%% Tackling Missing Data - Dropping 

