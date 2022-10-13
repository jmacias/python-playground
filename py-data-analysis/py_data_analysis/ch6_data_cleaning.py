"""
Data Cleaning

Detecting and Correcting data
"""
#%%
from unicodedata import numeric
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
# wdi_clean = wdi.copy()
wdi.to_pickle('wdi_clean.pkl')
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
# By rows
wdi.dropna() # Drop rows w/ any missing values
wdi.dropna(thresh=18) # Drop rows One missing value 
#By cols
wdi.dropna(axis=1) # Drop Col w/ missing values
wdi.dropna(axis=1, thresh=300) # Drop Col w/ more than 300 missing values

#%% Tackling Missing Data - Imputing Constant
# Filling the wholes w/ constants
# Let's get the Index Series for Num and not num
cat_cols = wdi.select_dtypes(exclude='number').columns
num_cols = wdi.select_dtypes(include='number').columns
num_cols
# Use the series index to filter
wdi[num_cols] = wdi[num_cols].fillna(-999)
wdi[cat_cols] = wdi[cat_cols].fillna('MISSING')
wdi['alcohol_consumption_per_capita'].value_counts(dropna=False)
# cat_cols = wdi_clean.select_dtypes(exclude='number').columns
# num_cols = wdi_clean.select_dtypes(include='number').columns

# The Series w/ index for num col is used to apply the mean to 
# The missing values
# wdi_clean[num_cols] = wdi_clean[num_cols].fillna(wdi_clean[num_cols].mean())

# you can use this to use the most common value to fill Cat cols
wdi[cat_cols].describe().loc['top'] 

# Filling w/ machine learning scikit-learn SimpleImputer
# Replace missing values using a descriptive statistic 
# (e.g. mean, median, or most frequent) along each column,
#  or using a constant value.

# RELOAD CLEAN DS
wdi = pd.read_pickle('wdi_clean.pkl')
wdi.shape

#%% Tackling Missing Data - Imputing with Model
# When missing values an be inferred from others cols
#  scikit-learn Iterative Imputer
#    Models each col w/ missing vals as functions of other cols

#%% Handle Outliers
# Unusual Values 
# Reasons - Typos, Input Errors, Mix Categories

# How to find outliers? Statistical Methods - Inter quartile Range
wdi.hist(figsize=(20,20))
# Try to catch  skews Histograms
#%%
wdi['population'].hist(figsize=(20,20), bins=50)
#%%
wdi[['population', 'country_name']].sort_values(by='population', ascending=False) 
# Values w/ World as country name
#  Different Categories
#%% is_region is categorical - we can remove Regions from countries
wdi.columns
wdi=wdi[wdi['is_region']==0]
wdi.shape
wdi['population'].hist(figsize=(20,20), bins=50)
# Still one outlier but less
#%%
wdi.boxplot('population')
#%% Use Inter quartile to remove
#  Q1 -1.5 * IQR or Q3 + 1.5 * IQR
q1=wdi['population'].quantile(0.25)
q3= wdi['population'].quantile(0.75)

q3
#  Depends on the data you can use 99 quantile 
# Use Keep Drop or Capping/flooring
#%%
wdi['population'].describe()
