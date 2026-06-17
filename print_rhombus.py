def print_rhombus(row):
    if row % 2 == 0:
        print('Row must bee an odd number.')
        return 
    
    for i in range(1, row, 2):
        print(' '*((row-i)//2)+'*'*i)
    
    for i in range(row, 0, -2):
        print(' '*((row-i)//2)+'*'*i)


print_rhombus(5)