import random

start = int(input('Enter start number: '))
stop = int(input('Enter stop number: '))

random_sample = random.sample(range(start, stop+1), 3)

print(random_sample)