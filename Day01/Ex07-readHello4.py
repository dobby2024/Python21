'''
파일명 : Ex07-readHello4.py
readlines()
    한줄 단위 리스트 반환
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    print(line_list)
    # for line in line_list:
    #     print(line, end='')
    for no, line in enumerate(line_list):
        print('{} {}'.format(no+1, line), end='')


