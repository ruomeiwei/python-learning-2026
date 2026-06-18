import copy 

def merge_dicts(dict1, dict2):
    merged_dict = copy.copy(dict1)
    merged_dict.update(dict2)

    return merged_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'c': 3, 'd': 4}

print(merge_dicts(dict1, dict2))
