import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

date =[]
total = []
fig, ax = plt.subplots(figsize=(12,8))
pd.read_csv('C:/Users/user/Desktop/Covid_Data/covid_traffic.csv', sep=',',
                    usecols=['date','day_traffic','day_bus','day_subway'],
                    parse_dates=['date'],
                    encoding='utf-8'
               ).set_index('date').plot(ax=ax)
ax2 = ax.twinx()
pd.read_csv('C:/Users/user/Desktop/Covid_Data/covid_traffic.csv', sep=',',
                    usecols=['date','total_covid'],
                    parse_dates=['date'],
                    encoding='utf-8',
               ).set_index('date').plot(ax=ax2, color='deeppink')
plt.legend(loc='upper right')
plt.show()