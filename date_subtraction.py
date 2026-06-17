import datetime

def calculate_previous_date(pdate, days):
    new_date = datetime.datetime.strptime(pdate,'%Y-%m-%d') + datetime.timedelta(days = days)
    return new_date.strftime('%Y-%m-%d')

print(calculate_previous_date('2026-06-17', 10))