from openpyxl import Workbook
workbook = Workbook() # 새 워크북 생성 : Excel 파일만 열어둔 상태 (예시 : 통합문서1.xlsx)
worksheet = workbook.active # 현재 활성화 된 excel sheet 가져오기
worksheet.title = "TEST sheet" # 워크시트의 이름 지정
workbook.save("sample.xlsx") # 엑셀파일 저장
workbook.close() # 파일 닫기
