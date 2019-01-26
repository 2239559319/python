import pandas as pd

xlsx=pd.ExcelFile("1.xlsx")
df=pd.read_excel(xlsx,"Sheet1")
print(df)
print(type(df))