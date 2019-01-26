import pandas as pd
from pandas import DataFrame,Series

tables=pd.read_html("https://gaokao.chsi.com.cn/zsgs/bsszgmd.do?method=listStudent&year=2018&jxId=31&ssdm=51")
print(tables[0])
print(type(tables[0]))
tables[0].to_excel('1.xlsx', sheet_name='Sheet1')