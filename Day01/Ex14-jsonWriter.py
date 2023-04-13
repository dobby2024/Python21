'''

파일명: Ex14-jsonWriter.py
JSON(JavaScript Object Notation)
  "키-값(Value)" 쌍으로 중괄호로 묶인 객체형태 데이터
  딕셔너리 비슷하다
  구조 { K : V }
'''
import json

dict_list = [
  {
      'name':'james',
      'age':20,
      'spec':[
        175.5,
        70.5
      ]
  },
  {
      'name':'alice',
      'age':21,
      'spec':[
        168.5,
        60.5
      ]
  }
]
# indent 들여쓰기, ensure_ascii=False 한글 아스키코드로 변환하지 않음
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)


with open('dictList.json', 'w') as file:
  file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')