import requests
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool
class choose(object):
    def __init__(self):
        self.username="2017141461249"
        self.password="086698"
        self.s=requests.Session()
        self.headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    def login(self):
        user_data = {
            "zjh":self.username,
            "mm":self.password
        }
        login_url = "http://zhjw.scu.edu.cn/loginAction.do"
        self.s.get(url=login_url, headers=self.headers)
        r1 = self.s.post(url=login_url, headers=self.headers, data=user_data)
        soup1 = BeautifulSoup(r1.text, "lxml")
        while True:
            if soup1.title.string == "学分制综合教务":
                print(r1.text)
                print("登录成功")
                break
            else:
                print("登录失败")
                r1 = self.s.post(url=login_url, data=user_data)
    def xuanke(self,course_id,course_num):
        choose_url = "http://zhjw.scu.edu.cn/xkAction.do"
        query_data = {
            'kch': course_id,
            'cxkxh': course_num,
            'kcm': '',
            'skjs': '',
            'kkxsjc': '',
            'skxq': '',
            'skjc': '',
            'pageNumber': '-2',
            'preActionType': '2',
            'actionType': '5',
        }
        course_data = {
            'kcId': course_id + '_' + course_num,
            'preActionType': '5',
            'actionType': '9'
        }
        self.s.get(url=choose_url, params=query_data, headers=self.headers)
        response = self.s.post(url=choose_url, data=course_data, headers=self.headers)
        count=0
        while True:
            r = self.s.get(url="http://zhjw.scu.edu.cn/xkAction.do?actionType=6", headers=self.headers)
            if course_id in r.text:
                print("选课成功")
                break
            else:
                count+=1
                print("%s第%d次选课失败"%(course_id,count))
                response = self.s.post(url=choose_url, data=course_data, headers=self.headers)
if __name__=="__main__":
    wan=choose()
    wan.login()
    pool=Pool(10)
    pool.apply_async(wan.xuanke,("107021030","20",))
    pool.apply_async(wan.xuanke,("107021030","03",))
    pool.apply_async(wan.xuanke,("107021030","11",))
    pool.apply_async(wan.xuanke,("309193020","01",))
    pool.close()
    pool.join()