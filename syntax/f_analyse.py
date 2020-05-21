# Felix hotel demand analysis

#%% Preparations

# import modules
#import datetime as dt
import pandas as pd
import numpy as np
import os

#save folder in variablex
file_folder = os.path.dirname(__file__)

# load data
df = pd.read_csv(os.path.join(file_folder, "..", "input", "hotel_bookings.csv"))


#%% Inspect data
# inspect (don't forget print)

#print(df.info())  # structure in R
#print(df.index)  # gives rows (special python style)
#print(df.columns)  # gives columns

#print(df.columns) #print column names

# show unique values of hotel column
#print(df["hotel"].unique())

# give frequencies of reservation_status
#print(df["reservation_status"].value_counts())

# subset 
#print(df.loc[df["reservation_status"] == "Check-Out", 
#             ["arrival_date", "reservation_status", 
#              "reservation_status_date", "days_spent"]].head())


#for variable in df.columns:
#    if df[variable].dtypes == "object":
#        print(df[variable].value_counts())


#%% Data transformation

# transform reservation_status_date to datetime object
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

# new arrival date variable in date format
df['arrival_date'] = ((df.arrival_date_year.astype(str) +
                       df.arrival_date_month +
                       df.arrival_date_day_of_month.astype(str)
                       )
                      .pipe(pd.to_datetime, format="%Y%B%d")
                      )


df['days_spent'] = np.where(df['reservation_status'] == "Check-Out",
                            (df['reservation_status_date'] - df['arrival_date']).dt.days, # also possible: / np.timedelta64(1, 'D'),
                            np.nan)


df['cost'] = np.where(df['reservation_status'] == "Check-Out",
                      df['adr'] * df['days_spent'],
                      df['adr'])

# drop columns starting with arrival_date_
df = df.loc[:, ~df.columns.str.startswith('arrival_date_')]



#%% Save transformed data 
#
df.to_csv(os.path.join(file_folder, "..", "input", "hotel_bookings_FE.csv"))



print(df.days_spent)
print(df.cost)
print(df.columns)
