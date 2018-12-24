import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.prothomalo.com'
keyword = '/bangladesh'
doc = requests.get(url+keyword)
doctext = doc.text

soup = BeautifulSoup(doctext, 'html.parser')

for link in soup.findAll('a'):
  m=re.match("(^/bangladesh/.+[^(#comments)]$)",link.get('href'))
  if m:
    full_url = url+link.get('href')
    link_object = requests.get(full_url)
    soup = BeautifulSoup(link_object.text, 'html.parser')
    des = soup.find("meta",  property='og:description')
    print(des.get('content'))
    break

