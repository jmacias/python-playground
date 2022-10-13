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
taxi_airport = taxi[taxi['PU_Address'].str.contains('airport')]
#%%
taxi_airport['PU_Address'].value_counts()
#%%
taxi_airport['PU_Address'].str[:5]
# [-3:]
#  This one does not work
taxi_airport['PU_Address']=taxi_airport.loc['PU_Address'].str.replace(' ny;', 'new york;')

taxi_airport['PU_Address'].str[:20]
# taxi_airport['PU_Address']

#%%
taxi.loc[taxi['PU_Address'].str.startswith('best western')]
#%%
taxi.loc[taxi['PU_Address'].str.endswith('nj;')]['PU_Address']
# OR
taxi[taxi['PU_Address'].str.endswith('nj;')]['PU_Address']

