'''
파일명 : Ex04-readHello.py
open 함수 모드
    r(read mode) : 읽 전용 모드 / 파일 없으면 에러
'''
'''
file = open('hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')


