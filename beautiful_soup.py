# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:12:11 2020

@author: camila
"""

from bs4 import BeautifulSoup
import requests

#response = requests.get('https://en.wikipedia.org/wiki/Special:Random')
response = requests.get('https://valor.globo.com/')
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# Print page title
print('Page Title:')
print(soup.title.string) 
print('')

# Print paragraph
print('First paragraph:')
print(soup.p)
print('')

# Get all links from page
for link in soup.find_all('a'):
    print(link.get('href'))
print('')

# Get all text from page
print(soup.get_text())    
    