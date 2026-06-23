import re 

content = """
bdadhsd2021/05/26dgsdg,daf2021.05.27fdg
dsgs05-28-2020,dfsg5/29/2020dfs
"""

content = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\1-\2-\3', content)
content = re.sub(r'(\d{4})\.(\d{2})\.(\d{2})', r'\1-\2-\3', content)
content = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\1-\2', content)
content = re.sub(r'(\d)/(\d{2})/(\d{4})', r'\3-0\1-\2', content)
print(content)