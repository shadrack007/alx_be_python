from datetime import datetime, timedelta

def display_current_datetime():
    current_date_time = datetime.now()
    print(f'Current date and time: {current_date_time.strftime("%Y-%m-%d %H:%M:%S")}')


def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = current_date + timedelta(days=number_of_days)
    print(f'Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}')





