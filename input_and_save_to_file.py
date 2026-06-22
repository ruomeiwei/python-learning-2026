
with open('user_input.txt', 'a', encoding='utf-8') as f:
        
    while True:
        input_string = input('Please enter: ')
        if input_string == '#':
            break 
        f.write(input_string + '\n')

    