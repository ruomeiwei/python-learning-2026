def product_of_list(lst):
    total = 1 
    for i in lst:
        total *= i 
    return total

lst = [1,2,3,4]
print(product_of_list(lst))