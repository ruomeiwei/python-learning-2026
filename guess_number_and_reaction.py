import random 
import time 

target_num = random.randint(0, 99)

print('Number is betweew 0 and 99')

start = time.time()

while True:

    try:
        guess = int(input('Enter the number: '))
    except ValueError:
        print('Enter the number')
    else:
        if guess < target_num:
            print('The number is less than target.')
        elif guess > target_num: 
            print('The number is greater than target.')
        else:
            print("It is correct")
            end = time.time()
            break

reaction_time = end - start

if reaction_time < 5:
    print(f"Good job! Reaction time is only {reaction_time:.2f}")
else:
    print(f'Reation time is {reaction_time:2f}')