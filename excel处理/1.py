import openpyxl

wb=openpyxl.load_workbook("邻水高校专项初审.xlsx")
ws=wb['Sheet1']
for row in ws.rows:         #每一行
    for cell in row:        #横向遍历
        print(len(row))     #len(row)   列数
        print(cell.value)