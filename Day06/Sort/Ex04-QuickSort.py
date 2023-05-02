'''
파일명: Ex04-QuickSort.py

4. 퀵 정렬(Quick Sort)
   분할 정복 알고리즘의 일종, 기준점(pivot)을 설정하고
   pivot 보다 작은 값을 왼쪽, 큰 값을 오른쪽으로 분할한 후
   각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘.
   
  최악의 경우 시간 복잡도: O(n^2)
  최선의 경우 시간 복잡도: O(n*log n)
  평균 시간복잡도 : O(n*log n)

'''
# 퀵 정렬 알고리즘을 구현하는 함수
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  '''
  arr = [6, 5, 3, 1, 8, 7, 2, 4] 
  pivot = 6
  left = [5, 3, 1, 2, 4]
  right = [8, 7]
  equal = [6]
  
  a = 6, 5, 3, 1, 8, 2, 4

    1. left   -> [1,2,3,4,5] + [6] + [7, 8]
    quick_sort([5, 3, 1, 2, 4])
    arr = [5, 3, 1, 2, 4] 
    pivot = 5
    left = [3, 1, 2, 4]
    right = []
    equal = [5]
      2. left -> [1,2,3,4]
        quick_sort([3, 1, 2, 4])
        arr = [3, 1, 2, 4]
        pivot = 3
        left = [1, 2]
        right = [4]
        equal = [3]
        
        3. left -> [1, 2]
          quick_sort([1, 2])
          arr = [1, 2]
          pivot = 1
          left = []
          right = [2]
          equal = [1]
        3. equal -> 3
        3. right -> 4
      2. equal -> 5
      2. right -> []
'''
  # pivot 값 설정  
  pivot = arr[0]
  
  left, right, equal = [], [], []
  for a in arr:
    if a < pivot:
      left.append(a)
    elif a > pivot:
      right.append(a)
    else:
      equal.append(a)
  
  return quick_sort(left) + equal + quick_sort(right)

# 실행 코드
arr = [6, 5, 3, 1, 8, 7, 2, 4] 
print(quick_sort(arr))

  
