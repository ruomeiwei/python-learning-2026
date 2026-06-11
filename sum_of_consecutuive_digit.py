n = int(input("Enter a number: "))
numb = int(input("Enter a number: "))

current_sum = 0

for i in range(1, n+1):
    current_sum += int(str(numb) * i)
print(f"The sum of the series is: {current_sum}")