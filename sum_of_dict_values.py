def sum_dict_values(d):
    total = 0
    for value in d.values():
        total += value
    return total

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"The sum of the values in the dictionary is: {sum_dict_values(my_dict)}")