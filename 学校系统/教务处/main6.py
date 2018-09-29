#写给我个人版本
import requests
import re
import json
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool

class stu(object):
    def __init__(self):
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        self.username="2017141461249"
        self.password="086698"

    def login(self):        #登录
        post_url = "http://zhjw.scu.edu.cn/j_spring_security_check"
        login_data = {
            "j_username": self.username,
            "j_password": self.password,
            "j_captcha1": "error"
        }
        r = self.s.post(url=post_url, headers=self.headers, data=login_data)
        while True:
            soup=BeautifulSoup(r.text,"lxml")
            if soup.title.string=="URP综合教务系统首页":
                print("登录成功")
                break
            else:
                r = self.s.post(url=post_url, headers=self.headers, data=login_data)
                print("登录失败")

    def getfajhh(self):
        #获取fajjh
        get_fajjh_url="http://zhjw.scu.edu.cn/student/courseSelect/courseSelect/index"
        r1=self.s.get(url=get_fajjh_url,headers=self.headers)
        str="fajhh=\d+"
        s=re.findall(str,r1.text)[0]
        fajjh=s[6:len(s)]
        return fajjh

    def getkcIds(self,courseId,courseNum):    #获取形如1231414_01_2018-2019-1-1
        '''
        这个函数也许可以改进（删去），直接构造 课程号_课序号_学期
        :param courseId:
        :param courseNum:
        :return:
        '''
        url="http://zhjw.scu.edu.cn/main/academicInfo"
        r=self.s.get(url=url,headers=self.headers)
        msg=r.json()[0]
        return courseId+"_"+courseNum+"_"+msg["zxjxjhh"]

    def getokenValue(self):
        url="http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/index"
        payload={
            "fajhh":self.getfajhh()
        }
        r=self.s.get(url=url,params=payload,headers=self.headers)
        soup=BeautifulSoup(r.text,"lxml")
        m=soup.find_all("input")
        t=str(m[0])
        tokenValue=t[46:len(t)-3]
        return tokenValue

    def getCourse(self,courseId,courseNum):       #courseId是课程号,courseNum是课序号
        '''
        这个函数也可以改进，直接构造  课程名_课序号
        :param courseId:课程号
        :param courseNum:课序号
        :return:课程名_课序号
        '''
        url="http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/courseList"
        data={
            "searchtj":courseId,
            "xq":"0",
            "jc":"0",
            "kyl":"0",
            "kclbdm":""
        }
        r=self.s.post(url=url,data=data,headers=self.headers)
        msg=r.json()["rwRxkZlList"]
        m=json.loads(msg)
        for i in m:
            if(i["kxh"]==courseNum):
                return i["kcm"]+"_"+courseNum       #返回组成的课程

    def choose(self,courseId,courseNum):            #抢课主代码
        post_url="http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/waitingfor?dealType=5"
        check_url="http://zhjw.scu.edu.cn/student/courseSelect/selectResult/query"
        post_data={
            "tokenValue":self.getokenValue(),
            "kcIds":self.getkcIds(courseId=courseId,courseNum=courseNum),
            "kcms":self.getCourse(courseId=courseId,courseNum=courseNum),
            "fajhh":self.getfajhh(),
            "sj":"0_0",
            "searchtj":courseId,
            "kclbdm":""
        }
        r=self.s.post(url=post_url,data=post_data,headers=self.headers)
        count=1
        while True:
            r = self.s.post(url=post_url, data=post_data, headers=self.headers)
            print("%s第%d次选课"%(courseId,count))
            count+=1
if __name__ == '__main__':
    a=stu()
    a.login()
    pool=Pool(4)            #同时选几节课，课数量是参数
    pool.apply_async(a.choose,("308226020","01",))      #以元组方式传参
    pool.close()
    pool.join()