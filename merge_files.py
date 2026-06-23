def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content  

text1 = read_file('text1.txt')
text2 = read_file('text2.txt') 

merge_content = text1 + text2 
sorted_content = "".join(sorted(merge_content))

with open('text3.txt', 'w', encoding='utf-8') as f:
    f.write(sorted_content)