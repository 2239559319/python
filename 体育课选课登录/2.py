#encoding=utf-8
import time
import hashlib
import requests
def GetTimestamp():
    times=int(time.time())
    timestamp=str(times)+"000"
    return timestamp
#获取sign
def Getsign(timestamp):
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

#while True:
#    time.sleep(1)
#    print(GetTimestamp())
#    print(Getsign(GetTimestamp()))

url1="http://202.115.33.181:8086/api/login"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
s=requests.Session()
data1={
    "app_key": "cgsoft",
    "timestamp":GetTimestamp(),
    "sign":Getsign(GetTimestamp()),
    "username":"2017141461249",
    "password":"461249",
}
s.options(url=url1)
r1=s.post(url=url1,headers=headers,data=data1,allow_redirects=True)
print(r1.status_code)
print(r1.text)