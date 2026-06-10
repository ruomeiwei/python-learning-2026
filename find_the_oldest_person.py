people = {'Alice': 30, 'Bob': 25, 'Charlie': 35, 'David': 28}

max_age = float('-inf')
max_name = ''

for name, age in people.items():
    if age > max_age:
        max_age = age 
        max_name = name 

print(f'The oldest person is {max_name} with age {max_age}.')