uppercase_string = input('Enter string').upper()

with open('user_input.txt', 'w', encoding='utf-8') as f:
    f.write(uppercase_string)