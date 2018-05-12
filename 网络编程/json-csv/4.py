#命名元组
from collections import namedtuple
import csv
with open('D:/txt/qiye.csv') as f:
    f_csv=csv.reader(f)
    headings=next(f_csv)
    print(headings)
    Row=namedtuple('Row',headings)
    for r in f_csv:
        row=Row(*r)
        print(row.Username,row.Password)
        print(row)