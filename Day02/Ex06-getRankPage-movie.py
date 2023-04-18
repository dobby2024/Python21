'''
Ex06-getRankPage-movie.py
'''
import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/boxoffice/weekly'
respose = requests.get(url)
html = respose.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('strong', class_='tit_item')

for idx, movie in enumerate(movie_list):
  print('{}위: {}'.format(idx+1, movie.text.strip()))




