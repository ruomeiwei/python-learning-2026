def sum_of_reciprocals(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return None
    total = 0
    if n%2 == 0:
        for i in range(2, n + 1, 2):
            total += 1/i 
    else:
        for i in range(1, n + 1, 2):
            total += 1/i 
    return total

n = -1
print(sum_of_reciprocals(n))