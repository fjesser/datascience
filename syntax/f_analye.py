# Felix hotel demand analysis

import datetime as dt
import pandas as pd
import numpy as np
import os

#save folder in variable
file_folder = os.path.dirname(__file__)

# load data
df = pd.read_csv(os.path.join(file_folder, "..", "input", "hotel_bookings.csv"))


# inspect
#df.info()  # structure in R
# df.index  # Zeilen ausgeben (besondere Python Art)
# df.columns  # Spalten ausgeben

print(df["hotel"].unique())
print(df["reservation_status"].value_counts())

print(df.columns)
#for variable in df.columns:
#    if df[variable].dtypes == "object":
#        print(df[variable].value_counts())


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

df.to_csv(os.path.join(file_folder, "..", "input", "hotel_bookings_FE.csv"))

print(df.loc[df["reservation_status"] == "Check-Out", ["arrival_date", "reservation_status", "reservation_status_date", "days_spent"]].head())
print(df.days_spent)
print(df.cost)
#print(df.reservation_status_date - df.arrival_date)
#print(df.info())
print(df.columns)
