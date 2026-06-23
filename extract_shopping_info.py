import re 

content = """
xiaoming is shopping 
bought 500g cucumber and spent 8 pounds;
bought 1000g grape and spent 13.5 pounds;
bought 1500g cabbage and spent 5.4 pounds;
"""

for line in content.split('\n'):
    pattern = r'(\d+)g (.+) and spent (\d+(\.\d+)?) pounds'
    match = re.search(pattern, line)
    if match:
        print(match.groups())