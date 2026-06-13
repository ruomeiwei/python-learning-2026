def remove_duplicates(lst):
    # result = []
    # for i in lst:
    #     if i not in result:
    #         result.append(i)
    # return result 
    return list(set(lst))

lst = [1, 2, 3, 2, 4, 5, 1, 6]
print(remove_duplicates(lst))