import datetime 

current_datetime = datetime.datetime.now()

time_str = current_datetime.strftime('%Y/%m/%d')

print(time_str)
print(current_datetime.year) 