"""
We will use Pandas for data manipulation
Loading Data - Diff Data Sources, examples in CSV (readCSV)and Excel(readExcel)
"""
#%%
import pandas as pd

#%%

df_powers=pd.read_csv('superhero_powers.csv')
df_dc=pd.read_excel('superhero_info.xlsx', sheet_name="DC Comics")
df_marvel=pd.read_excel('superhero_info.xlsx', sheet_name="Marvel Comics")
