import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import m_see_data as mh
import datetime as dt


hotel_data = pd.read_csv("../input/hotel_bookings.csv")
# hotel_data_new = mh.get_final_dataset()

outdict = {'categorical':[], 'numeric':[]}

for column in hotel_data.columns:
    if column == 'reservation_status' or column == 'is_canceled':
        pass
    elif hotel_data[column].dtype != 'int64':
        outdict['categorical'].append(column)
    else:
        outdict['numeric'].append(column)
        
# number_of_plots = len(outdict['numeric']) + len(outdict['categorical'])
    
# Rows, columns
fig, sub = plt.subplots(6,5)

sns.set()
sns.set_style('whitegrid')
for variable in outdict['categorical']:
    sns.countplot(x = variable, hue = 'reservation_status', data=hotel_data)
# first_plot = sns.countplot(x = 'deposit_type', hue = 'reservation_status', data=hotel_data_new, ax=sub[0])
# second_plot = sns.countplot(x = 'is_canceled', hue = 'reservation_status', data=hotel_data_new, ax=sub[1])
plt.show()

# nr_plots = len(hotel_data_new.columns)

# for variable in hotel_data_new.columns:
    


# Plot test...
# x = (dt.datetime(2015, 6, 1), dt.datetime(2017, 10, 1))
# sns.set()
# p = sns.scatterplot(x='arrival_date', y='cost', data=hotel_data_new, size = 0.5)
# p.set(xlim=x)
# p.set(ylim=(0, 3000))
# plt.show()


# print(hotel_data_new.head())
