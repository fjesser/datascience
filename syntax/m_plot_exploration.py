import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import m_see_data as mh

hotel_data = pd.read_csv("../input/hotel_bookings.csv")
# sns.set()
# p = sns.scatterplot(x='agent', y='adr', data=hotel_data)
# p.set(ylim=(0, 600))
# plt.show()

hotel_data_new = mh.fix_meal_manifestations(hotel_data)
print(hotel_data_new.head())
