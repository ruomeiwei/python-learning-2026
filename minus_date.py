import datetime 

start = '1997-01-30'

current_datetime = datetime.datetime.now()
start_datetime = datetime.datetime.strptime(start, '%Y-%m-%d')

print((current_datetime - start_datetime).days)
