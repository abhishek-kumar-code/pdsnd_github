"""
@author Kumar, Abhishek
Date Modified: 05/23/2021
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    """"""""
    
    """Messeges to genrate filters"""
    welcome_messege = 'Hello! Let\'s explore some US bikeshare data!\n'
    enter_city_name_messege = 'Which city would you like to filter by? Chicago, New York City or Washington? '
    filter_definition_messege = '\nWould you like to filter the data by - \n1. Month\n2. Day\n3. Both\n4. No Filter\n\nPlease choose the appropriate filter name.\nNote: Incorrect filter name will result as \'no filter selected\' by the user.\n'
    enter_filter_messege = 'Desired filter (e.g: Month, Day, Both or No Filter): '
    enter_month_name_messege = 'Enter month name (e.g: january, february, march, april, may or june): '
    enter_day_name_messege = 'Enter day of the week (e.g: monday, tuesday, wednesday, thursday, friday, saturday, sunday): '
    exception_messege = '\nWarning! That is not a valid input.\n'
    warning_city_name_messege = '\nWarning! Invalid city name. Select city name from the following cities only - Chicago, New York City or Washington.'    
    warning_month_name_messege = '\nWarning! Invalid month name. Select month name from the following months only - january, february, march, april, may or june'
    warning_day_name_messege = '\nWarning! Invalid day name. Select day name from the following days only - monday, tuesday, wednesday, thursday, friday, saturday, sunday'
    """"""""
    
    """City, Month and Day List"""
    city_list = ['chicago', 'new york city', 'washington']
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    """"""""
    
    print(welcome_messege)
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs  
    while True:
        try:
            city = input(enter_city_name_messege)
            break
        except:
            print(exception_messege)
            
    while city.lower() not in city_list:
        while True:
            try: 
                print(warning_city_name_messege)
                city = input(enter_city_name_messege)
                break
            except:
                print(exception_messege)
                
    print(filter_definition_messege)
    while True:
        try:
            filter_choice = input(enter_filter_messege)
            break
        except:
            print(exception_messege)
    while True:         
        if filter_choice.lower() == 'month':
            # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                try:
                    month = input(enter_month_name_messege) 
                    break
                except:
                    print(exception_messege)
            while month.lower() not in month_list:
                while True:
                    try: 
                        print(warning_month_name_messege)
                        month = input(enter_month_name_messege) 
                        break
                    except:
                        print(exception_messege)
            day = 'all'
            break
        
        elif filter_choice.lower() == 'day':
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
            while True:
                try:
                    day = input(enter_day_name_messege)
                    break
                except:
                    print(exception_messege)
            while day.lower() not in day_list:
                while True:
                    try: 
                        print(warning_day_name_messege)
                        day = input(enter_day_name_messege) 
                        break
                    except:
                        print(exception_messege)
            month = 'all'
            break
        
        elif filter_choice.lower() == 'both':
            # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                try:
                    month = input(enter_month_name_messege)
                    break
                except:
                    print(exception_messege)
            while month.lower() not in month_list:
                while True:
                    try: 
                        print(warning_month_name_messege)
                        month = input(enter_month_name_messege) 
                        break
                    except:
                        print(exception_messege)
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                try:
                    day = input(enter_day_name_messege)
                    break
                except:
                    print(exception_messege)
            while day.lower() not in day_list:
                while True:
                    try: 
                        print(warning_day_name_messege)
                        day = input(enter_day_name_messege) 
                        break
                    except:
                        print(exception_messege)
            break
        
        else:
            month = 'all'
            day = 'all'
            break
 

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
            
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def raw_data(df):
    """Displays raw data if the user desires to see."""
    row_display_messege = '\nWould you like to see the first 5 rows of the filtered data? Enter yes or no.\n'
    exception_messege = '\nWarning! That is not a valid input.\n'
    index = 0
    while True:
        try:
            restart = input(row_display_messege)
            if restart.lower() == 'yes' and index+5 < df.shape[0]:
                print(df.iloc[index:index+5])
                index += 5
            else:
                break
        except: 
            print(exception_messege)
            
    print('-'*40)
    return df            
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n#1 POPULAR TIMES OF TRAVEL\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    day_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of the week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', month_dict[popular_month])
    
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', day_dict[popular_day_of_week])
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n#2 POPULAR STATIONS AND TRIP\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Frequent Start Station:', popular_start_station)
    print('Count:', len(df[df['Start Station'] == popular_start_station]))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('\nMost Frequent End Station:', popular_end_station)
    print('Count:', len(df[df['End Station'] == popular_end_station]))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Common Trip from Start to End with Frequency:')
    print(df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n#3 TRIP DURATION\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    total_duration_structure = time.gmtime(total_duration)
    total_travel_time = time.strftime("%H:%M:%S", total_duration_structure)
    print('Total Travel Time: ', total_travel_time, 'HH:MM:SS')

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    average_duration_structure = time.gmtime(average_duration)
    average_travel_time = time.strftime("%H:%M:%S", average_duration_structure)
    print('\nAverage Travel Time: ', average_travel_time, 'HH:MM:SS')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n#4 USER INFO\nCalculating User Stats...\n')
    start_time = time.time()
       
    # TO DO: Display counts of user types
    print('Count of each User type:')
    print(df['User Type'].value_counts(dropna=False))
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nCount of each Gender type:')
        print(df['Gender'].value_counts(dropna=False))

   
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nBirth Year Statistics:')
        print(df['Birth Year'].value_counts(sort=True).head(1))
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
#         print(df)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
