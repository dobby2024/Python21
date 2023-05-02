'''
파일명: Ex03-InsertionSort.py

3. 삽입 정렬(Insertion Sort)
  리스트의 모든 요소를 앞에서 부터 차례대로 
  이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입
  
  최악의 경우 시간 복잡도: O(n^2)
  최선의 경우 시간 복잡도: O(n)
  평균 시간복잡도 : O(n^2)
'''
# 삽입 정렬 알고리즘을 구현하는 함수
def insertion_sort(arr):
  
  
  '''
  arr = [3, 5, 6, 1, 8, 7, 2, 4]
  n = 8
  
  i = 1, 2
  key(arr[i]) = 5, 3 
  j = 0, -1, 1, 0, -1
  
  while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
      
    
  # key 값을 적절한 위치에 저장
  arr[j + 1] = key
'''
  
  
  n = len(arr) # 배열의 길이
  
  for i in range(1, n):
    # 현재 원소의 값을 key 변수에 저장
    key = arr[i]
    
    # 현재 원소의 이전 원소 인덱스 j 변수에 저장
    j = i - 1
    
    # 이전 원소 부터 첫번째 원소까지 역순으로 반복하면서
    # key 값 보다 큰 원소들을 한 칸씩 오른쪽으로 이동시킨다.
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    
    # key 값을 적절한 위치에 저장
    arr[j + 1] = key
    
  return arr

# 실행코드 
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertion_sort(arr))
      
