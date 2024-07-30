import re
webSites='''
https://Google.com
http://www.facebook.net
https://melvin.in
http://www.nasa.com
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# match=pattern.finditer(webSites)
# for site in match:
#     # print(site)
#     print(site.group(3))
subbed_urls=pattern.sub(r'\2\3',webSites)
print(subbed_urls)