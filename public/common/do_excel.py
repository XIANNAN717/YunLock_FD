import xlrd
import os
from config import global_config

data_path = global_config.data_path
# print(data_path)

class ReadExcel():
    """
    读取Excel,并读取1行0列的数据
    """

    def __init__(self, filename, sheetname):
        datapath = os.path.join(data_path, filename)  # 获取Excel对象
        self.workBook = xlrd.open_workbook(datapath)
        self.sheetName = self.workBook.sheet_by_name(sheetname)

    def read_excel(self, rownum, clonum):
        value = self.sheetName.cell(rownum, clonum).value
        return value


# 调试
if __name__ == '__main__':
    data = ReadExcel("Login.xlsx", "Sheet1").read_excel(1, 0)
    print(data)
