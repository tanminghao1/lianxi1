import openpyxl
import requests
from openpyxl.worksheet.worksheet import Worksheet


# class Excel_lianxi:
#     def __init__(self,file):
#         self.file = file
#     def open_excel(self,sheet_name):
#         wb = openpyxl.load_workbook(self.file)
#         sheet = wb[sheet_name]
#         return sheet
#     def header(self,sheet_name):
#         sheet = self.open_excel(sheet_name)
#         headers = []
#         for cell in sheet[1]:
#             headers.append(cell.value)
#         return headers
#     def read_excel(self,sheet_name):
#         sheet = self.open_excel(sheet_name)
#         rows = list(sheet.rows)
#         data = []
#         for row in rows[1:]:
#             row_data = []
#             for cell in row:
#                 row_data.append(cell.value)
#                 data_dict = dict(zip(self.header("Sheet1"),row_data))
#             data.append(data_dict)
#         return data

class Excel_fengzhuang:
    def __init__(self,file):
        self.file = file
    def open(self,sheetname):
        wb = openpyxl.open(self.file)
        sheet = wb[sheetname]
        wb.close()
        return sheet
    def heard(self,sheetname):
        sheet = self.open(sheetname)
        headers = []
        for cell in sheet[1]:
            headers.append(cell.value)
        return headers

    def read(self,sheetname):
        sheet = self.open(sheetname)
        data = []
        # sheet.rows拿到的不是一个列表，是一个生成器，需要转换为list
        rows = list(sheet.rows)
        for row in rows[1:]:
            row_data = []
            for cell in row:
                row_data.append(cell.value)
            data_dict = dict(zip(self.heard(sheetname),row_data))
            data.append(data_dict)
        return data
    @staticmethod
    def write(file,sheetname,row,col,new_value):
        wb = openpyxl.load_workbook(file)
        sheet = wb[sheetname]
        sheet[row,col].value = new_value
        wb.save(file)
        wb.close()

class request_fengzhuang():
    def __init__(self):
        # 初始化一个session会话，模拟浏览器请求
        self.session = requests.sessions.session()
    def visit(self,method,url,header=None,data=None,json=None,params=None,**kwargs):
        res = self.session.request(method,url,header=None,data=None,json=None,params=None,**kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")


if __name__ == '__main__':
    # ex = Excel_lianxi(r"C:\Users\86176\Desktop\cases.xlsx")
    # print(ex.read_excel('Sheet1'))
    ex = Excel_fengzhuang(r"C:\Users\86176\Desktop\cases.xlsx")
    print(ex.read('Sheet1'))

