#%% Cleaning Text
#%%
import pandas as pd
taxi = pd.read_csv('nyc_federal_taxi.csv')
# taxi.shape
#%%
taxi.info()
#%%
taxi.head()

#%% Inconsistent Capitalization
taxi['PU_Address'].head(10)
#%%
taxi['PU_Address'] =taxi['PU_Address'].str.lower() 
taxi['PU_Address'].head(10)
#%%
taxi['PU_Address'] =taxi['PU_Address'].str.strip()
taxi['PU_Address'].head(10)
#%% Find outliers
taxi['PU_Address_len'] =taxi['PU_Address'].str.len()
taxi['PU_Address_len'].head(10)
taxi['PU_Address_len'].hist(bins=50)
#%% 
taxi[['PU_Address','PU_Address_len']].nlargest(n=10, columns='PU_Address_len')
#%% Special long  strings
taxi.loc[97, 'PU_Address']
#%%
taxi.loc[73, 'PU_Address']
#%%
taxi.loc[209, 'PU_Address']
#%%
taxi.loc[203, 'PU_Address']
#%% Some address contains airport to pickup

# this access gives a warning when trying to use to update selected cols
taxi_airport = taxi[taxi['PU_Address'].str.contains('airport')]
# To fix use copy to create a Series rather than a VIEW
taxi_airport = taxi[taxi['PU_Address'].str.contains('airport')].copy()
#  or use the preferred access method loc to create a new Series
taxi_airport = taxi.loc[taxi['PU_Address'].str.contains('airport')]
# See more https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

#%%
taxi_airport['PU_Address'].value_counts()
#%%
taxi_airport['PU_Address'].str[:5]
# [-3:]
#  This one does not work
taxi_airport['PU_Address']=taxi_airport['PU_Address'].str.replace(' ny;', 'new york;')
taxi_airport['PU_Address']=taxi_airport['PU_Address'].str.replace(' nynew york;', 'new york;')

taxi_airport['PU_Address'].str[:20]
# taxi_airport['PU_Address']

#%%
taxi.loc[taxi['PU_Address'].str.startswith('best western')]
#%%
taxi.loc[taxi['PU_Address'].str.endswith('nj;')]['PU_Address']
# OR
taxi[taxi['PU_Address'].str.endswith('nj;')]['PU_Address']