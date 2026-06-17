import datetime

def get_date_range(begin_date, end_date):
    begin_datetime = datetime.datetime.strptime(begin_date, '%Y-%m-%d') 
    end_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d') 

    current_date = begin_datetime
    date_lst = []

    while current_date <= end_datetime:
        current_time_str = current_date.strftime('%Y-%m-%d')
        date_lst.append(current_time_str)
        current_date += datetime.timedelta(days=1)
    return date_lst


print(get_date_range('2026-06-01', '2026-06-05'))