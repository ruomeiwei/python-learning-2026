import re 

content = """
    hellow world 19989881999anda, ehjsahfef6327483479549546,eref12345dfef15619292345'
"""

pattern=r'1[3-9]\d{9}'

result = re.findall(pattern, content)

print(result)