import os 

sum_size = 0
for file in os.listdir():
    if os.path.isfile(file):
        sum_size += os.path.getsize(file) 

sum_size_kb = sum_size/1024 
print(f'total file size is {sum_size_kb:2f}')