from bs4 import BeautifulSoup
import requests
import time

class yuyue(object):
    def __init__(self):
        #构造函数
        self.username=input("输入学号")
        self.password=input("输入密码")
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        self.url1="https://scusport.com/login"
        self.url2="https://scusport.com/reserve"
        self.url3="https://scusport.com/reserve/create"

    def Get_token(self):
        #获取登陆口令
        r1=self.s.get(url=self.url1,headers=self.headers)
        soup1 = BeautifulSoup(r1.text,'lxml')
        str1 = str(soup1.input)
        token_str1 = str1[42:-3]
        return token_str1

    def login(self):
        # 登录网站
        post = {
            '_token':self.Get_token(),
            'scuid': self.username,
            'password': self.password
        }
        r2=self.s.post(url=self.url1,headers=self.headers,data=post)
        while True:
            soup2 = BeautifulSoup(r2.text, 'lxml')
            if soup2.h2.string == "欢迎":
                print("登录成功")
                break
            else:
                print("登录失败")
                r2 = self.s.post(url=self.url1, headers=self.headers, data=post)

    def choose(self):
        r3 = self.s.get(url=self.url1, headers=self.headers)
        # 登录进去get
        r4 = self.s.get(url=self.url2, headers=self.headers)
        # 查询场地
        # schid=['1346','1347','1348','1349']
        # schid是场次的序号，网页上有
        schid = input("请输入场次编号:")
        postdata = {
            '_token': self.Get_token(),
            'schid': schid,
            'subject[1]': 'bmi',
            'subject[2]': 'vtc',
            'subject[3]': 'spt',
            'subject[4]': 'slj',
            'subject[5]': 'sar',
            'subject[6]': 'lrm',
            'subject[7]': 'plp',
            'tos': 'on'
        }
        list1 = [1, 2, 3, 4, 5, 6, 7]
        choose = input("输入项目，1234567代表全选(123代表前123项):")
        for i in choose:
            j = int(i)
            list1.remove(j)
        for i in list1:
            postdata.pop('subject[%d]' % i)
        r4 = self.s.post(url=self.url3, data=postdata, headers=self.headers)
        while True:
            print(r4.text)
            """
            待补充的地方
            """

if __name__=="__main__":
    wan=yuyue()
    wan.login()
    wan.choose()