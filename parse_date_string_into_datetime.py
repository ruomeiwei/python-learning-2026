from dateutil import parser

date_string = 'Aug 28 2025 8:00AM'

parsed_date = parser.parse(date_string)

print(parsed_date)