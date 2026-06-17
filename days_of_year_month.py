import calendar

year = int(input('Enter the year: '))
month = int(input('Enter the month: '))

first_weekday, num_days = calendar.monthrange(year, month)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(weekdays[first_weekday])