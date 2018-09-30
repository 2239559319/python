#获取ip模块
import requests
import re
import time
from bs4 import BeautifulSoup

def getxiciip(maxpage):
    '''
    获取西刺代理的ip
    :param maxpage:获取的最大页面数
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
    :param max_page:获取的ip最大页面
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

def get98mianfeiip(num):
    '''
    获取89免费代理上的ip
    :param num: 获取的ip数量
    :return: iplist,IP列表
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    url="http://www.89ip.cn/tqdl.html?num=%d&address=&kill_address=&port=&kill_port=&isp="%num
    r=requests.get(url=url,headers=headers)
    soup=BeautifulSoup(r.text,"lxml")
    s=soup.find_all(style="padding-left:20px;")
    ipstr = "\d+\.\d+\.\d+\.\d+:\d+"  # 匹配ip的正则
    iplist=re.findall(ipstr,str(s))
    print("98代理提取完毕")
    return iplist

def get66daili(num):
    '''

    :param num:提取的ip数量，少量分批提取
    :return: iplist
    '''
    url="http://www.66ip.cn/mo.php?sxb=&tqsl=%d&port=&export=&ktip=&sxa=&submit=%%CC%%E1++%%C8%%A1&textarea="%num
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    ipstr = "\d+\.\d+\.\d+\.\d+:\d+"  # 匹配ip的正则
    r=requests.get(url=url,headers=headers)
    r.encoding="gbk"
    iplist=re.findall(ipstr,r.text)
    print("66代理提取完毕")
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
    ip = re.findall(ipstr, r.text)  # ip是只含ip不含端口的列表
    port = re.findall(poststr, r.text)  # port是形如<td>8000</td>的端口列表
    realport = []  # 真正存放ip的列表
    for i in port:
        realport.append(i[4:-5])
    for i in range(len(realport)):
        iplist.append(ip[i] + ":" + realport[i])
    print("y代理提取完毕")
    return iplist