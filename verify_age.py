def verify_age(age):
    if age < 0 or age > 120:
        Exception('Age must be between 0 and 120')
    return age 

try: 
    print(verify_age(130))
except Exception as e:
    print(e)