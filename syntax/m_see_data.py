import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

hotel_data = pd.read_csv("../input/hotel_bookings.csv")

# described_data = hotel_data.describe()
#
# described_data.to_csv("../output/description.csv")

# print(hotel_data.describe(include="all"))

for variable in hotel_data.columns:
    if hotel_data[variable].dtype == 'object':
        print(hotel_data[variable].value_counts())
