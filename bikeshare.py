import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    try:
        city = input('Would you like to see data for Chicago, New york or Washington?: ')
        while city not in(CITY_DATA.keys()):
            print('you\'ve given invalid city name!.choose only between Chicago, New york or Washington.')
            city = input('Would you like to see data for Chicago, New york or Washington?: ')
    except Exception as e:
        print("Exception occurred: {}".format(e))

    try:
        month = input('Choose a month from january to june to filter the data by month, type "all" if no filter is needed: ')
        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('you\'ve given invalid month! try again')
            month = input('Choose a month from january to june to filter the data by month, type "all" if no filter is needed: ')
    except Exception as e:
        print("Exception occurred: {}".format(e))

    try:
        day = input('Choose a day of the week to filter the data by day or type "all" for no filter at all: ')
        while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print('Not a valid day! try again')
            day = input('Choose a day of the week to filter the data by day or type "all" for no filter at all: ')
    except Exception as e:
        print("Exception occurred: {}".format(e))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):


    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['Start Time'].dt.month.mode()[0]
    print('Most common month:', popular_month)

    popular_day = df['day_of_week'].mode()[0]
    print('Most common day:', popular_day)

    popular_start_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station)

    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station)

    df['Start-End Station'] = df['Start Station'] + " - " +  df['End Station']
    most_frequent_combination = df['Start-End Station'].mode()[0]
    print('Most frequent combination:', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Time Difference'] = df['End Time'] - df['Start Time']
    print('Total travel time:', df['Time Difference'].sum())

    print('Mean travel time:', df['Time Difference'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(df['User Type'].value_counts())

    try:
        if 'Gender' in df:
            print(df['Gender'].value_counts())
        else:
            print('Gender: Data not available')
    except Exception as e:
        print("Exception occurred: {}".format(e))

    try:
        if 'Birth Year' in df:
            print('earliest_year:', df['Birth Year'].min())
            print('most_recent_year:', df['Birth Year'].max())
            print('most_common_year:', df['Birth Year'].mode())
        else:
            print('Birth_Year: Data not available')
    except Exception as e:
        print("Exception occurred: {}".format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    x = 0
    y = 5
    while True:
        answer = input('Would you like to see the raw data?: ')
        if answer == 'yes':
            print(df.iloc[x:y])
            x += 5
            y += 5
            while True:
                more = input('Would you like to see more data?: ')
                if more == 'yes':
                    print(df.iloc[x:y])
                    x += 5
                    y += 5
                elif more == 'no':
                    break
                if more not in ['yes', 'no']:
                    print('Wrong input! answer can be only yes or no')

        elif answer == 'no':
                break
        if answer not in ['yes', 'no']:
                print('Wrong input! answer can be only yes or no')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
