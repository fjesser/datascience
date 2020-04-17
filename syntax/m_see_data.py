from datetime import date
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


# Load hotel data set from input folder
hotel_data = pd.read_csv("../input/hotel_bookings.csv")


def export_dataset_description_to_csv(dataset):
    '''
    Function takes description of dataset and saves it as csv
    Input:
      dataset: pd.dataFrame object
    Returns:
      nothing, saves csv-file
    '''
    described_data = dataset.describe(include="all")
    described_data.to_csv("../output/description.csv")


def print_occurence_of_object_types(dataset):
    '''
    Function prints how often each manifestation of non-numeric columns appears
    Input:
      dataset: pd.dataFrame object
    Returns:
      nothing, prints to console
    '''
    for variable in dataset.columns:
        if dataset[variable].dtype == 'object':
            print(dataset[variable].value_counts())


# print_occurence_of_object_types(hotel_data)

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


def convert_date_per_row(row):
    '''
    Function creates a date object by reading the year, month and date of arrival per row
    Input:
      dataset: a row of the hotel dataset as pd.Series
    Returns:
      dataset: a date object including the arrival date
    '''
    year = row['arrival_date_year']
    month = row['arrival_date_month']
    day = row['arrival_date_day_of_month']

    month = month.capitalize()
    months_string = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']
    months_numeric = [i for i in range(1, 13)]
    months = dict(zip(months_string, months_numeric))

    numeric_date = date(year, months[month], day)
    return(numeric_date)


''' My try to get the arrival_date as a date object. Uses apply and is thus really slow (seconds).
    For optimization, read this link: https://stackoverflow.com/questions/52673285/performance-of-pandas-apply-vs-np-vectorize-to-create-new-column-from-existing-c

    hotel_data['arrival_date'] = hotel_data.apply(convert_date, axis=1)
'''


def convert_date_in_dataset(dataset):
    dataset['arrival_date'] = dataset.apply(convert_date_per_row, axis=1)
    return(dataset)

# hotel_data['arrival_date'] = hotel_data.apply(convert_date, axis=1, args=(
# hotel_data['arrival_date_year'], hotel_data['arrival_date_month'], hotel_data['arrival_date_day_of_month']))


print(hotel_data.head())
