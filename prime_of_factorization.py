def prime_factorization(n):
    i = 2

    if n <= 0: 
        print('Enter positive integer')
        return 
    elif n == 1:
        print(1)
        return 
    
    while i ** 2 <= n:
        if n % i == 0: 
            print(i, end='*')
            n //= i 
        else: 
            i += 1
    
    if n > 1:
        print(n)


prime_factorization(9)
