'''
파일명 : Ex05-getRankPage.py
'''
import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p', class_='title')
artist_list = soup.find_all('p', class_='artist')

# I AM - IVE
for idx, chart in enumerate(music_list):
  print(chart.text.strip(), end=' - ')
  print(artist_list[idx].find_all('a')[0].text.strip())
  
  

  