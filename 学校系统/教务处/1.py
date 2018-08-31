import requests
from bs4 import BeautifulSoup

class stu(object):
    def __init__(self):
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
    def login(self):
        post_url = "http://zhjw.scu.edu.cn/j_spring_security_check"
        login_data = {
            "j_username": "2017141461249",
            "j_password": "086698",
            "j_captcha1": "error"
        }
        r1 = self.s.post(url=post_url, headers=self.headers, data=login_data)
        while True:
            soup=BeautifulSoup(r1.text,"lxml")
            if soup.title.string=="URP综合教务系统首页":
                print("登录成功")
                break
            else:
                r1 = self.s.post(url=post_url, headers=self.headers, data=login_data)

if __name__ == '__main__':
    wan=stu()
    wan.login()