def swap_dict_keys_values(dct):
    swapped_dict = {}
    for key in dct:
        swapped_dict[dct[key]] = key 
    
    return swapped_dict


original_dict = {'a': 1, 'b':2, 'c':3}

print(swap_dict_keys_values(original_dict))
