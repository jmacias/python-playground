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

#%%
"""
PANDAS EXPORTING DATA 
"""
df_powers.to_pickle("hpower.pkl")
df_powers_pkl=pd.read_pickle("hpower.pkl")
# Keeps data types - pickle is python specific format
df_powers_pkl.dtypes
