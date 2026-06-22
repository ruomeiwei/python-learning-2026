import os 

search_dir = r'D:\tools\Python'

result_file = []

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('.txt'):
            file_path = f'{root}/{file}'
            file_size_kb = os.path.getsize(file_path)/1024
            result_file.append((file_path, file_size_kb))


sorted_result_file = sorted(result_file, key = lambda x: x[1], reverse=True)
print(sorted_result_file[0])