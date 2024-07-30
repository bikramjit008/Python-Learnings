import re
textToSearch='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
OIU;HERTGOIHERTIGHOUHERFGJiuhgeurtgkjlhnrougvnrr
rfgoiuhjergjlnerolikgnergviuthgbertgbmlejthgtg
oijeferbgiou;ergjklernbiperjgoluergpowrmgoiergwe
`1234567890-=[]]/.,~!@#$%^&*()_+}|:?><
facebook.com

345-238-9851
800-238-9851
900-238-9851
235.675.8930
235*675*8930

bat
cat
mat
hat

Mr Bikram
Mr. Ghatak
Mr. B
Mrs. Jeni
Miss Bratu
Mrs Sayani

'''
sentence="This is a sentence which will be used later later"

# pattern=re.compile(r'abc')
# matches=pattern.finditer(textToSearch)
# for i in matches:
#     print(i)

# pattern=re.compile(r'.')

# pattern=re.compile(r'\.')

# pattern=re.compile(r'later')
# matches=pattern.finditer(sentence)
# for i in matches:
#     print(i)
# pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern=re.compile(r'[1-6]')
# pattern=re.compile(r'[a-cA-D]')
# pattern=re.compile(r'[^a-cA-D]')
# pattern=re.compile(r'[^b]at')
# pattern=re.compile(r'Mr\.?\s[A-z]\w*')
# pattern=re.compile(r'M(r|s|rs|iss)\.?\s[A-z]\w*')
# pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
pattern=re.compile(r'This')#--> only matches the 1st element.....returns none if not found
pattern2=re.compile(r'which')#-->matches every element
# matches=pattern.finditer(textToSearch)
# matches=pattern.findall(textToSearch)


pattern=re.compile(r'this',re.IGNORECASE)
matches=pattern.search(sentence)
# for i in matches:
#     print(i)
print(matches)