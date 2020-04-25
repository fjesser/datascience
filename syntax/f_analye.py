# Felix hotel demand analysis
import pandas as pd
import numpy as np

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)

# load data
df = pd.read_csv('./../input/hotel_bookings.csv')

# inspect
df.info()  # structure in R
# df.index  # Zeilen ausgeben (besondere Python Art)
# df.columns  # Spalten ausgeben

print(df["hotel"].unique())
print(df["reservation_status"].value_counts())

print(df.columns)
for variable in df.columns:
    if df[variable].dtypes == "object":
        print(df[variable].value_counts())


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

# new arrival date variable in date format
df['arrival_date'] = ((df.arrival_date_year.astype(str) +
                       df.arrival_date_month +
                       df.arrival_date_day_of_month.astype(str)
                       )
                      .pipe(pd.to_datetime, format="%Y%B%d")
                      )

df['days_spent'] = np.where(df['reservation_status'] == "Check-Out",
                            df['reservation_status_date'] - df['arrival_date'],
                            np.nan)




print(df.loc[df["reservation_status"] == "Check-Out", ["arrival_date", "reservation_status", "reservation_status_date", "days_spent"]].head())
#print(df.reservation_status_date - df.arrival_date)
#print(df.info())
#print(df.columns)
