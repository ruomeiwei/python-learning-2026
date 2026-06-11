
for i in range(7):
    while True:
        numb = int(input('Enter an integer between 1 and 50: '))

        if 1 <= numb <= 50:
            print('*'*numb)
            break 
        else:
            print("Invalid input. Please enter an integer between 1 and 50.")