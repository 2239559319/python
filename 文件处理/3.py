#encoding=utf-8
import openpyxl

a=openpyxl.load_workbook(r"C:\Users\w2239\Desktop\文件\18年邻水自主招生初审过.xlsx")
print(a.sheetnames)
sheet1=a["Sheet1"]
print(sheet1)
for i in range(1,100):
    if sheet1["A%d"%i]!= None and len(sheet1["A%d"%i].value):
        print(sheet1["A%d"%i].value)