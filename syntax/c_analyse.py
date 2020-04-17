# Analysis of hotel demand data set
df['arrival_date'] = df.arrival_date_year.astype(str) + df.arrival_date_month + df.arrival_date_day_of_month.astype(str)
df['arrival_date'] = pd.to_datetime(df.arrival_date, format="%Y%B%d")
