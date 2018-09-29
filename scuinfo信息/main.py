import requests
import re
import time

def getmsg(page):
    '''
    :param page:抓取的页面数
    :return: 得到的信息
    '''
    savedata=[]

    s=requests.Session()
    #第一次获取首页
    fromid=''
    start_url="http://www.scuinfo.com/api/posts?pageSize=15"
    headers = {
        "Referer":"http://www.scuinfo.com/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    r=s.get(url=start_url,headers=headers)
    datalist=r.json()['data']
    for i in datalist:
        dic={}
        timestamp=i['date']
        timeTuple = time.localtime(timestamp)
        dic['时间'] = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
        if i['gender']==1:
            dic["性别"]='男'
        else:
            dic["性别"] = '女'
        dic["内容"] =i['content'].replace('\n','')
        fromid=i['id']
        savedata.append(dic)

    #以后的页面
    count=1
    while count<=page:
        payload = {"fromId": fromid}
        r = s.get(url=start_url,params=payload,headers=headers)
        datalist = r.json()['data']
        for i in datalist:
            dic = {}
            timestamp = i['date']
            timeTuple = time.localtime(timestamp)
            dic['时间'] = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
            if i['gender'] == 1:
                dic["性别"] = '男'
            else:
                dic["性别"] = '女'
            dic["内容"] = i['content'].replace('\n','')
            fromid = i['id']
            savedata.append(dic)
        count+=1
    return savedata

def save(filepath,page):
    with open(filepath,'w',encoding='utf-8') as f:
        for i in getmsg(page=page):
            print(i)
            f.write("时间:"+i['时间']+" "+"性别"+i['性别']+" "+"内容"+i['内容']+"\n")

        f.close()
save("1.txt",10)