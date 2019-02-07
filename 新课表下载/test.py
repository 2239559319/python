import re

def get_colloge_dic():
    kxyx_dic={}
    f=open("list.txt",'r',encoding="utf-8")
    for i in range(66):
        str1=f.readline()
        str2='"\d+"'
        str3='>\S+<'
        kxyx=re.findall(str2,str1)[0][1:-1]     #学院编号
        collogeName = re.findall(str3, str1)[0][1:-1]
        kxyx_dic[kxyx]=collogeName
    return kxyx_dic

collogeDic=get_colloge_dic()
for i in collogeDic:
    print(i)
    print(collogeDic[i])