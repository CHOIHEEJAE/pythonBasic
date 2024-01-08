from openpyxl import Workbook
from random import *
workbook = Workbook()
worksheet = workbook.active

worksheet.append(["번호", "영어", "수학", "국어"]) # worksheet 내 한 줄 씩 데이터 삽입
# worksheet.append(["1" , "40점", "30점", "90점"]) # 이렇게하면? 두번쨰 줄에 데이터 삽입 (위에 append로 한 줄을 넣었기 때문)

for i in range(1, 11) : # 10개 데이터 넣기
    worksheet.append([i, randint(1, 100), randint(1,100)])

column_B = worksheet["B"] # B열 전체 가져오기
# print(column_B, ) # column_B.value : tuple객체이기 때문에 value 함수 동작 X  // ErrorMessage : 'tuple' object has no attribute 'cell_value'

# for cell_value in column_B : # tuple 내 value에 접근하기 위해서는 반복문을 사용해 처리한다
#     print(cell_value.value)

column_Range = worksheet["B:C"] # B,C열 함께 가져오기
for cell in column_Range : # cell : B열, C열 각각 tuple 객체
    print(type(cell)) # <class 'tuple'>
    for column_row_data in cell : # B열 데이터 싹 뽑고 C열 데이터 싹 뽑고
        print(column_row_data.value)


row_title = worksheet[1] # 1번째 row만 가져오기
for row in row_title :
    print(row.value)

row_range = worksheet[2:worksheet.max_row] # 2번째 row 부터 데이터가 있는 row 끝까지 가져오기
print(row_range)




workbook.save("sample.xlsx")