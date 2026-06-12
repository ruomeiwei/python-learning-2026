list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

def sum_of_list(lst):
    total = 0 
    for num in lst:
        total += num
    return total

print(f"The sum of list1 is: {sum_of_list(list1)}")

print(f"The sum of list1 is: {sum(list1)}")