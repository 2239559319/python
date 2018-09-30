import requests
import re
'''
url="http://www.baidu.com"
proxies={
    "http":"118.190.95.35:9001"
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}
r=requests.get(url=url,headers=headers,proxies=proxies)
r.encoding="utf-8"
print(r.text)
'''

def check():
    '''
    验证ip有效性函数
    :return:
    '''
    url="http://2018.ip138.com/ic.asp"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    proxies = {
        "http": "213.6.67.102:36127"
    }
    r=requests.get(url=url,headers=headers,proxies=proxies,timeout=3)
    r.encoding="gbk"
    print(r.text)

check()