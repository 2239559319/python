#写给我个人版本
import requests
import re
import json
import os
from bs4 import BeautifulSoup
from multiprocessing import Pool

class stu(object):
    def __init__(self):
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        self.username=input("输入学号")
        self.password=input("输入密码")

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

    def getlist(self):          #获取自己的课表,为判断删除课程做准备
        course_data={}
        url="http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback"
        r=self.s.get(url=url,headers=self.headers)
        list=r.json()["xkxx"][0]
        for i in list:
            each_course=list[i]
            course_data[each_course["courseName"]]={}
            course_data[each_course["courseName"]]["courseNum"]=each_course["id"]["coureNumber"]
            course_data[each_course["courseName"]]["courseId"]=each_course["id"]["coureSequenceNumber"]
            course_data[each_course["courseName"]]["day"]=each_course["timeAndPlaceList"][0]["classDay"]
            course_data[each_course["courseName"]]["starttime"]=each_course["timeAndPlaceList"][0]["classSessions"]
            course_data[each_course["courseName"]]["endtime"]=course_data[each_course["courseName"]]["starttime"]+each_course["timeAndPlaceList"][0]["continuingSession"]-1
        return course_data


    def getfajhh(self):
        #获取fajjh
        get_fajjh_url="http://zhjw.scu.edu.cn/student/courseSelect/courseSelect/index"
        r1=self.s.get(url=get_fajjh_url,headers=self.headers)
        str="fajhh=\d+"
        s=re.findall(str,r1.text)[0]
        fajjh=s[6:len(s)]
        return fajjh

    def getkcIds(self,courseId,courseNum):    #获取形如1324141_01_2018-2019-1-1的字符串
        url="http://zhjw.scu.edu.cn/main/academicInfo"
        r=self.s.get(url=url,headers=self.headers)
        msg=r.json()[0]
        return courseId+"_"+courseNum+"_"+msg["zxjxjhh"]

    def getdeltoken(self):          #获取删除课程时的token
        url="http://zhjw.scu.edu.cn/student/courseSelect/quitCourse/index"
        r=self.s.get(url=url,headers=self.headers)
        a = r"'tokenValue':'\S+'"
        r = re.findall(a, r.text)[0]
        token = r[14:-1]
        return token

    def getokenValue(self):             #获取token
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
        time_data={}
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
                s=i["sjdd"][0]              #上课时间信息
                time_data["day"]=int(s["skxq"])
                time_data["starttime"]=int(s["skjc"])
                time_data["endtime"]=int(s["skjc"])+int(s["cxjc"])-1
                return (time_data,i["kcm"]+"_"+courseNum)       #返回组成的课程

    def checkdelcourse(self,courseNum,courseId):               #判断删除的课程（时间重合）,返回要删除的课信息
        courseTable = self.getlist()                            #自己的课表
        choosecourse = self.getCourse(courseNum=courseNum, courseId=courseId)[0]    #选中的课
        for i in courseTable.keys():
            if (courseTable[i]["day"] == choosecourse["day"]):
                if (not (courseTable[i]["starttime"] >= choosecourse["endtime"] or
                         courseTable[i]["endtime"] <= choosecourse["starttime"])):
                    return (courseTable[i]["courseNum"],courseTable[i]["courseId"])

    def delcourse(self,courseNum,courseId):         #courseNum是删除的课序号

        url="http://zhjw.scu.edu.cn/student/courseSelect/delCourse/deleteOne"
        del_data={
            "fajhh":self.getfajhh(),
            "kch":courseNum,
            "kxh":courseId,
            "tokenValue":self.getdeltoken()
        }
        r=self.s.post(url=url,data=del_data,headers=self.headers)
        if("删除课程成功" in r.text):
            print("成功删除原来的课程")

    def choose(self,courseId,courseNum):            #抢课主代码
        post_url="http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/waitingfor?dealType=5"
        check_url="http://zhjw.scu.edu.cn/student/courseSelect/selectResult/query"
        post_data={
            "tokenValue":self.getokenValue(),
            "kcIds":self.getkcIds(courseId=courseId,courseNum=courseNum),
            "kcms":self.getCourse(courseId=courseId,courseNum=courseNum)[1],
            "fajhh":self.getfajhh(),
            "sj":"0_0",
            "searchtj":courseId,
            "kclbdm":""
        }
        check_data={
            "kcNum":"1",
            "redisKey":self.username+"5"
        }
        r1=self.s.post(url=post_url,data=post_data,headers=self.headers)
        count=1
        while True:
            r2=self.s.post(url=check_url,data=check_data,headers=self.headers)
            m=r2.json()
            statue_code=0                       #状态码
            for i in m.items():
                if (i[0] == "result" and "选课成功" in i[1][0]):
                    statue_code=1
                if(i[0]=="result" and "上课时间冲突" in i[1][0]):
                    statue_code=2               #选课时间冲突
            if(statue_code==1):
                print("选课成功")
                break
            if(statue_code==2):
                self.delcourse(self.checkdelcourse(courseNum=courseNum,courseId=courseId)[0],
                               self.checkdelcourse(courseNum=courseNum,courseId=courseId)[1])
            else:
                print("第%d次选课失败"%count)
                r1 = self.s.post(url=post_url, data=post_data, headers=self.headers)
                count+=1

if __name__ == '__main__':
    a=stu()
    courseNum=input("输入课程号")
    courseId=input("输入课序号")
    a.login()
    a.choose(courseNum=courseNum,courseId=courseId)
    os.system("pause")