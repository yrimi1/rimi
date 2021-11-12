from openpyxl import *


class MyExcel():
    def savefn(self, kor, eng, math, tot, avg):
        wb = load_workbook("a.Xlsx")
        ws = wb.active
        ws.append([kor, eng, math, tot, avg])
        wb.save('a.xlsx')
        wb.close()

    def loadfn(self):
        print("MyExcel loadfn")

    def createfn(self):
        try:
            wb = Workbook()
            ws = wb.active

            ws.append(['국어', '영어', '수학', '총합', '평균'])

            wb.save('a.xlsx')
            wb.close()
        except Exception as e:
            print(e)
