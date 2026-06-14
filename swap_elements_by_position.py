def swap_elements_by_position(lst, n, m):
    if not (0 <= n < len(lst)) or not (0 <= n < len(lst)):
        return 
    lst[n], lst[m] = lst[m], lst[n]
    return lst

lst = [1,2,3,4,5]
print(swap_elements_by_position(lst, 2,3))