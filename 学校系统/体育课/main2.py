import time
import hashlib
import requests

class stu(object):
    def __init__(self):
        self.s=requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        self.username=input("输入学号")
        self.password=input("输入密码")

        self.courseClassId=""
        self.teacherUid=""
        self.teacher_name=input("输入老师名字")
    def getTimestamp(self):         #初始化时间戳
        times = int(time.time())
        timestamp = str(times) + "000"
        return timestamp

    def getLoginSign(self,timestamp):         #登录时sign生成算法
        app_secret = "6d3121b650e42855976d0f70dd2048e4"
        app_key = "cgsoft"
        path = "/api/login"
        signString = app_secret + path
        signString += "password" + self.password + "username" + self.username
        signString += timestamp + " " + app_secret
        h1 = hashlib.md5()
        h1.update(signString.encode('utf-8'))
        sign = h1.hexdigest()
        return sign

    def getCourseSign(self,timestamp):      #查询课表时sign生成算法
        app_secret = "6d3121b650e42855976d0f70dd2048e4"
        app_key = "cgsoft"
        path = "/api/term/96/student/%s/course/classes"%self.username
        signString = app_secret + path
        signString += timestamp + " " + app_secret
        h1 = hashlib.md5()
        h1.update(signString.encode('utf-8'))
        sign = h1.hexdigest()
        return sign

    def getPostSign(self,timestamp):             #最后选课时sign算法
        app_secret = "6d3121b650e42855976d0f70dd2048e4"
        app_key = "cgsoft"
        path = "/api/courses/students"
        signString = app_secret + path
        signString += "courseClassId" + self.courseClassId + "studentUid" +self.username + "teacherName" + self.teacher_name + "teacherUid" + self.teacherUid
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
            "sign": self.getLoginSign(self.getTimestamp()),
            "username": self.username,
            "password": self.password
        }
        r1 = self.s.post(url=login_url, headers=self.headers, data=login_data)
        while True:                 #强制登录实现
            if self.username in r1.text:
                print("登录成功")
                break
            else:
                r1 = self.s.post(url=login_url, headers=self.headers, data=login_data)

    def getCourse(self):        #登录进去查询课表,得到自己的老师的信息并作为返回值
        url = "http://202.115.33.181:8086/api/term/96/student/%s/course/classes"%self.username
        payload={"app_key":"cgsoft","timestamp":self.getTimestamp(),"sign":self.getCourseSign(self.getTimestamp())}
        r=self.s.get(url=url,params=payload,headers=self.headers)
        return r.json()

    def matchMsg(self):   #输入老师名字皮匹配信息
        msg=self.getCourse()["data"]
        for i in msg:
            if self.teacher_name==i["teacherName"]:
                self.courseClassId=i["id"]
                self.teacherUid=i["teacherUid"]

    def choose(self):       #抢课主代码
        post_data={
            "app_key":"cgsoft",
            "timestamp":self.getTimestamp(),
            "sign":self.getPostSign(self.getTimestamp()),
            "courseClassId":self.courseClassId,
            "studentUid":self.username,
            "teacherUid":self.teacherUid,
            "teacherName":self.teacher_name
        }
        post_url="http://202.115.33.181:8086/api/courses/students"
        r=self.s.post(url=post_url,data=post_data,headers=self.headers)
        time=1
        while True:
            d=r.json()
            if d["code"]==200 and d["message"]=="OK":
                print("选课成功")
                break
            else:
                print("第%d次选课失败"%time)
                time+=1
                r = self.s.post(url=post_url, data=post_data, headers=self.headers)

if __name__=="__main__":
    a=stu()
    a.login()
    a.getCourse()
    a.matchMsg()
    a.choose()