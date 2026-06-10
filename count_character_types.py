s = input("Enter a string: ")

alpha_count = 0 
digit_count = 0
space_count = 0
other_count = 0

for i in s:
    if i.isalpha():
        alpha_count += 1 
    elif i.isdigit():
        digit_count += 1 
    elif i.isspace():
        space_count += 1 
    else:
        other_count += 1

print(f"Number of alphabetic characters: {alpha_count}; Number of digits: {digit_count}; Number of spaces: {space_count}; Number of other characters: {other_count}")
