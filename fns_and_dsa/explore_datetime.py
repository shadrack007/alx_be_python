from datetime import datetime, timedelta

def display_current_datetime():
    current_date_time = datetime.now()
    print(f'Current date and time: {current_date_time}')
    return current_date_time

def calculate_future_date():
    current_date_time = display_current_datetime()
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    print(f'Future date: {current_date_time + timedelta(days=number_of_days)}')





