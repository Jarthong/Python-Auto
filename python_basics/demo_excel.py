import xlrd, xlwt

workbook = xlrd.open_workbook('badu_praise.xlsx')

# 根据sheet索引或者名称获取sheet内容
sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
print(sheet1)

# 获取整行和整列的值（数组）
rows = sheet1.row_values(0)  # 获取第1行内容
cols = sheet1.col_values(0)  # 获取第2列内容
print(rows)
print(cols, type(cols))

# 获取单元格数据
data = sheet1.cell(0, 2).value
print('单元格：', data, type(data))
data_int = int(data)

for i in range(1, data_int+1):
    print('这是:', i)
