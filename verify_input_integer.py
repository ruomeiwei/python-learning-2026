def string_to_int():
    try:
        num = int(input('Enter an integer: '))
    except:
        return 'Not an valid integer'
    else:
        return num 

print(string_to_int())