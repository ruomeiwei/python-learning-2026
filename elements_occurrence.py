def count_occurrence(lst, ele):
    count = 0 
    for i in lst:
        if i == ele:
            count += 1
    
    return count 


lst = [1,2,2,2,3,4,]
print(count_occurrence(lst, 2))

print(lst.count(2))