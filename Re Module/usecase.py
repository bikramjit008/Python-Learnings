import re
emails='''
bikuTubai008@gmail.com
Biku-tubai@Makaut.net
biku.tubai-@Er-ep07.png
'''
pattern = re.compile(r'[a-zA-Z\d\.-]+@[a-zA-Z\d-]+\.(com|net|png)')
match=pattern.finditer(emails)
for mail in match:
    print(mail)