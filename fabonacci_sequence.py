def fabonacci(n):
    if n <= 0:
        print('Enter a positive integer')
        return 
    elif n == 1 or n == 2: 
        return 1 
    else: 
        return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(3))