#收集所有2018-2019秋课表

import requests
import re
import time
from openpyxl import Workbook

def query(kkxs):
    time.sleep(5)
    datalist = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    url = "http://zhjwjs.scu.edu.cn/teacher/personalSenate/giveLessonInfo/thisSemesterClassSchedule/getCourseArragementPublic"
    postdata = {
        "zxjxjhh":"2018-2019-2-1",  #学期
        "kch": "",  # 课程号
        "kcm": "",  # 课程名
        "js": "",  # 教师
        "kkxs": kkxs,  # 开课院系
        "skxq": "",  # 上课星期
        "skjc": "",  # 上课节次
        "xq": "",  # 校区
        "jxl": "",  # 教学楼
        "jas": "",  # 教室
        "pageNum": "1",  # 显示的页数
        "pageSize": "30",  # 每页的课程数
        "kclb": ""  # 课程类别
    }
    r = requests.post(url=url, data=postdata, headers=headers)
    m = r.json()["list"]
    totalcourse = m["pageContext"]["totalCount"]  # 总课数
    page = totalcourse / 30 + 1
    while int(postdata["pageNum"]) <= page:  # 存储数据到list
        currentpage = int(postdata["pageNum"])
        for i in r.json()["list"]["records"]:
            datalist.append(i)
        currentpage += 1
        postdata["pageNum"] = str(currentpage)
        r = requests.post(url=url, data=postdata, headers=headers)

    return datalist

def get_colloge_list():
    kxyx_list=[]
    f=open("list.txt",'r',encoding="utf-8")
    for i in range(66):
        str1=f.readline()
        str2='"\d+"'
        kxyx=re.findall(str2,str1)[0][1:-1]
        kxyx_list.append(kxyx)
    return kxyx_list

if __name__=="__main__":
    wb = Workbook()
    ws = wb.active
    ws.append(["课程号","课序号", "课程名","学分", "开课院系","上课教师","选课限制",
               "校区","上课教室","上课星期","周次","教学楼","上课节次"])
    collogelist=get_colloge_list()
    for colloge_id in collogelist:
        print(colloge_id)
        response_course=query(colloge_id)
        for each_course in response_course:
            kch = each_course['kch']  # 课程号
            kxh = each_course['kxh']  # 课序号
            kcm = each_course['kcm']  # 课程名
            xf = each_course['xf']  # 学分
            kkxsjc = each_course['kkxsjc']  # 开课院系
            skjs = each_course['skjs']  # 上课教师
            xkxzsm = each_course['xkxzsm'].strip()  # 选课限制说明
            kkxqm = each_course['kkxqm']  # 校区
            jash = each_course['jash']  # 上课教室
            skxq = each_course['skxq']  # 上课星期
            zcsm = each_course['zcsm']  # 周次
            jxlm = each_course['jxlm']  # 教学楼
            if (each_course['skjc'] != None):
                jieci = str(each_course['skjc']) + "-" + str(each_course['skjc'] + each_course['cxjc'] - 1)  # 上课节次
            else:
                jieci = None
            ws.append([kch,kxh,kcm,xf,kkxsjc,skjs,xkxzsm,kkxqm,jash,skxq,zcsm,jxlm,jieci])
    wb.save('course.xlsx')