from datetime import datetime, timedelta

current_date_time = datetime.now()

number_of_days = int(input('Enter the number of days to add to the current date: '))

print(f'Current date and time: {current_date_time}')
print(f'Future date: {current_date_time + timedelta(days=number_of_days)}')