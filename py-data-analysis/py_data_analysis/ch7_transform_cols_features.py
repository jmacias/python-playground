#%% Transforming 
#%% Datetime 
from warnings import catch_warnings
import pandas as pd
air = pd.read_csv('air_quality.csv')
air.info()
#%%
air.head()
#%%
air.info()
#%%
#  0   date_time  95685 non-null  object 
try:
    air['date_time'].dt.year
except AttributeError as e:
    print(e)
    print('Date time is Object - we need to transdorm to date obj')

#%% 
air['date_time']=pd.to_datetime(air['date_time'])
#  Now we can access the properties of the date
air['date_time'].dt.year

#%% Adding Cols from the date
air['year']= air['date_time'].dt.year
air['month']= air['date_time'].dt.month
air['day']= air['date_time'].dt.day
#%%
air.info()
#%% Find Max Min Date 
air['date_time'].max()
air['date_time'].min ()
#%% The Range of days between
range=air['date_time'].max() - air['date_time'].min ()
# pd.Timedelta(days=10)
range/pd.Timedelta(days=365) # Range in Years

#% Using Dates 
air['time_until_2022'] = pd.Timestamp('2022/01/01') -air['date_time']
air.head()
air['time_until_2022_in_days'] = air['time_until_2022']/pd.Timedelta(days=1)
air.head()

#% Using Dates to Filter
air['date_time']<pd.Timestamp('2016/01/01')
air[air['date_time']<pd.Timestamp('2016/01/01')]

#%% Binning - Transform num col to categorical cols 
# GRoup continues num data into bins