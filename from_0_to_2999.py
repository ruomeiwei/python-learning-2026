import time

start = time.perf_counter()

for i in range(9999+1):
    print(i)

end = time.perf_counter() 

print(f'Total time to print from 0 to 9999 is {end - start:.3f}')