li = [21, 33, 57, 88, 95]

num = int(input("Enter a number to insert into the sorted list: "))

for i in range(len(li)):
    if num < li[i]:
        li.insert(i, num)
        break 

else:
    li.append(num)

print(li)