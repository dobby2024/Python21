'''
파일명 : Ex03-beutifulsoup.py
'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'

headers = {'User-Agent' : 'Mozilla/5.0'} 
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
news_list = soup.find_all('a', class_='list_title')

for news in news_list:
  news_title = news.text.strip()
  print(news_title)
  




