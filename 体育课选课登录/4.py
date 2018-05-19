#encoding=utf-8
import time
import hashlib
import requests
import json

app_key="cgsoft"
#获取js式时间戳
def GetTimestamp():
    times=int(time.time())
    timestamp=str(times)+"000"
    return timestamp
#获取登录sign
def Getsign1(timestamp):
    app_secret="6d3121b650e42855976d0f70dd2048e4"
    app_key="cgsoft"
    #timestamp = Date.parse(new Date());
    path = "/api/login"
    signString = app_secret+path
    signString+="password"+"461249"+"username"+"2017141461249"
    signString += timestamp+" "+app_secret
    h1=hashlib.md5()
    h1.update(signString.encode('utf-8'))
    sign=h1.hexdigest()
    return sign
#获取get参数sign
def Getsign2(timestamp):
    app_secret="6d3121b650e42855976d0f70dd2048e4"
    app_key="cgsoft"
    #timestamp = Date.parse(new Date());
    path = "/api/terms"
    opt={
        "username":"2017141461249",
        "password":"461249"
    }
    opt.clear()
    keyArray = []
    signString = app_secret + path
    for key in opt:
        keyArray.append(key)
    keyArray.sort()
    for i in range(len(keyArray)):
        key=keyArray[i]
        signString += key + opt[key]
    signString += timestamp+" "+app_secret
    h1=hashlib.md5()
    h1.update(signString.encode('utf-8'))
    sign=h1.hexdigest()
    return sign

#while True:
#    time.sleep(1)
#    print(GetTimestamp1())
#    print(Getsign(GetTimestamp1()))

#几个主要需要访问的网页
url1="http://202.115.33.181:8086/api/login"
url2="http://202.115.33.181:8086/api/terms"
#登录时的请求头
headers1={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
#cookie自动处理
s=requests.Session()
#post登录表单内容
data1={
    "app_key": "cgsoft",
    "timestamp":GetTimestamp(),
    "sign":Getsign1(GetTimestamp()),
    "username":"2017141461249",
    "password":"461249",
}

#登录
s.options(url=url1)
r1=s.post(url=url1,headers=headers1,data=data1,allow_redirects=True)
print(r1.status_code)#登录成功的话应输出200
print(r1.text)
#获取token带入headers2
str1=r1.json()
str2=str1['data']
str3=str2['token']
token=str3['access_token']

headers2={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Referer":"http://202.115.33.181:81/",
    "Origin":"http://202.115.33.181:81",
    "Authorization":token
}
s.options(url=url2,allow_redirects=True)
#拼接url
proload={
    "app_key":app_key,
    "timestamp":GetTimestamp(),
    "sign":Getsign2(GetTimestamp())
}
#进去第一个get
r2=s.get(url=url2,headers=headers2,params=proload)
print(r2.url)
print(r2.status_code)
r2.encoding='utf-8'
print(r2.text)
