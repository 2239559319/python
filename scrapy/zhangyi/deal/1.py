import json

def get_msg():
    dic={}
    with open("a.json","r+",encoding="utf-8") as f:

        l=[]            #信息列表
        lines=f.readlines()

        for line in lines:
            l.append(json.loads(line.strip()))

    for dics in l:
        dic.update(dics)
    return dic              #返回查询字典

def deal():
    dic=get_msg()
    lines=[]        #待处理信息列表
    with open("a.txt","r+",encoding="utf-8") as f:
        for i in f.readlines():
            lines.append(i.strip())

    for i in range(449):
        if(lines[i] in dic.keys()):
            lines.insert(i+1,"\t"+dic[lines[i]])
            i+=2

    new_txt="\n".join(lines)
    print(new_txt)
    with open("b.txt","w+",encoding="utf-8") as f:
        f.write(new_txt)
deal()