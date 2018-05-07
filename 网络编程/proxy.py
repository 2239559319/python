# a.txt存IP地址，b.txt存端口号，其中a b 中的ip和端口一一对应
#encoding=utf-8
import requests
import re
url='http://www.xicidaili.com/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
r=requests.get(url,headers=headers)
print r.text

str1='<td>\d+.\d+.\d+.\d+</td>'
str2='<td>\d+</td>'
a=re.findall(str1,r.text)
b=re.findall(str2,r.text)
f1=open(r'D:/a.txt','w')
f2=open(r'D:/b.txt','w')
for i in a:
    print i[4:-5]
    f1.write(i[4:-5])
    f1.write('\n')
for i in b:
    print i[4:-5]
    f2.write(i[4:-5])
    f2.write('\n')
f1.close()
f2.close()