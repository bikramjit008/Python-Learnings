import re
pattern=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
with open("text.txt","r") as f:
    content=f.read()
    matches = pattern.finditer(content)
    for i in matches:
        print(i)