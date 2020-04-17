# Analysis of hotel demand data set
def fix_meal_manifestations(dataset):
    '''
    Function adds undefined meals to SC meals (according to kaggle, Undefined/SC - no meal)
    Input:
      dataset: pd.dataFrame object
    Returns:
      dataset: pd.dataFrame object in which SC = Undefined + SC from input
    '''
    dataset['meal'] = hotel_data['meal'].replace(to_replace="Undefined", value="SC")
    return(dataset)


df['arrival_date'] = df.arrival_date_year.astype(
    str) + df.arrival_date_month + df.arrival_date_day_of_month.astype(str)
df['arrival_date'] = pd.to_datetime(df.arrival_date, format="%Y%B%d")
