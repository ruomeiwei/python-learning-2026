def swap_variables(a, b):
    a, b = b, a 
    return a, b 

a = 'Hello'
b = 'World'
print(f"Before swapping: a = {a}, b = {b}")
a, b = swap_variables(a, b)
print(f"After swapping: a = {a}, b = {b}")