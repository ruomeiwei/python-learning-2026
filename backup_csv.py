import csv
with open('information.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

with open('backup_information.csv', 'w', newline = '',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)