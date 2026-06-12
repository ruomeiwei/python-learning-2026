def find_even_numbers(start, end):
    # even_numbers = []
    # for num in range(start, end + 1):
    #     if num % 2 == 0:
    #         even_numbers.append(num)
    return [num for num in range(start, end + 1) if num % 2 == 0]

print(f"Even numbers between 1 and 20: {find_even_numbers(1, 20)}")