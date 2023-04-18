'''
파일명 : Ex07-selenium-googleImages.py

pip install selenium

selenium 패키지
  어플리케이션 테스트하기위한 프레임워크 이다.
  웹 어플리케이션 다양한 브라우저 동작 테스트용
  웹 크롤링으로 많이 사용된다.
  java, python, c#, ruby 등 다양한 언어 지원
  ex) 브라우저 컨트롤로 사용
  
https://chromedriver.chromium.org/downloads

C:\Program Files\Google\Chrome\Application\chromedriver.exe

'''
import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import traceback

def download_images(keyword, num_images=10, output_dir='images'):
  # Chrome 드라이버 경로
  chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
  
  service = Service(executable_path=chrome_driver_path)
  
  # Chrome 드라이버 인스턴스 생성
  driver = webdriver.Chrome(service=service)
  
  # Google 이미지 검색 페이지 접속
  driver.get('https://google.co.kr/imghp')
  
  # 검색어 입력 find_element
  search_bar = driver.find_element(By.NAME, 'q')
  search_bar.send_keys(keyword) # 키워드 입력
  search_bar.send_keys(Keys.RETURN) # 엔터 입력
  
  # time.sleep(10)
  
  # 드라이버 종료
  # driver.quit()
  
# 실행코드
keyword = 'cute cat'
num_images = 10
output_dir = 'images'

# 이미지 다운로드 함수 호출
download_images(keyword, num_images, output_dir)

