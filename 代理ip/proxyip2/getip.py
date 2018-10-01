#获取ip模块
import requests
import re
import time
import os
import pic
from bs4 import BeautifulSoup

def getxiciip(maxpage):
    '''
    获取西刺代理的ip
    :param maxpage:获取的最大页面数,一页100个ip
    :return: iplist,ip列表
    '''
    iplist=[]
    page=1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    ipstr="\d+\.\d+\.\d+\.\d+"
    poststr="<td>\d+</td>"
    while page<=maxpage:
        url = "http://www.xicidaili.com/wt/%d" % page
        r = requests.get(url=url, headers=headers)
        ip=re.findall(ipstr,r.text)     #ip是只含ip不含端口的列表
        port=re.findall(poststr,r.text) #port是形如<td>8000</td>的端口列表
        realport=[]                     #真正存放ip的列表
        for i in port:
            realport.append(i[4:-5])
        for i in range(len(realport)):
            iplist.append(ip[i]+":"+realport[i])
        page+=1
    print("西刺代理提取完毕")
    return iplist

def getkuaidailiip(max_page):
    '''
    获取快代理的ip
    :param max_page:获取的ip最大页面,一页15个ip
    :return: iplist,ip列表
    '''
    iplist=[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    page=1
    ipstr = "\d+\.\d+\.\d+\.\d+"            #匹配ip的正则
    poststr = "\d+</td>"                #匹配oport的正则
    while page<=max_page:
        url="https://www.kuaidaili.com/free/intr/%d/"%page
        r=requests.get(url=url,headers=headers)
        ip = re.findall(ipstr, r.text)  # ip是只含ip不含端口的列表
        port = re.findall(poststr, r.text)  # port是形如<td>8000</td>的端口列表
        realport = []  # 真正存放ip的列表
        for i in port:
            realport.append(i[:-5])
        for i in range(len(ip)):
            iplist.append(ip[i] + ":" + realport[i])
        page+=1
    print("快代理提取完毕")
    return iplist

def get98mianfeiip(maxpage):
    '''
    获取89免费代理上的ip
    :param maxpage: 最大的页面,一页15个ip
    :return: iplist,IP列表
    '''
    iplist=[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    page=1
    while page<=maxpage:
        url="http://www.89ip.cn/index_%d.html"%page
        r=requests.get(url=url,headers=headers)
        ipstr = "\d+\.\d+\.\d+\.\d+"  # 匹配ip的正则
        portstr = "<td>\n\t\t\t\d+\t\t</td>"
        ip = re.findall(ipstr, r.text)
        port = re.findall(portstr, r.text)
        realport = []  # 真正存放ip的列表
        for i in port:
            realport.append(i[4:-5].strip())
        for i in range(len(ip)):
            iplist.append(ip[i] + ":" + realport[i])
        page+=1
    print("98代理提取完成")
    return iplist

def get5uip():
    '''
    获取5u代理上的ip,一次20个
    :return: iplist
    '''
    iplist = []
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    url1="http://www.data5u.com/free/gngn/index.shtml"
    url2="http://www.data5u.com/free/gnpt/index.shtml"
    page = 1
    maxpage=2
    while page <= maxpage:
        if page==1:
            url = url1
        else:
            url=url2
        r = requests.get(url=url, headers=headers)
        ipstr = "\d+\.\d+\.\d+\.\d+"  # 匹配ip的正则
        portstr = ">\d+</li>"
        ip = re.findall(ipstr, r.text)
        port = re.findall(portstr, r.text)
        realport = []  # 真正存放ip的列表
        for i in port:
            realport.append(i[1:-5])
        for i in range(len(ip)):
            iplist.append(ip[i] + ":" + realport[i])
        page += 1
    print("5u代理提取完成")
    return iplist

def getmipuip():
    '''
    获取米扑上的ip，一次20个
    :return: iplist
    '''
    iplist=[]
    url1="https://proxy.mimvp.com/free.php"
    url2="https://proxy.mimvp.com/free.php?proxy=in_tp"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    page=1
    while page<=2:
        if page==1:
            url=url1
        else:
            url=url2
        r=requests.get(url=url,headers=headers)
        ipstr = "\d+\.\d+\.\d+\.\d+"  # 匹配ip的正则
        portstr="common/ygrandimg.php\?id=\d+&port=\w+"
        ip=re.findall(ipstr,r.text)
        portlist=[]
        porturllist=re.findall(portstr,r.text)
        for i in porturllist:
            p=requests.get(url="https://proxy.mimvp.com/"+i)
            with open("1.png",'wb') as f:
                f.write(p.content)
            port=pic.getresult('1.png')
            portlist.append(port)
        for i in range(len(ip)):
            iplist.append(ip[i]+":"+portlist[i])
        page+=1
    os.remove('1.png')
    print("米扑提取完成")
    return iplist

def getyqieip():
    '''
    获取yqie上的ip
    :return:
    '''
    iplist=[]
    url="http://ip.yqie.com/ipproxy.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    ipstr = "\d+\.\d+\.\d+\.\d+"
    poststr = "<td>\d+</td>"
    r=requests.get(url=url,headers=headers)
    r.encoding='utf-8'
    ip = re.findall(ipstr,r.text.split("国外高匿代理IP")[0])  # ip是只含ip不含端口的列表
    port = re.findall(poststr, r.text.split("国外高匿代理IP")[0])  # port是形如<td>8000</td>的端口列表
    realport = []  # 真正存放ip的列表
    for i in port:
        realport.append(i[4:-5])
    for i in range(len(realport)):
        iplist.append(ip[i] + ":" + realport[i])
    print("y代理提取完毕")
    return iplist