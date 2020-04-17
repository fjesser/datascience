# Felix hotel demand analysis
import pandas as pd


pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)

# load data
df = pd.read_csv('./../input/hotel_bookings.csv')

# inspect
# df.info()  # structure in R
# df.index  # Zeilen ausgeben (besondere Python Art)
# df.columns  # Spalten ausgeben

print(df["hotel"].unique())
print(df["reservation_status"].value_counts())

for variable in df.columns:
    if df[variable].dtypes == "object":
        print(df[variable].value_counts())

# another comment

print(df.columns)

# create arrival date
#df["arrival_date"] = date(df.arrival_date_year, df.arrival_date_month, df.arrival_date_day_of_month)


#print(df.describe(include='all'))


print(type(df["arrival_date_year"]))
print(type(df.arrival_date_year))

#print(df[['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month']].head())
#print(datetime.strptime("18March2009", "%d%B%Y").date())
#date.strptime()
print(df.arrival_date_month.unique())

print(str(df.arrival_date_year.head()) + df.arrival_date_month.head())



df['arrival_date'] = df.arrival_date_year.astype(str) + df.arrival_date_month + df.arrival_date_day_of_month.astype(str)
df['arrival_date'] = pd.to_datetime(df.arrival_date, format="%Y%B%d")


df['arrival_date'] = (df.arrival_date_year.astype(str) + df.arrival_date_month + df.arrival_date_day_of_month.astype(str)
                      .pipe(pd.to_datetime, format="%Y%B%d"))
print(df.arrival_date.head())
#df['arrival_date'] = pd.to_datetime(df.arrival_date, format="%Y%B%d")
print("hhhhhhhh")
#print(str(df.arrival_date_year.head()) + df.arrival_date_month.head() + df.arrival_date.head())
print(df.arrival_date.head())
#pd.to_datetime()
#print(df.arrival_date_day_of_month.astype(str).str.pad(width=2, side='left', fillchar='0'))