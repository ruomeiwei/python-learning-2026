import time
print('Press Enter to start timer')

input('Ready')

start = time.time()

print('Timer start')

try:
    while True:

        elapsed_time = time.time() - start

        print(f'\r{elapsed_time:.0f}', end="")

        time.sleep(1)
except KeyboardInterrupt:
    end = time.time()
    print(f'\nTotal time: {(end - start):.2f}')