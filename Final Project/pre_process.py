import pandas as pd
from datetime import timedelta, datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
u_data = pd.read_csv("201601.txt", sep=" ")
u_data = u_data.loc[:,['rent_sta', 'rent_sta_sarea', 'rent_time']]
u_data['quantity'] = 1
def resampler(data):
    n_data = data.set_index(keys='rent_time')
    n_data.index = pd.to_datetime(n_data.index)
    n_data = n_data.groupby(['rent_sta', 'rent_sta_sarea', pd.Grouper(freq='H')]).sum()
    return n_data

def expand_time_range(data, time_range):
    temp = data\
        .reset_index()\
        .set_index(keys='rent_time')\
        .reindex(time_range)

    data = temp['quantity'].reset_index().fillna(0)
    return data

sta_lst = u_data.iloc[:,0].unique()
sta = sta_lst[0] # change staion here
sta_data = resampler(u_data.loc[u_data.rent_sta == sta,:])
time_range = pd.date_range(start='2016-01-01', end='2016-01-31', freq='H')

sta_data = expand_time_range(sta_data, time_range)

sta_data['weekday'] = sta_data['index'].apply(lambda x: x.dayofweek)
sta_data['weekday'] = sta_data['weekday'].apply(lambda x: 1 if x <=5 else 0)
file = /sta + ".csv"
pd.DataFrame.to_csv(sta_data, file, index=False)

plt.plot(sta_data.index, sta_data.quantity)


