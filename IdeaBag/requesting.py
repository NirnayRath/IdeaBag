#Let's talk about request lib..


import requests
from bs4 import BeautifulSoup
url='http://api.github.com/events'
r=requests.get(url)

r_html=r.text


soup=BeautifulSoup(r_html)

title=soup.find('span','articletitle').string()
print(r.url)