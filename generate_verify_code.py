import string
import random

length = int(input('Enter an integer: '))

characters = string.ascii_letters + string.digits

verify_code = ""
for i in range(1,length+1):
    verify_code += random.choice(characters)

print(verify_code)
