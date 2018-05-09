# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import time

try:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    url1 = 'https://scusport.com/login'
    url2 = 'https://scusport.com/reserve'
    url3 = 'https://scusport.com/reserve/create'
    s = requests.Session()
    # 获取token
    r1 = s.get(url1, headers=headers, allow_redirects=True)
    html_str1 = r1.text
    soup1 = BeautifulSoup(html_str1, 'lxml', from_encoding='utf-8')
    str1 = str(soup1.input)
    token_str1 = str1[42:-3]
    # 登录网站
    post = {
        '_token': token_str1,
        'scuid': raw_input("输入学号"),
        'password': raw_input("输入密码")
    }
    r2 = s.post(url=url1, headers=headers, data=post, allow_redirects=True)
    if r2.status_code == 200:
    # r2=200的话登录成功
        r3 = s.get(url=url1, headers=headers, allow_redirects=True)
        # 登录进去get
        r4 = s.get(url=url2, headers=headers, allow_redirects=True)
        # 查询场地
        # schid=['1346','1347','1348','1349']
        # schid是场次的序号，网页上有
        schid = raw_input("请输入场次编号:")
        postdata = {
            '_token': token_str1,
            'schid': schid,
            'subject[]':'bmi',
            'subject[]':'vtc',
            'subject[]':'spt',
            'subject[]':'slj',
            'subject[]':'sar',
            'subject[]':'lrm',
            'subject[]':'plp',
            'tos': 'on'
        }
        
        headers1 = {
            'origin': 'https://scusport.com',
            'referer': 'https://scusport.com/reserve',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        r4 = s.post(url=url3, data=postdata, headers=headers1, allow_redirects=True)
        while r4.status_code!=200:
            time.sleep(1)
            r4 = s.post(url=url3, data=postdata, headers=headers1, allow_redirects=True)
        if r4.status_code==200:
            print "预约成功"
except Exception:
    print "预约失败"