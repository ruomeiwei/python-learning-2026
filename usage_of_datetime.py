import datetime 

print(datetime.datetime.now().strftime('%Y-%m-%d'))

birthday = datetime.date(1941,1,5)
print(birthday) 

print(datetime.timedelta(days=1) + birthday)

print(birthday.replace(year=birthday.year+1))