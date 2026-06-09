result = 0

for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1,5):
            if x != y and y != z and x != z:
                result += 1

print(f"Number of three-digit numbers with distinct digits: {result}")