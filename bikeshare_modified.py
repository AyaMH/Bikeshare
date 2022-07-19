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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago', 'new york city', 'washington']
        city = input("please choose a city from: Chicago, New york city, Washington: ").lower()
        if city in cities:
            break
        else:
            print('You entered an invalid response')

    # TO DO: get user input for month (all, january, february, ... , june) 
    while True:
        months= ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("please choose a month: January, February, March, April, May, June. or All to review all months: ").lower()  
        if month in months:
            break
        else:
            print('You entered an invalid response')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
        day = input("please select a weekday: Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday. or All to review all days: ").lower() 
        if day in days:
            break
        else:
            print('You entered an invalid response')

    print('-'*40)
    print('You chose as a city : ' + city + ' and as a month: ' + month + ' and as a day: '+ day) 
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
       df = df[df['month'] == month]
   
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
   
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        most_common_month =  df['month'].mode()[0]
        print('Most common month is: ' + months[most_common_month - 1].title())

    # TO DO: display the most common day of week
    if day == 'all':
        most_common_day = df['day_of_week'].mode()[0]
        print('Most common Day of week is: ' + most_common_day)
    
    # TO DO: display the most common start hour
    most_common_hour =  df['Start Time'].mode()[0]
   
    print('Most common Start hour: ' + most_common_hour.strftime("%H:%M:%S")) 

    print("\nThais took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station =  df['Start Station'].mode()[0]
    print('Most common start station is: ' + most_common_start_station.title())

    # TO DO: display most commonly used end station
    most_common_end_station =  df['End Station'].mode()[0]
    print('Most common end station is: ' + most_common_end_station.title()) 

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combined = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip are from : ' + most_common_combined[0].title() + ' to: ' +               most_common_combined[1].title() )    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60
    print('Total travel time is (in minutes): ' + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() /60
    print('Mean travel time is (in minutes): ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
 
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(gender)
    # TO DO: Display the earliest, most recent, and most common birth year 
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest, Most recent and Most common year of birth of users are: {0}, {1}, {2} respectively.'.format(earliest,most_recent,most_common))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    show_data = False
    view_data = input("Would you like to view the first 5 rows of individual trip data? Enter yes or no?: ")
    if view_data.lower() == 'yes':
       show_data = True 
        
    start_loc = 0
    total_rows = df.shape[0]
    print("totalRows:" + str(total_rows))
    
    while (show_data):
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        if start_loc +1 >= total_rows:
             print("no more rows to show.")
             show_data = False   
         
        else:
            view_display = input("Do you wish to show the next 5 rows?: ").lower()
            if view_display.lower() != 'yes':
                show_data = False
        
    
def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
 #count = load_data('washington','may','all').shape[0]
    #print("count:" + str(count))
    #the reason for the error in loading data was the incorrect input of 'mai' instead of 'may'
