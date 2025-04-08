'''importing required libraries'''
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please Select a City to analyze...[chicago, new york, washington] ')
        city = city.lower()
        if city in CITY_DATA:
            break
        else:
            print('City choosen is not valid try again...')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
            month = input('Please select a month to analyze! ')
            month = month.lower()
            if month in months:
                break
            else:
                print('Please type month to analyze or all to view all. ')
            
          
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ['all', 'monday','tuesday','wednesday','thursday', 'friday','saturday','sunday']
    while True:
        day = input('Please select a day of the week or type all to view all. ')
        day = day.lower()
        if day in day_of_week:
            break
        else:
            print('Please choose a day of the week or type all to view all days. ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
 
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
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
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    
    print('The Most common month is ',months[common_month-1])
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is ',common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common Start Station ',common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station. ',common_end)
    # TO DO: display most frequent combination of start station and end station trip
    common_both = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most common trip from start to end is ', common_both)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total Travel Time is {} Hours, {} Minutes, and {} Seconds'.format(hour, minute, second))
 

    # TO DO: display mean travel time
    average_travel_duration = round(df['Trip Duration'].mean())
    mins, secs = divmod(average_travel_duration, 60)
    if mins> 60:
        hour, mins = divmod(mins, 60)
        print('The average time is {} Hours, {} Minutes, and {} seconds.'.format(hour, mins, secs))
    else:
        print('The average time is {} Minutes and {} Seconds.'.format(mins, secs))
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_types= df['User Type'].value_counts()
    print('Count of Each user type: \n', count_of_types)
    # TO DO: Display counts of gender
    try:
        count_of_gender = df['Gender'].value_counts()
        print('Gender Distribution \n',count_of_gender)
    except:
        print('Choosen city does not have gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('The Earliest Person born was in the year ', earliest)
        most_recent_year = df['Birth Year'].max()
        print('The most recent Birth year was on ', most_recent_year)
        most_common_year = df['Birth Year'].mode() 
        print('The most common birth year is ', most_common_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print('The choosen city does not have Birth Year')
    print('-'*40)
    
def display_raw_data (df):
    """5 rows will be displayed and increased"""
    user_typed = input('Press enter to display 5 rows of raw data, or type exit to leave ')
    x = 0
    while (user_typed!= 'exit'):
        x = x+5
        print(df.head(x))
        user_typed = input('Press enter to display 5 rows of raw data, or type exit to leave ')
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
