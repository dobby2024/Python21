'''
파일명 : Ex02-beutifulsoup.py


pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup
# https://news.nate.com/rank/?mid=n1000
url = 'https://news.nate.com/rank/'
param = {"mid":"n1000"}
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
tit_list = soup.find_all('strong', class_='tit')
for tit in tit_list:
  print(tit.text.strip())
  



