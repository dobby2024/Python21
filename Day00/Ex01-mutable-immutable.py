'''
Ex01-mutable-immutable.py

mutable - 메모리 값을 변경 가능 객체
  리스트(list), 세트(set), 딕셔너리(dict), 클래스(class) 등

immtable - 메모리 값 변경 불가
  정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me))
me += 1
print(id(me))
you = 10
print(id(you))

list1 = [1, 2, 3]
print(id(list1))
list1.append(4)
print(id(list1))

