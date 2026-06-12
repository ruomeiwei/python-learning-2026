def remove_elements(list1, list2):
    # for element in list2:
    #     if element in list1:
    #         list1.remove(element)
    # return list1
    return [element for element in list1 if element not in list2]


list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]
print(remove_elements(list1, list2))