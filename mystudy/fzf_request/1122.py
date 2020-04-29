#coding:utf-8
import xlrd
path = "D:\\"
workbook = xlrd.open_workbook(path + "ffzz.xlsx")
#sheet =workbook.sheet_by_name("Sheet1")
table = workbook.sheet_by_index(0)
# row表示行，cell表示列
print(table.row_values(0))   ##获取第二行数据
print(table.cell_value(1,0)) #获取第二行第一列内容
#循环获取所有行
nrows = table.nrows
for i in range(nrows):
    print((table.row_values(i)))

