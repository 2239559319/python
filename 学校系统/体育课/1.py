import time
import hashlib
import requests

class stu(object):
    def __init__(self):
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }

    def getTimestamp(self):         #初始化时间戳
        times = int(time.time())
        timestamp = str(times) + "000"
        return timestamp

    def getSign(self,timestamp):         #sign生成算法
        app_secret = "6d3121b650e42855976d0f70dd2048e4"
        app_key = "cgsoft"
        path = "/api/login"
        signString = app_secret + path
        signString += "password" + "461249" + "username" + "2017141461249"
        signString += timestamp + " " + app_secret
        h1 = hashlib.md5()
        h1.update(signString.encode('utf-8'))
        sign = h1.hexdigest()
        return sign

    def login(self):                    #登录
        login_url="http://202.115.33.181:8086/api/login"
        login_data = {
            "app_key": "cgsoft",
            "timestamp": self.getTimestamp(),
            "sign": self.getSign(self.getTimestamp()),
            "username": "2017141461249",
            "password": "461249",
        }
        r1 = self.s.post(url=login_url, headers=self.headers, data=login_data)
        while True:
            if "2017141461249" in r1.text:
                print("登录成功")
                break
            else:
                r1 = self.s.post(url=login_url, headers=self.headers, data=login_data)
if __name__=="__main__":
    wan=stu()
    wan.login()
