# Felix hotel demand analysis
import pandas as pd
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)

# load data
df = pd.read_csv('./../input/hotel_bookings.csv')

#inspect
#df.info()  # structure in R
# df.index  # Zeilen ausgeben (besondere Python Art)
# df.columns  # Spalten ausgeben

print(df["hotel"].unique())
print(df["reservation_status"].value_counts())

for variable in df.columns:
    if df[variable].dtypes == "object":
        print(df[variable].value_counts())

#another comment





#print(df.describe(include='all'))


