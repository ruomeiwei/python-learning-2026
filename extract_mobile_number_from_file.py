import re 

pattern = r'1[3-9]\d{9}'

with open('webpage_phone_numbers.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()

results = re.findall(pattern, file_content)

print(results)
