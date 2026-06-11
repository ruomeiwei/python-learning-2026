
while True:
    numb = int(input("Enter a number: "))

    if numb ** 2 >= 50:
        print(f"The square of {numb} is {numb ** 2}, which is greater than or equal to 50.")
    else:
        print(f"The square of {numb} is {numb ** 2}, which is less than 50. Please enter a larger number.")
        break