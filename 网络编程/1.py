#coding=utf-8

import re
f=open(r'D:\a.txt','r')
str1=f.read()
str11=str1.decode('utf-8')
while 1:
    str2='(\s+<td>.+?</td>\s+<td>.+?</td>\s+<td>.+'+raw_input()+'.+</td>\s+<td>.+?</td>)'
    str3=r'((?:\s+<td>.+?</td>)+)'
    r=re.findall(str2,str1)
    for i in range(len(r)):
        print r[i]