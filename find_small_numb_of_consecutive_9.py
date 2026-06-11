numb = int(input('Enter an odd number: '))

n = 1 

while True:
    n_9 = int('9' * n)
    if n_9 % numb == 0:
        print(f"The smallest number consisting of {n} consecutive 9's that is divisible by {numb} is: {n_9}")
        break
    
    n = n + 1 
