def read_file():
    content = []
    with open('students_grade_file.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line[:-1]
            line = line.split(',')
            content.append(line)
    return content 

def sort_grade(data):

    return sorted(data, key=lambda x: int(x[2]), reverse=True) 

def write_file(data):
    with open('students_grade_sorted_file.txt', 'w', encoding='utf-8') as f:
        for d in data:
            f.write(','.join(d) + '\n')


data = read_file()
print(sort_grade(data))