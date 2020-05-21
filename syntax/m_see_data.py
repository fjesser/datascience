import datetime as dt
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


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


def fix_meal_manifestations(dataset):
    '''
    Function adds undefined meals to SC meals (according to kaggle, Undefined/SC - no meal)
    Input:
      dataset: pd.dataFrame object
    Returns:
      dataset: pd.dataFrame object in which SC = Undefined + SC from input
    '''
    dataset['meal'] = dataset['meal'].replace(to_replace="Undefined", value="SC")
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
    '''
    This function is taken from Felix; my try is commented out
    '''
    dataset['arrival_date'] = ((dataset.arrival_date_year.astype(str) +
                                dataset.arrival_date_month +
                                dataset.arrival_date_day_of_month.astype(str)
                                )
                               .pipe(pd.to_datetime, format="%Y%B%d")
                               )

    # dataset['arrival_date'] = dataset.apply(convert_date_per_row, axis=1)
    return(dataset)

# hotel_data['arrival_date'] = hotel_data.apply(convert_date, axis=1, args=(
# hotel_data['arrival_date_year'], hotel_data['arrival_date_month'], hotel_data['arrival_date_day_of_month']))


def create_days_spent_column(dataset):
    '''
    Both reservation_status_date and arrival_date have to be dateobjects!
    TODO: Write a unit test for it and convert if needed
    '''
    dataset['reservation_status_date'] = pd.to_datetime(dataset['reservation_status_date'])
    dataset['days_spent'] = np.where(dataset['reservation_status'] == 'Check-Out',
                                     (dataset['reservation_status_date'] - dataset['arrival_date']).dt.days, np.nan)
    return(dataset)

    # hotel_data['arrival_date'] = pd.to_datetime(hotel_data['arrival_date'])


def create_cost_column(dataset):
    '''
    Create a cost value that is the average daily rate times the total days days_spent
    '''
    dataset['cost'] = np.where(dataset['reservation_status'] == 'Check-Out',
                               dataset['adr'] * dataset['days_spent'], dataset['adr'])
    return(dataset)

def set_noshows_to_na(dataset):
    '''
    Set occurences of "No-Show" in reservation_status column to NA
    '''
    dataset['reservation_status'] = np.where(dataset['reservation_status'] == 'No-Show', np.nan, dataset['reservation_status'])
    return(dataset)


def get_final_dataset():
    '''
    Load the hotel dataset and prepare it for plotting
    Input: nothing
    Returns: pd.dataFrame object that contains the hotel data in tidy format and
    with new columns for the arrival_date, total days spent and cost for the stay
    Unnecessary columns are deleted
    '''
    # Load hotel data set from input folder
    dataset = pd.read_csv("../input/hotel_bookings.csv")

    # Add new columns
    dataset = convert_date_in_dataset(dataset)
    dataset = create_days_spent_column(dataset)
    dataset = create_cost_column(dataset)
    dataset = fix_meal_manifestations(dataset)
    dataset = set_noshows_to_na(dataset)

    # Delete now Unnecessary columns
    dataset.drop(['arrival_date_year', 'arrival_date_month',
                  'arrival_date_day_of_month', 'adr', 'reservation_status_date'], axis=1)

    return(dataset)


def write_final_dataset(dataset):
    '''
    Create a csv-file with the final dataset, that was curated
    '''
    dataset.to_csv("../input/hotel_bookings_mh.csv")


if __name__ == '__main__':
    hotel_data = get_final_dataset()
    write_final_dataset(hotel_data)
