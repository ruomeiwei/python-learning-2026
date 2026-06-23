import re

content = """
    hellow 12345@qq.com ddhres
    eawgerew asdf12dsa#abc.com read
    #python666@163.cn reafbdf
    only python_ant-666@sina.net eafe f
"""

pattern = re.compile(r"""
    [0-9a-zA-Z_-]+
    @
    [0-9a-zA-Z]+
    \.
    [a-z]{2,4} 
""", re.VERBOSE)

result = re.findall(pattern, content) 

print(result)