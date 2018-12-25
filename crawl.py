import requests
import re
from bs4 import BeautifulSoup
news = [];
protom_alo = {'bangladesh':1,'international':2,'economy':3,'opinion':4}
for key,value in protom_alo.items():

  # Request from url
  url = 'https://www.prothomalo.com'
  keyword = '/'+key
  doc = requests.get(url+keyword)
  doctext = doc.text

  #make parser object
  soup = BeautifulSoup(doctext, 'html.parser')

  #find all links
  for link in soup.findAll('a'):
    m=re.match("(^/"+key+"/article/.+[^(#comments)]$)",link.get('href'))
    if m:
      full_url = url+link.get('href')
      link_object = requests.get(full_url)
      soup = BeautifulSoup(link_object.text, 'html.parser')
      news_object = {};
      # get data for every url
      title = soup.find("meta",  property='og:title')
      description = soup.find("meta",  property='og:description')
      site_name = soup.find("meta",  property='og:site_name')
      image = soup.find("meta",  property='og:image')
      #make object of a link
      news_object['title'] =  title.get('content')
      news_object['description'] =  description.get('content')
      news_object['site_name'] =  site_name.get('content')
      news_object['image'] =  image.get('content')
      news_object['category'] = value
      news.append(news_object)

print(news)