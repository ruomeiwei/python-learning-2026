import os 

data_dir = 'datas/many_texts'

content = []

for file in os.listdir(data_dir):
    file_path = f'{data_dir}/{file}'
    if os.path.isfile(file_path) and file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content.append(f.read())
final_content = "\n\n".join(content)

with open('datas_merge.txt', 'w', encoding='utf-8') as f:
    f.write(final_content)
