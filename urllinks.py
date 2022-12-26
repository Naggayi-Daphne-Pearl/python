'''
this code is extracting all the links (i.e., a tags with href attributes) from the specified web page and printing them.
'''
import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href'), None)
    