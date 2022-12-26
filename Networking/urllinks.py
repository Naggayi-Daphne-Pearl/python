'''
this code is extracting all the links (i.e., a tags with href attributes) from the specified web page and printing them.
'''
import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()

#This line creates a BeautifulSoup object by passing in the html variable and the HTML parser that should be used.
soup = BeautifulSoup(html, 'html.parser')

#This line uses the soup object to find all a (anchor) tags in the HTML document. 
tags = soup('a')

#This line prints the value of the href attribute of each tag, followed by None. The get method is used to retrieve the value of the href attribute.
for tag in tags:
    print(tag.get('href'), None)
    