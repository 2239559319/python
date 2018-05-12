import csv
headers=['ID','Username','Password','Age','Country']
rows=[(1001,"qiye","qiye_pass",24,"China"),
      (1002,"mary","mary_pass",20,"USA"),
      (1003,"jack","jakc_pass",19,"USA")
]
with open('D:/txt/qiye.csv','w') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
#rows列表中的数据除了元组也可以是字典
rows=[{'ID':1001,'Username':"qiye",'Password':"qiye_pass",'Age':24,'Country':"China"},
      {'ID':1002,'Username':"mary",'Password':"mary_pass",'Age':20,'Country':"USA"},
      {'ID':1003,'Username':"jack",'Password':"jack_pass",'Age':19,'Country':"USA"}
]
with open('D:/txt/qiye1.csv','w') as f:
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

with open('D:/txt/qiye.csv') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)