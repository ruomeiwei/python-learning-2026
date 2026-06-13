def is_leap_year(year):
    if year%100 != 0 and year%4 == 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

def day_of_year(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[1] = 29
    
    day_count = sum(days_in_month[:month-1]) + day 

    return day_count 

year = int(input('Enter the year: '))
month = int(input('Enter the month: '))
day = int(input('Enter the day: '))

print(day_of_year(year, month, day))