#通用版
import requests
import re
import os

class tice(object):
    def __init__(self):
        self.username=input("输入学号")
        self.password=input("输入密码")
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        self.token=""

    def gettoken(self):
        '''
        获取登陆时的token
        :return: token(class str)
        '''
        url="https://scusport.com/login"
        r=self.s.get(url=url,headers=self.headers)
        str='value="\w+"'
        t=re.findall(str,r.text)
        token=t[0][7:-1]
        return token

    def login(self):
        '''
        登陆
        :return:
        '''
        url = "https://scusport.com/login"
        login_data={
            "_token":self.gettoken(),
            "scuid":self.username,
            "password":self.password
        }
        r=self.s.post(url=url,data=login_data,headers=self.headers)
        while True:
            if "欢迎" in r.text:
                print("登录成功")
                self.token=login_data["_token"]
                break
            else:
                r = self.s.post(url=url, data=login_data, headers=self.headers)
                print("登录失败，尝试再次登录")

    def choose(self):
        choose_url="https://scusport.com/reservation/create"
        scuid=input("输入场次编号")
        postdata = {
            '_token': self.token,
            'schid':scuid ,
            'subject[1]': 'bmi',
            'subject[2]': 'vtc',
            'subject[3]': 'spt',
            'subject[4]': 'slj',
            'subject[5]': 'sar',
            'subject[6]': 'lrm',
            'subject[7]': 'plp',
            'tos': 'on'
        }
        r=self.s.post(url=choose_url,data=postdata,headers=self.headers)
        while True:
            if "成功" in r.text:
                print("预约成功")
                break
            else:
                r = self.s.post(url=choose_url, data=postdata, headers=self.headers)
                print("预约失败，尝试再次预约")

if __name__=="__main__":
    os.system("echo 程序开始")
    a=tice()
    a.login()
    a.choose()
    os.system("pause")