import time 

a1 = '2025-4-10 23:40:00'
time_array = time.strptime(a1, '%Y-%m-%d %H:%M:%S')
print(time_array)

timestamp = time.mktime(time_array)
print(timestamp)

a2 = '2025/4/10 23:40:00'
time_array2 = time.strptime(a2, '%Y/%m/%d %H:%M:%S')
print(time_array2)

timestamp2 = time.mktime(time_array2)
print(timestamp2)

time_string = time.strftime('%Y/%m/%d %H:%M:%S', time_array)
print(time_string)