import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tagname = input('Enter tagname: ')

tags = soup(tagname)

f = open("places.txt", "w+")

for tag in tags:
    p = tag.text.strip()
    p = re.sub('[^a-zA-Z ]+', '', p)
    f.write(p + '\n')
f.close()

f = open("places.txt", "r")
for line in f.readlines():
    print(line.rstrip())
