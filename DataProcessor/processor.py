import xlrd

file = '../Data/窃电用户数据.xlsx'

def read_data(file):
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    print(wb.sheet_names())  # 获取所有表格名字

if __name__ == '__main__':
    read_data(file)
