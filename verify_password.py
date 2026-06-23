import re  

def verify_password(password):
    if not 6 <= len(password) <= 20:
        return False, 'password len must be between 6 and 20'
    
    if not re.findall(r'[a-z]', password):
        return False, 'password must have at least one lowercase letter'

    if not re.findall(r'[A-Z]', password):
        return False, 'password must have at least one uppercase letter'

    if not re.findall(r'\d', password):
        return False, 'password must have at least one digital number'

    if not re.findall(r'\W', password):
        return False, 'password must have at least one special character'
    
    return True

