import re 

def date_is_right(date):
    return re.match(r'\d{4}-\d{2}-\d{2}', date) is not None

print(date_is_right('2025-02-07'))