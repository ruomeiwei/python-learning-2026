import datetime

unix_time = 1620747224 

datetime_object = datetime.datetime.fromtimestamp(unix_time)

print(datetime_object, type(datetime_object))

datetime_str = datetime_object.strftime('%Y/%m/%d %H:%M:%S')

print(datetime_str, type(datetime_str))