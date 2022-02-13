import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


class Excel_lianxi:
    def __init__(self,file):
        self.file = file
    def open_excel(self,sheet_name):
        wb = openpyxl.load_workbook(self.file)
        sheet = wb[sheet_name]
        return sheet
    def header(self,sheet_name):
        sheet = self.open_excel(sheet_name)
        headers = []
        for cell in sheet[1]:
            headers.append(cell.value)
        return headers
    def read_excel(self,sheet_name):
        sheet = self.open_excel(sheet_name)
        rows = list(sheet.rows)
        data = []
        for row in rows[1:]:
            row_data = []
            for cell in row:
                row_data.append(cell.value)
                data_dict = dict(zip(self.header("Sheet1"),row_data))
            data.append(data_dict)
        return data



if __name__ == '__main__':
    ex = Excel_lianxi(r"C:\Users\86176\Desktop\cases.xlsx")
    print(ex.read_excel('Sheet1'))