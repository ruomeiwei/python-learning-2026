import time 

local_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', local_time))

time.sleep(1)

local_time = time.localtime()

print(time.strftime('%Y-%m-%d %H:%M:%S', local_time))
